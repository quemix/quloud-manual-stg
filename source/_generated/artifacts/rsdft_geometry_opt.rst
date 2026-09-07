.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 6042191ba82c4be3056bf116bdfb49f2ea1ff9ab (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T21:34:15Z
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
   * - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
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
   * - ``sysinfo.json.out.cif``
     - -
     - json
     - ○
     - 必須
