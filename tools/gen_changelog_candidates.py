#!/usr/bin/env python3
"""v7.0 マイルストーンの issue から、変更履歴の候補一覧を作る。

入力  : meta/v70_issues_closed.json（tools/fetch_issues.sh が作る）
出力  : meta/changelog_candidates.csv

載せる基準は「その不具合を引き起こしたコードが origin/release/prd（本番 v6.1.2）に
存在したか」。issue は手動クローズされていて修正コミットを機械的に辿れないため、
機械分類は「確実に載せない」「確実に新機能側」に絞り、残りは人が判定する。

再実行しても 判定 / 系統 / 掲載文 / 備考 の4列は保持する。
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO / "meta" / "v70_issues_closed.json"
DEFAULT_OUTPUT = REPO / "meta" / "changelog_candidates.csv"

COLUMNS = ["number", "title", "labels", "created_at", "closed_at", "url",
           "auto_class", "判定", "系統", "見出し", "掲載文", "備考"]

# 人が書き換える列。再実行で上書きしない。
MANUAL_COLUMNS = ["判定", "系統", "見出し", "掲載文", "備考"]

# v7.0 で新規に入ったエンジン。これらの issue は個別の不具合修正ではなく
# 「新機能」としてまとめて書くので、不具合修正の候補には入れない。
NEW_ENGINES = re.compile(
    r"asemd|ASE-MD|FLARE|RadonPy|hybmd|psi4|dft12|DFT-1/2|GROMACS|SPRKKR", re.IGNORECASE)

FEATURE_LABELS = {"enhancement", "request"}
INFRA_LABELS = {"DevOps", "infra", "maintenance"}

# v7 テスト仕様書の実施を開始した日。これ以降に立った issue の多くは
# v7.0 開発中に作り込まれて v7.0 開発中に直ったもの。
TEST_CAMPAIGN_START = "2026-08-22"

# 本番（v6.1.2）で実際に踏んだ不具合の報告に付くタグ。issue 報告者自身が
# 「これは本番で起きた」と書いたものなので、ラベルやタイトルのエンジン名、
# 起票日よりも「本番 v6.1.2 に存在したか」という一点に対する証拠として強い。
# だからラベル判定・エンジン判定・日付判定より先に、無条件でこれを見る。
# こうしないと、同じ本番不具合でもタイトルの書き方次第で
# 要判断(それ以前) と 新機能の一部(新5エンジン) のように別バケツに散ってしまう
# （#975 と #994 が実例）。地の文で「本番」と言及するだけの [stg] issue と
# 区別するため、角括弧付きの表記だけを見る（"本番" 単体では拾わない）。
HONBAN_TAG = "[本番]"
HONBAN_CLASS = "要判断(本番報告)"

# 直近の取得結果に issue が含まれなかった行に付ける印。
MISSING_CLASS = "issue が見つからない"


def classify(issue: dict) -> str:
    labels = {label["name"] for label in issue.get("labels", [])}
    title = issue.get("title", "")

    if HONBAN_TAG in title:
        return HONBAN_CLASS
    if labels & FEATURE_LABELS:
        return "新機能・変更候補"
    if title.startswith("[stg]") or (labels & INFRA_LABELS):
        return "載せない(インフラ/保守)"
    if NEW_ENGINES.search(title):
        return "新機能の一部(新5エンジン)"
    if (issue.get("createdAt") or "") >= TEST_CAMPAIGN_START:
        return "要判断(テスト仕様書実施期)"
    return "要判断(それ以前)"


def load_existing(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as f:
        return {row["number"]: row for row in csv.DictReader(f)}


def build_rows(issues: list, existing: dict[str, dict]) -> list[dict]:
    rows_by_number: dict[str, dict] = {}
    for issue in issues:
        number = str(issue["number"])
        prev = existing.get(number, {})
        row = {
            "number": number,
            "title": issue.get("title", ""),
            "labels": ",".join(sorted(label["name"] for label in issue.get("labels", []))),
            "created_at": (issue.get("createdAt") or "")[:10],
            "closed_at": (issue.get("closedAt") or "")[:10],
            "url": issue.get("url", ""),
            "auto_class": classify(issue),
        }
        for column in MANUAL_COLUMNS:
            row[column] = prev.get(column, "")
        rows_by_number[number] = row

    # 取得した issue に含まれない番号は、マイルストーンから外れた
    # （reopen で closed.json から消えた等）ということ。人手の判定を
    # 黙って失うと Task 7 の作業がやり直しになるので、既存の値をすべて
    # そのまま残し、auto_class だけ「見つからない」に付け替えて可視化する。
    for number, prev in existing.items():
        if number in rows_by_number:
            continue
        row = {column: prev.get(column, "") for column in COLUMNS}
        row["number"] = number
        row["auto_class"] = MISSING_CLASS
        rows_by_number[number] = row

    return sorted(rows_by_number.values(), key=lambda r: int(r["number"]), reverse=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not args.input.exists():
        print(f"issue の JSON がありません: {args.input}\n"
              f"先に tools/fetch_issues.sh を実行してください。", file=sys.stderr)
        return 1

    issues = json.loads(args.input.read_text(encoding="utf-8"))
    existing = load_existing(args.output)
    rows = build_rows(issues, existing)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["auto_class"]] = counts.get(row["auto_class"], 0) + 1
    judged = sum(1 for row in rows if row["判定"])
    print(f"wrote {args.output}  {len(rows)} 件（判定済み {judged} 件）")
    for name, count in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {count:4d}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
