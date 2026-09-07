.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 6042191ba82c4be3056bf116bdfb49f2ea1ff9ab (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T21:34:15Z
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
   * - ``^(QuloudJob\.q2r\.in|q2r\.in)$``
     - q2r.x 入力（旧名 q2r.in にも対応）
     - text
     - ○
     - 必須
   * - ``^(QuloudJob\.fc|matdyn\.fc)$``
     - 実空間力定数（flfrc。matdyn.x の入力になる）
     - text
     - ○
     - 必須
   * - ``q2r.out``
     - q2r.x 標準出力
     - text
     - ○
     - 必須
