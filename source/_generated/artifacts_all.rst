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

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``ase.in``
     - -
     - text
   * - トラジェクトリ
     - ``QuloudJob.traj``
     - -
     - traj

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``ase.in``
     - -
     - text
   * - トラジェクトリ
     - ``QuloudJob.traj``
     - -
     - traj

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``ase.in``
     - -
     - text
   * - 主な出力
     - ``asemd.out``
     - -
     - text
   * - トラジェクトリ
     - ``QuloudJob.md``
     - -
     - ext\_xyz
   * - トラジェクトリ
     - ``QuloudJob.traj``
     - -
     - traj
   * - 構造
     - ``QuloudJob.xyz``
     - -
     - xyz

++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``ase.in``
     - -
     - text


#######
DFT-1/2
#######

+++++++++++++++++++++++++++++++++
DFT-1/2 擬ポテンシャル生成（UPF）
+++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``<名前>.upf``（``.dft12.`` を含むものを除く）
     - ベース UPF 擬ポテンシャル
     - upf
   * - 入力
     - ``dft12.json``
     - DFT-1/2 パッチャー設定
     - json
   * - 主な出力
     - ``<名前>.dft12.upf``
     - DFT-1/2 パッチ済み UPF 擬ポテンシャル
     - upf
   * - 補助出力
     - ``*.deltaV.dat``
     - PP\_LOCAL 補正量 ΔV(r)
     - text
   * - 補助出力
     - ``*.summary.csv``
     - パッチ処理サマリ（パラメータ・来歴ハッシュ）
     - csv
   * - 補助出力
     - ``*.theta.dat``
     - カットオフ関数 θ(r)
     - text
   * - 補助出力
     - ``*.vks_neutral.dat``
     - 中性配置の全電子 KS ポテンシャル
     - text
   * - 補助出力
     - ``*.vks_stripped.dat``
     - 剥ぎ取り配置の全電子 KS ポテンシャル
     - text
   * - 補助出力
     - ``*.vloc.dat``
     - パッチ前後の局所ポテンシャル
     - text
   * - 補助出力
     - ``*.vse.dat``
     - 自己エネルギーポテンシャル V\_S(r)
     - text
   * - ログ
     - ``QuloudJob.dft12.err``
     - パッチャー実行エラーログ
     - text
   * - ログ
     - ``QuloudJob.dft12.out``
     - パッチャー実行ログ（結果 JSON）
     - text
   * - ログ
     - ``QuloudJob.exit_status.json``
     - -
     - json


#####
FLARE
#####

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

この計算には、Quloud が登録する入出力ファイルはありません。


#######
GROMACS
#######

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``*.gro``
     - 初期構造ファイル（GROMACSフォーマット）
     - text
   * - 入力
     - ``*.itp``
     - トポロジーインクルードファイル（力場定義・分子定義）
     - text
   * - 入力
     - ``*.top``
     - トポロジーファイル（力場情報を含む）
     - text
   * - 入力
     - ``em.mdp``
     - エネルギー最小化パラメータファイル（自動生成）
     - text
   * - 主な出力
     - ``em.gro``
     - 最小化後の最終構造
     - text
   * - 補助出力
     - ``em.edr``
     - エネルギーデータ（バイナリ）
     - binary
   * - トラジェクトリ
     - ``em.trr``
     - 全フレームトラジェクトリ
     - binary
   * - ログ
     - ``em.log``
     - エネルギー最小化ログ
     - text

++++++++++++++
古典分子動力学
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``*.gro``
     - 初期構造ファイル（GROMACSフォーマット）
     - text
   * - 入力
     - ``*.itp``
     - トポロジーインクルードファイル（力場定義・分子定義）
     - text
   * - 入力
     - ``*.top``
     - トポロジーファイル（力場情報を含む）
     - text
   * - 入力
     - ``nvt.mdp``
     - MDパラメータファイル（自動生成）
     - text
   * - 主な出力
     - ``nvt.gro``
     - MD後の最終構造
     - text
   * - 補助出力
     - ``nvt.edr``
     - エネルギーデータ（バイナリ）
     - binary
   * - トラジェクトリ
     - ``nvt.xtc``
     - 圧縮トラジェクトリ
     - binary
   * - ログ
     - ``nvt.log``
     - MDログ
     - text


#####
HybMD
#####

+++++++++++++++++++++++
機械学習ポテンシャル MD
+++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``md.ini``
     - -
     - text
   * - 主な出力
     - ``md.log``
     - -
     - text
   * - トラジェクトリ
     - ``md.traj``
     - -
     - traj

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``scf.ini``
     - -
     - text


