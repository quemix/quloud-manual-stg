.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 6042191ba82c4be3056bf116bdfb49f2ea1ff9ab (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T21:34:15Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate

~~~~~~~~~~
物理モデル
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 18 16 8 6 12 16 22 22

   * - 項目名
     - キー
     - 型
     - 単位
     - 既定値
     - 範囲・制約
     - 選択肢
     - 表示条件
   * - 構造入力形式
     - ``radonpy_structure_input_type``
     - 選択
     - -
     - ``smiles``
     - 必須
     - SMILES（``smiles``） / 3次元構造ファイル（mol2/xyz/sdf/pdb）（``file``）
     - -
   * - SMILES（モノマー繰り返し単位）
     - ``radonpy_smiles``
     - 文字列
     - -
     - -
     - 必須
     - -
     - 「構造入力形式」が「SMILES」のとき
   * - 構造ファイル（mol2/xyz/sdf/pdb）
     - ``radonpy_structure_file``
     - ファイル
     - -
     - -
     - 必須
     - -
     - 「構造入力形式」が「3次元構造ファイル（mol2/xyz/sdf/pdb）」のとき
   * - QM手法
     - ``exchange_correlation``
     - 選択
     - -
     - ``wb97m-d3bj``
     - 必須
     - ωB97M-D3BJ（推奨）（``wb97m-d3bj``） / B3LYP-D3BJ（``b3lyp-d3bj``） / HF（高速）（``hf``） / CAM-B3LYP（``cam-b3lyp``）
     - -

