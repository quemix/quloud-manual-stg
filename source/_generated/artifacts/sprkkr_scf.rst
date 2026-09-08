.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 28 34 12 12 8

   * - ファイル
     - 内容
     - 形式
     - ダウンロード
     - 出力
   * - ``QuloudJob.pot_new``
     - 収束後ポテンシャル（交換結合パラメータ計算の入力になる）
     - text
     - ○
     - 必須
   * - ``QuloudJob_SCF*.dos``
     - SCF 開始時の状態密度
     - text
     - ○
     - 任意
   * - ``occupation.dat``
     - サイト占有率（kkr\_occupancy 由来）
     - text
     - ○
     - 任意
   * - ``QuloudJob.pot``
     - SPR-KKR ポテンシャルファイル
     - text
     - ○
     - 必須
   * - ``QuloudJob_SCF.inp``
     - SPR-KKR SCF 入力ファイル
     - text
     - ○
     - 必須
   * - ``buildbot.log``
     - ビルドボットログ
     - text
     - ○
     - 任意
   * - ``sprkkr_scf.exec.log``
     - kkrscfMPI の標準出力
     - text
     - ○
     - 任意
   * - ``QuloudJob_SCF.log``
     - SCF 反復表（kkrscfMPI 自身が書く。結果抽出の一次ソース）
     - text
     - ○
     - 必須
   * - ``rsdft.atom``
     - 原子構造ファイル
     - text
     - ○
     - 任意
   * - ``sysinfo.json``
     - システム情報（計算結果メタデータ）
     - json
     - ○
     - 任意