######
LAMMPS
######

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.lmp``
     - 初期構造（LAMMPS data 形式）
     - text
   * - 入力
     - ``in.QuloudJob``
     - LAMMPS入力スクリプト（Quloudが生成）
     - text
   * - 主な出力
     - ``log.lammps``
     - LAMMPS標準ログ（thermo 出力の時系列を含む）
     - text
   * - トラジェクトリ
     - ``QuloudJob.lammpstrj``
     - 原子構造トラジェクトリ（dump 出力）
     - text
   * - 構造
     - ``QuloudJob.out.lmp``
     - 最終構造（write\_data 出力。rsdft.atom.out.cif への変換元）
     - text

++++++++++++++
古典分子動力学
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.lmp``
     - 初期構造（LAMMPS data 形式）
     - text
   * - 入力
     - ``in.QuloudJob``
     - LAMMPS入力スクリプト（Quloudが生成）
     - text
   * - 主な出力
     - ``log.lammps``
     - LAMMPS標準ログ（thermo 出力の時系列を含む）
     - text
   * - トラジェクトリ
     - ``QuloudJob.lammpstrj``
     - 原子構造トラジェクトリ（dump 出力）
     - text
   * - 構造
     - ``QuloudJob.out.lmp``
     - 最終構造（write\_data 出力。rsdft.atom.out.cif への変換元）
     - text


##########
Quloud-Mag
##########

++++++++++++++++++++
モンテカルロ磁性計算
++++++++++++++++++++

この計算には、Quloud が登録する入出力ファイルはありません。

++++++++++++++++
LLG ダイナミクス
++++++++++++++++

この計算には、Quloud が登録する入出力ファイルはありません。


######
OpenMX
######

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``openmx.in``
     - OpenMX入力ファイル
     - text
   * - 主な出力
     - ``QuloudJob.out``
     - OpenMX標準出力（SCF収束履歴・全エネルギー・固有値等）
     - text
   * - ログ
     - ``QuloudJob.err``
     - OpenMX標準エラー出力
     - text

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``openmx.in``
     - OpenMX入力ファイル
     - text
   * - 主な出力
     - ``QuloudJob.out``
     - OpenMX標準出力（SCF収束履歴・全エネルギー・固有値等）
     - text
   * - ログ
     - ``QuloudJob.err``
     - OpenMX標準エラー出力
     - text

++++++++++++++
格子定数最適化
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``openmx.in``
     - OpenMX入力ファイル
     - text
   * - 主な出力
     - ``QuloudJob.out``
     - OpenMX標準出力（SCF収束履歴・全エネルギー・固有値等）
     - text
   * - ログ
     - ``QuloudJob.err``
     - OpenMX標準エラー出力
     - text

++++++++++++++
電子バンド構造
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``openmx.in``
     - OpenMX入力ファイル
     - text
   * - 主な出力
     - ``QuloudJob.out``
     - OpenMX標準出力（SCF収束履歴・全エネルギー・固有値等）
     - text
   * - ログ
     - ``QuloudJob.err``
     - OpenMX標準エラー出力
     - text

+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``openmx.in``
     - OpenMX入力ファイル
     - text
   * - 主な出力
     - ``QuloudJob.out``
     - OpenMX標準出力（SCF収束履歴・全エネルギー・固有値等）
     - text
   * - ログ
     - ``QuloudJob.err``
     - OpenMX標準エラー出力
     - text

++++++++++
分子動力学
++++++++++

この計算には、Quloud が登録する入出力ファイルはありません。

++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

この計算には、Quloud が登録する入出力ファイルはありません。

++++++++++++++++++
交換結合パラメータ
++++++++++++++++++

この計算には、Quloud が登録する入出力ファイルはありません。


####
Psi4
####

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``psi4_input.in``
     - Psi4 入力スクリプト（Python形式）
     - text
   * - 主な出力
     - ``psi4.out``
     - Psi4 計算ログ（エネルギー等を含む）
     - text

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``psi4_input.in``
     - Psi4 入力スクリプト（Python形式）
     - text
   * - 主な出力
     - ``psi4.out``
     - Psi4 計算ログ（最終エネルギー・最適化構造を含む）
     - text

++++++++++++
分子振動解析
++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``psi4_input.in``
     - Psi4 入力スクリプト（Python形式）
     - text
   * - 主な出力
     - ``psi4.out``
     - Psi4 計算ログ（振動数・熱化学データを含む）
     - text


