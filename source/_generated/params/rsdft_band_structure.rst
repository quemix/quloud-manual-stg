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
   * - バンド計算経路
     - ``band_kpath``
     - kpath
     - -
     - ``{"method": "k-auto", "points": [{"label": "Γ", "x": 0.0, "y": 0.0, "z": 0.0, "division": 20}, {"label": "Γ", "x": 1.0, "y": 0.0, "z": 0.0, "division": 20}]}``
     - -
     - -
     - -
     - 基本
   * - 初期スピン差 (NDSPIN)
     - ``rsdft_dspin``
     - 数値
     - -
     - ``0``
     - 0 以上 10 以下、必須
     - -
     - 「スピン」が「スピン偏極（非縮退）」のとき
     - 基本
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``300``
     - 1 以上 1000 以下
     - -
     - -
     - 詳細
   * - SCF 収束閾値（ポテンシャル）
     - ``scf_convergence_pot``
     - 数値（指数表記）
     - Hartree^2
     - ``1e-15``
     - 0.0 以上
     - -
     - -
     - 詳細
   * - 収束判定基準
     - ``rsdft_conv``
     - 選択
     - -
     - ``pot``
     - 必須
     - ポテンシャル差 (SCFCONV)（``pot``） / 全エネルギー差 (ETOTCONV)（``etot``）
     - -
     - 詳細
   * - 軌道占有数出力制御 (OC)
     - ``rsdft_ioctrl``
     - 整数
     - -
     - ``2``
     - -1 以上、必須
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
     - 非磁性（縮退）（``wospin``） / スピン偏極（非縮退）（``withspin``）
     - -
     - 基本
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``GGA_PBE96``
     - 必須
     - LDA (PZ81)（``LDA_PZ81``） / GGA-PBE (PBE96)（``GGA_PBE96``） / Hybrid (HSE06)（``HYB_HSE06``）
     - -
     - 基本
   * - SCF k グリッド（a 軸）
     - ``kgrid_a``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - SCF k グリッド（b 軸）
     - ``kgrid_b``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - SCF k グリッド（c 軸）
     - ``kgrid_c``
     - 整数
     - -
     - ``8``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - r グリッド（a 軸）
     - ``rgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
     - 基本
   * - r グリッド（b 軸）
     - ``rgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
     - -
     - 基本
   * - r グリッド（c 軸）
     - ``rgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、刻み 4、必須
     - -
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
   * - 対称性利用
     - ``symmetry_use``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 基本
   * - ファンデルワールス補正
     - ``vdw``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 基本
   * - 電子占有数スメアリング
     - ``smearing_method``
     - 選択
     - -
     - ``mp``
     - -
     - Methfessel-Paxton（``mp``） / フェルミ-ディラック（``fd``）
     - -
     - 詳細
   * - 電子温度 (EKBT)
     - ``smearing_width``
     - 数値
     - eV
     - ``0.03``
     - 0.0 以上 1000.0 以下、必須
     - -
     - -
     - 詳細
   * - Methfessel-Paxton次数 (KINTEG)
     - ``smearing_order``
     - 整数
     - -
     - ``0``
     - 5 以下
     - -
     - 「電子占有数スメアリング」が「Methfessel-Paxton」のとき
     - 詳細
   * - 擬ポテンシャルセット
     - ``pseudopotential_set``
     - 選択
     - -
     - ``FHI``
     - 必須
     - FHI (Fritz-Haber Institute)（``FHI``） / ONCVPSP (Optimized Norm-Conserving)（``ONCVPSP``）
     - -
     - 基本
