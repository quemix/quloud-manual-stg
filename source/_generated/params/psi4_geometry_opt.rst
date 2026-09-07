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
   * - 収束閾値 (G\_CONVERGENCE)
     - ``psi4_g_convergence``
     - 選択
     - -
     - ``QCHEM``
     - 必須
     - QCHEM（デフォルト）（``QCHEM``） / GAU（``GAU``） / GAU\_LOOSE（緩い）（``GAU_LOOSE``） / GAU\_TIGHT（厳しい）（``GAU_TIGHT``） / GAU\_VERYTIGHT（非常に厳しい）（``GAU_VERYTIGHT``） / TURBOMOLE（``TURBOMOLE``） / CFOUR（``CFOUR``） / MOLPRO（``MOLPRO``） / NWCHEM\_LOOSE（緩い）（``NWCHEM_LOOSE``） / INTERFRAG\_TIGHT（分子間、厳しい）（``INTERFRAG_TIGHT``）
     - -
     - 詳細
   * - 最大反復回数 (GEOM\_MAXITER)
     - ``psi4_geom_maxiter``
     - 整数
     - -
     - ``50``
     - 1 以上 1000 以下、必須
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
   * - スピン多重度
     - ``spin``
     - 整数
     - -
     - ``1``
     - 1 以上、必須
     - 非磁性（``wospin``） / コリニア磁性（``collinear``） / ノンコリニア磁性（``noncollinear``）
     - -
     - 基本
   * - Reference
     - ``reference``
     - 選択
     - -
     - ``RHF``
     - 必須
     - RHF（制限付き、閉殻専用）（``RHF``） / UHF（非制限）（``UHF``） / ROHF（制限付き開殻）（``ROHF``）
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
   * - 計算手法
     - ``exchange_correlation``
     - 選択
     - -
     - ``b3lyp``
     - 必須
     - HF（``hf``） / B3LYP（``b3lyp``） / PBE（``pbe``） / M06-2X（``m06-2x``） / ωB97X-D3BJ（``wb97x-d3bj``） / CAM-B3LYP（``cam-b3lyp``） / MP2（``mp2``）
     - -
     - 基本
   * - 基底関数系
     - ``basis_set``
     - 選択
     - -
     - ``6-31G(d,p)``
     - 必須
     - STO-3G（最小基底、高速・低精度）（``STO-3G``） / 3-21G（``3-21G``） / 6-31G(d,p)（標準）（``6-31G(d,p)``） / 6-311G(d,p)（``6-311G(d,p)``） / cc-pVDZ（``cc-pVDZ``） / cc-pVTZ（高精度）（``cc-pVTZ``） / aug-cc-pVDZ（拡散関数付き）（``aug-cc-pVDZ``）
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
   * - 分散補正種別
     - ``psi4_dispersion_type``
     - 選択
     - -
     - ``d3bj``
     - -
     - D3(BJ)（推奨）（``d3bj``） / D3(zero)（``d3zero``） / D2（``d2``） / NL（非局所）（``nl``）
     - 「ファンデルワールス補正」が「有効」のとき
     - 基本
