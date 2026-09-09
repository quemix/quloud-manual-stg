# Quloud オンラインマニュアル（Ver.7.0 ステージング）

Quloud **Ver.7.0** のオンラインマニュアルの原稿とビルド環境。
[quemix.github.io/quloud-manual-stg](https://quemix.github.io/quloud-manual-stg/) で公開している。

本番（Ver.6.1.2）のマニュアルは別リポジトリ **[quemix/quloud-manual](https://github.com/quemix/quloud-manual)** が
[manual.quloud-platform.quemix.com](https://manual.quloud-platform.quemix.com/) で公開している。
このリポジトリの `main` はそこから派生しているので、Ver.7.0 のリリース時は
**stg の `main` を quloud-manual の `main` へマージするだけ**でよい。

マージ時に衝突するのは `CNAME` と `conf.py` の `html_extra_path` の 2 箇所だけである。
本番は `CNAME`（独自ドメイン）、stg は `robots.txt`（検索除外）を配っており、
リポジトリごとに恒久的に異なる。マージでは必ず**本番側**を採ること。

## 構成

| パス | 内容 |
| --- | --- |
| `index.rst`, `source/*.rst` | 原稿（RST） |
| `source/_generated/` | 生成物。**手で編集しない**（`make generate` / `make release-notes` で作り直す） |
| `source/images/` | 画面キャプチャ |
| `docs/` | 公開物（GitHub Pages）。`make publish` の出力のみ |
| `tools/` | 生成スクリプト |
| `meta/` | **このリポジトリには入っていない**（下記） |
| `CLAUDE.md`, `.claude/` | **このリポジトリには入っていない**（`meta/claude/` へのシンボリックリンク。下記） |

## meta/ について

設計書・実装計画・変更履歴の判定根拠・マスタデータ dump は、非公開リポジトリ
**`quemix/quloud-manual-meta`** で管理している。参照元の `quemix/material_computation_v6`
が非公開であり、未修正の不具合情報や内部構成を含むため、公開されるこのリポジトリには置かない。

```bash
git clone git@github.com:quemix/quloud-manual-meta.git meta
```

`meta/` は `.gitignore` 済み。`tools/` の既定パスはすべて `meta/` を指すので、
上記のとおりクローンすれば `make dump` / `make generate` / `make release-notes` が動く。

## CLAUDE.md / .claude について

Claude Code 用の作業ルール（`CLAUDE.md`）と Skill（`.claude/`）の実体も、`meta/` と同じ理由で
非公開リポジトリ側（`meta/claude/`）に置いている。このリポジトリにはそこへの
シンボリックリンクとして置くだけで、内容そのものは含まれない。

```bash
make claude-link   # meta/claude/{CLAUDE.md,dotclaude} へのシンボリックリンクを張る
```

`meta/` を clone していない状態では `CLAUDE.md` と `.claude/` は存在しない（symlink 切れ）。

## セットアップ

```bash
git clone git@github.com:quemix/quloud-manual-stg.git
cd quloud-manual-stg
git clone git@github.com:quemix/quloud-manual-meta.git meta   # 非公開。上の「meta/ について」参照
make claude-link # CLAUDE.md / .claude/ のシンボリックリンクを張る。上の「CLAUDE.md / .claude について」参照
make venv        # python3.13 の .venv を作り requirements.txt を導入する
```

`python3`（3.14）では `ensurepip` が無く venv を作れない。必ず `python3.13` を使う。

## 編集の流れ

**編集を始める前に `CLAUDE.md` を読むこと。** 公開・非公開リポジトリの使い分け、
`make publish` の手順、踏みやすい罠（強調記法・見出しレベル・章番号のずれ等）を
まとめた恒久ルール集で、公開事故を防ぐために必読としている。

具体的な作業手順（章を書く、生成表を繋ぐ、マスタデータを取り直す、画面キャプチャを撮る、
変更履歴を編集する、公開する）は **`.claude/skills/quloud-manual-chapter/SKILL.md`** に
まとめている。Claude Code から作業する場合はこの Skill がそのまま使える
（`quloud-manual-chapter` として呼び出す）。手動で作業する場合も同じ手順に沿えばよい。

大まかな流れは次のとおり。

1. `source/*.rst` に章の原稿を書く／直す。章冒頭には対象バージョンと確認日を書く
   （参照元のコミット SHA は書かない。`CLAUDE.md` §1）
2. マスタデータ由来の表が必要なら `make dump && make generate && make checkgen` で
   生成物を作り直し、章から束ねたファイル（`_generated/*_all.rst`）を
   `.. include::` で繋ぐ
3. 画面キャプチャが必要なら `shots/`（独立した Playwright プロジェクト、
   `shots/README.md` 参照）で撮る。ローカル開発 DB とその中の実データへの
   禁止事項は `CLAUDE.md` §6 にまとまっている
4. 変更履歴（`source/release_notes.rst`）を足すときの掲載基準・書き方は
   `CLAUDE.md` §5
5. `make test && make checkgen && make strict` がすべて警告ゼロで通ることを確認する
6. `git commit`（原稿）→ `make publish` → `git commit`（`docs/`）の順序を守る。
   崩すと公開物が壊れる（`CLAUDE.md` §2）

## ビルド

```bash
make html          # _build/html にビルドする
make strict        # 警告をエラーとしてビルドする（章の完了判定）
make checkgen      # source/_generated/ 配下が RST として妥当か検査する
make test          # tools/ のテスト
make publish       # clean + strict の結果を docs/ に反映する
```

**`make publish` は必ず原稿をコミットしてから実行する。** `sphinx_last_updated_by_git` の
`git_untracked_show_sourcelink` は既定 `False` で、git 未追跡の `.rst` はソースリンクが
無効化され `_sources/` にもコピーされない。コミット前に publish すると、新設したページだけが
「ソースを表示」リンクの無い状態で公開される。

## 生成物の更新

```bash
make dump           # ~/v6.0 のマスタデータを meta/master_dump.json に落とす（ローカル Docker が必要）
make generate       # dump から source/_generated/ の表を作り直す
make release-notes  # meta/ の判定 CSV から変更履歴の Ver.7.0 の項を作り直す
```

`make dump` は生成 RST のヘッダに dump 実行時刻を刻むため、マスタが変わっていなくても
112 ファイルすべてが変わる。中身が変わったかを見るときはヘッダ 3 行を除いて比較する。

```bash
git diff -U0 source/_generated | grep -E '^[+-]' \
  | grep -vE '^[+-]{3}|生成元コミット|マスタ取得日時|マスタ同期日時' | head
```
