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
   * - NSCF k グリッド（a 軸）
     - ``qe_dos_kgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - NSCF k グリッド（b 軸）
     - ``qe_dos_kgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - NSCF k グリッド（c 軸）
     - ``qe_dos_kgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
     - 基本
   * - NSCF k グリッドオフセット（a 軸）
     - ``qe_dos_kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 基本
   * - NSCF k グリッドオフセット（b 軸）
     - ``qe_dos_kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 基本
   * - NSCF k グリッドオフセット（c 軸）
     - ``qe_dos_kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
     - 基本
