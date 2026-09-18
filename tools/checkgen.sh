#!/usr/bin/env bash
# source/_generated/ 配下の全ファイルが RST として読めるかを検査する。
#
# conf.py の exclude_patterns が source/_generated をトップレベルの
# ビルド対象から外しているため、章本文から .. include:: されていない
# 生成ファイルは make strict でもパースされない。
#
# 検査は**1 ファイル 1 ドキュメント**で行う。以前は全ファイルを 1 つの
# index.rst に並べて include していたが、RST の見出しレベルは下線文字の
# 初出順で決まるので、前のファイルが使った下線文字が後のファイルの
# 解釈に影響してしまう。実際 params_all.rst（#, +, ~ の 3 階層）が、
# 先に並んだ params/*.rst の ~ のせいで "Title level inconsistent" に
# なった。見逃しも起こりうるので、文書を分ける。
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

# 生成ファイルの中には、本文の章を :doc:`specifications` のように参照する
# ものがある（本文へ .. include:: された状態では章本文と同じ文書なので解決
# できる）。ここでは各生成ファイルを本文から切り離して単独の文書として
# 検査するため、参照先の章がスクラッチ環境に無いと "unknown document" に
# なってしまう。実際の本文は使わず、章タイトルだけの空文書を用意して
# 参照が解決できるようにする。
SOURCE_DIR="$MANUAL_DIR/source"
CHAPTER_TOCTREE=""
while IFS= read -r chapter; do
    name="$(basename "$chapter" .rst)"
    {
        echo "$name"
        printf '=%.0s' $(seq 1 ${#name})
    } > "$SCRATCH/$name.rst"
    CHAPTER_TOCTREE="$CHAPTER_TOCTREE   $name"$'\n'
done < <(cd "$SOURCE_DIR" && find . -maxdepth 1 -name '*.rst' | sed 's|^\./||' | sort)

COUNT=0
{
    echo "checkgen"
    echo "========"
    echo
    echo ".. toctree::"
    echo
    printf '%s' "$CHAPTER_TOCTREE"
    while IFS= read -r rel; do
        COUNT=$((COUNT + 1))
        doc="$(printf 'doc_%04d' "$COUNT")"
        # 生成ファイルごとに独立した文書を作る。見出しレベルはこの文書の
        # 中だけで決まるので、他のファイルの影響を受けない。
        {
            echo "$rel"
            printf '=%.0s' $(seq 1 ${#rel})
            echo
            echo
            echo ".. include:: _generated/$rel"
        } > "$SCRATCH/$doc.rst"
        echo "   $doc"
    done < <(cd "$GENERATED_DIR" && find . -name '*.rst' | sed 's|^\./||' | sort)
} > "$SCRATCH/index.rst"

COUNT="$(find "$GENERATED_DIR" -name '*.rst' | wc -l)"

"$SPHINXBUILD" -b html -W -q "$SCRATCH" "$SCRATCH/_build"
echo "checkgen: OK ($COUNT 個の生成ファイルをそれぞれ独立にパースできた)"
