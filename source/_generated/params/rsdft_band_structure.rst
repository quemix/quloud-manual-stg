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

