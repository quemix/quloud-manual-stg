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
   * - ``^.*\.[uU][pP][fF]$``
     - -
     - upf
     - ○
     - 必須
   * - ``QuloudJob.scf.in``
     - -
     - text
     - ○
     - 必須
   * - ``QuloudJob.scf.err``
     - -
     - text
     - ○
     - 任意
   * - ``QuloudJob.scf.out``
     - -
     - text
     - ○
     - 必須
   * - ``work``
     - -
     - dir
     - ○
     - 必須
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
