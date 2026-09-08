.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate


######
ASE-MD
######

++++++++++++++
格子定数最適化
++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++
構造最適化
++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


#######
DFT-1/2
#######

+++++++++++++++++++++++++++++++++
DFT-1/2 擬ポテンシャル生成（UPF）
+++++++++++++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


#####
FLARE
#####

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


#######
GROMACS
#######

++++++++++
構造最適化
++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++
古典分子動力学
++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


#####
HybMD
#####

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


######
LAMMPS
######

++++++++++
構造最適化
++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++
古典分子動力学
++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


##########
Quloud-Mag
##########

++++++++++++++++++++
モンテカルロ磁性計算
++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++
LLG ダイナミクス
++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


######
OpenMX
######

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - SCF 収束度（密度）
     - ``scf_convergence_den``
     - 数値（指数表記）
     - bohr^-3
   * - SCF 反復回数
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - Hartree
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - Hartree
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - Hartree


++++++++++
構造最適化
++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - SCF 収束度（密度）
     - ``scf_convergence_den``
     - 数値（指数表記）
     - bohr^-3
   * - SCF 反復回数（最終実行）
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~~~
構造最適化
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 力の最大値
     - ``opt_total_force``
     - 数値
     - Hartree/Bohr
   * - 反復回数
     - ``opt_num_iter``
     - 整数
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - Hartree
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - Hartree
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - Hartree


++++++++++++++
格子定数最適化
++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - SCF 収束度（密度）
     - ``scf_convergence_den``
     - 数値（指数表記）
     - bohr^-3
   * - SCF 反復回数（最終実行）
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~~~
構造最適化
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 力の最大値
     - ``opt_total_force``
     - 数値
     - Hartree/Bohr
   * - 反復回数
     - ``opt_num_iter``
     - 整数
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - Hartree
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - Hartree
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - Hartree


++++++++++++++
電子バンド構造
++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - SCF 収束度（密度）
     - ``scf_convergence_den``
     - 数値（指数表記）
     - bohr^-3
   * - SCF 反復回数
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s


+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - SCF 収束度（密度）
     - ``scf_convergence_den``
     - 数値（指数表記）
     - bohr^-3
   * - SCF 反復回数
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - Hartree
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - Hartree
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - Hartree


++++++++++
分子動力学
++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++++
交換結合パラメータ
++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


####
Psi4
####

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++
構造最適化
++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++
分子振動解析
++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


################
Quantum ESPRESSO
################

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Ry
   * - SCF 収束性（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
   * - SCF 反復回数
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~~~
構造最適化
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 力の最大値
     - ``opt_total_force``
     - 数値
     - Ry/Bohr

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - k点数
     - ``num_k_points``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - eV
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - eV
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - eV
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - eV

~~~~~~~~~~
応力・圧力
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 圧力
     - ``pressure``
     - 数値
     - kbar
   * - 応力テンソル
     - ``stress_tensor``
     - 数値
     - kbar


++++++++++
構造最適化
++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Ry
   * - SCF 収束性（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
   * - SCF 反復回数（最終実行）
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF 実行回数
     - ``scf_cycle_count``
     - 整数
     - -
   * - SCF 総反復回数
     - ``scf_total_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~~~
構造最適化
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 力の最大値
     - ``opt_total_force``
     - 数値
     - Ry/Bohr
   * - 収束性（エネルギー）
     - ``opt_energy_error``
     - 数値（指数表記）
     - Ry
   * - 収束性（勾配）
     - ``opt_gradient_error``
     - 数値（指数表記）
     - Ry/Bohr
   * - 反復回数
     - ``opt_num_iter``
     - 整数
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - k点数
     - ``num_k_points``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - eV
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - eV
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - eV
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - eV

~~~~~~~~~~
応力・圧力
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 圧力
     - ``pressure``
     - 数値
     - kbar
   * - 応力テンソル
     - ``stress_tensor``
     - 数値
     - kbar


