.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 789272e8ff4737a6a8aaf0d461f6b71abb84fb54 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T07:21:28Z
.. マスタ同期日時: 2026-09-07T06:19:19Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 28 34 12 12 8

   * - ファイル
     - 内容
     - 形式
     - ダウンロード
     - 出力
   * - ``QuloudJob.lmp``
     - 初期構造（LAMMPS data 形式）
     - text
     - ○
     - 必須
   * - ``in.QuloudJob``
     - LAMMPS入力スクリプト（Quloudが生成）
     - text
     - ○
     - 必須
   * - ``log.lammps``
     - LAMMPS標準ログ（thermo 出力の時系列を含む）
     - text
     - ○
     - 必須
   * - ``QuloudJob.out.lmp``
     - 最終構造（write\_data 出力。rsdft.atom.out.cif への変換元）
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
   * - ``QuloudJob.lammpstrj``
     - 原子構造トラジェクトリ（dump 出力）
     - text
     - ○
     - 任意
