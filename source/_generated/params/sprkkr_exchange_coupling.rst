.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate

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
   * - 計算モード (MODE)
     - ``sprkkr_mode``
     - 選択
     - -
     - ``SP-SREL``
     - -
     - SP-SREL (スカラー相対論的)（``SP-SREL``） / FREL (完全相対論的)（``FREL``）
     - -
   * - k点数 (NKTAB)
     - ``sprkkr_nktab``
     - 整数
     - -
     - ``300``
     - -
     - -
     - -
   * - エネルギーメッシュ数 (NE)
     - ``sprkkr_ne``
     - 整数
     - -
     - ``32``
     - -
     - -
     - -
   * - エネルギー最小値 (EMIN)
     - ``sprkkr_emin``
     - 数値
     - -
     - ``-0.2``
     - -
     - -
     - -
   * - クラスター半径 (CLURAD)
     - ``sprkkr_clurad``
     - 整数
     - -
     - ``2``
     - -
     - -
     - -

