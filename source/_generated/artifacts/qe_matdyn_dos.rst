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
   * - ``matdyn.modes``
     - フォノン固有ベクトル（flvec）
     - text
     - ○
     - 任意
   * - ``^(QuloudJob\.freq|matdyn\.freq)$``
     - フォノン振動数（flfrq）
     - text
     - ○
     - 任意
   * - ``^(QuloudJob\.freq\.gp|matdyn\.freq\.gp)$``
     - フォノン振動数（gnuplot 形式）
     - text
     - ○
     - 任意
   * - ``^(QuloudJob\.matdyn\.in|matdyn_dos\.in)$``
     - matdyn.x 入力（フォノンDOS。旧名 matdyn\_dos.in にも対応）
     - text
     - ○
     - 必須
   * - ``matdyn_dos.out``
     - matdyn.x 標準出力（フォノンDOS）
     - text
     - ○
     - 必須
   * - ``^(QuloudJob\.dos|matdyn\.dos)$``
     - フォノン状態密度（fldos）
     - text
     - ○
     - 必須
