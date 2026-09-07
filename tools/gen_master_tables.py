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
        ])
    return rows


# capability_parameter.section（basic / advanced）は列に出さない。
# 「ジョブ作成」フォーム（nuxt/components/job/capability-param-form.vue）は
# section を一切参照しておらず、項目の出し分けにも並び順にも使っていない。
# 画面が使うのは param_group の方。マスタに値はあるが画面に効かないものを
# 表に出すと、読者が画面上で対応を探せない。
PARAM_HEADERS = ["項目名", "キー", "型", "単位", "既定値", "範囲・制約", "選択肢", "表示条件"]
PARAM_WIDTHS = [18, 16, 8, 6, 12, 16, 22, 22]

# 「ジョブ作成」フォームが項目をまとめる見出し。フォームは
# job.parameters.physicalModel と job.parameters.groups.<param_group> を使う。
# 文言は nuxt/locals/ja/job.ts 由来で、マスタには入っていないのでここに置く。
PHYSICAL_GROUP_JA = "物理モデル"
PARAM_GROUP_JA = {
    "experimental": "実験パラメータ",
    "instrument": "装置パラメータ",
}


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


def _compute_steps(template: dict) -> list:
    """計算のステップだけを返す。

    role が付いているステップは計算ではなく入力の選択（既存 Job や構造を選ばせる
    タブ）。create2.vue の computeSteps と同じ判定にする。全ステップが選択用の
    場合は元のリストを返す（create2.vue も同じフォールバックをしている）。
    """
    steps = [s for s in template.get("steps", []) if not s.get("role")]
    return steps or template.get("steps", [])


def render_calc_list(dump: dict) -> str:
    """「ジョブ作成」の選択ダイアログに出る組み合わせの一覧。

    ダイアログが見せるのはテンプレート名（name_ja）ではなく、
    「計算ソフト」＝ステップが使うエンジンの表示名、
    「計算機能」＝テンプレートの代表 capability の名称。
    テンプレート名で表を作ると画面と一致しないので、ダイアログと同じ組み立てにする。
    """
    engines = {e["code"]: e.get("name") or e["code"] for e in dump.get("engines", [])}
    caps = {c["code"]: c.get("name_ja") or c["code"] for c in dump.get("capabilities", [])}

    rows = []
    for t in dump.get("workflow_templates", []):
        if not t.get("enabled"):
            continue
        steps = _compute_steps(t)
        engine_label = " + ".join(dict.fromkeys(engines.get(s["engine"], s["engine"]) for s in steps))
        cap_code = t.get("capability")
        step_label = " → ".join(caps.get(s["capability"], s["capability"]) for s in steps)
        rows.append([
            rst.escape(engine_label),
            rst.escape(caps.get(cap_code, cap_code or "-")),
            f"``{cap_code}``" if cap_code else "-",
            rst.escape(step_label),
        ])
    return (
        rst.header_comment(dump, SCRIPT)
        + rst.list_table(
            ["計算ソフト", "計算機能", "機能コード", "実行されるステップ"],
            rows,
            widths=[20, 24, 16, 40],
        )
    )


def _params_body(ec: dict) -> str:
    """入力項目の表だけを返す（ヘッダコメントを含まない）。

    表は「ジョブ作成」フォームと同じまとまりで分ける。フォームは
    物理モデル（physical_model_parameters）を先に出し、そのあとに
    capability parameter を param_group ごとにまとめて出す。
    1 つの大きな表にすると、読者が画面のどのまとまりの項目かを追えない。
    """
    params = ec.get("parameters") or []
    physical = ec.get("physical_model_parameters") or []
    params_by_key = {p["key"]: p for p in [*params, *physical]}

    if not params and not physical:
        return "この計算には、「ジョブ作成」で入力する項目はありません。\n"

    out = []

    def table(title: str, items: list) -> None:
        out.append(rst.section(rst.escape(title), "~"))
        out.append("\n")
        out.append(rst.list_table(PARAM_HEADERS, _param_rows(items, params_by_key),
                                  widths=PARAM_WIDTHS))
        out.append("\n")

    if physical:
        table(PHYSICAL_GROUP_JA, physical)

    # param_group の出現順を保つ（フォームも visibleParams の出現順で並べる）。
    for group in dict.fromkeys(p.get("param_group") for p in
                               sorted(params, key=lambda x: x.get("sort_order") or 0)):
        items = [p for p in params if p.get("param_group") == group]
        table(PARAM_GROUP_JA.get(group, group or "その他"), items)

    return "".join(out)


def render_params(ec: dict, dump: dict) -> str:
    return rst.header_comment(dump, SCRIPT) + _params_body(ec)


def render_params_all(dump: dict) -> str:
    """全 engine x capability の入力項目を、見出し付きで 1 ファイルにまとめる。

    章から include するのはこのファイルだけにする。params/<engine>_<cap>.rst を
    章ごとに手で並べると、マスタにエンジンや機能が増えたときに漏れる。
    実際、生成した 112 ファイルのうち 110 がどの章からも include されておらず、
    Sphinx に一度もパースされない状態だった（CLAUDE.md §3）。

    見出しの深さはこのリポジトリの階層に合わせる。
    小節（####）= 計算ソフト、小々節（++++）= 機能、その下に render_params が
    出す「~」の見出しが入る。include する側の節（----）の下に置くこと。
    """
    engine_names = {e["code"]: e.get("name") or e["code"] for e in dump.get("engines", [])}
    cap_names = {c["code"]: c.get("name_ja") or c["code"] for c in dump.get("capabilities", [])}

    out = [rst.header_comment(dump, SCRIPT)]
    for engine_code in dict.fromkeys(ec["engine"] for ec in dump["engine_capabilities"]):
        out.append("\n")
        out.append(rst.section(rst.escape(engine_names.get(engine_code, engine_code)), "#"))
        out.append("\n")
        for ec in dump["engine_capabilities"]:
            if ec["engine"] != engine_code:
                continue
            cap = ec["capability"]
            out.append(rst.section(rst.escape(cap_names.get(cap, cap)), "+"))
            out.append("\n")
            out.append(_params_body(ec))
            out.append("\n")
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
    write("params_all.rst", render_params_all(dump))
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
