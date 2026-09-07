"""tools/rst.py のテスト。"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import rst  # noqa: E402


class TestEscape(unittest.TestCase):
    def test_none_becomes_hyphen(self):
        self.assertEqual(rst.escape(None), "-")

    def test_empty_becomes_hyphen(self):
        self.assertEqual(rst.escape(""), "-")

    def test_plain_text_passes_through(self):
        self.assertEqual(rst.escape("SCF 最大反復回数"), "SCF 最大反復回数")

    def test_inline_markup_is_escaped(self):
        # * ` | _ \ は RST のインライン記法なのでエスケープする
        self.assertEqual(rst.escape("a*b"), r"a\*b")
        self.assertEqual(rst.escape("a|b"), r"a\|b")
        self.assertEqual(rst.escape("a_b"), r"a\_b")
        self.assertEqual(rst.escape("a`b"), r"a\`b")

    def test_newline_becomes_space(self):
        self.assertEqual(rst.escape("a\nb"), "a b")


class TestListTable(unittest.TestCase):
    def test_renders_header_and_rows(self):
        out = rst.list_table(["項目", "値"], [["A", "1"], ["B", "2"]])
        self.assertIn(".. list-table::", out)
        self.assertIn("   :header-rows: 1", out)
        self.assertIn("   * - 項目\n     - 値", out)
        self.assertIn("   * - A\n     - 1", out)
        self.assertIn("   * - B\n     - 2", out)

    def test_widths_are_emitted(self):
        out = rst.list_table(["a", "b"], [["1", "2"]], widths=[30, 70])
        self.assertIn("   :widths: 30 70", out)

    def test_empty_rows_returns_empty_string(self):
        # 行が無い list-table は Sphinx がエラーにするので、空文字を返す
        self.assertEqual(rst.list_table(["a"], []), "")


class TestHeaderComment(unittest.TestCase):
    def test_contains_commit_and_timestamp(self):
        dump = {"source_commit": "abc1234def", "source_branch": "dev_v700_ji",
                "generated_at": "2026-09-07T06:00:00Z",
                "master_synced_at": "2026-09-07T05:00:00Z"}
        out = rst.header_comment(dump, "tools/gen_master_tables.py")
        self.assertIn("手で編集しないでください", out)
        self.assertIn("abc1234def", out)
        self.assertIn("dev_v700_ji", out)
        self.assertIn("2026-09-07T06:00:00Z", out)
        self.assertIn("2026-09-07T05:00:00Z", out)
        # マスタ取得日時（dump 実行）とマスタ同期日時は読者が混同しうる別物なので、
        # ラベル文言そのものと「取得日時の直後に同期日時が来る」順序を固定する。
        lines = out.splitlines()
        generated_idx = lines.index(".. マスタ取得日時（dump 実行）: 2026-09-07T06:00:00Z")
        self.assertEqual(lines[generated_idx + 1], ".. マスタ同期日時: 2026-09-07T05:00:00Z")
        for line in out.splitlines():
            if line.strip():
                self.assertTrue(line.startswith(".."), f"コメント行でない: {line!r}")

    def test_missing_keys_do_not_raise(self):
        out = rst.header_comment({}, "x.py")
        self.assertIn("(不明)", out)
        sync_line = next(line for line in out.splitlines() if "マスタ同期日時" in line)
        self.assertIn("(不明)", sync_line)


class TestSection(unittest.TestCase):
    def test_rule_matches_display_width(self):
        # 日本語は幅2として数える。罫線が短いと Sphinx が警告を出す。
        out = rst.section("入力項目", "=")
        over, title, under = out.strip().splitlines()
        self.assertEqual(title, "入力項目")
        self.assertEqual(over, "=" * 8)
        self.assertEqual(under, "=" * 8)

    def test_has_overline(self):
        # 上線が無いと、章へ include したときに既存の見出し書式と衝突して
        # "Title level inconsistent" でビルドが落ちる。
        out = rst.section("QE", "-")
        self.assertEqual(out, "--\nQE\n--\n")


if __name__ == "__main__":
    unittest.main()
