"""tools/gen_changelog_candidates.py のテスト。"""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import gen_changelog_candidates as g  # noqa: E402


def _issue(number=1, title="タイトル", labels=(), created="2026-07-01T00:00:00Z",
           closed="2026-07-02T00:00:00Z"):
    return {
        "number": number, "title": title,
        "labels": [{"name": n} for n in labels],
        "createdAt": created, "closedAt": closed,
        "url": f"https://example.invalid/{number}",
    }


class TestClassify(unittest.TestCase):
    def test_enhancement_is_feature_candidate(self):
        self.assertEqual(g.classify(_issue(labels=["enhancement"])), "新機能・変更候補")
        self.assertEqual(g.classify(_issue(labels=["request"])), "新機能・変更候補")

    def test_stg_prefix_is_excluded(self):
        self.assertEqual(
            g.classify(_issue(title="[stg] postsetup が壊れている")), "載せない(インフラ/保守)")

    def test_infra_labels_are_excluded(self):
        for label in ("DevOps", "infra", "maintenance"):
            self.assertEqual(g.classify(_issue(labels=[label])), "載せない(インフラ/保守)")

    def test_new_engine_titles_go_to_feature_bucket(self):
        for title in ("【ASE-MD】NEB が失敗する", "【FLARE】otf の固定値",
                      "【RadonPy】不正な SMILES", "hybmd の入力生成",
                      "psi4 の結果カード", "【SPRKKR】parse スクリプトが無い",
                      "GROMACS のログ", "dft12 の UPF"):
            self.assertEqual(g.classify(_issue(title=title)), "新機能の一部(新5エンジン)",
                             msg=title)

    def test_enhancement_wins_over_new_engine(self):
        # ラベル判定を先に見る。新機能ラベルが付いていればそちらを優先する。
        self.assertEqual(
            g.classify(_issue(title="【ASE-MD】新機能", labels=["enhancement"])),
            "新機能・変更候補")

    def test_recent_bug_needs_judgement_marked_as_test_campaign(self):
        self.assertEqual(
            g.classify(_issue(title="一覧が壊れる", labels=["bug"],
                              created="2026-08-25T00:00:00Z")),
            "要判断(テスト仕様書実施期)")

    def test_older_issue_needs_judgement(self):
        self.assertEqual(
            g.classify(_issue(title="招待画面の検索", created="2026-07-29T00:00:00Z")),
            "要判断(それ以前)")

    def test_boundary_date_is_inclusive(self):
        self.assertEqual(
            g.classify(_issue(title="x", created="2026-08-22T00:00:00Z")),
            "要判断(テスト仕様書実施期)")
        self.assertEqual(
            g.classify(_issue(title="x", created="2026-08-21T23:59:59Z")),
            "要判断(それ以前)")


class TestBuildRows(unittest.TestCase):
    def test_row_has_all_columns(self):
        rows = g.build_rows([_issue(number=42, labels=["bug"])], {})
        self.assertEqual(len(rows), 1)
        self.assertEqual(set(rows[0].keys()), set(g.COLUMNS))
        self.assertEqual(rows[0]["number"], "42")
        self.assertEqual(rows[0]["labels"], "bug")
        self.assertEqual(rows[0]["判定"], "")

    def test_sorted_by_number_descending(self):
        rows = g.build_rows([_issue(number=1), _issue(number=99)], {})
        self.assertEqual([r["number"] for r in rows], ["99", "1"])

    def test_existing_judgement_is_preserved(self):
        # 再実行で人手の判定が消えると、判断のやり直しになる
        existing = {"42": {"判定": "載せる", "系統": "不具合修正", "見出し": "招待画面",
                           "掲載文": "招待画面の検索結果が正しくなるよう修正", "備考": "本番で再現"}}
        rows = g.build_rows([_issue(number=42)], existing)
        self.assertEqual(rows[0]["判定"], "載せる")
        self.assertEqual(rows[0]["系統"], "不具合修正")
        self.assertEqual(rows[0]["見出し"], "招待画面")
        self.assertEqual(rows[0]["掲載文"], "招待画面の検索結果が正しくなるよう修正")
        self.assertEqual(rows[0]["備考"], "本番で再現")

    def test_auto_class_is_refreshed_even_when_existing(self):
        # auto_class は機械が付け直す。人手で書き換えるのは 判定 以降の列だけ。
        existing = {"42": {"判定": "載せる", "auto_class": "古い分類"}}
        rows = g.build_rows([_issue(number=42, labels=["enhancement"])], existing)
        self.assertEqual(rows[0]["auto_class"], "新機能・変更候補")

    def test_title_is_refreshed(self):
        existing = {"42": {"判定": "載せる", "title": "昔のタイトル"}}
        rows = g.build_rows([_issue(number=42, title="いまのタイトル")], existing)
        self.assertEqual(rows[0]["title"], "いまのタイトル")


class TestLoadExisting(unittest.TestCase):
    def test_missing_file_returns_empty(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(g.load_existing(Path(td) / "nope.csv"), {})

    def test_reads_back_written_csv(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "c.csv"
            rows = g.build_rows([_issue(number=7)], {})
            rows[0]["判定"] = "載せない"
            with path.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=g.COLUMNS)
                w.writeheader()
                w.writerows(rows)
            existing = g.load_existing(path)
            self.assertEqual(existing["7"]["判定"], "載せない")


if __name__ == "__main__":
    unittest.main()
