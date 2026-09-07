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
   * - ひずみ速度
     - ``radonpy_elong_strain_rate``
     - 数値
     - ε/fs
     - ``5e-06``
     - 1e-07 以上 1e-05 以下、必須
     - -
     - -
     - 基本
   * - 最大ひずみ
     - ``radonpy_elong_max_strain``
     - 数値
     - -
     - ``0.5``
     - 0.01 以上 2.0 以下、必須
     - -
     - -
     - 基本
   * - 変形方向
     - ``radonpy_elong_deform_axis``
     - 選択
     - -
     - ``x``
     - 必須
     - X軸（``x``） / Y軸（``y``） / Z軸（``z``）
     - -
     - 基本
