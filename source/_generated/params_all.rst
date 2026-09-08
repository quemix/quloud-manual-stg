.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate


######
ASE-MD
######

++++++++++++++
格子定数最適化
++++++++++++++

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
   * - 応力の収束閾値
     - ``opt_pressure_convergence``
     - 数値
     - GPa
     - ``0.5``
     - 0.0001 以上
     - -
     - -


++++++++++
構造最適化
++++++++++

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


+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``1.0``
     - 0.001 以上 100.0 以下、必須
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
     - ``ensemble``
     - 選択
     - -
     - ``NVT``
     - 必須
     - NVE（ミクロカノニカル）（``NVE``） / NVT（カノニカル）（``NVT``） / NPT（等温等圧）（``NPT``）
     - -
   * - 圧力（NPT のみ）
     - ``pressure``
     - 数値
     - GPa
     - ``0.0``
     - -
     - -
     - 「アンサンブル」が「NPT（等温等圧）」のとき


++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

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
   * - NEB イメージ数
     - ``num_images``
     - 整数
     - -
     - ``5``
     - 3 以上 20 以下、必須
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
     - ``1e-05``
     - 1e-12 以上
     - -
     - -
   * - Climbing Image NEB
     - ``climb_image``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - スプリング定数
     - ``spring_constant``
     - 数値
     - eV/Å²
     - ``0.5``
     - 0.01 以上
     - -
     - -



#######
DFT-1/2
#######

+++++++++++++++++++++++++++++++++
DFT-1/2 擬ポテンシャル生成（UPF）
+++++++++++++++++++++++++++++++++

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
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA-PW（Perdew-Wang 92）（``LDA-PW``） / LDA-PZ（Perdew-Zunger 81、UPFアップロードのみ）（``LDA-PZ``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（UPFアップロードのみ）（``GGA-PBEsol``）
     - -



#####
FLARE
#####

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

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
   * - OTF モード
     - ``flare_otf_mode``
     - 選択
     - -
     - ``fresh``
     - 必須
     - 新規（Fresh）（``fresh``） / 再開（Restart）（``restart``）
     - -
   * - ガウス過程タイプ
     - ``flare_gp``
     - 選択
     - -
     - ``SGP_Wrapper``
     - 必須
     - Sparse GP（SGP\_Wrapper）（``SGP_Wrapper``） / Full GP（GaussianProcess）（``GaussianProcess``）
     - -
   * - MD エンジン
     - ``flare_otf_md_engine``
     - 選択
     - -
     - ``Langevin``
     - 必須
     - Langevin（``Langevin``） / NPT（``NPT``）
     - -
   * - カーネル
     - ``flare_kernel_name``
     - 選択
     - -
     - ``NormalizedDotProduct``
     - 必須
     - NormalizedDotProduct（``NormalizedDotProduct``） / SquaredExponential（``SquaredExponential``）
     - -
   * - カーネル sigma
     - ``flare_kernel_sigma``
     - 数値
     - -
     - ``2.0``
     - 0.0 以上、必須
     - -
     - -
   * - カーネル power
     - ``flare_kernel_power``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - 温度
     - ``flare_otf_temperature_K``
     - 数値
     - K
     - ``800.0``
     - 0.0 以上、必須
     - -
     - -
   * - ディスクリプタ
     - ``flare_descriptor_name``
     - 選択
     - -
     - ``B2``
     - 必須
     - B2（ACE）（``B2``）
     - -
   * - 径方向基底数 (nmax)
     - ``flare_descriptor_nmax``
     - 整数
     - -
     - ``5``
     - 1 以上、必須
     - -
     - -
   * - 角運動量最大値 (lmax)
     - ``flare_descriptor_lmax``
     - 整数
     - -
     - ``3``
     - 0 以上、必須
     - -
     - -
   * - カットオフ関数
     - ``flare_descriptor_cutoff_function``
     - 選択
     - -
     - ``quadratic``
     - 必須
     - quadratic（``quadratic``） / cos（``cos``）
     - -
   * - 径方向基底関数
     - ``flare_descriptor_radial_basis``
     - 選択
     - -
     - ``chebyshev``
     - 必須
     - Chebyshev（``chebyshev``）
     - -
   * - Langevin 摩擦係数
     - ``flare_otf_friction``
     - 数値
     - -
     - ``0.10180527006906766``
     - 0.0 以上、必須
     - -
     - 「MD エンジン」が「Langevin」のとき
   * - NPT 温度緩和時間
     - ``flare_otf_ttime``
     - 数値
     - fs
     - ``2.0``
     - 0.0 以上、必須
     - -
     - 「MD エンジン」が「NPT」のとき
   * - エネルギーノイズ
     - ``flare_energy_noise``
     - 数値（指数表記）
     - -
     - ``0.01``
     - 0.0 以上、必須
     - -
     - -
   * - NPT 圧力緩和係数
     - ``flare_otf_pfactor``
     - 数値
     - -
     - ``100.0``
     - 0.0 以上
     - -
     - 「MD エンジン」が「NPT」のとき
   * - 力ノイズ
     - ``flare_forces_noise``
     - 数値（指数表記）
     - -
     - ``0.05``
     - 0.0 以上、必須
     - -
     - -
   * - 外部圧力
     - ``flare_otf_externalstress``
     - 数値
     - bar
     - ``0.0``
     - -
     - -
     - 「MD エンジン」が「NPT」のとき
   * - ストレスノイズ
     - ``flare_stress_noise``
     - 数値（指数表記）
     - -
     - ``0.005``
     - 0.0 以上、必須
     - -
     - -
   * - タイムステップ
     - ``flare_otf_dt``
     - 数値
     - ps
     - ``0.001``
     - 0.0001 以上、必須
     - -
     - -
   * - カットオフ半径
     - ``flare_cutoff``
     - 数値
     - Å
     - ``5.0``
     - 0.0 以上、必須
     - -
     - -
   * - ステップ数
     - ``flare_otf_number_of_steps``
     - 整数
     - -
     - ``2000``
     - 1 以上、必須
     - -
     - -
   * - 分散タイプ
     - ``flare_variance_type``
     - 選択
     - -
     - ``local``
     - 必須
     - local（``local``） / DTC（``DTC``） / SOR（``SOR``）
     - -
   * - 超パラメータ最適化回数
     - ``flare_max_iterations``
     - 整数
     - -
     - ``20``
     - 0 以上、必須
     - -
     - -
   * - LAMMPSマッピング使用
     - ``flare_use_mapping``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - 初期速度（温度 K）
     - ``flare_otf_initial_velocity``
     - 数値
     - K
     - ``800.0``
     - 0.0 以上、必須
     - -
     - -
   * - 不確かさ閾値
     - ``flare_otf_std_tolerance_factor``
     - 数値
     - -
     - ``-0.04``
     - 必須
     - -
     - -
   * - DFT呼び出し時の最大追加原子数（-1: 無制限）
     - ``flare_otf_max_atoms_added``
     - 整数
     - -
     - ``-1``
     - 必須
     - -
     - -
   * - 超パラメータ最適化開始 DFT 回数
     - ``flare_otf_train_hyps_start``
     - 整数
     - -
     - ``10``
     - 0 以上、必須
     - -
     - -
   * - 超パラメータ最適化終了 DFT 回数（inf: 無限）
     - ``flare_otf_train_hyps_end``
     - 文字列
     - -
     - ``inf``
     - -
     - -
     - -
   * - GPモデル書き出し詳細度
     - ``flare_otf_write_model``
     - 選択
     - -
     - ``4``
     - 必須
     - 0（書き出しなし）（``0``） / 1（終了時）（``1``） / 2（超パラメータ最適化後）（``2``） / 3（DFT呼び出し後）（``3``） / 4（チェックポイント付き）（``4``）
     - -
   * - 原子追加スタイル
     - ``flare_otf_update_style``
     - 選択
     - -
     - ``threshold``
     - 必須
     - threshold（閾値以上を追加）（``threshold``） / add\_n（最大N個追加）（``add_n``）
     - -
   * - 原子追加閾値
     - ``flare_otf_update_threshold``
     - 数値
     - -
     - ``0.02``
     - 0.0 以上、必須
     - -
     - -
   * - 力のみで学習
     - ``flare_otf_force_only``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -



#######
GROMACS
#######