################
Quantum ESPRESSO
################

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.scf.in``
     - -
     - text
   * - 入力
     - ``<名前>.upf``
     - -
     - upf
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 主な出力
     - ``work``
     - -
     - dir
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.scf.in``
     - -
     - text
   * - 入力
     - ``<名前>.upf``
     - -
     - upf
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 主な出力
     - ``work``
     - -
     - dir
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

++++++++++++++
格子定数最適化
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.scf.in``
     - -
     - text
   * - 入力
     - ``<名前>.upf``
     - -
     - upf
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 主な出力
     - ``work``
     - -
     - dir
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

++++++++++++++
電子バンド構造
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.bands.in``
     - -
     - text
   * - 入力
     - ``QuloudJob.bands2.in``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.bands.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.bands2.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.nscf.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.bands``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.bands.gnu``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.bands.rap``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.bands2``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.bands2.gnu``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.bands2.rap``
     - -
     - text
   * - 補助出力
     - ``band.json``
     - -
     - json
   * - ログ
     - ``QuloudJob.bands.err``
     - -
     - text
   * - ログ
     - ``QuloudJob.bands2.err``
     - -
     - text
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.dos.in``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.dos``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.dos.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.nscf.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 補助出力
     - ``dos.json``
     - -
     - json
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

++++++++++++++++++++
投影状態密度（PDOS）
++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.nscf.in``
     - -
     - text
   * - 入力
     - ``QuloudJob.pdos.in``
     - -
     - text
   * - 入力
     - ``QuloudJob.scf.in``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.nscf.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.pdos.out``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.pdos.pdos_atm#*``
     - -
     - text
   * - 補助出力
     - ``QuloudJob.pdos.pdos_tot``
     - -
     - text
   * - 補助出力
     - ``atomic_proj.xml``
     - -
     - xml
   * - 補助出力
     - ``pdos.json``
     - -
     - json
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

++++++++++++++++++++++++++
NEB（Nudged Elastic Band）
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.scf.in``
     - NEB では neb.x に直接渡さないが、擬ポテンシャル選択の記録として生成される
     - text
   * - 入力
     - ``QuloudJob.neb.in`` または ``neb.in``
     - neb.x 入力（旧名 neb.in にも対応）
     - text
   * - 入力
     - ``<名前>.upf``
     - -
     - upf
   * - 主な出力
     - ``QuloudJob.dat``
     - 経路のエネルギープロファイル（反応座標／エネルギー[eV]／誤差[eV/A]）
     - text
   * - 主な出力
     - ``neb.out``
     - neb.x 標準出力（活性化エネルギー・イメージ別エネルギー・収束状況）
     - text
   * - 主な出力
     - ``work``
     - -
     - dir
   * - 補助出力
     - ``QuloudJob.int``
     - 経路エネルギーの内挿曲線
     - text
   * - 補助出力
     - ``QuloudJob.path``
     - 経路最適化の再開情報
     - text
   * - 補助出力
     - ``pw_<番号>.in``
     - neb.x が生成するイメージ別 pw.x 入力
     - text
   * - 補助出力
     - ``neb.dat``
     - neb.x が入力から切り出す &PATH ネームリスト（入力ではなく生成物）
     - text
   * - 構造
     - ``QuloudJob.axsf``
     - 全イメージのアニメーション構造（XCrySDen AXSF）
     - axsf
   * - 構造
     - ``QuloudJob.crd``
     - 全イメージの原子座標（ATOMIC\_POSITIONS 形式）
     - text
   * - 構造
     - ``QuloudJob.xyz``
     - 全イメージの構造（XYZ）
     - xyz
   * - ログ
     - ``neb.err``
     - neb.x 標準エラー出力
     - text

++++++++++++
フォノン計算
++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.ph.in`` または ``ph.in``
     - ph.x 入力（DFPT。旧名 ph.in にも対応）
     - text
   * - 主な出力
     - ``ph.out``
     - ph.x 標準出力（各 q 点の振動数・計算時間）
     - text
   * - 補助出力
     - ``QuloudJob.dyn<番号>`` または ``matdyn.dyn<番号>``
     - 動力学行列（fildyn。dyn0 は q 点グリッド情報、dyn1 以降が各 q 点）
     - text
   * - ログ
     - ``ph.err``
     - ph.x 標準エラー出力
     - text

