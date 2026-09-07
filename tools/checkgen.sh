#!/usr/bin/env bash
# source/_generated/ 配下の全ファイルが RST として読めるかを検査する。
#
# conf.py の exclude_patterns が source/_generated をトップレベルの
# ビルド対象から外しているため、章本文から .. include:: されていない
# 生成ファイルは make strict でもパースされない。ここでは全生成ファイルを
# 列挙した使い捨ての Sphinx プロジェクトを一時ディレクトリに作ってビルドし、
# エラーが無いことを確認する。プロジェクトはビルド後に削除する。
set -euo pipefail

MANUAL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GENERATED_DIR="$MANUAL_DIR/source/_generated"
SPHINXBUILD="$MANUAL_DIR/.venv/bin/sphinx-build"

test -d "$GENERATED_DIR" || { echo "エラー: $GENERATED_DIR が無い（先に make generate）" >&2; exit 1; }
test -x "$SPHINXBUILD" || { echo "エラー: $SPHINXBUILD が無い（先に make venv）" >&2; exit 1; }

SCRATCH="$(mktemp -d)"
cleanup() { rm -rf "$SCRATCH"; }
trap cleanup EXIT

cat > "$SCRATCH/conf.py" <<'EOF'
project = "checkgen"
extensions = []
language = "ja"
exclude_patterns = ["_generated"]
EOF

ln -s "$GENERATED_DIR" "$SCRATCH/_generated"

{
    echo "checkgen"
    echo "========"
    echo
    while IFS= read -r f; do
        rel="${f#"$GENERATED_DIR"/}"
        echo ".. include:: _generated/$rel"
        echo
    done < <(cd "$GENERATED_DIR" && find . -name '*.rst' | sed 's|^\./||' | sort)
} > "$SCRATCH/index.rst"

COUNT="$(find "$GENERATED_DIR" -name '*.rst' | wc -l)"

"$SPHINXBUILD" -b html -W -q "$SCRATCH" "$SCRATCH/_build"
echo "checkgen: OK ($COUNT 個の生成ファイルをパースできた)"
