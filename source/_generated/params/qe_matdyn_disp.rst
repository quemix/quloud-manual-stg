.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 789272e8ff4737a6a8aaf0d461f6b71abb84fb54 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T07:21:28Z
.. マスタ同期日時: 2026-09-07T06:19:19Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 16 14 8 6 10 14 20 20 6

   * - 項目名
     - キー
     - 型
     - 単位
     - 既定値
     - 範囲・制約
     - 選択肢
     - 表示条件
     - 区分
   * - フォノン分散経路
     - ``q_kpath``
     - kpath
     - -
     - ``{"method": "k-auto", "points": [{"label": "Γ", "x": 0.0, "y": 0.0, "z": 0.0, "division": 20}, {"label": "Γ", "x": 1.0, "y": 0.0, "z": 0.0, "division": 20}]}``
     - -
     - -
     - -
     - 基本
