#!/usr/bin/env python3
"""マスタデータの dump から Sphinx 用の RST 表を生成する。

入力  : meta/master_dump.json（tools/dump_master.sh が作る）
出力  : source/_generated/**.rst

出力は生成物なので手で編集しない。章本文からは .. include:: で取り込む。
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import rst  # noqa: E402

SCRIPT = "tools/gen_master_tables.py"
REPO = Path(__file__).resolve().parent.parent
DEFAULT_DUMP = REPO / "meta" / "master_dump.json"
DEFAULT_OUT = REPO / "source" / "_generated"

# params.<key> === '<value>' / === true / === false と、
# その否定形 params.<key> !== ... だけを解釈する。
# それ以外の式は日本語化せず原文のまま出す。
_CLAUSE = re.compile(
    r"^params\.([A-Za-z0-9_]+)\s*(===|!==)\s*(?:'([^']*)'|\"([^\"]*)\"|(true|false))$"
)

INPUT_TYPE_JA = {
    "integer": "整数",
    "number": "数値",
    "scientific": "数値（指数表記）",
    "select": "選択",
    "boolean": "有効・無効",
    "file": "ファイル",
    "string": "文字列",
    "text": "文字列",
}

SECTION_JA = {"basic": "基本", "advanced": "詳細"}


# --- 値の整形 -------------------------------------------------------------

def format_default(value) -> str:
    if value is None or value == "":
        return "-"
    if isinstance(value, bool):
        return "有効" if value else "無効"
    if isinstance(value, (list, dict)):
        return f"``{json.dumps(value, ensure_ascii=False)}``"
    return f"``{value}``"


def format_validation(rules) -> str:
    if not rules:
        return "-"
    parts: list[str] = []
    lo, hi = rules.get("min"), rules.get("max")
    if lo is not None and hi is not None:
        parts.append(f"{lo} 以上 {hi} 以下")
    elif lo is not None:
        parts.append(f"{lo} 以上")
    elif hi is not None:
        parts.append(f"{hi} 以下")
    if rules.get("step") is not None:
        parts.append(f"刻み {rules['step']}")
    if rules.get("required"):
        parts.append("必須")
    return "、".join(parts) if parts else "-"


def _option_label(option: dict) -> str:
    return option.get("label_ja") or option.get("label_en") or str(option.get("value"))


def format_options(options) -> str:
    if not options:
        return "-"
    return " / ".join(
        f"{rst.escape(_option_label(o))}（``{o.get('value')}``）" for o in options
    )


def format_condition(condition, params_by_key: dict) -> str:
    """表示条件の式を日本語にする。解釈できない式は原文のまま出す。

    !== （否定）は、値が有効・無効（真偽値）に解決される場合はもう一方の
    状態に読み替える（二重否定を避ける）。それ以外の値は「<値>以外」にする。
    """
    if not condition:
        return "-"
    rendered: list[str] = []
    for clause in condition.split("&&"):
        m = _CLAUSE.match(clause.strip())
        if not m:
            return f"``{condition}``"
        key, op = m.group(1), m.group(2)
        raw = next(v for v in (m.group(3), m.group(4), m.group(5)) if v is not None)
        param = params_by_key.get(key) or {}
        key_label = param.get("label_ja") or key
        value_label = None
        for option in param.get("options") or []:
            if str(option.get("value")) == raw:
                value_label = _option_label(option)
                break
        if value_label is None:
            value_label = {"true": "有効", "false": "無効"}.get(raw, raw)
        key_label = rst.escape(key_label)
        if op == "===":
            rendered.append(f"「{key_label}」が「{rst.escape(value_label)}」")
        elif value_label == "有効":
            rendered.append(f"「{key_label}」が「無効」")
        elif value_label == "無効":
            rendered.append(f"「{key_label}」が「有効」")
        else:
            rendered.append(f"「{key_label}」が「{rst.escape(value_label)}」以外")
    return "、かつ".join(rendered) + "のとき"


# --- 表の生成 -------------------------------------------------------------

def _engine_name(dump: dict, code: str) -> str:
    for e in dump.get("engines", []):
        if e["code"] == code:
            return e.get("name") or code
    return code


def _capability_name(dump: dict, code: str) -> str:
    for c in dump.get("capabilities", []):
        if c["code"] == code:
            return c.get("name_ja") or c.get("name_en") or code
    return code


def _param_rows(params: list, params_by_key: dict) -> list[list[str]]:
    rows = []
    for p in sorted(params, key=lambda x: x.get("sort_order") or 0):
        rows.append([
            rst.escape(p.get("label_ja") or p.get("label_en")),
            f"``{p['key']}``",
            INPUT_TYPE_JA.get(p.get("input_type"), rst.escape(p.get("input_type"))),
            rst.escape(p.get("unit")),
            format_default(p.get("default_value")),
            format_validation(p.get("validation_rules")),
            format_options(p.get("options")),
            format_condition(p.get("condition"), params_by_key),
            SECTION_JA.get(p.get("section"), rst.escape(p.get("section"))),
        ])
    return rows


PARAM_HEADERS = ["項目名", "キー", "型", "単位", "既定値", "範囲・制約", "選択肢", "表示条件", "区分"]
PARAM_WIDTHS = [16, 14, 8, 6, 10, 14, 20, 20, 6]


def render_engine_matrix(dump: dict) -> str:
    # engine_capability.visible は列に出さない。マスタでは「UI 表示フラグ」だが、
    # Ver.7.0 の画面でこのフラグを見ているのは /api/capabilities（Job 検索の
    # ソフトウェア絞り込みリスト）だけで、「ジョブ作成」で選べるかどうかとは
    # 対応していない。実測では visible=false の matdyn_disp / matdyn_dos が
    # 選択できるテンプレート「フォノンバンド」「フォノン状態密度」の代表
    # capability であり、逆に visible=true の bands は単独では選べない。
    # ○/× を出すと読者に「使えない機能」と読まれるので列自体を落とす。
    rows = []
    for ec in dump["engine_capabilities"]:
        rows.append([
            rst.escape(_engine_name(dump, ec["engine"])),
            f"``{ec['engine']}``",
            rst.escape(_capability_name(dump, ec["capability"])),
            f"``{ec['capability']}``",
            rst.escape(ec.get("ui_group_label_ja")),
        ])
    return (
        rst.header_comment(dump, SCRIPT)
        + rst.list_table(
            ["計算エンジン", "エンジンコード", "機能", "機能コード", "区分"],
            rows,
            widths=[22, 14, 28, 20, 16],
        )
    )


def render_calc_list(dump: dict) -> str:
    rows = []
    for t in dump.get("workflow_templates", []):
        if not t.get("enabled"):
            continue
        rows.append([
            rst.escape(t.get("name_ja")),
            rst.escape(t.get("name_en")),
            f"``{t.get('capability')}``" if t.get("capability") else "-",
        ])
    return (
        rst.header_comment(dump, SCRIPT)
        + rst.list_table(["名称", "英語表記", "機能コード"], rows, widths=[40, 40, 20])
    )


def render_params(ec: dict, dump: dict) -> str:
    params = ec.get("parameters") or []
    physical = ec.get("physical_model_parameters") or []
    params_by_key = {p["key"]: p for p in [*params, *physical]}

    out = [rst.header_comment(dump, SCRIPT)]
    if not params and not physical:
        out.append(
            "この計算には、Create Job ダイアログで入力する項目はありません。\n"
        )
        return "".join(out)

    if params:
        out.append(rst.list_table(PARAM_HEADERS, _param_rows(params, params_by_key),
                                  widths=PARAM_WIDTHS))
    if physical:
        out.append("\n")
        out.append(rst.section("物理モデルパラメータ", "~"))
        out.append("\n")
        out.append(rst.list_table(PARAM_HEADERS, _param_rows(physical, params_by_key),
                                  widths=PARAM_WIDTHS))
    return "".join(out)


def render_artifacts(ec: dict, dump: dict) -> str:
    specs = ec.get("artifact_specs") or []
    out = [rst.header_comment(dump, SCRIPT)]
    if not specs:
        out.append("この計算には、出力ファイルの登録はありません。\n")
        return "".join(out)
    rows = []
    for a in sorted(specs, key=lambda x: (x.get("artifact_role") or "", x.get("artifact_key") or "")):
        rows.append([
            f"``{a.get('filename_pattern')}``" if a.get("filename_pattern") else "-",
            rst.escape(a.get("description")),
            rst.escape(a.get("format")),
            "○" if a.get("downloadable") else "×",
            "必須" if a.get("is_required") else "任意",
        ])
    out.append(rst.list_table(
        ["ファイル", "内容", "形式", "ダウンロード", "出力"], rows, widths=[28, 34, 12, 12, 8]))
    return "".join(out)


# --- 書き出し -------------------------------------------------------------

def generate(dump: dict, out_dir: Path) -> list[Path]:
    """RST を書き出し、書いたファイルの一覧を返す。

    マスタから消えた engine_capability の RST が残ると、実在しない計算が
    マニュアルに載るので、params/ と artifacts/ は毎回作り直す。
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    for sub in ("params", "artifacts"):
        shutil.rmtree(out_dir / sub, ignore_errors=True)
        (out_dir / sub).mkdir(parents=True)

    written: list[Path] = []

    def write(rel: str, text: str) -> None:
        path = out_dir / rel
        path.write_text(text, encoding="utf-8")
        written.append(path)

    write("engine_matrix.rst", render_engine_matrix(dump))
    write("calc_list.rst", render_calc_list(dump))
    for ec in dump["engine_capabilities"]:
        slug = f"{ec['engine']}_{ec['capability']}"
        write(f"params/{slug}.rst", render_params(ec, dump))
        write(f"artifacts/{slug}.rst", render_artifacts(ec, dump))
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dump", type=Path, default=DEFAULT_DUMP)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    if not args.dump.exists():
        print(f"dump がありません: {args.dump}\n先に make dump を実行してください。", file=sys.stderr)
        return 1

    dump = json.loads(args.dump.read_text(encoding="utf-8"))
    written = generate(dump, args.out)
    print(f"generated {len(written)} files under {args.out}")
    print(f"  source_commit={dump.get('source_commit', '(不明)')[:8]} "
          f"({dump.get('source_branch', '(不明)')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
