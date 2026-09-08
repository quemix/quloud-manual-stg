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
   * - ``QuloudJob_JXC_Jij_*.agr``
     - J\_ij グラフファイル（元素名がファイル名に入る）
     - text
     - ○
     - 任意
   * - ``QuloudJob_JXC.inp``
     - SPR-KKR JXC 入力ファイル
     - text
     - ○
     - 必須
   * - ``QuloudJob.pot``
     - SPR-KKR ポテンシャルファイル
     - text
     - ○
     - 必須
   * - ``buildbot.log``
     - ビルドボットログ
     - text
     - ○
     - 任意
   * - ``sprkkr_jxc.exec.log``
     - kkrgenMPI の標準出力（キュリー温度の抽出元）
     - text
     - ○
     - 任意
   * - ``QuloudJob_JXC_J_ij.dat``
     - 交換結合パラメータ J\_ij データファイル
     - text
     - ○
     - 任意
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
