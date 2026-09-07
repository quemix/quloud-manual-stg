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
   * - ``QuloudJob.int``
     - 経路エネルギーの内挿曲線
     - text
     - ○
     - 任意
   * - ``^pw_[0-9]+\.in$``
     - neb.x が生成するイメージ別 pw.x 入力
     - text
     - ○
     - 任意
   * - ``neb.dat``
     - neb.x が入力から切り出す &PATH ネームリスト（入力ではなく生成物）
     - text
     - ○
     - 任意
   * - ``QuloudJob.path``
     - 経路最適化の再開情報
     - text
     - ○
     - 任意
   * - ``^(QuloudJob\.neb\.in|neb\.in)$``
     - neb.x 入力（旧名 neb.in にも対応）
     - text
     - ○
     - 必須
   * - ``^.*\.[uU][pP][fF]$``
     - -
     - upf
     - ○
     - 必須
   * - ``QuloudJob.scf.in``
     - NEB では neb.x に直接渡さないが、擬ポテンシャル選択の記録として生成される
     - text
     - ○
     - 任意
   * - ``neb.err``
     - neb.x 標準エラー出力
     - text
     - ○
     - 任意
   * - ``QuloudJob.dat``
     - 経路のエネルギープロファイル（反応座標／エネルギー[eV]／誤差[eV/A]）
     - text
     - ○
     - 任意
   * - ``neb.out``
     - neb.x 標準出力（活性化エネルギー・イメージ別エネルギー・収束状況）
     - text
     - ○
     - 必須
   * - ``work``
     - -
     - dir
     - ○
     - 任意
   * - ``QuloudJob.axsf``
     - 全イメージのアニメーション構造（XCrySDen AXSF）
     - axsf
     - ○
     - 任意
   * - ``QuloudJob.crd``
     - 全イメージの原子座標（ATOMIC\_POSITIONS 形式）
     - text
     - ○
     - 任意
   * - ``QuloudJob.xyz``
     - 全イメージの構造（XYZ）
     - xyz
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
   * - ``rsdft.atom.2``
     - 終期構造（LAST\_IMAGE の元になる構造）
     - cif
     - ○
     - 任意
   * - ``parameters.json``
     - -
     - json
     - ○
     - 必須
   * - ``structure_refs.json``
     - 初期／終期構造の参照（capability駆動フォームが書き出す）
     - json
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
   * - ``sysinfo.json.out.cif``
     - -
     - json
     - ○
     - 必須
