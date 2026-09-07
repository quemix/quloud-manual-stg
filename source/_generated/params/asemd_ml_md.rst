.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 6042191ba82c4be3056bf116bdfb49f2ea1ff9ab (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T21:34:15Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate

~~~~~~~~~~
物理モデル
~~~~~~~~~~

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
   * - Pretrained-model プロバイダー
     - ``pretrained_model_provider``
     - 選択
     - -
     - ``7net``
     - 必須
     - SevenNet（``7net``） / fairchem（``fairchem``）
     - -
   * - モデル名
     - ``pretrained_model_name_7net``
     - 選択
     - -
     - ``7net-mf-ompa``
     - 必須
     - 7net-mf-ompa（``7net-mf-ompa``）
     - 「Pretrained-model プロバイダー」が「SevenNet」のとき
   * - モデル名
     - ``pretrained_model_name_fairchem``
     - 選択
     - -
     - ``uma-s-1p1``
     - 必須
     - uma-s-1p1（``uma-s-1p1``）
     - 「Pretrained-model プロバイダー」が「fairchem」のとき

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
   * - タイムステップ
     - ``timestep``
     - 数値
     - fs
     - ``1.0``
     - 0.001 以上 100.0 以下、必須
     - -
     - -
   * - ステップ数
     - ``num_steps``
     - 整数
     - -
     - ``10000``
     - 1 以上、必須
     - -
     - -
   * - 温度
     - ``temperature``
     - 数値
     - K
     - ``300.0``
     - 0.0 以上、必須
     - -
     - -
   * - アンサンブル
     - ``ensemble``
     - 選択
     - -
     - ``NVT``
     - 必須
     - NVE（ミクロカノニカル）（``NVE``） / NVT（カノニカル）（``NVT``） / NPT（等温等圧）（``NPT``）
     - -
   * - 圧力（NPT のみ）
     - ``pressure``
     - 数値
     - GPa
     - ``0.0``
     - -
     - -
     - 「アンサンブル」が「NPT（等温等圧）」のとき

