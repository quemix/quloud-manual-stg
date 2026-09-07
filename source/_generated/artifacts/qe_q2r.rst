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
