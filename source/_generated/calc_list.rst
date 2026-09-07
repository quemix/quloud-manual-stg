.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 789272e8ff4737a6a8aaf0d461f6b71abb84fb54 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-07T07:21:28Z
.. マスタ同期日時: 2026-09-07T06:19:19Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 40 40 20

   * - 名称
     - 英語表記
     - 機能コード
   * - 自己無撞着電子状態計算（QE）
     - Self-consistent Electronic Structure Calculation (QE)
     - ``scf``
   * - 構造最適化（QE）
     - Geometry Optimization (QE)
     - ``geometry_opt``
   * - 格子定数最適化（QE）
     - Lattice Optimization (QE)
     - ``lattice_opt``
   * - 固定ポテンシャル電子状態計算（QE）
     - Fixed-Potential Electronic Structure (QE)
     - ``nscf``
   * - 電子バンド
     - Electronic Band Structure
     - ``band_structure``
   * - NEB（QE）
     - NEB (QE)
     - ``neb``
   * - DFT-1/2 擬ポテンシャル生成（QE）
     - DFT-1/2 Pseudopotential Generation (QE)
     - ``dft12_upf``
   * - 電子状態密度
     - Electronic Density of States
     - ``dos``
   * - 投影状態密度
     - Projected Density of States
     - ``projected_dos``
   * - フォノンバンド
     - Phonon Band Structure
     - ``matdyn_disp``
   * - フォノン状態密度
     - Phonon Density of States
     - ``matdyn_dos``
   * - X線吸収スペクトル
     - X-ray Absorption Spectrum
     - ``xspectra``
   * - 自己無撞着電子状態計算（OpenMX）
     - Self-consistent Electronic Structure Calculation (OpenMX)
     - ``scf``
   * - 構造最適化（OpenMX）
     - Geometry Optimization (OpenMX)
     - ``geometry_opt``
   * - 格子定数最適化（OpenMX）
     - Lattice Optimization (OpenMX)
     - ``lattice_opt``
   * - バンド計算（OpenMX）
     - Band Structure (OpenMX)
     - ``band_structure``
   * - 状態密度計算（OpenMX）
     - Density of States (OpenMX)
     - ``dos``
   * - 第一原理分子動力学（OpenMX）
     - First-Principles MD (OpenMX)
     - ``fp_md``
   * - NEB（OpenMX）
     - NEB (OpenMX)
     - ``neb``
   * - 交換結合定数（OpenMX）
     - Exchange Coupling Constants
     - ``exchange_coupling``
   * - 自己無撞着電子状態計算（RSDFT）
     - Self-consistent Electronic Structure Calculation (RSDFT)
     - ``scf``
   * - 構造最適化（RSDFT）
     - Geometry Optimization (RSDFT)
     - ``geometry_opt``
   * - 格子定数最適化（RSDFT）
     - Lattice Optimization (RSDFT)
     - ``lattice_opt``
   * - バンド計算（RSDFT）
     - Band Structure (RSDFT)
     - ``band_structure``
   * - 状態密度計算（RSDFT）
     - Density of States (RSDFT)
     - ``dos``
   * - 第一原理分子動力学（RSDFT）
     - First-Principles MD (RSDFT)
     - ``fp_md``
   * - 構造最適化（ASE-MD）
     - Geometry Optimization (ASE-MD)
     - ``geometry_opt``
   * - 格子最適化（ASE-MD）
     - Lattice Optimization (ASE-MD)
     - ``lattice_opt``
   * - 機械学習ポテンシャル MD（ASE-MD）
     - Machine-Learning Potential MD (ASE-MD)
     - ``ml_md``
   * - NEB（ASE-MD）
     - NEB (ASE-MD)
     - ``neb``
   * - 古典分子動力学（LAMMPS）
     - Classical MD (LAMMPS)
     - ``classical_md``
   * - 構造最適化（LAMMPS）
     - Geometry Optimization (LAMMPS)
     - ``geometry_opt``
   * - On-the-fly 機械学習ポテンシャル生成（FLARE）
     - On-the-fly Machine-Learning Potential Generation (FLARE)
     - ``ml_ff``
   * - LLG ダイナミクス（Quloud-Mag）
     - LLG Dynamics (Quloud-Mag)
     - ``llg_dynamics``
   * - モンテカルロ磁性計算（Quloud-Mag）
     - Magnetic Monte Carlo (Quloud-Mag)
     - ``monte_carlo_mag``
   * - 自己無撞着電子状態計算（SPRKKR）
     - Self-consistent Electronic Structure Calculation (SPRKKR)
     - ``scf``
   * - 交換結合パラメータ（SPRKKR）
     - Exchange Coupling Parameters (SPRKKR)
     - ``exchange_coupling``
   * - エネルギー最小化（GROMACS）
     - Energy Minimization (GROMACS)
     - ``geometry_opt``
   * - 古典分子動力学（GROMACS）
     - Classical Molecular Dynamics (GROMACS)
     - ``classical_md``
   * - HybMD
     - HybMD
     - ``ml_md``
   * - 高分子密度計算（RadonPy）
     - Polymer Density Calculation (RadonPy)
     - ``polymer_density``
   * - 高分子溶解度パラメータ（RadonPy）
     - Polymer Solubility Parameter (RadonPy)
     - ``polymer_sp``
   * - 高分子ガラス転移温度（RadonPy）
     - Polymer Glass Transition Temperature (RadonPy)
     - ``polymer_tg``
   * - 高分子熱伝導率（RadonPy）
     - Polymer Thermal Conductivity (RadonPy)
     - ``polymer_tc``
   * - 高分子ヤング率（RadonPy）
     - Polymer Young's Modulus (RadonPy)
     - ``polymer_elong``
   * - 高分子複素誘電率（RadonPy）
     - Polymer Complex Dielectric Constant (RadonPy)
     - ``polymer_dielectric``
   * - 単一点エネルギー計算（Psi4）
     - Single-Point Energy Calculation (Psi4)
     - ``scf``
   * - 構造最適化（Psi4）
     - Geometry Optimization (Psi4)
     - ``geometry_opt``
   * - 振動数解析（Psi4）
     - Frequency Analysis (Psi4)
     - ``frequency``
