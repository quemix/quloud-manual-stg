"""tools/gen_release_notes_v70.py のテスト。"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import gen_release_notes_v70 as g  # noqa: E402


def _row(number="1", judge="載せる", series="不具合修正", group="招待画面",
         text="〜する問題を解消"):
    return {"number": number, "判定": judge, "系統": series,
            "見出し": group, "掲載文": text}


class TestValidate(unittest.TestCase):
    def test_ok_rows_have_no_errors(self):
        self.assertEqual(g.validate([_row()]), [])

    def test_missing_group_is_reported(self):
        errors = g.validate([_row(number="42", group="")])
        self.assertEqual(len(errors), 1)
        self.assertIn("42", errors[0])

    def test_missing_text_is_reported(self):
        errors = g.validate([_row(number="42", text="")])
        self.assertEqual(len(errors), 1)
        self.assertIn("42", errors[0])

    def test_rows_not_marked_are_ignored(self):
        self.assertEqual(g.validate([_row(judge="載せない", group="", text="")]), [])


class TestRender(unittest.TestCase):
    def test_only_marked_rows_appear(self):
        out = g.render([_row(text="載る文"),
                        _row(number="2", judge="載せない", text="載らない文")])
        self.assertIn("載る文", out)
        self.assertNotIn("載らない文", out)

    def test_groups_are_bulleted(self):
        out = g.render([_row(group="招待画面", text="A")])
        self.assertIn("-   招待画面", out)
        self.assertIn("    -   A", out)

    def test_same_group_is_merged(self):
        out = g.render([_row(group="招待画面", text="A"),
                        _row(number="2", group="招待画面", text="B")])
        self.assertEqual(out.count("-   招待画面"), 1)
        self.assertIn("    -   A", out)
        self.assertIn("    -   B", out)

    def test_group_order_follows_group_order_list(self):
        # 画面系を先に、エンジン系を後に出す
        out = g.render([_row(group="Quantum ESPRESSO", text="Q"),
                        _row(number="2", group="ダッシュボード", text="D")])
        self.assertLess(out.index("ダッシュボード"), out.index("Quantum ESPRESSO"))

    def test_unknown_group_goes_last(self):
        out = g.render([_row(group="ZZZ 未知", text="Z"),
                        _row(number="2", group="ダッシュボード", text="D")])
        self.assertLess(out.index("ダッシュボード"), out.index("ZZZ 未知"))

    def test_series_order_within_group(self):
        out = g.render([_row(group="ダッシュボード", series="不具合修正", text="FIX"),
                        _row(number="2", group="ダッシュボード", series="新機能", text="NEW")])
        self.assertLess(out.index("NEW"), out.index("FIX"))

    def test_starts_with_version_heading(self):
        out = g.render([_row()])
        self.assertTrue(out.lstrip().startswith("**Ver.7.0**"))

    def test_empty_input_still_renders_heading(self):
        out = g.render([])
        self.assertIn("**Ver.7.0**", out)


if __name__ == "__main__":
    unittest.main()