++++++++++++++
格子定数最適化
++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Ry
   * - SCF 収束性（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
   * - SCF 反復回数（最終実行）
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF 実行回数
     - ``scf_cycle_count``
     - 整数
     - -
   * - SCF 総反復回数
     - ``scf_total_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~~~
構造最適化
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 力の最大値
     - ``opt_total_force``
     - 数値
     - Ry/Bohr
   * - 収束性（エネルギー）
     - ``opt_energy_error``
     - 数値（指数表記）
     - Ry
   * - 収束性（勾配）
     - ``opt_gradient_error``
     - 数値（指数表記）
     - Ry/Bohr
   * - 反復回数
     - ``opt_num_iter``
     - 整数
     - -

~~~~~~~~~~
格子最適化
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 格子ベクトル行列
     - ``cell_parameters_matrix``
     - 数値
     - Angstrom
   * - 体積
     - ``volume``
     - 数値
     - Ang^3
   * - 密度
     - ``lattice_density``
     - 数値
     - g/cm^3
   * - エンタルピー
     - ``lattice_enthalpy``
     - 数値
     - Ry
   * - 収束性（格子勾配）
     - ``lattice_gradient_error``
     - 数値（指数表記）
     - kbar

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - k点数
     - ``num_k_points``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - eV
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - eV
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - eV
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - eV

~~~~~~~~~~
応力・圧力
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 圧力
     - ``pressure``
     - 数値
     - kbar
   * - 応力テンソル
     - ``stress_tensor``
     - 数値
     - kbar


++++++++++++++
電子バンド構造
++++++++++++++

~~~~~
Bands
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - Bands計算時間
     - ``bands_elapsed_time``
     - 数値
     - s


+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

~~~
DOS
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - DOS計算時間
     - ``dos_elapsed_time``
     - 数値
     - s


++++++++++++++++++++
投影状態密度（PDOS）
++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

~~~~~~~~~~~~~~~
NEB（反応経路）
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 活性化エネルギー（順方向）
     - ``neb_activation_energy_forward``
     - 数値
     - eV
   * - 活性化エネルギー（逆方向）
     - ``neb_activation_energy_backward``
     - 数値
     - eV
   * - 経路長
     - ``neb_path_length``
     - 数値
     - Bohr
   * - イメージ間距離
     - ``neb_inter_image_distance``
     - 数値
     - Bohr
   * - Climbing image（遷移状態イメージ番号）
     - ``neb_climbing_image``
     - 整数
     - -
   * - 経路最適化の反復回数
     - ``neb_num_iterations``
     - 整数
     - -
   * - NEB 計算時間
     - ``neb_elapsed_time``
     - 数値
     - s


++++++++++++
フォノン計算
++++++++++++

~~~~~~~~~~~~~~~~
フォノン（DFPT）
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - q 点数
     - ``phonon_num_q_points``
     - 整数
     - -
   * - フォノン計算時間
     - ``phonon_elapsed_time``
     - 数値
     - s


+++++++++++++++++++++++++++++
X線吸収スペクトル（XSpectra）
+++++++++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

+++++++++++++++++++++++
X線吸収スペクトル用 SCF
+++++++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Ry
   * - SCF 収束性（エネルギー）
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Ry
   * - SCF 反復回数
     - ``scf_num_iter``
     - 整数
     - -
   * - SCF計算時間
     - ``scf_elapsed_time``
     - 数値
     - s

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - k点数
     - ``num_k_points``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - eV
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - eV
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - eV
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - eV


++++++++++++++++++++++++++++
固定ポテンシャル電子状態計算
++++++++++++++++++++++++++++

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - k点数
     - ``num_k_points``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - eV
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - eV
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - eV
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - eV
   * - NSCF計算時間
     - ``nscf_elapsed_time``
     - 数値
     - s


