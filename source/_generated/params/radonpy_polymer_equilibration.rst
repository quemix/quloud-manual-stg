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
   * - 温度
     - ``temperature``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上、必須
     - -
     - -
     - 基本
   * - 圧力
     - ``radonpy_pressure``
     - 数値
     - atm
     - ``1.0``
     - 0.0 以上、必須
     - -
     - -
     - 基本
   * - 平衡化プロトコル
     - ``radonpy_eq_protocol``
     - 選択
     - -
     - ``EQ21step``
     - 必須
     - EQ21step（Larsen圧縮・再現性高）（``EQ21step``） / Annealing（焼きなまし）（``Annealing``）
     - -
     - 詳細
   * - 乱数シード
     - ``radonpy_random_seed``
     - 整数
     - -
     - ``42``
     - 0 以上、必須
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
   * - 目標原子数
     - ``radonpy_n_atoms``
     - 整数
     - -
     - ``1000``
     - 100 以上、必須
     - -
     - -
     - 基本
   * - 古典力場タイプ
     - ``classical_ff_type``
     - 選択
     - -
     - ``GAFF2``
     - 必須
     - GAFF2（推奨）（``GAFF2``） / GAFF2_mod（``GAFF2_mod``） / GAFF（``GAFF``） / Dreiding（``Dreiding``）
     - -
     - 基本
   * - 高分子鎖数
     - ``radonpy_n_chains``
     - 整数
     - -
     - ``10``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - 高分子タイプ
     - ``radonpy_polymer_type``
     - 選択
     - -
     - ``homo``
     - 必須
     - ホモポリマー（``homo``）
     - -
     - 基本
   * - タクティシティ
     - ``radonpy_tacticity``
     - 選択
     - -
     - ``atactic``
     - 必須
     - アタクチック（``atactic``） / アイソタクチック（``isotactic``） / シンジオタクチック（``syndiotactic``）
     - -
     - 基本