+++++++++++++++++++++++++++++
X線吸収スペクトル（XSpectra）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.xspectra.in`` または ``xspectra.in``
     - xspectra.x 入力（旧名 xspectra.in にも対応）
     - text
   * - 主な出力
     - ``xanes.dat``
     - XANES スペクトル（エネルギー vs 吸収強度）
     - text
   * - 主な出力
     - ``xspectra.out``
     - xspectra.x 標準出力（収束状況・計算時間）
     - text
   * - 補助出力
     - ``Core.wfc``
     - コア波動関数（filecore。upf2plotcore.sh が生成する固定名。#1194）
     - text
   * - 補助出力
     - ``xanes.sav``
     - xspectra.x の再開用データ（Lanczos 係数）
     - binary
   * - ログ
     - ``xspectra.err``
     - xspectra.x 標準エラー出力
     - text

+++++++++++++++++++++++
X線吸収スペクトル用 SCF
+++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.scf.in``
     - -
     - text
   * - 入力
     - ``<名前>.upf``
     - -
     - upf
   * - 主な出力
     - ``QuloudJob.scf.out``
     - -
     - text
   * - 主な出力
     - ``work``
     - -
     - dir
   * - ログ
     - ``QuloudJob.scf.err``
     - -
     - text

++++++++++++++++++++++++++++
固定ポテンシャル電子状態計算
++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 主な出力
     - ``QuloudJob.nscf.out``
     - -
     - text

++++++++++++++++++++++++++++++++++++++
固定ポテンシャル電子状態計算（バンド）
++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.nscf.in``
     - -
     - text
   * - 主な出力
     - ``QuloudJob.nscf.out``
     - -
     - text

+++++++++++++++++
力定数計算（q2r）
+++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.q2r.in`` または ``q2r.in``
     - q2r.x 入力（旧名 q2r.in にも対応）
     - text
   * - 主な出力
     - ``QuloudJob.fc`` または ``matdyn.fc``
     - 実空間力定数（flfrc。matdyn.x の入力になる）
     - text
   * - 主な出力
     - ``q2r.out``
     - q2r.x 標準出力
     - text

++++++++++++++++++++++++++++
フォノンバンド分散（matdyn）
++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.matdyn.in`` または ``matdyn_disp.in``
     - matdyn.x 入力（分散曲線。旧名 matdyn\_disp.in にも対応）
     - text
   * - 主な出力
     - ``QuloudJob.freq`` または ``matdyn.freq``
     - フォノン振動数（flfrq）
     - text
   * - 主な出力
     - ``matdyn_disp.out``
     - matdyn.x 標準出力（分散曲線）
     - text
   * - 補助出力
     - ``QuloudJob.freq.gp`` または ``matdyn.freq.gp``
     - フォノン振動数（gnuplot 形式）
     - text
   * - 補助出力
     - ``matdyn.modes``
     - フォノン固有ベクトル（flvec）
     - text

++++++++++++++++++++++++++
フォノン状態密度（matdyn）
++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.matdyn.in`` または ``matdyn_dos.in``
     - matdyn.x 入力（フォノンDOS。旧名 matdyn\_dos.in にも対応）
     - text
   * - 主な出力
     - ``QuloudJob.dos`` または ``matdyn.dos``
     - フォノン状態密度（fldos）
     - text
   * - 主な出力
     - ``matdyn_dos.out``
     - matdyn.x 標準出力（フォノンDOS）
     - text
   * - 補助出力
     - ``QuloudJob.freq.gp`` または ``matdyn.freq.gp``
     - フォノン振動数（gnuplot 形式）
     - text
   * - 補助出力
     - ``QuloudJob.freq`` または ``matdyn.freq``
     - フォノン振動数（flfrq）
     - text
   * - 補助出力
     - ``matdyn.modes``
     - フォノン固有ベクトル（flvec）
     - text


#######
RadonPy
#######

+++++++++++++++++++++++
QM構造最適化 / RESP電荷
+++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - 拡張子が ``.mol2`` / ``.xyz`` / ``.sdf`` / ``.pdb`` のいずれか
     - 3次元構造ファイル（mol2/xyz/sdf/pdb。SMILES入力時は不要）
     - text
   * - 主な出力
     - ``monomer.pickle``
     - RESP電荷付きモノマーオブジェクト（次ステップへの引き継ぎファイル）
     - binary
   * - 主な出力
     - ``qm_result.json``
     - QM計算結果（HOMO/LUMO/双極子/偏極率等）
     - json
   * - ログ
     - ``psi4.log``
     - Psi4計算ログ
     - text

