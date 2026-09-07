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
   * - 計算モード (MODE)
     - ``sprkkr_mode``
     - 選択
     - -
     - ``SP-SREL``
     - -
     - SP-SREL (スカラー相対論的)（``SP-SREL``） / FREL (完全相対論的)（``FREL``）
     - -
     - 基本
   * - k点数 (NKTAB)
     - ``sprkkr_nktab``
     - 整数
     - -
     - ``300``
     - -
     - -
     - -
     - 基本
   * - エネルギーメッシュ数 (NE)
     - ``sprkkr_ne``
     - 整数
     - -
     - ``32``
     - -
     - -
     - -
     - 基本
   * - エネルギー最小値 (EMIN)
     - ``sprkkr_emin``
     - 数値
     - -
     - ``-0.2``
     - -
     - -
     - -
     - 基本
   * - クラスター半径 (CLURAD)
     - ``sprkkr_clurad``
     - 整数
     - -
     - ``2``
     - -
     - -
     - -
     - 基本