++++++++++
構造最適化
++++++++++

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
   * - 周期境界条件
     - ``pbc``
     - 選択
     - -
     - ``xyz``
     - 必須
     - xyz（全方向周期）（``xyz``） / xy（z方向非周期）（``xy``） / no（非周期）（``False``）
     - -
   * - トポロジーファイル
     - ``topology_file``
     - ファイル
     - -
     - -
     - -
     - -
     - -

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
     - ``1000``
     - 1 以上 2000 以下、必須
     - -
     - -
   * - 力の収束閾値
     - ``opt_force_convergence``
     - 数値
     - kJ/mol/nm
     - ``100.0``
     - 0.001 以上、必須
     - -
     - -
   * - 初期ステップ幅
     - ``gromacs_emstep``
     - 数値
     - nm
     - ``0.01``
     - 0.0001 以上
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 積分器（最小化アルゴリズム）
     - ``gromacs_integrator``
     - 選択
     - -
     - ``steep``
     - 必須
     - 最急降下法（steep）（``steep``） / 共役勾配法（cg）（``cg``） / L-BFGS（``l-bfgs``）
     - -


++++++++++++++
古典分子動力学
++++++++++++++

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
   * - 周期境界条件
     - ``pbc``
     - 選択
     - -
     - ``xyz``
     - 必須
     - xyz（全方向周期）（``xyz``） / xy（z方向非周期）（``xy``） / no（非周期）（``False``）
     - -
   * - トポロジーファイル
     - ``topology_file``
     - ファイル
     - -
     - -
     - -
     - -
     - -

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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``1.0``
     - 0.001 以上 100.0 以下、必須
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
     - ``ensemble``
     - 選択
     - -
     - ``NVT``
     - 必須
     - NVE（ミクロカノニカル）（``NVE``） / NVT（カノニカル）（``NVT``） / NPT（等温等圧）（``NPT``）
     - -
   * - 圧力（NPT のみ）
     - ``pressure``
     - 数値
     - GPa
     - ``0.0``
     - -
     - -
     - 「アンサンブル」が「NPT（等温等圧）」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 温度制御アルゴリズム
     - ``thermostat``
     - 選択
     - -
     - ``V-rescale``
     - 必須
     - V-rescale（推奨）（``V-rescale``） / Nosé-Hoover（``Nose-Hoover``） / Berendsen（``Berendsen``）
     - -
   * - 温度緩和時間
     - ``gromacs_tau_t``
     - 数値
     - ps
     - ``1.0``
     - 0.001 以上、必須
     - -
     - -
   * - 出力間隔
     - ``gromacs_output_freq``
     - 整数
     - steps
     - ``100``
     - 1 以上、必須
     - -
     - -



#####
HybMD
#####

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``0.5``
     - 0.001 以上 100.0 以下、必須
     - -
     - -
   * - ステップ数
     - ``num_steps``
     - 整数
     - -
     - ``100``
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
   * - MD積分器
     - ``hybmd_dynamics_func``
     - 選択
     - -
     - ``Langevin``
     - 必須
     - Langevin（``Langevin``） / Nose-Hoover Chain（``NHC``）
     - -
   * - 外部電場 X
     - ``hybmd_efield_x``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場 Y
     - ``hybmd_efield_y``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場 Z
     - ``hybmd_efield_z``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - OFDFT/Bader更新間隔
     - ``hybmd_of_interval``
     - 整数
     - -
     - ``10``
     - 1 以上、必須
     - -
     - -
   * - 機械学習ポテンシャル
     - ``hybmd_mlip_potential``
     - 選択
     - -
     - ``chgnet``
     - 必須
     - CHGNet（``chgnet``） / Orb-v3（``orbv3``）
     - -
   * - MLIP計算デバイス
     - ``hybmd_mlip_device``
     - 選択
     - -
     - ``cpu``
     - 必須
     - CPU（``cpu``） / CUDA GPU（``cuda``）
     - -
   * - 初期化モード
     - ``hybmd_init_mode``
     - 選択
     - -
     - ``scratch``
     - 必須
     - 新規開始（``scratch``） / 継続計算（``continue``）
     - -
   * - 初期構造ファイル
     - ``hybmd_structure_file``
     - ファイル
     - -
     - ``rsdft.atom``
     - -
     - -
     - 「初期化モード」が「新規開始」のとき
   * - 初期構造フォーマット
     - ``hybmd_structure_format``
     - 選択
     - -
     - ``cif``
     - -
     - CIF（``cif``） / Extended XYZ（``extxyz``） / VASP（``vasp``）
     - 「初期化モード」が「新規開始」のとき
   * - 再開用trajectory
     - ``hybmd_restart_file``
     - ファイル
     - -
     - -
     - -
     - -
     - 「初期化モード」が「継続計算」のとき
   * - OFDFT入力ファイル
     - ``hybmd_dftinput_file``
     - ファイル
     - -
     - ``scf.ini``
     - 必須
     - -
     - -
   * - Langevin摩擦係数
     - ``hybmd_friction``
     - 数値
     - -
     - ``0.1``
     - 0.0 以上
     - -
     - 「MD積分器」が「Langevin」のとき
   * - NHC緩和時間
     - ``hybmd_tdamp``
     - 数値
     - fs
     - ``50.0``
     - 0.0 以上
     - -
     - 「MD積分器」が「Nose-Hoover Chain」のとき
   * - trajectory出力間隔
     - ``hybmd_traj_interval``
     - 整数
     - -
     - ``1``
     - 1 以上
     - -
     - -
   * - 電場力用Bader解析
     - ``hybmd_bader_force``
     - 選択
     - -
     - ``pybader``
     - 必須
     - pybader（``pybader``） / Henkelman bader（``henkelman``）
     - -
   * - Henkelman Baderを併用
     - ``hybmd_bader_henkelman``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 乱数シード
     - ``hybmd_seed``
     - 整数
     - -
     - ``111``
     - 0 以上
     - -
     - -
   * - trajectory出力ファイル名
     - ``hybmd_traj_file``
     - 文字列
     - -
     - ``md.traj``
     - 必須
     - -
     - -
   * - MDログファイル名
     - ``hybmd_log_file``
     - 文字列
     - -
     - ``md.log``
     - 必須
     - -
     - -
   * - Bader電荷ログファイル名
     - ``hybmd_bader_log_file``
     - 文字列
     - -
     - ``bader.log``
     - 必須
     - -
     - -
   * - 停止ファイル名
     - ``hybmd_stopfile_name``
     - 文字列
     - -
     - ``hybmd_stopfile``
     - -
     - -
     - -


+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - OFDFTグリッドカットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - eV
     - ``800.0``
     - 0.0 以上、必須
     - -
     - -

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
   * - OFDFTタスク
     - ``hybmd_job_task``
     - 選択
     - -
     - ``Optdensity``
     - 必須
     - 密度最適化（``Optdensity``） / 計算のみ（``Calculation``）
     - -
   * - 密度最適化最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``1000``
     - 1 以上、必須
     - -
     - -
   * - 密度最適化収束閾値
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
     - ``1e-08``
     - 0.0 以上、必須
     - -
     - -
   * - 運動エネルギー密度汎関数
     - ``hybmd_kedf``
     - 選択
     - -
     - ``GGA``
     - 必須
     - TF（``TF``） / vW（``vW``） / GGA（``GGA``） / WT（``WT``） / MGP（``MGP``）
     - -
   * - KEDFカーネル
     - ``hybmd_kedf_kernel``
     - 選択
     - -
     - ``LKT``
     - -
     - LKT（``LKT``）
     - 「運動エネルギー密度汎関数」が「GGA」のとき
   * - 初期電子密度
     - ``hybmd_density_initialization``
     - 選択
     - -
     - ``atomic``
     - 必須
     - 原子密度重ね合わせ（``atomic``） / 一様電子ガス（``heg``） / 密度ファイルから読み込み（``read``）
     - -
   * - 初期密度ファイル
     - ``hybmd_density_file``
     - ファイル
     - -
     - -
     - -
     - -
     - 「初期電子密度」が「密度ファイルから読み込み」のとき
   * - 密度最適化手法
     - ``hybmd_opt_method``
     - 選択
     - -
     - ``CG-HS``
     - 必須
     - CG-HS（``CG-HS``） / CG-DY（``CG-DY``） / CG-FR（``CG-FR``） / LBFGS（``LBFGS``）
     - -
   * - ラインサーチ最大回数
     - ``hybmd_opt_maxls``
     - 整数
     - -
     - ``200``
     - 1 以上
     - -
     - -
   * - 関数評価最大回数
     - ``hybmd_opt_maxfun``
     - 整数
     - -
     - ``50``
     - 1 以上
     - -
     - -
   * - ラインサーチ係数 c1
     - ``hybmd_opt_c1``
     - 数値（指数表記）
     - -
     - ``0.0001``
     - 0.0 以上
     - -
     - -
   * - ラインサーチ係数 c2
     - ``hybmd_opt_c2``
     - 数値
     - -
     - ``0.8``
     - 0.0 以上
     - -
     - -
   * - 初期ステップ幅
     - ``hybmd_opt_h0``
     - 数値
     - -
     - ``0.025``
     - 0.0 以上
     - -
     - -
   * - PME線形補間
     - ``hybmd_math_linearie``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - マルチステップ数
     - ``hybmd_math_multistep``
     - 整数
     - -
     - ``1``
     - 1 以上
     - -
     - -
   * - 密度再利用（MATH.reuse）
     - ``hybmd_math_reuse``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - 初期磁気モーメント
     - ``hybmd_density_magmom``
     - 数値
     - -
     - ``0.0``
     - -
     - -
     - 「スピン」が「コリニア磁性」のとき
   * - 密度出力ファイル名
     - ``hybmd_density_output``
     - 文字列
     - -
     - ``den.cube``
     - -
     - -
     - -
   * - 参照密度出力ファイル名（Henkelman用）
     - ``hybmd_density_ref_output``
     - 文字列
     - -
     - ``refden.cube``
     - -
     - -
     - 「Henkelman Bader用密度出力」が「有効」のとき
   * - Henkelman参照密度出力（計算用）
     - ``hybmd_density_ref_output_calc``
     - 文字列
     - -
     - ``refden_calc.cube``
     - -
     - -
     - 「Henkelman Bader用密度出力」が「有効」のとき
   * - Bader解析を出力
     - ``hybmd_output_write_bader``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - Bader voxel offset
     - ``hybmd_output_voxeloff``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - 価電子Bader電荷
     - ``hybmd_bader_charge_val``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - コア密度Bader電荷
     - ``hybmd_bader_charge_core``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - 参照密度Bader電荷
     - ``hybmd_bader_charge_ref``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
   * - Henkelman Bader用密度出力
     - ``hybmd_henkelman_density``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 擬ポテンシャルファイル（元素 = ファイル名）
     - ``hybmd_pp_files``
     - textarea
     - -
     - -
     - 必須
     - -
     - -
   * - Core Width（元素 = 値）
     - ``hybmd_core_widths``
     - textarea
     - -
     - -
     - -
     - -
     - -



