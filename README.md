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

## meta/ について

設計書・実装計画・変更履歴の判定根拠・マスタデータ dump は、非公開リポジトリ
**`quemix/quloud-manual-meta`** で管理している。参照元の `quemix/material_computation_v6`
が非公開であり、未修正の不具合情報や内部構成を含むため、公開されるこのリポジトリには置かない。

```bash
git clone git@github.com:quemix/quloud-manual-meta.git meta
```

`meta/` は `.gitignore` 済み。`tools/` の既定パスはすべて `meta/` を指すので、
上記のとおりクローンすれば `make dump` / `make generate` / `make release-notes` が動く。

## セットアップ

```bash
make venv        # python3.13 の .venv を作り requirements.txt を導入する
```

`python3`（3.14）では `ensurepip` が無く venv を作れない。必ず `python3.13` を使う。

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
