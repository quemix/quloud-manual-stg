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
   * - NSCF k グリッド（a 軸）
     - ``qe_dos_kgrid_a``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
   * - NSCF k グリッド（b 軸）
     - ``qe_dos_kgrid_b``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
   * - NSCF k グリッド（c 軸）
     - ``qe_dos_kgrid_c``
     - 整数
     - -
     - ``16``
     - 1 以上、必須
     - -
     - -
   * - NSCF k グリッドオフセット（a 軸）
     - ``qe_dos_kgrid_offset_a``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - NSCF k グリッドオフセット（b 軸）
     - ``qe_dos_kgrid_offset_b``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -
   * - NSCF k グリッドオフセット（c 軸）
     - ``qe_dos_kgrid_offset_c``
     - 有効・無効
     - -
     - 無効
     - -
     - -
     - -

