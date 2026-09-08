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

