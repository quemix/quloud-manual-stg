.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 28 34 12 12 8

   * - ファイル
     - 内容
     - 形式
     - ダウンロード
     - 出力
   * - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
     - ○
     - 任意
   * - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
     - ○
     - 任意
   * - ``rsdft.json_min``
     - 最小エネルギー点での計算結果（rsdft.json と同形式）
     - json
     - ○
     - 任意
   * - ``linmin_ef.dat``
     - 直線探索・フェルミエネルギー探索の内部状態（バイナリ）
     - binary
     - ○
     - 任意
   * - ``optconv.csv``
     - 原子位置最適化の収束履歴（イテレーションごとの最大力）
     - csv
     - ○
     - 任意
   * - ``optlat.restart``
     - 格子探索の状態（探索点ごとのスケールとエネルギー）
     - text
     - ○
     - 任意
   * - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
     - ○
     - 任意
   * - ``ve.dat``
     - 体積-エネルギー曲線（1行 = 体積 / 全エネルギー / a1 / a2 / a3 / Ecut / Ngrid×3 / 原子数）
     - text
     - ○
     - 任意
   * - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
     - ○
     - 任意
   * - ``wopt.dat``
     - 原子位置最適化の内部状態（バイナリ、リスタート用）
     - binary
     - ○
     - 任意
   * - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
     - ○
     - 必須
   * - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
     - ○
     - 任意
   * - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text
     - ○
     - 任意
   * - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
     - ○
     - 必須
   * - ``fort.980``
     - サイト別初期スピン配置（NDSPIN が負値のとき RSDFT が読む）
     - text
     - ○
     - 任意
   * - ``site_property_settings.b64``
     - -
     - base64
     - ○
     - 必須
   * - ``rsdft.atom``
     - -
     - cif
     - ○
     - 必須
   * - ``parameters.json``
     - -
     - json
     - ○
     - 必須
   * - ``rsdft.atom_ini``
     - 格子探索開始時の初期構造（最適化後との比較用）
     - cif
     - ○
     - 任意
   * - ``sysinfo.json``
     - -
     - json
     - ○
     - 必須
   * - ``rsdft.atom.out.cif``
     - -
     - cif
     - ○
     - 必須
   * - ``QuloudJob.exit_status.json``
     - -
     - json
     - ○
     - 任意
   * - ``rsdft.atom_min``
     - 最小エネルギーを与えた構造
     - cif
     - ○
     - 任意
   * - ``sysinfo.json.out.cif``
     - -
     - json
     - ○
     - 必須
