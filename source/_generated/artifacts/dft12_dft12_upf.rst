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
   * - ``*.deltaV.dat``
     - PP\_LOCAL 補正量 ΔV(r)
     - text
     - ○
     - 任意
   * - ``*.summary.csv``
     - パッチ処理サマリ（パラメータ・来歴ハッシュ）
     - csv
     - ○
     - 必須
   * - ``*.theta.dat``
     - カットオフ関数 θ(r)
     - text
     - ○
     - 任意
   * - ``*.vks_neutral.dat``
     - 中性配置の全電子 KS ポテンシャル
     - text
     - ○
     - 任意
   * - ``*.vks_stripped.dat``
     - 剥ぎ取り配置の全電子 KS ポテンシャル
     - text
     - ○
     - 任意
   * - ``*.vloc.dat``
     - パッチ前後の局所ポテンシャル
     - text
     - ○
     - 任意
   * - ``*.vse.dat``
     - 自己エネルギーポテンシャル V\_S(r)
     - text
     - ○
     - 任意
   * - ``^(?!.*\.dft12\.).*\.[uU][pP][fF]$``
     - ベース UPF 擬ポテンシャル
     - upf
     - ○
     - 任意
   * - ``dft12.json``
     - DFT-1/2 パッチャー設定
     - json
     - ○
     - 必須
   * - ``QuloudJob.dft12.err``
     - パッチャー実行エラーログ
     - text
     - ○
     - 任意
   * - ``QuloudJob.dft12.out``
     - パッチャー実行ログ（結果 JSON）
     - text
     - ○
     - 必須
   * - ``QuloudJob.exit_status.json``
     - -
     - json
     - ○
     - 任意
   * - ``^.*\.dft12\.[uU][pP][fF]$``
     - DFT-1/2 パッチ済み UPF 擬ポテンシャル
     - upf
     - ○
     - 必須
