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
   * - サイト占有率
     - ``sprkkr_site_occupancy``
     - kkr\_occupancy
     - -
     - -
     - -
     - -
     - -
     - 基本
   * - 計算モード (MODE)
     - ``sprkkr_mode``
     - 選択
     - -
     - ``FREL``
     - 必須
     - FREL（完全相対論）（``FREL``） / SP-SREL（スカラー相対論・スピン分極）（``SP-SREL``）
     - -
     - 基本
   * - SCF 収束閾値 (TOL × 10⁻⁵)
     - ``sprkkr_tol``
     - 数値
     - -
     - ``1.0``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - k 点数（NKTAB）
     - ``sprkkr_nktab``
     - 整数
     - -
     - ``300``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - ミキシング係数 (MIX)
     - ``sprkkr_mix``
     - 数値
     - -
     - ``0.2``
     - 0.0 以上 1.0 以下、必須
     - -
     - -
     - 詳細
   * - エネルギーメッシュ数 (NE)
     - ``sprkkr_ne``
     - 整数
     - -
     - ``32``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - ミキシングアルゴリズム (ALG)
     - ``sprkkr_alg``
     - 選択
     - -
     - ``BROYDEN2``
     - 必須
     - BROYDEN2（``BROYDEN2``） / TCHEBY（``TCHEBY``）
     - -
     - 詳細
   * - 最小エネルギー (EMIN) [Ry]
     - ``sprkkr_emin``
     - 数値
     - -
     - ``-0.2``
     - 必須
     - -
     - -
     - 基本
   * - ETA
     - ``sprkkr_eta``
     - 数値
     - -
     - ``1.6``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - SCF 最大反復回数
     - ``scf_max_iter``
     - 整数
     - -
     - ``200``
     - 1 以上 1000 以下
     - -
     - -
     - 基本
   * - RMAX [a.u.]
     - ``sprkkr_rmax``
     - 数値
     - -
     - ``6.0``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - GMAX [a.u.]
     - ``sprkkr_gmax``
     - 数値
     - -
     - ``6.0``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - Broyden 履歴数 (ISTBRY)
     - ``sprkkr_istbry``
     - 整数
     - -
     - ``1``
     - 0 以上、必須
     - -
     - -
     - 詳細
   * - Tchebycheff 次数 (ITDEPT)
     - ``sprkkr_itdept``
     - 整数
     - -
     - ``40``
     - 0 以上、必須
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
   * - 交換相関汎関数
     - ``exchange_correlation``
     - 選択
     - -
     - ``VWN``
     - 必須
     - VWN (LDA)（``VWN``） / JWN（``JWN``） / VBH（``VBH``） / PBE (GGA)（``PBE``）
     - -
     - 基本
