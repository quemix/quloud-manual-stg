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
   * - NEB イメージ数
     - ``num_images``
     - 整数
     - -
     - ``5``
     - 3 以上 20 以下、必須
     - -
     - -
     - 基本
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
     - 詳細
   * - SCF 収束閾値
     - ``scf_convergence``
     - 数値（指数表記）
     - Ry
     - ``1e-05``
     - 1e-12 以上
     - -
     - -
     - 詳細
   * - Climbing Image NEB
     - ``climb_image``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 詳細
   * - スプリング定数
     - ``spring_constant``
     - 数値
     - eV/Å²
     - ``0.5``
     - 0.01 以上
     - -
     - -
     - 詳細

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
   * - Pretrained-model プロバイダー
     - ``pretrained_model_provider``
     - 選択
     - -
     - ``7net``
     - 必須
     - SevenNet（``7net``） / fairchem（``fairchem``）
     - -
     - 基本
   * - モデル名
     - ``pretrained_model_name_7net``
     - 選択
     - -
     - ``7net-mf-ompa``
     - 必須
     - 7net-mf-ompa（``7net-mf-ompa``）
     - 「Pretrained-model プロバイダー」が「SevenNet」のとき
     - 基本
   * - モデル名
     - ``pretrained_model_name_fairchem``
     - 選択
     - -
     - ``uma-s-1p1``
     - 必須
     - uma-s-1p1（``uma-s-1p1``）
     - 「Pretrained-model プロバイダー」が「fairchem」のとき
     - 基本