++++++++++++++++++++++++++++++++++++++
固定ポテンシャル電子状態計算（バンド）
++++++++++++++++++++++++++++++++++++++

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 電子数
     - ``num_electrons``
     - 数値
     - -
   * - Kohn-Sham 状態数
     - ``num_kohn_sham_states``
     - 整数
     - -
   * - k点数
     - ``num_k_points``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - eV
   * - 価電子帯上端
     - ``vbm``
     - 数値
     - eV
   * - 伝導帯下端
     - ``cbm``
     - 数値
     - eV
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - eV
   * - NSCF計算時間
     - ``nscf_elapsed_time``
     - 数値
     - s


+++++++++++++++++
力定数計算（q2r）
+++++++++++++++++

~~~~~~~~~~~~~
力定数（q2r）
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - q 空間グリッド点数
     - ``q2r_num_q_points``
     - 整数
     - -
   * - q2r 計算時間
     - ``q2r_elapsed_time``
     - 数値
     - s


++++++++++++++++++++++++++++
フォノンバンド分散（matdyn）
++++++++++++++++++++++++++++

~~~~~~~~~~~~~~
フォノンバンド
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - matdyn 計算時間
     - ``matdyn_elapsed_time``
     - 数値
     - s


++++++++++++++++++++++++++
フォノン状態密度（matdyn）
++++++++++++++++++++++++++

~~~~~~~~~~~~~~~~
フォノン状態密度
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - matdyn 計算時間
     - ``matdyn_elapsed_time``
     - 数値
     - s



#######
RadonPy
#######

+++++++++++++++++++++++
QM構造最適化 / RESP電荷
+++++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++
高分子平衡化MD
++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++
溶解度パラメータ
++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++
ガラス転移温度
++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++
熱伝導率
++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++++++++++++
ヤング率（機械特性）
++++++++++++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。

++++++++++
複素誘電率
++++++++++

この計算には、数値の一覧として表示される結果の登録はありません。


#####
RSDFT
#####

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - 全エネルギーの誤差
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
   * - 終了ステータス
     - ``rsdft_exit_status``
     - 文字列
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - HOMO-LUMO ギャップ
     - ``rsdft_homo_lumo_gap``
     - 数値
     - Hartree
   * - スピン上向き電子数
     - ``rsdft_spin_up``
     - 数値
     - -
   * - スピン下向き電子数
     - ``rsdft_spin_down``
     - 数値
     - -
   * - スピン差
     - ``rsdft_spin_difference``
     - 数値
     - -

~~~~~~~~~~~~~~
エネルギー内訳
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 運動エネルギー
     - ``rsdft_kinetic_energy``
     - 数値
     - Hartree
   * - ハートリーエネルギー
     - ``rsdft_hartree_energy``
     - 数値
     - Hartree
   * - 交換相関エネルギー
     - ``rsdft_xc_energy``
     - 数値
     - Hartree
   * - Ewaldエネルギー
     - ``rsdft_ewald_energy``
     - 数値
     - Hartree
   * - 局所擬ポテンシャルエネルギー
     - ``rsdft_local_pp_energy``
     - 数値
     - Hartree
   * - 非局所擬ポテンシャルエネルギー
     - ``rsdft_nonlocal_pp_energy``
     - 数値
     - Hartree
   * - 分散力エネルギー
     - ``rsdft_vdw_energy``
     - 数値
     - Hartree


++++++++++
構造最適化
++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - 全エネルギーの誤差
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
   * - 終了ステータス
     - ``rsdft_exit_status``
     - 文字列
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - HOMO-LUMO ギャップ
     - ``rsdft_homo_lumo_gap``
     - 数値
     - Hartree
   * - スピン上向き電子数
     - ``rsdft_spin_up``
     - 数値
     - -
   * - スピン下向き電子数
     - ``rsdft_spin_down``
     - 数値
     - -
   * - スピン差
     - ``rsdft_spin_difference``
     - 数値
     - -

