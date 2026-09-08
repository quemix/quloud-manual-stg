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

