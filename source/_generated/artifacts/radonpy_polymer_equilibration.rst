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
   * - ``polymer_cell.lammps``
     - LAMMPSデータファイル（高分子非晶セル）
     - text
     - ○
     - 任意
   * - ``monomer.pickle``
     - QMステップから引き継いだモノマーオブジェクト
     - binary
     - ×
     - 任意
   * - ``eq.log``
     - LAMMPS平衡化MDログ
     - text
     - ○
     - 任意
   * - ``eq_result.json``
     - 平衡化MD結果（密度・エネルギー・Rg等）
     - json
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
   * - ``eq.xtc``
     - 平衡化MDトラジェクトリ（XTC形式）
     - binary
     - ○
     - 任意
