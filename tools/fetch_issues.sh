#!/usr/bin/env bash
# v7.0 マイルストーンの issue を JSON に落とす。
set -euo pipefail

MANUAL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="${QULOUD_REPO:-quemix/material_computation_v6}"
MILESTONE="${QULOUD_MILESTONE:-v7.0}"
LIMIT=500

mkdir -p "$MANUAL_DIR/meta"

for state in closed open; do
  out="$MANUAL_DIR/meta/v70_issues_${state}.json"
  gh issue list --repo "$REPO" --milestone "$MILESTONE" --state "$state" \
     --limit "$LIMIT" --json number,title,labels,createdAt,closedAt,url > "$out"
  count="$(python3 -c "import json,sys;print(len(json.load(open(sys.argv[1]))))" "$out")"
  if [ "$count" -eq "$LIMIT" ]; then
    echo "エラー: $state の取得件数が --limit ($LIMIT) と一致しました。" \
         "結果が切り詰められている可能性があります。LIMIT を上げて再実行してください。" >&2
    exit 1
  fi
  echo "wrote $out  ($count 件)"
done