~~~~~~~~~~~~~~
エネルギー内訳
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 運動エネルギー
     - ``rsdft_kinetic_energy``
     - 数値
     - Hartree
   * - ハートリーエネルギー
     - ``rsdft_hartree_energy``
     - 数値
     - Hartree
   * - 交換相関エネルギー
     - ``rsdft_xc_energy``
     - 数値
     - Hartree
   * - Ewaldエネルギー
     - ``rsdft_ewald_energy``
     - 数値
     - Hartree
   * - 局所擬ポテンシャルエネルギー
     - ``rsdft_local_pp_energy``
     - 数値
     - Hartree
   * - 非局所擬ポテンシャルエネルギー
     - ``rsdft_nonlocal_pp_energy``
     - 数値
     - Hartree
   * - 分散力エネルギー
     - ``rsdft_vdw_energy``
     - 数値
     - Hartree


++++++++++++++
格子定数最適化
++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - 全エネルギーの誤差
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
   * - 終了ステータス
     - ``rsdft_exit_status``
     - 文字列
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - HOMO-LUMO ギャップ
     - ``rsdft_homo_lumo_gap``
     - 数値
     - Hartree
   * - スピン上向き電子数
     - ``rsdft_spin_up``
     - 数値
     - -
   * - スピン下向き電子数
     - ``rsdft_spin_down``
     - 数値
     - -
   * - スピン差
     - ``rsdft_spin_difference``
     - 数値
     - -

~~~~~~~~~~~~~~
エネルギー内訳
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 運動エネルギー
     - ``rsdft_kinetic_energy``
     - 数値
     - Hartree
   * - ハートリーエネルギー
     - ``rsdft_hartree_energy``
     - 数値
     - Hartree
   * - 交換相関エネルギー
     - ``rsdft_xc_energy``
     - 数値
     - Hartree
   * - Ewaldエネルギー
     - ``rsdft_ewald_energy``
     - 数値
     - Hartree
   * - 局所擬ポテンシャルエネルギー
     - ``rsdft_local_pp_energy``
     - 数値
     - Hartree
   * - 非局所擬ポテンシャルエネルギー
     - ``rsdft_nonlocal_pp_energy``
     - 数値
     - Hartree
   * - 分散力エネルギー
     - ``rsdft_vdw_energy``
     - 数値
     - Hartree


++++++++++++++
電子バンド構造
++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - 全エネルギーの誤差
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
   * - 終了ステータス
     - ``rsdft_exit_status``
     - 文字列
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - HOMO-LUMO ギャップ
     - ``rsdft_homo_lumo_gap``
     - 数値
     - Hartree
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - Hartree
   * - スピン上向き電子数
     - ``rsdft_spin_up``
     - 数値
     - -
   * - スピン下向き電子数
     - ``rsdft_spin_down``
     - 数値
     - -
   * - スピン差
     - ``rsdft_spin_difference``
     - 数値
     - -

~~~~~~~~~~~~~~
エネルギー内訳
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 運動エネルギー
     - ``rsdft_kinetic_energy``
     - 数値
     - Hartree
   * - ハートリーエネルギー
     - ``rsdft_hartree_energy``
     - 数値
     - Hartree
   * - 交換相関エネルギー
     - ``rsdft_xc_energy``
     - 数値
     - Hartree
   * - Ewaldエネルギー
     - ``rsdft_ewald_energy``
     - 数値
     - Hartree
   * - 局所擬ポテンシャルエネルギー
     - ``rsdft_local_pp_energy``
     - 数値
     - Hartree
   * - 非局所擬ポテンシャルエネルギー
     - ``rsdft_nonlocal_pp_energy``
     - 数値
     - Hartree
   * - 分散力エネルギー
     - ``rsdft_vdw_energy``
     - 数値
     - Hartree


