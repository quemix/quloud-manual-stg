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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``0.001``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - ステップ数
     - ``num_steps``
     - 整数
     - -
     - ``10000``
     - 1 以上、必須
     - -
     - -
   * - 温度
     - ``temperature``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上、必須
     - -
     - -
   * - アンサンブル
     - ``lammps_ensemble``
     - 選択
     - -
     - ``nvt``
     - 必須
     - NVE（ミクロカノニカル）（``nve``） / NVT（カノニカル）（``nvt``） / NPT（等温等圧）（``npt``）
     - -
   * - 圧力
     - ``lammps_pressure``
     - 数値
     - bars
     - ``0.0``
     - 0.0 以上、必須
     - -
     - 「アンサンブル」が「NPT（等温等圧）」のとき
   * - 圧力異方性
     - ``lammps_aniso``
     - 選択
     - -
     - ``aniso``
     - 必須
     - 異方性 (aniso)（``aniso``） / 等方性 (iso)（``iso``） / 三斜 (tri)（``tri``）
     - 「アンサンブル」が「NPT（等温等圧）」のとき
   * - 追加で計算する物理量 (compute)
     - ``lammps_compute``
     - 選択
     - -
     - ``none``
     - 必須
     - 計算しない（``none``） / 動径分布関数 (rdf)（``rdf``） / 平均二乗変位 (msd)（``msd``）
     - -
   * - rdf を計算する元素ペア（空欄で全ペア。例: Si-O, Si-Si）
     - ``lammps_compute_rdf_pairs``
     - 文字列
     - -
     - -
     - -
     - -
     - 「追加で計算する物理量 (compute)」が「動径分布関数 (rdf)」のとき
   * - msd を計算する元素（空欄で全元素。例: Si, O）
     - ``lammps_compute_msd_elements``
     - 文字列
     - -
     - -
     - -
     - -
     - 「追加で計算する物理量 (compute)」が「平均二乗変位 (msd)」のとき
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
     - ``1 all atom 50 QuloudJob.lammpstrj``
     - 必須
     - -
     - -