######
LAMMPS
######

++++++++++
構造最適化
++++++++++

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


++++++++++++++
古典分子動力学
++++++++++++++

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



##########
Quloud-Mag
##########

++++++++++++++++++++
モンテカルロ磁性計算
++++++++++++++++++++

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
   * - 境界条件 a 方向
     - ``mag_boundary_x``
     - 選択
     - -
     - ``1``
     - -
     - Free（``0``） / Periodic（``1``）
     - -
   * - 境界条件 b 方向
     - ``mag_boundary_y``
     - 選択
     - -
     - ``1``
     - -
     - Free（``0``） / Periodic（``1``）
     - -
   * - 境界条件 c 方向
     - ``mag_boundary_z``
     - 選択
     - -
     - ``1``
     - -
     - Free（``0``） / Periodic（``1``）
     - -
   * - スーパーセル n1
     - ``mag_n1``
     - 整数
     - -
     - ``10``
     - -
     - -
     - -
   * - スーパーセル n2
     - ``mag_n2``
     - 整数
     - -
     - ``10``
     - -
     - -
     - -
   * - スーパーセル n3
     - ``mag_n3``
     - 整数
     - -
     - ``10``
     - -
     - -
     - -
   * - 温度 最小値 (K)
     - ``mag_temp_min``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 温度 最大値 (K)
     - ``mag_temp_max``
     - 数値
     - -
     - ``1200``
     - -
     - -
     - -
   * - 温度 刻み幅 ΔT (K)
     - ``mag_temp_delta``
     - 数値
     - -
     - ``100``
     - -
     - -
     - -
   * - モンテカルロステップ数 (平衡化)
     - ``mag_nstep_equilibrium``
     - 整数
     - -
     - ``10000``
     - -
     - -
     - -
   * - モンテカルロステップ数 (測定)
     - ``mag_nstep_measure``
     - 整数
     - -
     - ``10000``
     - -
     - -
     - -
   * - サンプル数
     - ``mag_nreplica``
     - 整数
     - -
     - ``1``
     - -
     - -
     - -
   * - 磁場 最小値 (Tesla)
     - ``mag_hmag_min``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 磁場 最大値 (Tesla)
     - ``mag_hmag_max``
     - 数値
     - -
     - ``0.1``
     - -
     - -
     - -
   * - 磁場 刻み幅 ΔH (Tesla)
     - ``mag_hmag_delta``
     - 数値
     - -
     - ``1``
     - -
     - -
     - -
   * - 磁場方向 x
     - ``mag_hmag_x``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 磁場方向 y
     - ``mag_hmag_y``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 磁場方向 z
     - ``mag_hmag_z``
     - 数値
     - -
     - ``1``
     - -
     - -
     - -
   * - 一軸異方性定数 k1x (meV)
     - ``mag_aniso_unix``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 一軸異方性定数 k1y (meV)
     - ``mag_aniso_uniy``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 一軸異方性定数 k1z (meV)
     - ``mag_aniso_uniz``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 立方異方性定数 k2x (meV)
     - ``mag_aniso_cubx``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 立方異方性定数 k2y (meV)
     - ``mag_aniso_cuby``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 立方異方性定数 k2z (meV)
     - ``mag_aniso_cubz``
     - 数値
     - -
     - ``0``
     - -
     - -
     - -
   * - 初期状態パラメータ
     - ``mag_initial_state``
     - 選択
     - -
     - ``0``
     - -
     - 平衡探索 (Searching Equilibrium)（``0``） / ランダム開始 (Random Start)（``1``） / heis.in に従う (Init Mag.)（``2``）
     - -
   * - アルゴリズム
     - ``mag_algorithm``
     - 選択
     - -
     - ``0``
     - -
     - メトロポリス法（``0``） / ヒートバス法（``1``）
     - -


++++++++++++++++
LLG ダイナミクス
++++++++++++++++

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
   * - Nx
     - ``mag_llg_nx``
     - 整数
     - -
     - ``50``
     - 1 以上、必須
     - -
     - -
   * - Ny
     - ``mag_llg_ny``
     - 整数
     - -
     - ``50``
     - 1 以上、必須
     - -
     - -
   * - Nz
     - ``mag_llg_nz``
     - 整数
     - -
     - ``50``
     - 1 以上、必須
     - -
     - -
   * - Lx
     - ``mag_llg_lx``
     - 数値（指数表記）
     - m
     - ``1e-08``
     - 0 以上、必須
     - -
     - -
   * - Ly
     - ``mag_llg_ly``
     - 数値（指数表記）
     - m
     - ``1e-08``
     - 0 以上、必須
     - -
     - -
   * - Lz
     - ``mag_llg_lz``
     - 数値（指数表記）
     - m
     - ``1e-08``
     - 0 以上、必須
     - -
     - -
   * - 境界条件
     - ``mag_llg_bc``
     - 選択
     - -
     - ``1``
     - -
     - Free（``0``） / Periodic（``1``）
     - -
   * - 温度
     - ``mag_llg_temperature``
     - 数値
     - K
     - ``296``
     - 0 以上、必須
     - -
     - -
   * - M0（飽和磁化）
     - ``mag_llg_m0``
     - 数値（指数表記）
     - A/m
     - ``473980.0``
     - 0 以上、必須
     - -
     - -
   * - Mnormal（規格化磁化）
     - ``mag_llg_mnormal``
     - 数値
     - -
     - ``0.7779475927``
     - 0 以上 1 以下、必須
     - -
     - -
   * - A0（交換スティフネス）
     - ``mag_llg_a0``
     - 数値（指数表記）
     - J/m
     - ``8.3845e-12``
     - 0 以上、必須
     - -
     - -
   * - Ku1\_x0（一次異方性定数 x）
     - ``mag_llg_ku1x0``
     - 数値
     - J/m³
     - ``0``
     - 必須
     - -
     - -
   * - Ku1\_y0（一次異方性定数 y）
     - ``mag_llg_ku1y0``
     - 数値
     - J/m³
     - ``0``
     - 必須
     - -
     - -
   * - Ku1\_z0（一次異方性定数 z）
     - ``mag_llg_ku1z0``
     - 数値
     - J/m³
     - ``0``
     - 必須
     - -
     - -
   * - Ku2\_x0（二次異方性定数 x）
     - ``mag_llg_ku2x0``
     - 数値
     - J/m³
     - ``0``
     - 必須
     - -
     - -
   * - Ku2\_y0（二次異方性定数 y）
     - ``mag_llg_ku2y0``
     - 数値
     - J/m³
     - ``0``
     - 必須
     - -
     - -
   * - Ku2\_z0（二次異方性定数 z）
     - ``mag_llg_ku2z0``
     - 数値
     - J/m³
     - ``0``
     - 必須
     - -
     - -
   * - alpha（ギルバート減衰定数）
     - ``mag_llg_alpha``
     - 数値
     - -
     - ``0.002847469702``
     - 0 以上、必須
     - -
     - -
   * - Field Strength（磁場強度）
     - ``mag_llg_field_strength``
     - 数値
     - A/m
     - ``0.1``
     - 0 以上、必須
     - -
     - -
   * - Frequency（周波数）
     - ``mag_llg_frequency``
     - 数値（指数表記）
     - Hz
     - ``500000000.0``
     - 0 以上、必須
     - -
     - -
   * - hx（磁場方向 x 成分）
     - ``mag_llg_hx``
     - 数値
     - -
     - ``0``
     - 必須
     - -
     - -
   * - hy（磁場方向 y 成分）
     - ``mag_llg_hy``
     - 数値
     - -
     - ``0``
     - 必須
     - -
     - -
   * - hz（磁場方向 z 成分）
     - ``mag_llg_hz``
     - 数値
     - -
     - ``1``
     - 必須
     - -
     - -
   * - Simulation Time（シミュレーション時間）
     - ``mag_llg_simulation_time``
     - 数値（指数表記）
     - s
     - ``1e-09``
     - 0 以上、必須
     - -
     - -
   * - Time Step（タイムステップ）
     - ``mag_llg_time_step``
     - 数値（指数表記）
     - s
     - ``1e-13``
     - 0 以上、必須
     - -
     - -
   * - Thermalization Time（熱化時間）
     - ``mag_llg_thermalization_time``
     - 数値（指数表記）
     - s
     - ``1e-07``
     - 0 以上、必須
     - -
     - -



