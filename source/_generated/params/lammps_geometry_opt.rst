.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
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
   * - 原子間ポテンシャル
     - ``lammps_iap``
     - 選択
     - -
     - ``chgnet``
     - 必須
     - CHGNet（機械学習ポテンシャル）（``chgnet``） / SevenNet（機械学習ポテンシャル、GPU専用）（``sevennet``） / FairChem UMA（機械学習ポテンシャル、GPU専用）（``fairchem``） / ファイルアップロード（``file``）
     - -
   * - SevenNetモデル名
     - ``lammps_sevennet_model``
     - 文字列
     - -
     - ``7net-mf-ompa``
     - 必須
     - -
     - 「原子間ポテンシャル」が「SevenNet（機械学習ポテンシャル、GPU専用）」のとき
   * - 原子間ポテンシャルファイル
     - ``lammps_iap_file``
     - ファイル
     - -
     - -
     - 必須
     - -
     - 「原子間ポテンシャル」が「ファイルアップロード」のとき

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
   * - 境界条件 (a軸)
     - ``lammps_boundary_a``
     - 選択
     - -
     - ``p``
     - 必須
     - Periodic（周期）（``p``） / Fixed（固定）（``f``）
     - -
   * - 境界条件 (b軸)
     - ``lammps_boundary_b``
     - 選択
     - -
     - ``p``
     - 必須
     - Periodic（周期）（``p``） / Fixed（固定）（``f``）
     - -
   * - 境界条件 (c軸)
     - ``lammps_boundary_c``
     - 選択
     - -
     - ``p``
     - 必須
     - Periodic（周期）（``p``） / Fixed（固定）（``f``）
     - -
   * - スーパーセル複製 (a軸)
     - ``lammps_replicate_n1``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
     - -
     - -
   * - スーパーセル複製 (b軸)
     - ``lammps_replicate_n2``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
     - -
     - -
   * - スーパーセル複製 (c軸)
     - ``lammps_replicate_n3``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
     - -
     - -
   * - エネルギー収束閾値 (etol)
     - ``lammps_etol``
     - 数値（指数表記）
     - -
     - ``1.0e-15``
     - 1e-18 以上 1000.0 以下、必須
     - -
     - -
   * - 力収束閾値 (ftol)
     - ``lammps_ftol``
     - 数値（指数表記）
     - eV/Å
     - ``1.0e-7``
     - 1e-18 以上 1000.0 以下、必須
     - -
     - -
   * - 最大反復回数 (maxiter)
     - ``lammps_maxiter``
     - 整数
     - -
     - ``1000``
     - 0 以上、必須
     - -
     - -
   * - 最大エネルギー評価回数 (maxeval)
     - ``lammps_maxeval``
     - 整数
     - -
     - ``10000``
     - 0 以上、必須
     - -
     - -
   * - セル形状最適化 (box/relax)
     - ``lammps_box_opt``
     - 有効・無効
     - -
     - ``true``
     - 必須
     - 有効（``true``） / 無効（``false``）
     - -
   * - 圧力異方性
     - ``lammps_aniso``
     - 選択
     - -
     - ``aniso``
     - 必須
     - 異方性 (aniso)（``aniso``） / 等方性 (iso)（``iso``） / 三斜 (tri)（``tri``）
     - 「セル形状最適化 (box/relax)」が「有効」のとき
   * - thermo\_style
     - ``lammps_thermo_style``
     - 文字列
     - -
     - ``custom step etotal temp density vol press enthalpy``
     - 必須
     - -
     - -
   * - thermo 出力間隔
     - ``lammps_thermo``
     - 整数
     - -
     - ``10``
     - 1 以上、必須
     - -
     - -
   * - dump コマンド
     - ``lammps_dump``
     - 文字列
     - -
     - ``1 all atom 5 QuloudJob.lammpstrj``
     - 必須
     - -
     - -

