.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 789272e8ff4737a6a8aaf0d461f6b71abb84fb54 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T07:21:28Z
.. マスタ同期日時: 2026-09-07T06:19:19Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 28 34 12 12 8

   * - ファイル
     - 内容
     - 形式
     - ダウンロード
     - 出力
   * - ``Core.wfc``
     - コア波動関数（filecore。upf2plotcore.sh が生成する固定名。#1194）
     - text
     - ○
     - 任意
   * - ``xanes.sav``
     - xspectra.x の再開用データ（Lanczos 係数）
     - binary
     - ○
     - 任意
   * - ``^(QuloudJob\.xspectra\.in|xspectra\.in)$``
     - xspectra.x 入力（旧名 xspectra.in にも対応）
     - text
     - ○
     - 必須
   * - ``xspectra.err``
     - xspectra.x 標準エラー出力
     - text
     - ○
     - 任意
   * - ``xanes.dat``
     - XANES スペクトル（エネルギー vs 吸収強度）
     - text
     - ○
     - 必須
   * - ``xspectra.out``
     - xspectra.x 標準出力（収束状況・計算時間）
     - text
     - ○
     - 必須
