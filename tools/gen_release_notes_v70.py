#!/usr/bin/env python3
"""判定済みの候補一覧から、変更履歴の Ver.7.0 の項を生成する。

入力  : meta/changelog_candidates.csv と meta/changelog_manual_entries.csv
出力  : source/_generated/release_notes_v70.rst

既存の source/release_notes.rst（Ver.6.1.2 以前）と同じ書式に揃える。
見出し（画面・エンジン）ごとの箇条書きで、各見出しの後ろに行ブロック | を置く。
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_CANDIDATES = REPO / "meta" / "changelog_candidates.csv"
DEFAULT_MANUAL = REPO / "meta" / "changelog_manual_entries.csv"
DEFAULT_OUTPUT = REPO / "source" / "_generated" / "release_notes_v70.rst"

# 見出しの並び順。画面系を先に、計算エンジンを後に置く。
# ここに無い見出しは、この一覧の後ろに並ぶ。
GROUP_ORDER = [
    "サインアップ", "サインイン", "招待画面", "ダッシュボード",
    "Material の登録", "Material 詳細画面", "モデリング画面",
    "計算 Job の登録", "計算 Job の実行", "Property", "計算結果の可視化",
    "ファイル", "ヘッダーメニュー", "全般",
    "Quantum ESPRESSO", "OpenMX", "RSDFT", "LAMMPS", "GROMACS",
    "ASE", "FLARE", "SPRKKR", "Quloud-Mag", "RadonPy", "Psi4", "hybmd", "DFT-1/2",
]

# 見出しの中での並び順。
SERIES_ORDER = ["新機能", "変更", "不具合修正", "注意事項"]


def load_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate(rows: list[dict]) -> list[str]:
    """載せると判定した行に見出しと掲載文があるかを確かめる。"""
    errors = []
    for row in rows:
        if row.get("判定") != "載せる":
            continue
        if not row.get("見出し"):
            errors.append(f"#{row.get('number')}: 見出しが空")
        if not row.get("掲載文"):
            errors.append(f"#{row.get('number')}: 掲載文が空")
    return errors


def _group_key(group: str):
    try:
        return (0, GROUP_ORDER.index(group), "")
    except ValueError:
        return (1, 0, group)


def _series_key(series: str) -> int:
    try:
        return SERIES_ORDER.index(series)
    except ValueError:
        return len(SERIES_ORDER)


def render(rows: list[dict]) -> str:
    marked = [r for r in rows if r.get("判定") == "載せる"]
    grouped: dict[str, list[dict]] = {}
    for row in marked:
        grouped.setdefault(row.get("見出し", ""), []).append(row)

    lines = ["**Ver.7.0**", "", "|", ""]
    for group in sorted(grouped, key=_group_key):
        lines.append(f"-   {group}")
        lines.append("")
        for row in sorted(grouped[group], key=lambda r: _series_key(r.get("系統", ""))):
            lines.append(f"    -   {row['掲載文']}")
        lines.append("")
        lines.append("    |")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--manual", type=Path, default=DEFAULT_MANUAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = load_rows(args.candidates) + load_rows(args.manual)
    if not rows:
        print(f"候補がありません: {args.candidates}", file=sys.stderr)
        return 1

    errors = validate(rows)
    if errors:
        print("載せると判定した行に不足があります:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(rows), encoding="utf-8")
    marked = sum(1 for r in rows if r.get("判定") == "載せる")
    print(f"wrote {args.output}  掲載 {marked} 件 / 候補 {len(rows)} 件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
