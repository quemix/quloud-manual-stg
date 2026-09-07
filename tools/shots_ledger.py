#!/usr/bin/env python3
"""画面キャプチャの台帳（meta/images_assets.csv, meta/images_placements.csv）を扱う。

台帳を 2 枚に分けているのは、変わる理由が違うため（設計書 §6.3）。

- images_assets.csv    : 画像ファイルの台帳。**このスクリプトが機械的に書く。**
                         撮影日・参照コミット・ビューポートといった撮影の事実だけ。
- images_placements.csv: 掲載箇所の台帳。**人が書く。** どの章のどの節でどの画像を
                         使い、alt とキャプションを何にするか。編集方針の話なので
                         自動生成しない。build は触らない。

使い方:
    python tools/shots_ledger.py build   # shots/.out/*.json を assets に取り込む
    python tools/shots_ledger.py check   # 画像・assets・placements の整合を検査する

CSV は必ず csv モジュールで読み書きする。sed や手編集はフィールド内のカンマ・
引用符・日本語約物で行を壊す（CLAUDE.md §5 と同じ理由）。
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "shots" / ".out"
IMAGE_DIR = REPO / "source" / "images" / "v70"
ASSETS_CSV = REPO / "meta" / "images_assets.csv"
PLACEMENTS_CSV = REPO / "meta" / "images_placements.csv"

ASSET_FIELDS = [
    "asset_id",
    "file",
    "章",
    "機能",
    "状態",
    "撮影日",
    "参照コミット",
    "ビューポート",
]
PLACEMENT_FIELDS = ["placement_id", "asset_id", "章", "節", "alt", "caption"]


def code_commit(code_dir: Path) -> str:
    """撮影時に参照していたアプリのコミット。取れなければ空にする。"""
    try:
        out = subprocess.run(
            ["git", "-C", str(code_dir), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def read_csv(path: Path, fields: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for key in fields:
            row.setdefault(key, "")
    return rows


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def build(commit: str) -> int:
    """shots/.out/*.json を images_assets.csv に取り込む。

    再撮影した画像は行を差し替える。撮り直していない行はそのまま残す
    （撮影ハーネスを部分的に走らせても台帳が消えないようにする）。
    """
    sidecars = sorted(OUT_DIR.glob("*.json"))
    if not sidecars:
        print(f"取り込む撮影記録が無い: {OUT_DIR}", file=sys.stderr)
        print("先に make shots を実行してください。", file=sys.stderr)
        return 1

    rows = {row["asset_id"]: row for row in read_csv(ASSETS_CSV, ASSET_FIELDS)}
    added, updated = 0, 0
    for path in sidecars:
        rec = json.loads(path.read_text(encoding="utf-8"))
        asset_id = rec["asset_id"]
        if asset_id in rows:
            updated += 1
        else:
            added += 1
        rows[asset_id] = {
            "asset_id": asset_id,
            "file": rec["file"],
            "章": rec.get("chapter", ""),
            "機能": rec.get("feature", ""),
            "状態": rec.get("state", ""),
            # captured_on は撮影側が JST で作った日付。無い古い記録だけ
            # captured_at（UTC の ISO）から切り出す。
            "撮影日": rec.get("captured_on") or rec.get("captured_at", "")[:10],
            "参照コミット": commit,
            "ビューポート": rec.get("viewport", ""),
        }

    ordered = sorted(rows.values(), key=lambda r: (r["章"], r["asset_id"]))
    write_csv(ASSETS_CSV, ASSET_FIELDS, ordered)
    print(f"{ASSETS_CSV.relative_to(REPO)}: 新規 {added} 件 / 更新 {updated} 件 / 合計 {len(ordered)} 件")
    if commit:
        print(f"  参照コミット={commit[:8]}")
    else:
        print("  参照コミットは取得できなかった（アプリのリポジトリが見つからない）")
    return 0


def check() -> int:
    """画像・assets・placements の食い違いを列挙する。"""
    problems: list[str] = []

    assets = read_csv(ASSETS_CSV, ASSET_FIELDS)
    asset_ids = {row["asset_id"] for row in assets}
    placements = read_csv(PLACEMENTS_CSV, PLACEMENT_FIELDS)

    on_disk = {p.stem for p in IMAGE_DIR.glob("*.png")} if IMAGE_DIR.exists() else set()

    for row in assets:
        if not (REPO / row["file"]).exists():
            problems.append(f"台帳にあるが画像が無い: {row['asset_id']} -> {row['file']}")
    for stem in sorted(on_disk - asset_ids):
        problems.append(f"画像はあるが台帳に無い: {stem}.png（make shots-ledger を実行）")

    seen: set[str] = set()
    for row in placements:
        pid = row["placement_id"]
        if not pid:
            problems.append("placement_id が空の行がある")
        elif pid in seen:
            problems.append(f"placement_id が重複している: {pid}")
        seen.add(pid)
        if row["asset_id"] not in asset_ids:
            problems.append(f"掲載箇所が存在しない画像を指している: {pid} -> {row['asset_id']}")
        if not row["alt"]:
            problems.append(f"alt が空: {pid}")
        if not row["caption"]:
            problems.append(f"caption が空: {pid}")

    # 掲載箇所台帳と原稿の食い違いを見る。台帳だけ直して章を直し忘れる（逆も）と
    # 台帳が監査の役に立たなくなるので、実ファイルに当たって確かめる。
    for row in placements:
        pid, chapter = row["placement_id"], row["章"]
        rst = REPO / "source" / f"{chapter}.rst"
        if not rst.exists():
            problems.append(f"章の原稿が無い: {pid} -> source/{chapter}.rst")
            continue
        body = rst.read_text(encoding="utf-8")
        ref = f"images/v70/{row['asset_id']}.png"
        if ref not in body:
            problems.append(f"原稿がこの画像を参照していない: {pid} -> {ref}（source/{chapter}.rst）")
        # RST は行を折り返すことがあり、折り返し位置に空白が入る。日本語では
        # 空白に意味が無いので、両側から空白をすべて落として比較する。
        flat = "".join(body.split())
        for field in ("alt", "caption"):
            value = "".join(row[field].split())
            if value and value not in flat:
                problems.append(f"原稿の{field}が台帳と違う: {pid}（source/{chapter}.rst）")

    placed = {row["asset_id"] for row in placements}
    unplaced = sorted(asset_ids - placed)

    if problems:
        print("台帳に問題がある:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(f"shots-check: OK（画像 {len(asset_ids)} 件 / 掲載箇所 {len(placements)} 件）")
    if unplaced:
        # まだ章に貼っていない画像。撮影が章より先に進むのは正常なので、
        # 失敗にはせず数だけ知らせる。
        print(f"  まだどの章にも貼っていない画像: {len(unplaced)} 件")
        for a in unplaced:
            print(f"    - {a}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["build", "check"])
    parser.add_argument("--code-dir", type=Path, default=None,
                        help="参照コミットを取るアプリのリポジトリ（既定 $QULOUD_CODE_DIR か ~/v6.0）")
    args = parser.parse_args()

    if args.command == "build":
        import os
        code_dir = args.code_dir or Path(os.environ.get("QULOUD_CODE_DIR", Path.home() / "v6.0"))
        return build(code_commit(code_dir))
    return check()


if __name__ == "__main__":
    sys.exit(main())
