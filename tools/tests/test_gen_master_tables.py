"""tools/gen_master_tables.py のテスト。"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import gen_master_tables as g  # noqa: E402


def _param(**kw):
    base = {
        "key": "scf_max_iter", "param_group": "experimental", "section": "advanced",
        "input_type": "integer", "label_ja": "SCF 最大反復回数", "label_en": "Max SCF Iterations",
        "unit": None, "default_value": 100, "validation_rules": {"min": 1, "max": 1000},
        "options": [], "condition": None, "sort_order": 50, "source": "canonical",
    }
    base.update(kw)
    return base


def _dump(**kw):
    base = {
        "source_commit": "abc1234", "source_branch": "dev_v700_ji",
        "generated_at": "2026-09-07T06:00:00Z",
        "engines": [{"code": "qe", "name": "Quantum ESPRESSO", "description": "", "active": True}],
        "capabilities": [{"code": "scf", "name_ja": "電子状態 SCF", "name_en": "Single-Point SCF",
                          "description_ja": "", "description_en": ""}],
        "workflow_templates": [
            {"key": "qe_scf", "capability": "scf", "name_ja": "自己無撞着電子状態計算（QE）",
             "name_en": "Self-consistent Electronic Structure Calculation (QE)", "enabled": True},
            {"key": "qe_old", "capability": "scf", "name_ja": "旧", "name_en": "Old", "enabled": False},
        ],
        "engine_capabilities": [{
            "engine": "qe", "capability": "scf", "visible": True, "recommended": False,
            "sort_order": 10, "ui_group_key": "first_principles",
            "ui_group_label_ja": "第一原理計算", "legacy_rsdft_job_type": 2,
            "legacy_software_code": "qe",
            "parameters": [_param()], "physical_model_parameters": [],
            "artifact_specs": [], "property_mappings": [],
        }],
    }
    base.update(kw)
    return base


class TestFormatDefault(unittest.TestCase):
    def test_none(self):
        self.assertEqual(g.format_default(None), "-")

    def test_bool(self):
        self.assertEqual(g.format_default(True), "有効")
        self.assertEqual(g.format_default(False), "無効")

    def test_number_is_literal(self):
        self.assertEqual(g.format_default(100), "``100``")

    def test_string_is_literal(self):
        self.assertEqual(g.format_default("PBE"), "``PBE``")

    def test_list_is_json_literal(self):
        self.assertEqual(g.format_default([1, 2]), "``[1, 2]``")

    def test_empty_string_is_hyphen(self):
        self.assertEqual(g.format_default(""), "-")


class TestFormatValidation(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(g.format_validation({}), "-")
        self.assertEqual(g.format_validation(None), "-")

    def test_min_and_max(self):
        self.assertEqual(g.format_validation({"min": 1, "max": 1000}), "1 以上 1000 以下")

    def test_min_only(self):
        self.assertEqual(g.format_validation({"min": 0}), "0 以上")

    def test_max_only(self):
        self.assertEqual(g.format_validation({"max": 10}), "10 以下")

    def test_required(self):
        self.assertEqual(g.format_validation({"required": True}), "必須")

    def test_combined(self):
        self.assertEqual(
            g.format_validation({"min": 1, "max": 2000, "required": True}),
            "1 以上 2000 以下、必須",
        )

    def test_step(self):
        self.assertEqual(g.format_validation({"step": 0.1}), "刻み 0.1")


class TestFormatOptions(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(g.format_options([]), "-")

    def test_label_and_value(self):
        out = g.format_options([{"value": "GGA_PBE96", "label_ja": "GGA-PBE", "label_en": "GGA-PBE"}])
        self.assertEqual(out, "GGA-PBE（``GGA_PBE96``）")

    def test_falls_back_to_english_then_value(self):
        self.assertEqual(g.format_options([{"value": "x", "label_en": "X"}]), "X（``x``）")
        self.assertEqual(g.format_options([{"value": "y"}]), "y（``y``）")

    def test_multiple_joined(self):
        out = g.format_options([{"value": "a", "label_ja": "A"}, {"value": "b", "label_ja": "B"}])
        self.assertEqual(out, "A（``a``） / B（``b``）")

    def test_label_with_rst_metacharacter_is_escaped(self):
        # ラベルに "|" があると、そのままでは RST の置換参照として
        # 解釈されてしまう（Undefined substitution referenced エラー）。
        out = g.format_options([{"value": "OptC4", "label_ja": "|a1|=|a2|≠|a3|・最急降下"}])
        self.assertEqual(out, r"\|a1\|=\|a2\|≠\|a3\|・最急降下（``OptC4``）")


class TestFormatCondition(unittest.TestCase):
    def setUp(self):
        self.params = {
            "ensemble": _param(key="ensemble", label_ja="アンサンブル", input_type="select",
                               options=[{"value": "NPT", "label_ja": "NPT（定圧定温）"},
                                        {"value": "NVT", "label_ja": "NVT（定積定温）"}]),
            "henkelman": _param(key="henkelman", label_ja="Henkelman 補正", input_type="boolean",
                                options=[]),
        }

    def test_none(self):
        self.assertEqual(g.format_condition(None, self.params), "-")

    def test_single_clause_uses_labels(self):
        out = g.format_condition("params.ensemble === 'NPT'", self.params)
        self.assertEqual(out, "「アンサンブル」が「NPT（定圧定温）」のとき")

    def test_two_clauses_joined(self):
        out = g.format_condition(
            "params.ensemble === 'NPT' && params.henkelman === true", self.params)
        self.assertEqual(
            out, "「アンサンブル」が「NPT（定圧定温）」、かつ「Henkelman 補正」が「有効」のとき")

    def test_unknown_key_falls_back_to_raw_key(self):
        out = g.format_condition("params.nosuch === 'x'", self.params)
        self.assertEqual(out, "「nosuch」が「x」のとき")

    def test_unparsable_expression_is_emitted_verbatim(self):
        # 想定外の式を勝手に日本語にしない。原文をそのまま出す。
        out = g.format_condition("params.a > 3", self.params)
        self.assertEqual(out, "``params.a > 3``")

    def test_negated_boolean_inverts_to_the_other_state(self):
        out = g.format_condition("params.henkelman !== true", self.params)
        self.assertEqual(out, "「Henkelman 補正」が「無効」のとき")

    def test_negated_false_boolean_inverts_to_enabled(self):
        out = g.format_condition("params.henkelman !== false", self.params)
        self.assertEqual(out, "「Henkelman 補正」が「有効」のとき")

    def test_negated_select_value_uses_igai(self):
        out = g.format_condition("params.ensemble !== 'NPT'", self.params)
        self.assertEqual(out, "「アンサンブル」が「NPT（定圧定温）」以外のとき")

    def test_negation_combines_with_conjunction(self):
        out = g.format_condition(
            "params.ensemble === 'NPT' && params.henkelman !== true", self.params)
        self.assertEqual(
            out, "「アンサンブル」が「NPT（定圧定温）」、かつ「Henkelman 補正」が「無効」のとき")

    def test_metacharacter_in_label_is_escaped(self):
        # key_label・value_label のどちらに RST のメタ文字（"|" など）が
        # 含まれていても、そのまま出すと置換参照として誤解釈される。
        params = {
            "opt_method": _param(key="opt_method", label_ja="最適化手法|種別", input_type="select",
                                 options=[{"value": "OptC4", "label_ja": "|a1|=|a2|"}]),
        }
        out = g.format_condition("params.opt_method === 'OptC4'", params)
        self.assertEqual(out, r"「最適化手法\|種別」が「\|a1\|=\|a2\|」のとき")


class TestRenderEngineMatrix(unittest.TestCase):
    def test_contains_engine_and_capability(self):
        out = g.render_engine_matrix(_dump())
        self.assertIn("Quantum ESPRESSO", out)
        self.assertIn("電子状態 SCF", out)
        self.assertIn("第一原理計算", out)
        self.assertIn(".. list-table::", out)

    def test_has_no_visible_column(self):
        # visible は Ver.7.0 の画面で選択可否を表さないので列に出さない。
        # ○/× を出すと読者に「使えない機能」と誤読される。
        out = g.render_engine_matrix(_dump())
        self.assertNotIn("画面表示", out)
        self.assertNotIn("○", out)
        self.assertNotIn("×", out)


class TestRenderCalcList(unittest.TestCase):
    def test_only_enabled_templates(self):
        out = g.render_calc_list(_dump())
        self.assertIn("自己無撞着電子状態計算（QE）", out)
        self.assertNotIn("旧", out)


class TestRenderParams(unittest.TestCase):
    def test_table_has_all_columns(self):
        ec = _dump()["engine_capabilities"][0]
        out = g.render_params(ec, _dump())
        for col in ["項目名", "キー", "型", "単位", "既定値", "範囲・制約", "選択肢", "表示条件", "区分"]:
            self.assertIn(col, out)
        self.assertIn("SCF 最大反復回数", out)
        self.assertIn("``scf_max_iter``", out)
        self.assertIn("1 以上 1000 以下", out)

    def test_no_parameters_emits_note_not_empty_table(self):
        # qe/band_structure、qe/dos、radonpy/polymer_sp は入力項目が0件。
        # 空の list-table は Sphinx がエラーにするので、注記を出す。
        d = _dump()
        d["engine_capabilities"][0]["parameters"] = []
        ec = d["engine_capabilities"][0]
        out = g.render_params(ec, d)
        self.assertNotIn(".. list-table::", out)
        self.assertIn("入力する項目はありません", out)

    def test_physical_model_parameters_get_their_own_table(self):
        d = _dump()
        d["engine_capabilities"][0]["physical_model_parameters"] = [
            _param(key="temperature", label_ja="温度", unit="K", source="physical_model")
        ]
        ec = d["engine_capabilities"][0]
        out = g.render_params(ec, d)
        self.assertIn("物理モデルパラメータ", out)
        self.assertIn("温度", out)


class TestRenderArtifacts(unittest.TestCase):
    def test_lists_downloadable_files(self):
        d = _dump()
        d["engine_capabilities"][0]["artifact_specs"] = [{
            "artifact_key": "qe_scf_out", "artifact_role": "main_output",
            "artifact_type": "log", "description": "SCF の標準出力",
            "downloadable": True, "filename_pattern": "QuloudJob_SCF.log",
            "format": "text", "generator_key": None, "is_multiple": False,
            "is_required": True, "parser_name": None, "retention_class": "long",
        }]
        ec = d["engine_capabilities"][0]
        out = g.render_artifacts(ec, d)
        self.assertIn("QuloudJob_SCF.log", out)
        self.assertIn("SCF の標準出力", out)

    def test_no_artifacts_emits_note(self):
        ec = _dump()["engine_capabilities"][0]
        out = g.render_artifacts(ec, _dump())
        self.assertNotIn(".. list-table::", out)
        self.assertIn("出力ファイルの登録はありません", out)


class TestGenerate(unittest.TestCase):
    def test_writes_expected_files(self):
        with tempfile.TemporaryDirectory() as td:
            out_dir = Path(td)
            written = g.generate(_dump(), out_dir)
            names = {p.relative_to(out_dir).as_posix() for p in written}
            self.assertIn("engine_matrix.rst", names)
            self.assertIn("calc_list.rst", names)
            self.assertIn("params/qe_scf.rst", names)
            self.assertIn("artifacts/qe_scf.rst", names)
            for p in written:
                text = p.read_text(encoding="utf-8")
                self.assertTrue(text.startswith(".. これは"), f"生成ヘッダが無い: {p}")
                self.assertIn("abc1234", text)

    def test_removes_stale_generated_files(self):
        # マスタから消えた ec の RST が残ると、実在しない計算がマニュアルに載る
        with tempfile.TemporaryDirectory() as td:
            out_dir = Path(td)
            (out_dir / "params").mkdir(parents=True)
            stale = out_dir / "params" / "qe_removed.rst"
            stale.write_text(".. stale\n", encoding="utf-8")
            g.generate(_dump(), out_dir)
            self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
