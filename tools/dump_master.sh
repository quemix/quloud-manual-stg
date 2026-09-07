#!/usr/bin/env bash
# ~/v6.0 のマスタデータを meta/master_dump.json に落とす。
#
# 前提: ~/v6.0 で docker compose の rails / db が起動していること。
#   cd ~/v6.0 && docker compose ps
set -euo pipefail

MANUAL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CODE_DIR="${QULOUD_CODE_DIR:-$HOME/v6.0}"
OUT="$MANUAL_DIR/meta/master_dump.json"
RUNNER_TMP="$CODE_DIR/rails/tmp_dump_master.rb"
JSON_TMP="$CODE_DIR/rails/tmp_master_dump.json"

cleanup() { rm -f "$RUNNER_TMP" "$JSON_TMP"; }
trap cleanup EXIT

echo "code dir : $CODE_DIR"
cp "$MANUAL_DIR/tools/dump_master.rb" "$RUNNER_TMP"

( cd "$CODE_DIR" && docker compose exec -T -e RAILS_ENV=development rails \
    bundle exec rails runner /app/tmp_dump_master.rb )

test -f "$JSON_TMP" || { echo "dump が生成されなかった" >&2; exit 1; }

COMMIT="$(git -C "$CODE_DIR" rev-parse HEAD)"
BRANCH="$(git -C "$CODE_DIR" rev-parse --abbrev-ref HEAD)"

mkdir -p "$MANUAL_DIR/meta"
python3 - "$JSON_TMP" "$OUT" "$COMMIT" "$BRANCH" <<'PY'
import json, sys
src, dst, commit, branch = sys.argv[1:5]
with open(src, encoding="utf-8") as f:
    data = json.load(f)
merged = {"source_commit": commit, "source_branch": branch}
merged.update(data)
with open(dst, "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"wrote {dst}  ec={len(merged['engine_capabilities'])}  commit={commit[:8]} ({branch})")
PY