######
OpenMX
######

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

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
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -


++++++++++
構造最適化
++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 最適化アルゴリズム
     - ``openmx_opt_type``
     - 選択
     - -
     - ``RF``
     - 必須
     - Steepest Descent (Opt)（``Opt``） / DIIS（``DIIS``） / BFGS（``BFGS``） / Rational Function (RF)（``RF``） / Eigenvector Following (EF)（``EF``）
     - -
   * - DIIS 履歴数
     - ``openmx_diis_history``
     - 整数
     - -
     - ``3``
     - 1 以上、必須
     - -
     - -
   * - DIIS 開始ステップ
     - ``openmx_start_diis``
     - 整数
     - -
     - ``5``
     - 1 以上、必須
     - -
     - -
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -

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
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
   * - 最適化最大ステップ数
     - ``opt_max_steps``
     - 整数
     - -
     - ``100``
     - 1 以上 2000 以下、必須
     - -
     - -
   * - 力の収束閾値
     - ``opt_force_convergence``
     - 数値（指数表記）
     - eV/Å
     - ``0.0154``
     - 1e-06 以上
     - -
     - -
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき


++++++++++++++
格子定数最適化
++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 最適化アルゴリズム
     - ``openmx_opt_type``
     - 選択
     - -
     - ``RFC5``
     - 必須
     - 格子のみ・最急降下（OptC1）（``OptC1``） / \|a1\|=\|a2\|≠\|a3\|・最急降下（OptC4）（``OptC4``） / 格子＋内部座標・最急降下（OptC5）（``OptC5``） / 格子＋内部座標・RF/DIIS/BFGS（RFC5）（``RFC5``）
     - -
   * - DIIS 履歴数
     - ``openmx_diis_history``
     - 整数
     - -
     - ``3``
     - 1 以上、必須
     - -
     - -
   * - DIIS 開始ステップ
     - ``openmx_start_diis``
     - 整数
     - -
     - ``5``
     - 1 以上、必須
     - -
     - -
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -

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
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
   * - 最適化最大ステップ数
     - ``opt_max_steps``
     - 整数
     - -
     - ``100``
     - 1 以上 2000 以下、必須
     - -
     - -
   * - 力の収束閾値
     - ``opt_force_convergence``
     - 数値（指数表記）
     - eV/Å
     - ``0.0154``
     - 1e-06 以上
     - -
     - -
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき


++++++++++++++
電子バンド構造
++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - SCF k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

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
   * - バンド計算経路
     - ``band_kpath``
     - kpath
     - -
     - ``{"method": "k-auto", "points": [{"label": "Γ", "x": 0.0, "y": 0.0, "z": 0.0, "division": 20}, {"label": "Γ", "x": 1.0, "y": 0.0, "z": 0.0, "division": 20}]}``
     - -
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
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -


+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - SCF k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

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
   * - DOS k グリッド（a 軸）
     - ``openmx_dos_kgrid_a``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - DOS k グリッド（b 軸）
     - ``openmx_dos_kgrid_b``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - DOS k グリッド（c 軸）
     - ``openmx_dos_kgrid_c``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - DOS エネルギー範囲（最小）
     - ``openmx_dos_erange_min``
     - 数値
     - eV
     - ``-20.0``
     - 必須
     - -
     - -
   * - DOS エネルギー範囲（最大）
     - ``openmx_dos_erange_max``
     - 数値
     - eV
     - ``20.0``
     - 必須
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
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -


++++++++++
分子動力学
++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``0.5``
     - 0.01 以上 10.0 以下、必須
     - -
     - -
   * - ステップ数
     - ``num_steps``
     - 整数
     - -
     - ``2000``
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
     - ``ensemble``
     - 選択
     - -
     - ``NVT``
     - 必須
     - NVE（ミクロカノニカル）（``NVE``） / NVT（カノニカル）（``NVT``）
     - -
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
   * - 熱浴質量
     - ``md_mass_heat_bath``
     - 数値
     - bohr²AMU
     - ``20.0``
     - 0.0 以上、必須
     - -
     - 「アンサンブル」が「NVT（カノニカル）」のとき
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -


++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / スピン偏極（非縮退）（``withspin``） / ノンコリニア（スピン軌道相互作用）（``nc``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LSDA-CA（``LSDA-CA``） / LSDA-PW（``LSDA-PW``） / GGA-PBE（``GGA-PBE``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子温度
     - ``smearing_width``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - カットオフエネルギー
     - ``ecut``
     - 数値
     - Ry
     - ``200.0``
     - 1.0 以上、必須
     - -
     - 「グリッド点数を固定する」が「無効」のとき
   * - グリッド点数を固定する
     - ``grid_fixed``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - グリッド点数（a軸）
     - ``ngrid_a``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（b軸）
     - ``ngrid_b``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - グリッド点数（c軸）
     - ``ngrid_c``
     - 整数
     - -
     - ``0``
     - 0 以上
     - -
     - 「グリッド点数を固定する」が「有効」のとき
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``on1``
     - -
     - on1 (vac-z-vac)（``on1``） / on2 (metal-z-metal)（``on2``） / on3 (vac-z-metal)（``on3``） / on4 (metal-z-metal with E field)（``on4``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - 軌道基底精度
     - ``orbital_basis_accuracy``
     - 選択
     - -
     - ``Standard``
     - 必須
     - Quick（``Quick``） / Standard（``Standard``） / Precise（``Precise``）
     - -
   * - 外部電場（a軸）
     - ``electric_field_a``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（b軸）
     - ``electric_field_b``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
   * - 外部電場（c軸）
     - ``electric_field_c``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -

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
   * - NEB イメージ数
     - ``num_images``
     - 整数
     - -
     - ``5``
     - 3 以上 20 以下、必須
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
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -
   * - Climbing Image NEB
     - ``climb_image``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - スプリング定数
     - ``spring_constant``
     - 数値
     - eV/Å²
     - ``0.5``
     - 0.01 以上
     - -
     - -
   * - NC スピン拘束
     - ``openmx_ncspin``
     - 選択
     - -
     - 無効
     - -
     - True（``True``） / False（``False``）
     - 「スピン」が「ノンコリニア（スピン軌道相互作用）」のとき
   * - NC スピン拘束ポテンシャル
     - ``openmx_ncv``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「NC スピン拘束」が「on」のとき
   * - ESM 方向
     - ``openmx_esm_dir``
     - 選択
     - -
     - ``z``
     - -
     - x（``x``） / y（``y``） / z（``z``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM 電位差
     - ``openmx_esm_efield``
     - 数値
     - eV
     - ``0.0``
     - 必須
     - -
     - 「ESM境界条件」が「on4 (metal-z-metal with E field)」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - ミキシング手法
     - ``openmx_mixing_type``
     - 選択
     - -
     - ``rmm-diisk``
     - 必須
     - Simple（``Simple``） / RMM-DIISK（``rmm-diisk``）
     - -
   * - 初期ミキシング重み
     - ``openmx_init_weight``
     - 数値
     - -
     - ``0.3``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - 最小ミキシング重み
     - ``openmx_min_weight``
     - 数値
     - -
     - ``0.001``
     - 0.0 以上 1.0 以下、刻み 0.001、必須
     - -
     - -
   * - 最大ミキシング重み
     - ``openmx_max_weight``
     - 数値
     - -
     - ``0.4``
     - 0.0 以上 1.0 以下、刻み 0.1、必須
     - -
     - -
   * - ミキシング履歴数
     - ``openmx_mix_history``
     - 整数
     - -
     - ``30``
     - 1 以上、必須
     - -
     - -
   * - Pulay ミキシング開始ステップ
     - ``openmx_start_pulay``
     - 整数
     - -
     - ``6``
     - 1 以上、必須
     - -
     - -
   * - 固有値ソルバー
     - ``openmx_solver``
     - 選択
     - -
     - ``band``
     - 必須
     - Band（``band``） / Cluster（``cluster``）
     - -


