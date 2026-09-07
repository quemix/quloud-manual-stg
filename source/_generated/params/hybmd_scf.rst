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
   * - OFDFTタスク
     - ``hybmd_job_task``
     - 選択
     - -
     - ``Optdensity``
     - 必須
     - 密度最適化（``Optdensity``） / 計算のみ（``Calculation``）
     - -
     - 基本
   * - 密度最適化最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``1000``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - 密度最適化収束閾値
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
     - ``1e-08``
     - 0.0 以上、必須
     - -
     - -
     - 基本
   * - 運動エネルギー密度汎関数
     - ``hybmd_kedf``
     - 選択
     - -
     - ``GGA``
     - 必須
     - TF（``TF``） / vW（``vW``） / GGA（``GGA``） / WT（``WT``） / MGP（``MGP``）
     - -
     - 基本
   * - KEDFカーネル
     - ``hybmd_kedf_kernel``
     - 選択
     - -
     - ``LKT``
     - -
     - LKT（``LKT``）
     - 「運動エネルギー密度汎関数」が「GGA」のとき
     - 基本
   * - 初期電子密度
     - ``hybmd_density_initialization``
     - 選択
     - -
     - ``atomic``
     - 必須
     - 原子密度重ね合わせ（``atomic``） / 一様電子ガス（``heg``） / 密度ファイルから読み込み（``read``）
     - -
     - 基本
   * - 初期密度ファイル
     - ``hybmd_density_file``
     - ファイル
     - -
     - -
     - -
     - -
     - 「初期電子密度」が「密度ファイルから読み込み」のとき
     - 基本
   * - 密度最適化手法
     - ``hybmd_opt_method``
     - 選択
     - -
     - ``CG-HS``
     - 必須
     - CG-HS（``CG-HS``） / CG-DY（``CG-DY``） / CG-FR（``CG-FR``） / LBFGS（``LBFGS``）
     - -
     - 詳細
   * - ラインサーチ最大回数
     - ``hybmd_opt_maxls``
     - 整数
     - -
     - ``200``
     - 1 以上
     - -
     - -
     - 詳細
   * - 関数評価最大回数
     - ``hybmd_opt_maxfun``
     - 整数
     - -
     - ``50``
     - 1 以上
     - -
     - -
     - 詳細
   * - ラインサーチ係数 c1
     - ``hybmd_opt_c1``
     - 数値（指数表記）
     - -
     - ``0.0001``
     - 0.0 以上
     - -
     - -
     - 詳細
   * - ラインサーチ係数 c2
     - ``hybmd_opt_c2``
     - 数値
     - -
     - ``0.8``
     - 0.0 以上
     - -
     - -
     - 詳細
   * - 初期ステップ幅
     - ``hybmd_opt_h0``
     - 数値
     - -
     - ``0.025``
     - 0.0 以上
     - -
     - -
     - 詳細
   * - PME線形補間
     - ``hybmd_math_linearie``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - マルチステップ数
     - ``hybmd_math_multistep``
     - 整数
     - -
     - ``1``
     - 1 以上
     - -
     - -
     - 詳細
   * - 密度再利用（MATH.reuse）
     - ``hybmd_math_reuse``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - 初期磁気モーメント
     - ``hybmd_density_magmom``
     - 数値
     - -
     - ``0.0``
     - -
     - -
     - 「スピン」が「コリニア磁性」のとき
     - 詳細
   * - 密度出力ファイル名
     - ``hybmd_density_output``
     - 文字列
     - -
     - ``den.cube``
     - -
     - -
     - -
     - 詳細
   * - 参照密度出力ファイル名（Henkelman用）
     - ``hybmd_density_ref_output``
     - 文字列
     - -
     - ``refden.cube``
     - -
     - -
     - 「Henkelman Bader用密度出力」が「有効」のとき
     - 詳細
   * - Henkelman参照密度出力（計算用）
     - ``hybmd_density_ref_output_calc``
     - 文字列
     - -
     - ``refden_calc.cube``
     - -
     - -
     - 「Henkelman Bader用密度出力」が「有効」のとき
     - 詳細
   * - Bader解析を出力
     - ``hybmd_output_write_bader``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - Bader voxel offset
     - ``hybmd_output_voxeloff``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - 価電子Bader電荷
     - ``hybmd_bader_charge_val``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - コア密度Bader電荷
     - ``hybmd_bader_charge_core``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - 参照密度Bader電荷
     - ``hybmd_bader_charge_ref``
     - 有効・無効
     - -
     - 有効
     - -
     - -
     - -
     - 詳細
   * - Henkelman Bader用密度出力
     - ``hybmd_henkelman_density``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 詳細
   * - 擬ポテンシャルファイル（元素 = ファイル名）
     - ``hybmd_pp_files``
     - textarea
     - -
     - -
     - 必須
     - -
     - -
     - 詳細
   * - Core Width（元素 = 値）
     - ``hybmd_core_widths``
     - textarea
     - -
     - -
     - -
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
   * - スピン
     - ``spin``
     - 選択
     - -
     - ``wospin``
     - 必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``）
     - -
     - 基本
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA-PBE``
     - 必須
     - LDA（``LDA``） / GGA-PBE（``GGA-PBE``） / GGA-PBEsol（``GGA-PBEsol``）
     - -
     - 基本
   * - 荷電状態
     - ``charge_state``
     - 整数
     - e
     - ``0``
     - -
     - -
     - -
     - 基本
   * - OFDFTグリッドカットオフエネルギー
     - ``ecut_wfc``
     - 数値
     - eV
     - ``800.0``
     - 0.0 以上、必須
     - -
     - -
     - 詳細
