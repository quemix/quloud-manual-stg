.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 789272e8ff4737a6a8aaf0d461f6b71abb84fb54 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T07:21:28Z
.. マスタ同期日時: 2026-09-07T06:19:19Z
.. 再生成: make dump && make generate


物理モデルパラメータ
~~~~~~~~~~~~~~~~~~~~

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
   * - 構造入力形式
     - ``radonpy_structure_input_type``
     - 選択
     - -
     - ``smiles``
     - 必須
     - SMILES（``smiles``） / 3次元構造ファイル（mol2/xyz/sdf/pdb）（``file``）
     - -
     - 基本
   * - SMILES（モノマー繰り返し単位）
     - ``radonpy_smiles``
     - 文字列
     - -
     - -
     - 必須
     - -
     - 「構造入力形式」が「SMILES」のとき
     - 基本
   * - 構造ファイル（mol2/xyz/sdf/pdb）
     - ``radonpy_structure_file``
     - ファイル
     - -
     - -
     - 必須
     - -
     - 「構造入力形式」が「3次元構造ファイル（mol2/xyz/sdf/pdb）」のとき
     - 基本
   * - QM手法
     - ``exchange_correlation``
     - 選択
     - -
     - ``wb97m-d3bj``
     - 必須
     - ωB97M-D3BJ（推奨）（``wb97m-d3bj``） / B3LYP-D3BJ（``b3lyp-d3bj``） / HF（高速）（``hf``） / CAM-B3LYP（``cam-b3lyp``）
     - -
     - 基本