++++++++++++++++++
交換結合パラメータ
++++++++++++++++++

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
   * - 極の数
     - ``jx_npoles``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - JX k グリッド (k1)
     - ``jx_nkgrid_k1``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - JX k グリッド (k2)
     - ``jx_nkgrid_k2``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - JX k グリッド (k3)
     - ``jx_nkgrid_k3``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - 最大セル ID (c1)
     - ``jx_max_cel_id_c1``
     - 整数
     - -
     - ``2``
     - 0 以上、必須
     - -
     - -
   * - 最大セル ID (c2)
     - ``jx_max_cel_id_c2``
     - 整数
     - -
     - ``2``
     - 0 以上、必須
     - -
     - -
   * - 最大セル ID (c3)
     - ``jx_max_cel_id_c3``
     - 整数
     - -
     - ``2``
     - 0 以上、必須
     - -
     - -



####
Psi4
####

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

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
   * - スピン多重度
     - ``spin``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
   * - Reference
     - ``reference``
     - 選択
     - -
     - ``RHF``
     - 必須
     - RHF（制限付き、閉殻専用）（``RHF``） / UHF（非制限）（``UHF``） / ROHF（制限付き開殻）（``ROHF``）
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 計算手法
     - ``exchange_correlation``
     - 選択
     - -
     - ``b3lyp``
     - 必須
     - HF（``hf``） / B3LYP（``b3lyp``） / PBE（``pbe``） / M06-2X（``m06-2x``） / ωB97X-D3BJ（``wb97x-d3bj``） / CAM-B3LYP（``cam-b3lyp``） / MP2（``mp2``）
     - -
   * - 基底関数系
     - ``basis_set``
     - 選択
     - -
     - ``6-31G(d,p)``
     - 必須
     - STO-3G（最小基底、高速・低精度）（``STO-3G``） / 3-21G（``3-21G``） / 6-31G(d,p)（標準）（``6-31G(d,p)``） / 6-311G(d,p)（``6-311G(d,p)``） / cc-pVDZ（``cc-pVDZ``） / cc-pVTZ（高精度）（``cc-pVTZ``） / aug-cc-pVDZ（拡散関数付き）（``aug-cc-pVDZ``）
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 分散補正種別
     - ``psi4_dispersion_type``
     - 選択
     - -
     - ``d3bj``
     - -
     - D3(BJ)（推奨）（``d3bj``） / D3(zero)（``d3zero``） / D2（``d2``） / NL（非局所）（``nl``）
     - 「ファンデルワールス補正」が「有効」のとき


++++++++++
構造最適化
++++++++++

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
   * - スピン多重度
     - ``spin``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
   * - Reference
     - ``reference``
     - 選択
     - -
     - ``RHF``
     - 必須
     - RHF（制限付き、閉殻専用）（``RHF``） / UHF（非制限）（``UHF``） / ROHF（制限付き開殻）（``ROHF``）
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 計算手法
     - ``exchange_correlation``
     - 選択
     - -
     - ``b3lyp``
     - 必須
     - HF（``hf``） / B3LYP（``b3lyp``） / PBE（``pbe``） / M06-2X（``m06-2x``） / ωB97X-D3BJ（``wb97x-d3bj``） / CAM-B3LYP（``cam-b3lyp``） / MP2（``mp2``）
     - -
   * - 基底関数系
     - ``basis_set``
     - 選択
     - -
     - ``6-31G(d,p)``
     - 必須
     - STO-3G（最小基底、高速・低精度）（``STO-3G``） / 3-21G（``3-21G``） / 6-31G(d,p)（標準）（``6-31G(d,p)``） / 6-311G(d,p)（``6-311G(d,p)``） / cc-pVDZ（``cc-pVDZ``） / cc-pVTZ（高精度）（``cc-pVTZ``） / aug-cc-pVDZ（拡散関数付き）（``aug-cc-pVDZ``）
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 分散補正種別
     - ``psi4_dispersion_type``
     - 選択
     - -
     - ``d3bj``
     - -
     - D3(BJ)（推奨）（``d3bj``） / D3(zero)（``d3zero``） / D2（``d2``） / NL（非局所）（``nl``）
     - 「ファンデルワールス補正」が「有効」のとき

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
   * - 収束閾値 (G\_CONVERGENCE)
     - ``psi4_g_convergence``
     - 選択
     - -
     - ``QCHEM``
     - 必須
     - QCHEM（デフォルト）（``QCHEM``） / GAU（``GAU``） / GAU\_LOOSE（緩い）（``GAU_LOOSE``） / GAU\_TIGHT（厳しい）（``GAU_TIGHT``） / GAU\_VERYTIGHT（非常に厳しい）（``GAU_VERYTIGHT``） / TURBOMOLE（``TURBOMOLE``） / CFOUR（``CFOUR``） / MOLPRO（``MOLPRO``） / NWCHEM\_LOOSE（緩い）（``NWCHEM_LOOSE``） / INTERFRAG\_TIGHT（分子間、厳しい）（``INTERFRAG_TIGHT``）
     - -
   * - 最大反復回数 (GEOM\_MAXITER)
     - ``psi4_geom_maxiter``
     - 整数
     - -
     - ``50``
     - 1 以上 1000 以下、必須
     - -
     - -


++++++++++++
分子振動解析
++++++++++++

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
   * - 温度 (K)
     - ``psi4_temperature_k``
     - 数値
     - K
     - ``298.15``
     - 0.0 以上
     - -
     - -
   * - 圧力 (atm)
     - ``psi4_pressure_atm``
     - 数値
     - atm
     - ``1.0``
     - 0.0 以上
     - -
     - -



################
Quantum ESPRESSO
################

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（a 軸）
     - ``kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（b 軸）
     - ``kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（c 軸）
     - ``kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``Gaussian``
     - -
     - ガウシアン（``Gaussian``） / Methfessel-Paxton（``MP``） / フェルミ-ディラック（``FD``） / Marzari-Vanderbilt（``MV``）
     - -
   * - スメアリング幅
     - ``smearing_width``
     - 数値
     - Ry
     - ``0.01``
     - 0.001 以上 1000.0 以下、必須
     - -
     - -
   * - 平面波カットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 密度・ポテンシャルカットオフエネルギー
     - ``ecut_rho``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``bc1``
     - -
     - bc1 (vac-slab-vac)（``bc1``） / bc2 (metal-slab-metal)（``bc2``） / bc3 (vac-slab-metal)（``bc3``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM電場
     - ``esm_efield``
     - 数値
     - Ry/a.u.
     - ``0.0``
     - -1000.0 以上 1000.0 以下、必須
     - -
     - 「有効遮蔽媒質」が「有効」、かつ「ESM境界条件」が「bc2 (metal-slab-metal)」のとき

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
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``100``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 対角化手法
     - ``qe_diagonalization``
     - 選択
     - -
     - ``david``
     - 必須
     - Davidson（``david``） / 共役勾配法（``cg``）
     - -