+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - 全エネルギーの誤差
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
   * - 終了ステータス
     - ``rsdft_exit_status``
     - 文字列
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - HOMO-LUMO ギャップ
     - ``rsdft_homo_lumo_gap``
     - 数値
     - Hartree
   * - バンドギャップ
     - ``band_gap``
     - 数値
     - Hartree
   * - スピン上向き電子数
     - ``rsdft_spin_up``
     - 数値
     - -
   * - スピン下向き電子数
     - ``rsdft_spin_down``
     - 数値
     - -
   * - スピン差
     - ``rsdft_spin_difference``
     - 数値
     - -

~~~~~~~~~~~~~~
エネルギー内訳
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 運動エネルギー
     - ``rsdft_kinetic_energy``
     - 数値
     - Hartree
   * - ハートリーエネルギー
     - ``rsdft_hartree_energy``
     - 数値
     - Hartree
   * - 交換相関エネルギー
     - ``rsdft_xc_energy``
     - 数値
     - Hartree
   * - Ewaldエネルギー
     - ``rsdft_ewald_energy``
     - 数値
     - Hartree
   * - 局所擬ポテンシャルエネルギー
     - ``rsdft_local_pp_energy``
     - 数値
     - Hartree
   * - 非局所擬ポテンシャルエネルギー
     - ``rsdft_nonlocal_pp_energy``
     - 数値
     - Hartree
   * - 分散力エネルギー
     - ``rsdft_vdw_energy``
     - 数値
     - Hartree


++++++++++
分子動力学
++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Hartree
   * - 全エネルギーの誤差
     - ``scf_convergence_ene``
     - 数値（指数表記）
     - Hartree
   * - 終了ステータス
     - ``rsdft_exit_status``
     - 文字列
     - -

~~~~~~~~
電子構造
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Hartree
   * - HOMO-LUMO ギャップ
     - ``rsdft_homo_lumo_gap``
     - 数値
     - Hartree
   * - スピン上向き電子数
     - ``rsdft_spin_up``
     - 数値
     - -
   * - スピン下向き電子数
     - ``rsdft_spin_down``
     - 数値
     - -
   * - スピン差
     - ``rsdft_spin_difference``
     - 数値
     - -

~~~~~~~~~~~~~~
エネルギー内訳
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 運動エネルギー
     - ``rsdft_kinetic_energy``
     - 数値
     - Hartree
   * - ハートリーエネルギー
     - ``rsdft_hartree_energy``
     - 数値
     - Hartree
   * - 交換相関エネルギー
     - ``rsdft_xc_energy``
     - 数値
     - Hartree
   * - Ewaldエネルギー
     - ``rsdft_ewald_energy``
     - 数値
     - Hartree
   * - 局所擬ポテンシャルエネルギー
     - ``rsdft_local_pp_energy``
     - 数値
     - Hartree
   * - 非局所擬ポテンシャルエネルギー
     - ``rsdft_nonlocal_pp_energy``
     - 数値
     - Hartree
   * - 分散力エネルギー
     - ``rsdft_vdw_energy``
     - 数値
     - Hartree

~~~~~~~~~~
分子動力学
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - MD総時間
     - ``rsdft_total_md_time``
     - 数値
     - fs



######
SPRKKR
######

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

~~~
SCF
~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - 全エネルギー
     - ``total_energy``
     - 数値
     - Ry
   * - SCF 反復回数
     - ``scf_num_iter``
     - 整数
     - -
   * - フェルミエネルギー
     - ``fermi_energy``
     - 数値
     - Ry
   * - スピン磁気モーメント
     - ``sprkkr_mu_spn``
     - 数値
     - μB
   * - 軌道磁気モーメント
     - ``sprkkr_mu_orb``
     - 数値
     - μB


++++++++++++++++++
交換結合パラメータ
++++++++++++++++++

~~~~~~~~~~~~~~~~~~
交換結合パラメータ
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 30 18 18

   * - 項目名
     - キー
     - 型
     - 単位
   * - キュリー温度（平均場近似）
     - ``sprkkr_curie_temperature``
     - 数値
     - K


