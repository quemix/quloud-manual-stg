"""tools/shots_ledger.py の単体テスト。

台帳は人の手が入る CSV なので、build が人の記入を消さないこと、check が
食い違いを見逃さないことを押さえる。
"""
import csv
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

import tools.shots_ledger as L


class LedgerTestBase(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        root = Path(self._tmp.name)
        self.repo = root
        self.out = root / "shots" / ".out"
        self.images = root / "source" / "images" / "v70"
        self.assets = root / "meta" / "images_assets.csv"
        self.placements = root / "meta" / "images_placements.csv"
        for d in (self.out, self.images, self.assets.parent):
            d.mkdir(parents=True, exist_ok=True)
        self._patches = [
            mock.patch.object(L, "REPO", root),
            mock.patch.object(L, "OUT_DIR", self.out),
            mock.patch.object(L, "IMAGE_DIR", self.images),
            mock.patch.object(L, "ASSETS_CSV", self.assets),
            mock.patch.object(L, "PLACEMENTS_CSV", self.placements),
        ]
        for p in self._patches:
            p.start()

    def tearDown(self):
        for p in self._patches:
            p.stop()
        self._tmp.cleanup()

    def add_sidecar(self, asset_id, chapter="signin", feature="機能", state="状態"):
        rel = f"source/images/v70/{asset_id}.png"
        (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (self.repo / rel).write_bytes(b"png")
        (self.out / f"{asset_id}.json").write_text(json.dumps({
            "asset_id": asset_id,
            "file": rel,
            "chapter": chapter,
            "feature": feature,
            "state": state,
            "captured_at": "2026-09-07T16:02:03.000Z",
            "captured_on": "2026-09-08",
            "viewport": "1440x900",
        }), encoding="utf-8")

    def add_legacy_sidecar(self, asset_id):
        """captured_on が無い古い形式の記録。UTC の ISO から日付を切り出す。"""
        rel = f"source/images/v70/{asset_id}.png"
        (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (self.repo / rel).write_bytes(b"png")
        (self.out / f"{asset_id}.json").write_text(json.dumps({
            "asset_id": asset_id,
            "file": rel,
            "chapter": "signin",
            "feature": "機能",
            "state": "状態",
            "captured_at": "2026-09-07T16:02:03.000Z",
            "viewport": "1440x900",
        }), encoding="utf-8")

    def read_assets(self):
        with self.assets.open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))

    def write_placements(self, rows):
        with self.placements.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=L.PLACEMENT_FIELDS)
            w.writeheader()
            w.writerows(rows)


class TestBuild(LedgerTestBase):
    def test_creates_rows_from_sidecars(self):
        self.add_sidecar("signin_form_initial")
        self.assertEqual(L.build("abc123"), 0)
        rows = self.read_assets()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["asset_id"], "signin_form_initial")
        # captured_on（JST）を採る。captured_at は UTC なので前日になっている。
        self.assertEqual(rows[0]["撮影日"], "2026-09-08")
        self.assertEqual(rows[0]["参照コミット"], "abc123")
        self.assertEqual(rows[0]["ビューポート"], "1440x900")

    def test_keeps_rows_not_recaptured(self):
        # 部分的に撮り直しても、撮っていない行が消えないこと。
        self.add_sidecar("a_one")
        L.build("c1")
        (self.out / "a_one.json").unlink()
        self.add_sidecar("b_two")
        L.build("c2")
        ids = [r["asset_id"] for r in self.read_assets()]
        self.assertEqual(ids, ["a_one", "b_two"])

    def test_recapture_updates_row(self):
        self.add_sidecar("a_one")
        L.build("old")
        L.build("new")
        rows = self.read_assets()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["参照コミット"], "new")

    def test_falls_back_to_captured_at_when_no_captured_on(self):
        self.add_legacy_sidecar("legacy_one")
        self.assertEqual(L.build("abc"), 0)
        rows = self.read_assets()
        self.assertEqual(rows[0]["撮影日"], "2026-09-07")

    def test_fails_without_sidecars(self):
        self.assertEqual(L.build("abc"), 1)

    def test_missing_code_dir_leaves_commit_empty(self):
        self.assertEqual(L.code_commit(self.repo / "no-such-dir"), "")


