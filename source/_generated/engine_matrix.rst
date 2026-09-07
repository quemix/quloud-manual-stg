.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 789272e8ff4737a6a8aaf0d461f6b71abb84fb54 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T07:21:28Z
.. マスタ同期日時: 2026-09-07T06:19:19Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 20 12 24 16 14 8

   * - 計算エンジン
     - エンジンコード
     - 機能
     - 機能コード
     - 区分
     - 画面表示
   * - ASE-MD
     - ``asemd``
     - 格子定数最適化
     - ``lattice_opt``
     - 機械学習MD
     - ○
   * - ASE-MD
     - ``asemd``
     - 構造最適化
     - ``geometry_opt``
     - 機械学習MD
     - ○
   * - ASE-MD
     - ``asemd``
     - 機械学習ポテンシャル MD
     - ``ml_md``
     - 機械学習MD
     - ○
   * - ASE-MD
     - ``asemd``
     - NEB（Nudged Elastic Band）
     - ``neb``
     - 機械学習MD
     - ○
   * - DFT-1/2
     - ``dft12``
     - DFT-1/2 擬ポテンシャル生成（UPF）
     - ``dft12_upf``
     - 第一原理計算（擬ポテンシャル）
     - ○
   * - FLARE
     - ``flare``
     - 機械学習ポテンシャル MD
     - ``ml_md``
     - 機械学習MD
     - ○
   * - GROMACS
     - ``gromacs``
     - 構造最適化
     - ``geometry_opt``
     - 古典MD・分子力学
     - ○
   * - GROMACS
     - ``gromacs``
     - 古典分子動力学
     - ``classical_md``
     - 古典MD・分子力学
     - ○
   * - HybMD
     - ``hybmd``
     - 機械学習ポテンシャル MD
     - ``ml_md``
     - 第一原理／機械学習ハイブリッドMD
     - ○
   * - HybMD
     - ``hybmd``
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 第一原理／機械学習ハイブリッドMD
     - ○
   * - LAMMPS
     - ``lammps``
     - 構造最適化
     - ``geometry_opt``
     - 古典MD
     - ○
   * - LAMMPS
     - ``lammps``
     - 古典分子動力学
     - ``classical_md``
     - 古典MD
     - ○
   * - Quloud-Mag
     - ``mag``
     - モンテカルロ磁性計算
     - ``monte_carlo_mag``
     - 磁性計算
     - ○
   * - Quloud-Mag
     - ``mag``
     - LLG ダイナミクス
     - ``llg_dynamics``
     - 磁性計算
     - ○
   * - OpenMX
     - ``openmx``
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - 構造最適化
     - ``geometry_opt``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - 格子定数最適化
     - ``lattice_opt``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - 電子バンド構造
     - ``band_structure``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - 状態密度計算（DOS）
     - ``dos``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - 分子動力学
     - ``molecular_dynamics``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - NEB（Nudged Elastic Band）
     - ``neb``
     - 第一原理計算
     - ○
   * - OpenMX
     - ``openmx``
     - 交換結合パラメータ
     - ``exchange_coupling``
     - 第一原理計算
     - ○
   * - Psi4
     - ``psi4``
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 量子化学計算
     - ○
   * - Psi4
     - ``psi4``
     - 構造最適化
     - ``geometry_opt``
     - 量子化学計算
     - ○
   * - Psi4
     - ``psi4``
     - 分子振動解析
     - ``frequency``
     - 量子化学計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 構造最適化
     - ``geometry_opt``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 格子定数最適化
     - ``lattice_opt``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 電子バンド構造
     - ``band_structure``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 状態密度計算（DOS）
     - ``dos``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 投影状態密度（PDOS）
     - ``projected_dos``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - NEB（Nudged Elastic Band）
     - ``neb``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - フォノン計算
     - ``phonon``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - X線吸収スペクトル（XSpectra）
     - ``xspectra``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - X線吸収スペクトル用 SCF
     - ``xas_scf``
     - 第一原理計算
     - ×
   * - Quantum ESPRESSO
     - ``qe``
     - 固定ポテンシャル電子状態計算
     - ``nscf``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 固定ポテンシャル電子状態計算（バンド）
     - ``bands``
     - 第一原理計算
     - ○
   * - Quantum ESPRESSO
     - ``qe``
     - 力定数計算（q2r）
     - ``q2r``
     - 第一原理計算
     - ×
   * - Quantum ESPRESSO
     - ``qe``
     - フォノンバンド分散（matdyn）
     - ``matdyn_disp``
     - 第一原理計算
     - ×
   * - Quantum ESPRESSO
     - ``qe``
     - フォノン状態密度（matdyn）
     - ``matdyn_dos``
     - 第一原理計算
     - ×
   * - RadonPy
     - ``radonpy``
     - QM構造最適化 / RESP電荷
     - ``qm_resp``
     - 高分子物性計算
     - ○
   * - RadonPy
     - ``radonpy``
     - 高分子平衡化MD
     - ``polymer_equilibration``
     - 高分子物性計算
     - ○
   * - RadonPy
     - ``radonpy``
     - 溶解度パラメータ
     - ``polymer_sp``
     - 高分子物性計算
     - ○
   * - RadonPy
     - ``radonpy``
     - ガラス転移温度
     - ``polymer_tg``
     - 高分子物性計算
     - ○
   * - RadonPy
     - ``radonpy``
     - 熱伝導率
     - ``polymer_tc``
     - 高分子物性計算
     - ○
   * - RadonPy
     - ``radonpy``
     - ヤング率（機械特性）
     - ``polymer_elong``
     - 高分子物性計算
     - ○
   * - RadonPy
     - ``radonpy``
     - 複素誘電率
     - ``polymer_dielectric``
     - 高分子物性計算
     - ○
   * - RSDFT
     - ``rsdft``
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 第一原理計算
     - ○
   * - RSDFT
     - ``rsdft``
     - 構造最適化
     - ``geometry_opt``
     - 第一原理計算
     - ○
   * - RSDFT
     - ``rsdft``
     - 格子定数最適化
     - ``lattice_opt``
     - 第一原理計算
     - ○
   * - RSDFT
     - ``rsdft``
     - 電子バンド構造
     - ``band_structure``
     - 第一原理計算
     - ○
   * - RSDFT
     - ``rsdft``
     - 状態密度計算（DOS）
     - ``dos``
     - 第一原理計算
     - ○
   * - RSDFT
     - ``rsdft``
     - 分子動力学
     - ``molecular_dynamics``
     - 第一原理計算
     - ○
   * - SPRKKR
     - ``sprkkr``
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 磁性計算
     - ○
   * - SPRKKR
     - ``sprkkr``
     - 交換結合パラメータ
     - ``exchange_coupling``
     - 磁性計算
     - ○
