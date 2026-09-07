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

.PHONY: venv html strict dump generate checkgen test publish clean help

venv:
	python3.13 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

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
	@echo "venv     : .venv を作り requirements.txt を導入する"
	@echo "html     : _build/html にビルドする"
	@echo "strict   : 警告をエラーとしてビルドする"
	@echo "dump     : ~/v6.0 のマスタデータを meta/master_dump.json に落とす"
	@echo "generate : dump から source/_generated/**.rst を生成する"
	@echo "checkgen : source/_generated/ 配下の全ファイルが RST として読めるか検査する"
	@echo "test     : tools/ のテストを走らせる"
	@echo "publish  : strict ビルドの結果を docs/ に反映する"
	@echo "clean    : _build/html を消す"
