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
   * - Pretrained-model プロバイダー
     - ``pretrained_model_provider``
     - 選択
     - -
     - ``7net``
     - 必須
     - SevenNet（``7net``） / fairchem（``fairchem``）
     - -
   * - モデル名
     - ``pretrained_model_name_7net``
     - 選択
     - -
     - ``7net-mf-ompa``
     - 必須
     - 7net-mf-ompa（``7net-mf-ompa``）
     - 「Pretrained-model プロバイダー」が「SevenNet」のとき
   * - モデル名
     - ``pretrained_model_name_fairchem``
     - 選択
     - -
     - ``uma-s-1p1``
     - 必須
     - uma-s-1p1（``uma-s-1p1``）
     - 「Pretrained-model プロバイダー」が「fairchem」のとき

~~~~~~~~~~~~~~
実験パラメータ
~~~~~~~~~~~~~~

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
   * - 最適化最大ステップ数
     - ``opt_max_steps``
     - 整数
     - -
     - ``100``
     - 1 以上 2000 以下、必須
     - -
     - -
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値
     - ``scf_convergence``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 1e-12 以上
     - -
     - -
   * - 力の収束閾値
     - ``opt_force_convergence``
     - 数値
     - eV/Å
     - ``0.05``
     - 1e-06 以上
     - -
     - -

