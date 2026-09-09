# Quloud マニュアルのビルド
#
# BUILDDIR は _build/html。docs/ は GitHub Pages の公開物で、
# make publish のときだけ更新する。docs/ を直接のビルド先にすると、
# そこに置いた手作業のファイルがビルドのたびに失われる。

VENV        = .venv
PYTHON      = $(VENV)/bin/python
SPHINXBUILD = $(VENV)/bin/sphinx-build
SPHINXOPTS  ?=
SOURCEDIR   = .
BUILDDIR    = _build/html
PUBLISHDIR  = docs

.PHONY: venv html strict dump generate checkgen test release-notes \
        shots-install shots shots-ledger shots-check publish clean help claude-link

.DEFAULT_GOAL := help

venv:
	python3.13 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

# meta/claude/ にある CLAUDE.md と .claude/ の実体へシンボリックリンクを張る。
# 実体は非公開リポジトリ meta/ 側にあるため、meta/ を clone していない環境では
# リンク先が無く CLAUDE.md / .claude/ は使えない。
claude-link:
	ln -sfn meta/claude/CLAUDE.md CLAUDE.md
	ln -sfn meta/claude/dotclaude .claude

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# 警告をエラーとして扱う。章の完了判定に使う。
strict:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" -W $(SPHINXOPTS)

# ~/v6.0 のマスタデータを meta/master_dump.json に落とす（rails コンテナが必要）
dump:
	tools/dump_master.sh

# dump から source/_generated/**.rst を生成する
generate:
	$(PYTHON) tools/gen_master_tables.py

# source/_generated/ 配下の全ファイルが RST として読めるかを検査する。
# conf.py が source/_generated を toctree から外しているため、章から
# include されていないファイルは make strict では検査されない。
checkgen:
	tools/checkgen.sh

test:
	$(PYTHON) -m unittest discover -s tools/tests -t . -v

# 判定済みの候補一覧（meta/changelog_candidates.csv, meta/changelog_manual_entries.csv）
# から source/_generated/release_notes_v70.rst を生成する。
# generate とは入力が違う（master_dump.json ではなく triage の CSV）ので分けている。
release-notes:
	$(PYTHON) tools/gen_release_notes_v70.py

# 画面キャプチャ。撮影対象はローカル Docker の Nuxt（http://localhost:3000）で、
# 保存先は source/images/v70/。撮影直前に meta/shots_redactions.json で識別情報を
# 置換し、置換漏れがあれば撮影を失敗させる（素の画面が公開物に混ざらないようにする）。
#
#   QULOUD_SHOTS_EMAIL=... QULOUD_SHOTS_PASSWORD=... make shots
#
# 資格情報は非公開リポジトリ meta/ の README を参照。ここに既定値は置かない。
shots-install:
	cd shots && npm install

shots: shots-install
	cd shots && npx playwright test $(SHOTSOPTS)
	$(MAKE) shots-ledger
	$(MAKE) shots-check

# 撮影記録（shots/.out/*.json）を meta/images_assets.csv に取り込む。
shots-ledger:
	$(PYTHON) tools/shots_ledger.py build

# 画像・画像台帳・掲載箇所台帳の整合を検査する。
shots-check:
	$(PYTHON) tools/shots_ledger.py check

# 公開物を更新する。
#
# 必ず clean してから strict ビルドする。sphinx.ext.githubpages は
# html_baseurl が未設定のとき出力先の CNAME を削除する実装で
# (sphinx/ext/githubpages.py の create_nojekyll_and_cname)、CNAME を
# 戻すのは html_extra_path のコピーだけ。ソース無変更の再ビルドでは
# 戻らないので、増分ビルドの結果を rsync --delete で反映すると
# docs/CNAME が消えて独自ドメインが落ちる。
publish:
	$(MAKE) clean
	$(MAKE) strict
	rsync -a --delete "$(BUILDDIR)/" "$(PUBLISHDIR)/"

clean:
	rm -rf "$(BUILDDIR)"

help:
	@echo "venv          : .venv を作り requirements.txt を導入する"
	@echo "claude-link   : CLAUDE.md / .claude/ を meta/claude/ へのシンボリックリンクとして張る"
	@echo "html          : _build/html にビルドする"
	@echo "strict        : 警告をエラーとしてビルドする"
	@echo "dump          : ~/v6.0 のマスタデータを meta/master_dump.json に落とす"
	@echo "generate      : dump から source/_generated/**.rst を生成する"
	@echo "checkgen      : source/_generated/ 配下の全ファイルが RST として読めるか検査する"
	@echo "test          : tools/ のテストを走らせる"
	@echo "release-notes : 判定済みの候補一覧から source/_generated/release_notes_v70.rst を生成する"
	@echo "shots         : 画面キャプチャを撮り直し、台帳を更新して検査する"
	@echo "shots-ledger  : 撮影記録を meta/images_assets.csv に取り込む"
	@echo "shots-check   : 画像と台帳の整合を検査する"
	@echo "publish       : clean してから strict ビルドし、結果を docs/ に反映する"
	@echo "clean         : _build/html を消す"