class TestCheck(LedgerTestBase):
    def write_chapter(self, name, body):
        d = self.repo / "source"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{name}.rst").write_text(body, encoding="utf-8")

    def test_ok_when_consistent(self):
        self.add_sidecar("signin_form_initial")
        L.build("abc")
        self.write_chapter("signin", (
            ".. figure:: images/v70/signin_form_initial.png\n"
            "   :alt: サインイン画面\n"
            "\n"
            "   サインイン画面\n"
        ))
        self.write_placements([{
            "placement_id": "signin-1",
            "asset_id": "signin_form_initial",
            "章": "signin",
            "節": "サインイン",
            "alt": "サインイン画面",
            "caption": "サインイン画面",
        }])
        self.assertEqual(L.check(), 0)

    def test_detects_image_missing_from_ledger(self):
        (self.images / "orphan.png").write_bytes(b"png")
        self.assertEqual(L.check(), 1)

    def test_detects_ledger_row_without_image(self):
        self.add_sidecar("gone")
        L.build("abc")
        (self.repo / "source/images/v70/gone.png").unlink()
        self.assertEqual(L.check(), 1)

    def test_detects_placement_pointing_at_unknown_asset(self):
        self.write_placements([{
            "placement_id": "p1", "asset_id": "nope", "章": "signin",
            "節": "節", "alt": "a", "caption": "c",
        }])
        self.assertEqual(L.check(), 1)

    def test_detects_missing_alt_and_caption(self):
        self.add_sidecar("shot_one")
        L.build("abc")
        self.write_chapter("signin", ".. image:: images/v70/shot_one.png\n")
        self.write_placements([{
            "placement_id": "p1", "asset_id": "shot_one", "章": "signin",
            "節": "節", "alt": "", "caption": "",
        }])
        self.assertEqual(L.check(), 1)

    def test_detects_duplicate_placement_id(self):
        self.add_sidecar("shot_one")
        L.build("abc")
        self.write_chapter("signin", ".. image:: images/v70/shot_one.png\n   :alt: a\n\n   c\n")
        self.write_placements([
            {"placement_id": "p1", "asset_id": "shot_one", "章": "signin",
             "節": "節", "alt": "a", "caption": "c"},
            {"placement_id": "p1", "asset_id": "shot_one", "章": "signin",
             "節": "別の節", "alt": "a", "caption": "c"},
        ])
        self.assertEqual(L.check(), 1)

    def test_unplaced_asset_is_not_an_error(self):
        # 撮影が章より先に進むのは正常な進め方なので、失敗にはしない。
        self.add_sidecar("shot_one")
        L.build("abc")
        self.assertEqual(L.check(), 0)


if __name__ == "__main__":
    unittest.main()


class TestCheckAgainstManuscript(LedgerTestBase):
    """掲載箇所台帳と章の原稿の照合。"""

    def setUp(self):
        super().setUp()
        self.chapters = self.repo / "source"
        self.chapters.mkdir(parents=True, exist_ok=True)
        self.add_sidecar("signin_form_initial")
        L.build("abc")

    def write_chapter(self, name, body):
        (self.chapters / f"{name}.rst").write_text(body, encoding="utf-8")

    def placement(self, **over):
        row = {
            "placement_id": "signin-01",
            "asset_id": "signin_form_initial",
            "章": "signin",
            "節": "サインイン",
            "alt": "サインイン画面。入力欄がある。",
            "caption": "サインイン画面",
        }
        row.update(over)
        return row

    def test_ok_when_manuscript_matches(self):
        self.write_chapter("signin", (
            ".. figure:: images/v70/signin_form_initial.png\n"
            "   :alt: サインイン画面。入力欄がある。\n"
            "\n"
            "   サインイン画面\n"
        ))
        self.write_placements([self.placement()])
        self.assertEqual(L.check(), 0)

    def test_ok_when_alt_is_wrapped_across_lines(self):
        # RST は長い alt を折り返すので、改行をまたいでも一致とみなす。
        self.write_chapter("signin", (
            ".. figure:: images/v70/signin_form_initial.png\n"
            "   :alt: サインイン画面。\n"
            "      入力欄がある。\n"
            "\n"
            "   サインイン画面\n"
        ))
        self.write_placements([self.placement()])
        self.assertEqual(L.check(), 0)

    def test_detects_chapter_without_the_image(self):
        self.write_chapter("signin", "サインイン\n=========\n")
        self.write_placements([self.placement()])
        self.assertEqual(L.check(), 1)

    def test_detects_alt_drift(self):
        self.write_chapter("signin", (
            ".. figure:: images/v70/signin_form_initial.png\n"
            "   :alt: 古い説明文\n"
            "\n"
            "   サインイン画面\n"
        ))
        self.write_placements([self.placement()])
        self.assertEqual(L.check(), 1)

    def test_detects_missing_chapter_file(self):
        self.write_placements([self.placement(章="no_such_chapter")])
        self.assertEqual(L.check(), 1)
