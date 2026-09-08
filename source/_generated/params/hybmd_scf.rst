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

