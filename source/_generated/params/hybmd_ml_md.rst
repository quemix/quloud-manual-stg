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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``0.5``
     - 0.001 以上 100.0 以下、必須
     - -
     - -
     - 基本
   * - ステップ数
     - ``num_steps``
     - 整数
     - -
     - ``100``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - 温度
     - ``temperature``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上、必須
     - -
     - -
     - 基本
   * - MD積分器
     - ``hybmd_dynamics_func``
     - 選択
     - -
     - ``Langevin``
     - 必須
     - Langevin（``Langevin``） / Nose-Hoover Chain（``NHC``）
     - -
     - 基本
   * - 外部電場 X
     - ``hybmd_efield_x``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
     - 基本
   * - 外部電場 Y
     - ``hybmd_efield_y``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
     - 基本
   * - 外部電場 Z
     - ``hybmd_efield_z``
     - 数値
     - V/Å
     - ``0.0``
     - 必須
     - -
     - -
     - 基本
   * - OFDFT/Bader更新間隔
     - ``hybmd_of_interval``
     - 整数
     - -
     - ``10``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - 機械学習ポテンシャル
     - ``hybmd_mlip_potential``
     - 選択
     - -
     - ``chgnet``
     - 必須
     - CHGNet（``chgnet``） / Orb-v3（``orbv3``）
     - -
     - 基本
   * - MLIP計算デバイス
     - ``hybmd_mlip_device``
     - 選択
     - -
     - ``cpu``
     - 必須
     - CPU（``cpu``） / CUDA GPU（``cuda``）
     - -
     - 基本
   * - 初期化モード
     - ``hybmd_init_mode``
     - 選択
     - -
     - ``scratch``
     - 必須
     - 新規開始（``scratch``） / 継続計算（``continue``）
     - -
     - 詳細
   * - 初期構造ファイル
     - ``hybmd_structure_file``
     - ファイル
     - -
     - ``rsdft.atom``
     - -
     - -
     - 「初期化モード」が「新規開始」のとき
     - 詳細
   * - 初期構造フォーマット
     - ``hybmd_structure_format``
     - 選択
     - -
     - ``cif``
     - -
     - CIF（``cif``） / Extended XYZ（``extxyz``） / VASP（``vasp``）
     - 「初期化モード」が「新規開始」のとき
     - 詳細
   * - 再開用trajectory
     - ``hybmd_restart_file``
     - ファイル
     - -
     - -
     - -
     - -
     - 「初期化モード」が「継続計算」のとき
     - 詳細
   * - OFDFT入力ファイル
     - ``hybmd_dftinput_file``
     - ファイル
     - -
     - ``scf.ini``
     - 必須
     - -
     - -
     - 詳細
   * - Langevin摩擦係数
     - ``hybmd_friction``
     - 数値
     - -
     - ``0.1``
     - 0.0 以上
     - -
     - 「MD積分器」が「Langevin」のとき
     - 詳細
   * - NHC緩和時間
     - ``hybmd_tdamp``
     - 数値
     - fs
     - ``50.0``
     - 0.0 以上
     - -
     - 「MD積分器」が「Nose-Hoover Chain」のとき
     - 詳細
   * - trajectory出力間隔
     - ``hybmd_traj_interval``
     - 整数
     - -
     - ``1``
     - 1 以上
     - -
     - -
     - 詳細
   * - 電場力用Bader解析
     - ``hybmd_bader_force``
     - 選択
     - -
     - ``pybader``
     - 必須
     - pybader（``pybader``） / Henkelman bader（``henkelman``）
     - -
     - 詳細
   * - Henkelman Baderを併用
     - ``hybmd_bader_henkelman``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 詳細
   * - 乱数シード
     - ``hybmd_seed``
     - 整数
     - -
     - ``111``
     - 0 以上
     - -
     - -
     - 詳細
   * - trajectory出力ファイル名
     - ``hybmd_traj_file``
     - 文字列
     - -
     - ``md.traj``
     - 必須
     - -
     - -
     - 詳細
   * - MDログファイル名
     - ``hybmd_log_file``
     - 文字列
     - -
     - ``md.log``
     - 必須
     - -
     - -
     - 詳細
   * - Bader電荷ログファイル名
     - ``hybmd_bader_log_file``
     - 文字列
     - -
     - ``bader.log``
     - 必須
     - -
     - -
     - 詳細
   * - 停止ファイル名
     - ``hybmd_stopfile_name``
     - 文字列
     - -
     - ``hybmd_stopfile``
     - -
     - -
     - -
     - 詳細
