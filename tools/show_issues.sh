#!/usr/bin/env bash
# 指定した issue 番号の本文をまとめて表示する。
#   tools/show_issues.sh 1132 1110 1090
set -euo pipefail
REPO="${QULOUD_REPO:-quemix/material_computation_v6}"
for n in "$@"; do
  echo "================ #$n ================"
  gh issue view "$n" --repo "$REPO" --json number,title,labels,createdAt,body \
     --template '{{.number}} {{.title}}
labels: {{range .labels}}{{.name}} {{end}}
created: {{.createdAt}}

{{.body}}
'
done
