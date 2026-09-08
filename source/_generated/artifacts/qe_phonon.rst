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
   * - ``^(QuloudJob|matdyn)\.dyn[0-9]+$``
     - 動力学行列（fildyn。dyn0 は q 点グリッド情報、dyn1 以降が各 q 点）
     - text
     - ○
     - 任意
   * - ``^(QuloudJob\.ph\.in|ph\.in)$``
     - ph.x 入力（DFPT。旧名 ph.in にも対応）
     - text
     - ○
     - 必須
   * - ``ph.err``
     - ph.x 標準エラー出力
     - text
     - ○
     - 任意
   * - ``ph.out``
     - ph.x 標準出力（各 q 点の振動数・計算時間）
     - text
     - ○
     - 必須