++++++++++
構造最適化
++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（a 軸）
     - ``kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（b 軸）
     - ``kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（c 軸）
     - ``kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``Gaussian``
     - -
     - ガウシアン（``Gaussian``） / Methfessel-Paxton（``MP``） / フェルミ-ディラック（``FD``） / Marzari-Vanderbilt（``MV``）
     - -
   * - スメアリング幅
     - ``smearing_width``
     - 数値
     - Ry
     - ``0.01``
     - 0.001 以上 1000.0 以下、必須
     - -
     - -
   * - 平面波カットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 密度・ポテンシャルカットオフエネルギー
     - ``ecut_rho``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``bc1``
     - -
     - bc1 (vac-slab-vac)（``bc1``） / bc2 (metal-slab-metal)（``bc2``） / bc3 (vac-slab-metal)（``bc3``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM電場
     - ``esm_efield``
     - 数値
     - Ry/a.u.
     - ``0.0``
     - -1000.0 以上 1000.0 以下、必須
     - -
     - 「有効遮蔽媒質」が「有効」、かつ「ESM境界条件」が「bc2 (metal-slab-metal)」のとき

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
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
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

~~~~~~~~~~~~~~
装置パラメータ
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
   * - イオン動力学
     - ``qe_ion_dynamics``
     - 選択
     - -
     - ``bfgs``
     - 必須
     - BFGS（``bfgs``） / Damped (quick-min Verlet)（``damp``） / FIRE（``fire``）
     - -
   * - 対角化手法
     - ``qe_diagonalization``
     - 選択
     - -
     - ``david``
     - 必須
     - Davidson（``david``） / 共役勾配法（``cg``）
     - -


++++++++++++++
格子定数最適化
++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（a 軸）
     - ``kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（b 軸）
     - ``kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（c 軸）
     - ``kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``Gaussian``
     - -
     - ガウシアン（``Gaussian``） / Methfessel-Paxton（``MP``） / フェルミ-ディラック（``FD``） / Marzari-Vanderbilt（``MV``）
     - -
   * - スメアリング幅
     - ``smearing_width``
     - 数値
     - Ry
     - ``0.01``
     - 0.001 以上 1000.0 以下、必須
     - -
     - -
   * - 平面波カットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 密度・ポテンシャルカットオフエネルギー
     - ``ecut_rho``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``bc1``
     - -
     - bc1 (vac-slab-vac)（``bc1``） / bc2 (metal-slab-metal)（``bc2``） / bc3 (vac-slab-metal)（``bc3``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM電場
     - ``esm_efield``
     - 数値
     - Ry/a.u.
     - ``0.0``
     - -1000.0 以上 1000.0 以下、必須
     - -
     - 「有効遮蔽媒質」が「有効」、かつ「ESM境界条件」が「bc2 (metal-slab-metal)」のとき

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
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
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
   * - 応力の収束閾値
     - ``opt_pressure_convergence``
     - 数値
     - GPa
     - ``0.5``
     - 0.0001 以上
     - -
     - -
   * - 目標圧力
     - ``opt_target_pressure``
     - 数値
     - GPa
     - ``0.0``
     - -
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - イオン動力学
     - ``qe_ion_dynamics``
     - 選択
     - -
     - ``bfgs``
     - 必須
     - BFGS（``bfgs``） / Damped (Beeman)（``damp``）
     - -
   * - 対角化手法
     - ``qe_diagonalization``
     - 選択
     - -
     - ``david``
     - 必須
     - Davidson（``david``） / 共役勾配法（``cg``）
     - -


++++++++++++++
電子バンド構造
++++++++++++++

この計算には、「ジョブ作成」で入力する項目はありません。

+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

この計算には、「ジョブ作成」で入力する項目はありません。

++++++++++++++++++++
投影状態密度（PDOS）
++++++++++++++++++++

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
   * - PDOS エネルギー下限
     - ``pdos_emin``
     - 数値
     - eV
     - ``-20.0``
     - 必須
     - -
     - -
   * - PDOS エネルギー上限
     - ``pdos_emax``
     - 数値
     - eV
     - ``20.0``
     - 必須
     - -
     - -
   * - PDOS エネルギー刻み
     - ``pdos_delta_e``
     - 数値
     - eV
     - ``0.01``
     - 1e-12 以上、必須
     - -
     - -


++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（a 軸）
     - ``kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（b 軸）
     - ``kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（c 軸）
     - ``kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``Gaussian``
     - -
     - ガウシアン（``Gaussian``） / Methfessel-Paxton（``MP``） / フェルミ-ディラック（``FD``） / Marzari-Vanderbilt（``MV``）
     - -
   * - スメアリング幅
     - ``smearing_width``
     - 数値
     - Ry
     - ``0.01``
     - 0.001 以上 1000.0 以下、必須
     - -
     - -
   * - 平面波カットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 密度・ポテンシャルカットオフエネルギー
     - ``ecut_rho``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``bc1``
     - -
     - bc1 (vac-slab-vac)（``bc1``） / bc2 (metal-slab-metal)（``bc2``） / bc3 (vac-slab-metal)（``bc3``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM電場
     - ``esm_efield``
     - 数値
     - Ry/a.u.
     - ``0.0``
     - -1000.0 以上 1000.0 以下、必須
     - -
     - 「有効遮蔽媒質」が「有効」、かつ「ESM境界条件」が「bc2 (metal-slab-metal)」のとき

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
   * - NEB イメージ数
     - ``num_images``
     - 整数
     - -
     - ``5``
     - 3 以上 20 以下、必須
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
     - ``1e-05``
     - 1e-12 以上
     - -
     - -
   * - Climbing Image NEB
     - ``climb_image``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - スプリング定数
     - ``spring_constant``
     - 数値
     - eV/Å²
     - ``0.5``
     - 0.01 以上
     - -
     - -


++++++++++++
フォノン計算
++++++++++++

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
   * - q点グリッド（a方向）
     - ``nq1``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - q点グリッド（b方向）
     - ``nq2``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - q点グリッド（c方向）
     - ``nq3``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - フォノン収束閾値
     - ``tr2_ph``
     - 数値（指数表記）
     - -
     - ``1e-14``
     - 必須
     - -
     - -
   * - 途中再開（recover）
     - ``recover``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -


+++++++++++++++++++++++++++++
X線吸収スペクトル（XSpectra）
+++++++++++++++++++++++++++++

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
   * - 計算タイプ
     - ``xas_calc_type``
     - 選択
     - -
     - ``xanes_dipole``
     - 必須
     - XANES 双極子（``xanes_dipole``） / XANES 四重極（``xanes_quadrupole``）
     - -
   * - X 線吸収端
     - ``xas_edge``
     - 選択
     - -
     - ``K``
     - 必須
     - K 端（``K``） / L1 端（``L1``） / L2 端（``L2``） / L3 端（``L3``）
     - -
   * - X 線 k ベクトル（x）
     - ``xkvec_x``
     - 数値
     - -
     - ``0.0``
     - 必須
     - -
     - -
   * - X 線 k ベクトル（y）
     - ``xkvec_y``
     - 数値
     - -
     - ``0.0``
     - 必須
     - -
     - -
   * - X 線 k ベクトル（z）
     - ``xkvec_z``
     - 数値
     - -
     - ``1.0``
     - 必須
     - -
     - -
   * - X 線偏極ベクトル（x）
     - ``xepsilon_x``
     - 数値
     - -
     - ``1.0``
     - 必須
     - -
     - -
   * - X 線偏極ベクトル（y）
     - ``xepsilon_y``
     - 数値
     - -
     - ``0.0``
     - 必須
     - -
     - -
   * - X 線偏極ベクトル（z）
     - ``xepsilon_z``
     - 数値
     - -
     - ``0.0``
     - 必須
     - -
     - -
   * - エネルギー下限
     - ``xemin``
     - 数値
     - eV
     - ``-10.0``
     - -
     - -
     - -
   * - エネルギー上限
     - ``xemax``
     - 数値
     - eV
     - ``30.0``
     - -
     - -
     - -
   * - ローレンツ幅
     - ``xgamma``
     - 数値
     - eV
     - ``0.8``
     - 0.001 以上
     - -
     - -
   * - Lanczos ステップ数
     - ``xniter``
     - 整数
     - -
     - ``2000``
     - 100 以上
     - -
     - -
   * - 占有状態カット
     - ``cut_occ_states``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - r\_paw（双極子）
     - ``r_paw_d``
     - 数値
     - -
     - ``2.0``
     - 0.1 以上
     - -
     - -
   * - r\_paw（四重極）
     - ``r_paw_q``
     - 数値
     - -
     - ``2.0``
     - 0.1 以上
     - -
     - -