++++++++++++++
高分子平衡化MD
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``monomer.pickle``
     - QMステップから引き継いだモノマーオブジェクト
     - binary
   * - 主な出力
     - ``eq_result.json``
     - 平衡化MD結果（密度・エネルギー・Rg等）
     - json
   * - 補助出力
     - ``polymer_cell.lammps``
     - LAMMPSデータファイル（高分子非晶セル）
     - text
   * - トラジェクトリ
     - ``eq.xtc``
     - 平衡化MDトラジェクトリ（XTC形式）
     - binary
   * - ログ
     - ``eq.log``
     - LAMMPS平衡化MDログ
     - text

++++++++++++++++
溶解度パラメータ
++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 主な出力
     - ``sp_result.json``
     - 溶解度パラメータ計算結果（SP\_total/SP\_vdw/SP\_ele/CED）
     - json
   * - ログ
     - ``sp.log``
     - LAMMPS rerunログ
     - text

++++++++++++++
ガラス転移温度
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 主な出力
     - ``tg_result.json``
     - ガラス転移温度計算結果（Tg/熱膨張係数）
     - json
   * - ログ
     - ``tg.log``
     - LAMMPS冷却MDログ
     - text

++++++++
熱伝導率
++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 主な出力
     - ``tc_result.json``
     - 熱伝導率計算結果（κ/熱拡散率等）
     - json
   * - ログ
     - ``tc.log``
     - LAMMPS NEMD計算ログ
     - text

++++++++++++++++++++
ヤング率（機械特性）
++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 主な出力
     - ``elong_result.json``
     - ヤング率・応力ひずみ計算結果
     - json
   * - ログ
     - ``elong.log``
     - LAMMPS変形MDログ
     - text

++++++++++
複素誘電率
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 主な出力
     - ``dielectric_result.json``
     - 複素誘電率計算結果（ε'/ε''/tan δ）
     - json
   * - ログ
     - ``dielectric.log``
     - LAMMPS電場印加MDログ
     - text


#####
RSDFT
#####

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
   * - 主な出力
     - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
   * - 補助出力
     - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
   * - 補助出力
     - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
   * - 補助出力
     - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
   * - 補助出力
     - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
   * - ログ
     - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
   * - ログ
     - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text

++++++++++
構造最適化
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
   * - 主な出力
     - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
   * - 補助出力
     - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
   * - 補助出力
     - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
   * - 補助出力
     - ``linmin_ef.dat``
     - 直線探索・フェルミエネルギー探索の内部状態（バイナリ）
     - binary
   * - 補助出力
     - ``optconv.csv``
     - 原子位置最適化の収束履歴（イテレーションごとの最大力）
     - csv
   * - 補助出力
     - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
   * - 補助出力
     - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
   * - 補助出力
     - ``wopt.dat``
     - 原子位置最適化の内部状態（バイナリ、リスタート用）
     - binary
   * - ログ
     - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
   * - ログ
     - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text

++++++++++++++
格子定数最適化
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
   * - 主な出力
     - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
   * - 補助出力
     - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
   * - 補助出力
     - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
   * - 補助出力
     - ``linmin_ef.dat``
     - 直線探索・フェルミエネルギー探索の内部状態（バイナリ）
     - binary
   * - 補助出力
     - ``optconv.csv``
     - 原子位置最適化の収束履歴（イテレーションごとの最大力）
     - csv
   * - 補助出力
     - ``optlat.restart``
     - 格子探索の状態（探索点ごとのスケールとエネルギー）
     - text
   * - 補助出力
     - ``rsdft.json_min``
     - 最小エネルギー点での計算結果（rsdft.json と同形式）
     - json
   * - 補助出力
     - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
   * - 補助出力
     - ``ve.dat``
     - 体積-エネルギー曲線（1行 = 体積 / 全エネルギー / a1 / a2 / a3 / Ecut / Ngrid×3 / 原子数）
     - text
   * - 補助出力
     - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
   * - 補助出力
     - ``wopt.dat``
     - 原子位置最適化の内部状態（バイナリ、リスタート用）
     - binary
   * - ログ
     - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
   * - ログ
     - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text

++++++++++++++
電子バンド構造
++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
   * - 主な出力
     - ``band.json``
     - バンド構造データ（rsdft.xが直接出力。変換スクリプト不要）
     - json
   * - 主な出力
     - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
   * - 補助出力
     - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
   * - 補助出力
     - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
   * - 補助出力
     - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
   * - 補助出力
     - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
   * - ログ
     - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
   * - ログ
     - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text

