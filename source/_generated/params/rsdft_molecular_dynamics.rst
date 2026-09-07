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