+++++++++++++++++++++++
X線吸収スペクトル用 SCF
+++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（a 軸）
     - ``kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（b 軸）
     - ``kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッドオフセット（c 軸）
     - ``kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``Gaussian``
     - -
     - ガウシアン（``Gaussian``） / Methfessel-Paxton（``MP``） / フェルミ-ディラック（``FD``） / Marzari-Vanderbilt（``MV``）
     - -
   * - スメアリング幅
     - ``smearing_width``
     - 数値
     - Ry
     - ``0.01``
     - 0.001 以上 1000.0 以下、必須
     - -
     - -
   * - 平面波カットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 密度・ポテンシャルカットオフエネルギー
     - ``ecut_rho``
     - 数値
     - Ry
     - ``0.0``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
   * - 有効遮蔽媒質
     - ``esm``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ESM境界条件
     - ``esm_bc``
     - 選択
     - -
     - ``bc1``
     - -
     - bc1 (vac-slab-vac)（``bc1``） / bc2 (metal-slab-metal)（``bc2``） / bc3 (vac-slab-metal)（``bc3``）
     - 「有効遮蔽媒質」が「有効」のとき
   * - ESM電場
     - ``esm_efield``
     - 数値
     - Ry/a.u.
     - ``0.0``
     - -1000.0 以上 1000.0 以下、必須
     - -
     - 「有効遮蔽媒質」が「有効」、かつ「ESM境界条件」が「bc2 (metal-slab-metal)」のとき

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
   * - 吸収原子インデックス
     - ``absorber_atom_index``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
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
   * - SCF 収束閾値（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
     - ``1e-06``
     - 0.0 以上
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 対角化手法
     - ``qe_diagonalization``
     - 選択
     - -
     - ``david``
     - 必須
     - Davidson（``david``） / 共役勾配法（``cg``）
     - -


++++++++++++++++++++++++++++
固定ポテンシャル電子状態計算
++++++++++++++++++++++++++++

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
   * - NSCF k グリッド（a 軸）
     - ``qe_dos_kgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
   * - NSCF k グリッド（b 軸）
     - ``qe_dos_kgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
   * - NSCF k グリッド（c 軸）
     - ``qe_dos_kgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
   * - NSCF k グリッドオフセット（a 軸）
     - ``qe_dos_kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - NSCF k グリッドオフセット（b 軸）
     - ``qe_dos_kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - NSCF k グリッドオフセット（c 軸）
     - ``qe_dos_kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -


++++++++++++++++++++++++++++++++++++++
固定ポテンシャル電子状態計算（バンド）
++++++++++++++++++++++++++++++++++++++

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
   * - バンド計算経路
     - ``band_kpath``
     - kpath
     - -
     - ``{"method": "k-auto", "points": [{"label": "Γ", "x": 0.0, "y": 0.0, "z": 0.0, "division": 20}, {"label": "Γ", "x": 1.0, "y": 0.0, "z": 0.0, "division": 20}]}``
     - -
     - -
     - -


+++++++++++++++++
力定数計算（q2r）
+++++++++++++++++

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
   * - 音響和則補正
     - ``zasr``
     - 選択
     - -
     - ``simple``
     - -
     - なし（``no``） / simple（``simple``） / crystal（``crystal``） / one-dim（``one-dim``） / zero-dim（``zero-dim``）
     - -


++++++++++++++++++++++++++++
フォノンバンド分散（matdyn）
++++++++++++++++++++++++++++

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
   * - フォノン分散経路
     - ``q_kpath``
     - kpath
     - -
     - ``{"method": "k-auto", "points": [{"label": "Γ", "x": 0.0, "y": 0.0, "z": 0.0, "division": 20}, {"label": "Γ", "x": 1.0, "y": 0.0, "z": 0.0, "division": 20}]}``
     - -
     - -
     - -


++++++++++++++++++++++++++
フォノン状態密度（matdyn）
++++++++++++++++++++++++++

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
   * - q点グリッド（a方向）
     - ``matdyn_nk1``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - q点グリッド（b方向）
     - ``matdyn_nk2``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - q点グリッド（c方向）
     - ``matdyn_nk3``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -



#######
RadonPy
#######

+++++++++++++++++++++++
QM構造最適化 / RESP電荷
+++++++++++++++++++++++

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


++++++++++++++
高分子平衡化MD
++++++++++++++

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
   * - 目標原子数
     - ``radonpy_n_atoms``
     - 整数
     - -
     - ``1000``
     - 100 以上、必須
     - -
     - -
   * - 古典力場タイプ
     - ``classical_ff_type``
     - 選択
     - -
     - ``GAFF2``
     - 必須
     - GAFF2（推奨）（``GAFF2``） / GAFF2\_mod（``GAFF2_mod``） / GAFF（``GAFF``） / Dreiding（``Dreiding``）
     - -
   * - 高分子鎖数
     - ``radonpy_n_chains``
     - 整数
     - -
     - ``10``
     - 1 以上、必須
     - -
     - -
   * - 高分子タイプ
     - ``radonpy_polymer_type``
     - 選択
     - -
     - ``homo``
     - 必須
     - ホモポリマー（``homo``）
     - -
   * - タクティシティ
     - ``radonpy_tacticity``
     - 選択
     - -
     - ``atactic``
     - 必須
     - アタクチック（``atactic``） / アイソタクチック（``isotactic``） / シンジオタクチック（``syndiotactic``）
     - -

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
   * - 温度
     - ``temperature``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上、必須
     - -
     - -
   * - 圧力
     - ``radonpy_pressure``
     - 数値
     - atm
     - ``1.0``
     - 0.0 以上、必須
     - -
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 平衡化プロトコル
     - ``radonpy_eq_protocol``
     - 選択
     - -
     - ``EQ21step``
     - 必須
     - EQ21step（Larsen圧縮・再現性高）（``EQ21step``） / Annealing（焼きなまし）（``Annealing``）
     - -
   * - 乱数シード
     - ``radonpy_random_seed``
     - 整数
     - -
     - ``42``
     - 0 以上、必須
     - -
     - -


++++++++++++++++
溶解度パラメータ
++++++++++++++++

この計算には、「ジョブ作成」で入力する項目はありません。

++++++++++++++
ガラス転移温度
++++++++++++++

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
   * - 冷却開始温度
     - ``radonpy_tg_temp_high``
     - 数値
     - K
     - ``600.0``
     - 100.0 以上、必須
     - -
     - -
   * - 温度ステップ
     - ``radonpy_tg_temp_step``
     - 数値
     - K
     - ``20.0``
     - 1.0 以上、必須
     - -
     - -


++++++++
熱伝導率
++++++++

~~~~~~~~~~~~~~
装置パラメータ
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
   * - NEMD ステップ数
     - ``radonpy_tc_nemd_steps``
     - 整数
     - -
     - ``5000000``
     - 100000 以上、必須
     - -
     - -
   * - セル複製数（熱流方向）
     - ``radonpy_tc_n_replicate``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - 熱流方向
     - ``radonpy_tc_axis``
     - 選択
     - -
     - ``x``
     - 必須
     - X軸（``x``） / Y軸（``y``） / Z軸（``z``）
     - -


++++++++++++++++++++
ヤング率（機械特性）
++++++++++++++++++++

~~~~~~~~~~~~~~
装置パラメータ
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
   * - ひずみ速度
     - ``radonpy_elong_strain_rate``
     - 数値
     - ε/fs
     - ``5e-06``
     - 1e-07 以上 1e-05 以下、必須
     - -
     - -
   * - 変形方向
     - ``radonpy_elong_deform_axis``
     - 選択
     - -
     - ``x``
     - 必須
     - X軸（``x``） / Y軸（``y``） / Z軸（``z``）
     - -

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
   * - 最大ひずみ
     - ``radonpy_elong_max_strain``
     - 数値
     - -
     - ``0.5``
     - 0.01 以上 2.0 以下、必須
     - -
     - -


++++++++++
複素誘電率
++++++++++

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
   * - 交流電場周波数
     - ``radonpy_dielectric_freq``
     - 数値（指数表記）
     - Hz
     - ``1000000000.0``
     - 1.0 以上、必須
     - -
     - -
   * - 電場振幅
     - ``radonpy_dielectric_amplitude``
     - 数値
     - V/Å
     - ``0.01``
     - 0.0001 以上、必須
     - -
     - -



#####
RSDFT
#####

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 1e-06 以上 1000.0 以下、必須
     - -
     - -
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -

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
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
     - -
     - -


++++++++++
構造最適化
++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 1e-06 以上 1000.0 以下、必須
     - -
     - -
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -

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
   * - 力の収束閾値
     - ``opt_force_convergence``
     - 数値（指数表記）
     - eV/Å
     - ``0.0257``
     - 1e-06 以上
     - -
     - -
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
     - -
     - -