+++++++++++++++++++
状態密度計算（DOS）
+++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
   * - 主な出力
     - ``dos.json``
     - 状態密度データ（rsdft.xが直接出力）
     - json
   * - 主な出力
     - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
   * - 補助出力
     - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
   * - 補助出力
     - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
   * - 補助出力
     - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
   * - 補助出力
     - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
   * - ログ
     - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
   * - ログ
     - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text

++++++++++
分子動力学
++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``rsdft.in``
     - RSDFT入力ファイル（XCTYPE/NGRID/KGRID/ECUT等）
     - text
   * - 主な出力
     - ``rsdft.json``
     - RSDFT計算結果本体（全エネルギー内訳・efermi・egap・スピン等のスカラー値）
     - json
   * - 補助出力
     - ``cif_*.dat``
     - 対称解析・CIF生成用の中間ファイル（原子基底/対称操作/対称記述）
     - text
   * - 補助出力
     - ``eigenvalues.json``
     - k点・スピンごとの固有値（バンドエネルギー）
     - json
   * - 補助出力
     - ``etot.json``
     - MD時系列（全エネルギー Etot / DFTエネルギー Edft）
     - json
   * - 補助出力
     - ``fke.json``
     - MD時系列（架空運動エネルギー FKE）
     - json
   * - 補助出力
     - ``scfconv.csv``
     - SCF収束履歴（CSV）
     - csv
   * - 補助出力
     - ``temp.json``
     - MD時系列（イオン温度 Temperature）
     - json
   * - 補助出力
     - ``vrho.dat1``
     - 電荷密度バイナリ
     - binary
   * - トラジェクトリ
     - ``TRAJECTORY.cif``
     - MDトラジェクトリ（#RS-CPMD\_STEP-> 区切りの複数フレームCIF）
     - text
   * - ログ
     - ``QuloudJob.err``
     - RSDFT標準エラー出力
     - text
   * - ログ
     - ``QuloudJob.out``
     - RSDFT標準出力（SCF収束履歴等）
     - text


######
SPRKKR
######

+++++++++++++++++++++++++++++
自己無撞着電子状態計算（SCF）
+++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.pot``
     - SPR-KKR ポテンシャルファイル
     - text
   * - 入力
     - ``QuloudJob_SCF.inp``
     - SPR-KKR SCF 入力ファイル
     - text
   * - 入力
     - ``occupation.dat``
     - サイト占有率（kkr\_occupancy 由来）
     - text
   * - 主な出力
     - ``QuloudJob_SCF.log``
     - SCF 反復表（kkrscfMPI 自身が書く。結果抽出の一次ソース）
     - text
   * - 補助出力
     - ``QuloudJob.pot_new``
     - 収束後ポテンシャル（交換結合パラメータ計算の入力になる）
     - text
   * - 補助出力
     - ``QuloudJob_SCF*.dos``
     - SCF 開始時の状態密度
     - text
   * - 構造
     - ``rsdft.atom``
     - 原子構造ファイル
     - text
   * - ログ
     - ``buildbot.log``
     - ビルドボットログ
     - text
   * - ログ
     - ``sprkkr_scf.exec.log``
     - kkrscfMPI の標準出力
     - text

++++++++++++++++++
交換結合パラメータ
++++++++++++++++++

.. list-table::
   :header-rows: 1
   :widths: 14 34 38 14

   * - 役割
     - ファイル
     - 内容
     - 形式
   * - 入力
     - ``QuloudJob.pot``
     - SPR-KKR ポテンシャルファイル
     - text
   * - 入力
     - ``QuloudJob_JXC.inp``
     - SPR-KKR JXC 入力ファイル
     - text
   * - 主な出力
     - ``QuloudJob_JXC_J_ij.dat``
     - 交換結合パラメータ J\_ij データファイル
     - text
   * - 補助出力
     - ``QuloudJob_JXC_Jij_*.agr``
     - J\_ij グラフファイル（元素名がファイル名に入る）
     - text
   * - 構造
     - ``rsdft.atom``
     - 原子構造ファイル
     - text
   * - ログ
     - ``buildbot.log``
     - ビルドボットログ
     - text
   * - ログ
     - ``sprkkr_jxc.exec.log``
     - kkrgenMPI の標準出力（キュリー温度の抽出元）
     - text

