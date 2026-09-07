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
   * - OTF モード
     - ``flare_otf_mode``
     - 選択
     - -
     - ``fresh``
     - 必須
     - 新規（Fresh）（``fresh``） / 再開（Restart）（``restart``）
     - -
     - 基本
   * - ガウス過程タイプ
     - ``flare_gp``
     - 選択
     - -
     - ``SGP_Wrapper``
     - 必須
     - Sparse GP（SGP_Wrapper）（``SGP_Wrapper``） / Full GP（GaussianProcess）（``GaussianProcess``）
     - -
     - 詳細
   * - MD エンジン
     - ``flare_otf_md_engine``
     - 選択
     - -
     - ``Langevin``
     - 必須
     - Langevin（``Langevin``） / NPT（``NPT``）
     - -
     - 基本
   * - カーネル
     - ``flare_kernel_name``
     - 選択
     - -
     - ``NormalizedDotProduct``
     - 必須
     - NormalizedDotProduct（``NormalizedDotProduct``） / SquaredExponential（``SquaredExponential``）
     - -
     - 詳細
   * - カーネル sigma
     - ``flare_kernel_sigma``
     - 数値
     - -
     - ``2.0``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - カーネル power
     - ``flare_kernel_power``
     - 整数
     - -
     - ``2``
     - 1 以上、必須
     - -
     - -
     - 詳細
   * - 温度
     - ``flare_otf_temperature_K``
     - 数値
     - K
     - ``800.0``
     - 0.0 以上、必須
     - -
     - -
     - 基本
   * - ディスクリプタ
     - ``flare_descriptor_name``
     - 選択
     - -
     - ``B2``
     - 必須
     - B2（ACE）（``B2``）
     - -
     - 詳細
   * - 径方向基底数 (nmax)
     - ``flare_descriptor_nmax``
     - 整数
     - -
     - ``5``
     - 1 以上、必須
     - -
     - -
     - 詳細
   * - 角運動量最大値 (lmax)
     - ``flare_descriptor_lmax``
     - 整数
     - -
     - ``3``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - カットオフ関数
     - ``flare_descriptor_cutoff_function``
     - 選択
     - -
     - ``quadratic``
     - 必須
     - quadratic（``quadratic``） / cos（``cos``）
     - -
     - 詳細
   * - 径方向基底関数
     - ``flare_descriptor_radial_basis``
     - 選択
     - -
     - ``chebyshev``
     - 必須
     - Chebyshev（``chebyshev``）
     - -
     - 詳細
   * - Langevin 摩擦係数
     - ``flare_otf_friction``
     - 数値
     - -
     - ``0.10180527006906766``
     - 0.0 以上、必須
     - -
     - 「MD エンジン」が「Langevin」のとき
     - 基本
   * - NPT 温度緩和時間
     - ``flare_otf_ttime``
     - 数値
     - fs
     - ``2.0``
     - 0.0 以上、必須
     - -
     - 「MD エンジン」が「NPT」のとき
     - 基本
   * - エネルギーノイズ
     - ``flare_energy_noise``
     - 数値（指数表記）
     - -
     - ``0.01``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - NPT 圧力緩和係数
     - ``flare_otf_pfactor``
     - 数値
     - -
     - ``100.0``
     - 0.0 以上
     - -
     - 「MD エンジン」が「NPT」のとき
     - 基本
   * - 力ノイズ
     - ``flare_forces_noise``
     - 数値（指数表記）
     - -
     - ``0.05``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - 外部圧力
     - ``flare_otf_externalstress``
     - 数値
     - bar
     - ``0.0``
     - -
     - -
     - 「MD エンジン」が「NPT」のとき
     - 基本
   * - ストレスノイズ
     - ``flare_stress_noise``
     - 数値（指数表記）
     - -
     - ``0.005``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - タイムステップ
     - ``flare_otf_dt``
     - 数値
     - ps
     - ``0.001``
     - 0.0001 以上、必須
     - -
     - -
     - 基本
   * - カットオフ半径
     - ``flare_cutoff``
     - 数値
     - Å
     - ``5.0``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - ステップ数
     - ``flare_otf_number_of_steps``
     - 整数
     - -
     - ``2000``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - 分散タイプ
     - ``flare_variance_type``
     - 選択
     - -
     - ``local``
     - 必須
     - local（``local``） / DTC（``DTC``） / SOR（``SOR``）
     - -
     - 詳細
   * - 超パラメータ最適化回数
     - ``flare_max_iterations``
     - 整数
     - -
     - ``20``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - LAMMPSマッピング使用
     - ``flare_use_mapping``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - 初期速度（温度 K）
     - ``flare_otf_initial_velocity``
     - 数値
     - K
     - ``800.0``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - 不確かさ閾値
     - ``flare_otf_std_tolerance_factor``
     - 数値
     - -
     - ``-0.04``
     - 必須
     - -
     - -
     - 詳細
   * - DFT呼び出し時の最大追加原子数（-1: 無制限）
     - ``flare_otf_max_atoms_added``
     - 整数
     - -
     - ``-1``
     - 必須
     - -
     - -
     - 詳細
   * - 超パラメータ最適化開始 DFT 回数
     - ``flare_otf_train_hyps_start``
     - 整数
     - -
     - ``10``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - 超パラメータ最適化終了 DFT 回数（inf: 無限）
     - ``flare_otf_train_hyps_end``
     - 文字列
     - -
     - ``inf``
     - -
     - -
     - -
     - 詳細
   * - GPモデル書き出し詳細度
     - ``flare_otf_write_model``
     - 選択
     - -
     - ``4``
     - 必須
     - 0（書き出しなし）（``0``） / 1（終了時）（``1``） / 2（超パラメータ最適化後）（``2``） / 3（DFT呼び出し後）（``3``） / 4（チェックポイント付き）（``4``）
     - -
     - 詳細
   * - 原子追加スタイル
     - ``flare_otf_update_style``
     - 選択
     - -
     - ``threshold``
     - 必須
     - threshold（閾値以上を追加）（``threshold``） / add_n（最大N個追加）（``add_n``）
     - -
     - 詳細
   * - 原子追加閾値
     - ``flare_otf_update_threshold``
     - 数値
     - -
     - ``0.02``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
   * - 力のみで学習
     - ``flare_otf_force_only``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