++++++++++++++
格子定数最適化
++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``4``
     - 1 以上、必須
     - -
     - -
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 1e-06 以上 1000.0 以下、必須
     - -
     - -
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -

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
   * - 力の収束閾値
     - ``opt_force_convergence``
     - 数値（指数表記）
     - eV/Å
     - ``0.0257``
     - 1e-06 以上
     - -
     - -
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
     - -
     - -


++++++++++++++
電子バンド構造
++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
   * - SCF k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 1e-06 以上 1000.0 以下、必須
     - -
     - -
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -

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
   * - バンド計算経路
     - ``band_kpath``
     - kpath
     - -
     - ``{"method": "k-auto", "points": [{"label": "Γ", "x": 0.0, "y": 0.0, "z": 0.0, "division": 20}, {"label": "Γ", "x": 1.0, "y": 0.0, "z": 0.0, "division": 20}]}``
     - -
     - -
     - -
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
     - -
     - -


+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
   * - SCF k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - SCF k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 1e-06 以上 1000.0 以下、必須
     - -
     - -
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -

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
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
     - -
     - -


++++++++++
分子動力学
++++++++++

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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
   * - k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 1e-06 以上 1000.0 以下、必須
     - -
     - -
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -

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
   * - MD法
     - ``rsdft_md_method``
     - 選択
     - -
     - ``bomd``
     - 必須
     - BOMD (Born-Oppenheimer)（``bomd``） / CPMD (Car-Parrinello)（``cpmd``）
     - -
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``0.5``
     - 0.001 以上 10.0 以下、必須
     - -
     - -
   * - ステップ数
     - ``num_steps``
     - 整数
     - -
     - ``2000``
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
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
   * - アンサンブル
     - ``rsdft_ensemble``
     - 選択
     - -
     - ``nvt``
     - 必須
     - NVE（ミクロカノニカル）（``nve``） / NVT（カノニカル）（``nvt``）
     - -
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
   * - 仮想電子質量
     - ``rsdft_fictmass``
     - 数値
     - Hartree
     - ``400.0``
     - 0.0 以上、必須
     - -
     - 「MD法」が「CPMD (Car-Parrinello)」のとき
   * - 温度制御（イオン）
     - ``rsdft_tcontrol``
     - 選択
     - -
     - ``nose``
     - 必須
     - NHC (Nosé-Hoover Chain)（``nose``） / Berendsen（``bere``） / 速度スケーリング（``vscl``）
     - 「アンサンブル」が「NVT（カノニカル）」のとき
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -
   * - NHCサーモスタット振動数
     - ``rsdft_omegan``
     - 数値
     - cm⁻¹
     - ``200.0``
     - 0.0 以上、必須
     - -
     - 「アンサンブル」が「NVT（カノニカル）」、かつ「温度制御（イオン）」が「NHC (Nosé-Hoover Chain)」のとき
   * - 速度スケーリング温度変動幅
     - ``rsdft_vsclparam``
     - 数値
     - K
     - ``50.0``
     - 0.0 以上、必須
     - -
     - 「アンサンブル」が「NVT（カノニカル）」、かつ「温度制御（イオン）」が「速度スケーリング」のとき
   * - 仮想運動エネルギー制御（電子）
     - ``rsdft_tcontrole``
     - 選択
     - -
     - ``none``
     - 必須
     - 制御なし（``none``） / NHC (Nosé-Hoover Chain)（``nosee``） / 速度スケーリング（``vscle``）
     - 「MD法」が「CPMD (Car-Parrinello)」のとき
   * - 目標FKE (Hartree)
     - ``rsdft_noseeparam1``
     - 数値
     - -
     - ``0.004``
     - 0.0 以上、必須
     - -
     - 「MD法」が「CPMD (Car-Parrinello)」、かつ「仮想運動エネルギー制御（電子）」が「NHC (Nosé-Hoover Chain)」のとき
   * - 熱浴振動数 (cm⁻¹)
     - ``rsdft_noseeparam2``
     - 数値
     - -
     - ``1000.0``
     - 0.0 以上、必須
     - -
     - 「MD法」が「CPMD (Car-Parrinello)」、かつ「仮想運動エネルギー制御（電子）」が「NHC (Nosé-Hoover Chain)」のとき
   * - 目標FKE (Hartree)
     - ``rsdft_vscleparam1``
     - 数値
     - -
     - ``0.004``
     - 0.0 以上、必須
     - -
     - 「MD法」が「CPMD (Car-Parrinello)」、かつ「仮想運動エネルギー制御（電子）」が「速度スケーリング」のとき
   * - スケーリング適用閾値
     - ``rsdft_vscleparam2``
     - 数値
     - -
     - ``0.01``
     - 0.0 以上、必須
     - -
     - 「MD法」が「CPMD (Car-Parrinello)」、かつ「仮想運動エネルギー制御（電子）」が「速度スケーリング」のとき

~~~~~~~~~~~~~~
装置パラメータ
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
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
     - -
     - -



######
SPRKKR
######

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

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
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``VWN``
     - 必須
     - VWN (LDA)（``VWN``） / JWN（``JWN``） / VBH（``VBH``） / PBE (GGA)（``PBE``）
     - -

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
   * - サイト占有率
     - ``sprkkr_site_occupancy``
     - kkr\_occupancy
     - -
     - -
     - -
     - -
     - -
   * - 計算モード (MODE)
     - ``sprkkr_mode``
     - 選択
     - -
     - ``FREL``
     - 必須
     - FREL（完全相対論）（``FREL``） / SP-SREL（スカラー相対論・スピン分極）（``SP-SREL``）
     - -
   * - SCF 収束閾値 (TOL × 10⁻⁵)
     - ``sprkkr_tol``
     - 数値
     - -
     - ``1.0``
     - 0 以上、必須
     - -
     - -
   * - k 点数（NKTAB）
     - ``sprkkr_nktab``
     - 整数
     - -
     - ``300``
     - 1 以上、必須
     - -
     - -
   * - ミキシング係数 (MIX)
     - ``sprkkr_mix``
     - 数値
     - -
     - ``0.2``
     - 0.0 以上 1.0 以下、必須
     - -
     - -
   * - エネルギーメッシュ数 (NE)
     - ``sprkkr_ne``
     - 整数
     - -
     - ``32``
     - 1 以上、必須
     - -
     - -
   * - ミキシングアルゴリズム (ALG)
     - ``sprkkr_alg``
     - 選択
     - -
     - ``BROYDEN2``
     - 必須
     - BROYDEN2（``BROYDEN2``） / TCHEBY（``TCHEBY``）
     - -
   * - 最小エネルギー (EMIN) [Ry]
     - ``sprkkr_emin``
     - 数値
     - -
     - ``-0.2``
     - 必須
     - -
     - -
   * - ETA
     - ``sprkkr_eta``
     - 数値
     - -
     - ``1.6``
     - 0 以上、必須
     - -
     - -
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``200``
     - 1 以上 1000 以下
     - -
     - -
   * - RMAX [a.u.]
     - ``sprkkr_rmax``
     - 数値
     - -
     - ``6.0``
     - 0 以上、必須
     - -
     - -
   * - GMAX [a.u.]
     - ``sprkkr_gmax``
     - 数値
     - -
     - ``6.0``
     - 0 以上、必須
     - -
     - -
   * - Broyden 履歴数 (ISTBRY)
     - ``sprkkr_istbry``
     - 整数
     - -
     - ``1``
     - 0 以上、必須
     - -
     - -
   * - Tchebycheff 次数 (ITDEPT)
     - ``sprkkr_itdept``
     - 整数
     - -
     - ``40``
     - 0 以上、必須
     - -
     - -


++++++++++++++++++
交換結合パラメータ
++++++++++++++++++

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
   * - 計算モード (MODE)
     - ``sprkkr_mode``
     - 選択
     - -
     - ``SP-SREL``
     - -
     - SP-SREL (スカラー相対論的)（``SP-SREL``） / FREL (完全相対論的)（``FREL``）
     - -
   * - k点数 (NKTAB)
     - ``sprkkr_nktab``
     - 整数
     - -
     - ``300``
     - -
     - -
     - -
   * - エネルギーメッシュ数 (NE)
     - ``sprkkr_ne``
     - 整数
     - -
     - ``32``
     - -
     - -
     - -
   * - エネルギー最小値 (EMIN)
     - ``sprkkr_emin``
     - 数値
     - -
     - ``-0.2``
     - -
     - -
     - -
   * - クラスター半径 (CLURAD)
     - ``sprkkr_clurad``
     - 整数
     - -
     - ``2``
     - -
     - -
     - -


