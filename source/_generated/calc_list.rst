.. これは tools/gen_master_tables.py が生成したファイルです。手で編集しないでください。
.. 生成元コミット: 1921e3ff124454d0c40f97e602857af9ceb09fe6 (dev_v700_ji)
.. マスタ取得日時（dump 実行）: 2026-09-08T01:28:28Z
.. マスタ同期日時: 2026-09-07T16:54:23Z
.. 再生成: make dump && make generate

.. list-table::
   :header-rows: 1
   :widths: 20 24 16 40

   * - 計算ソフト
     - 計算機能
     - 機能コード
     - 実行されるステップ
   * - Quantum ESPRESSO
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 自己無撞着電子状態計算（SCF）
   * - Quantum ESPRESSO
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - Quantum ESPRESSO
     - 格子定数最適化
     - ``lattice_opt``
     - 格子定数最適化
   * - Quantum ESPRESSO
     - 固定ポテンシャル電子状態計算
     - ``nscf``
     - 自己無撞着電子状態計算（SCF） → 固定ポテンシャル電子状態計算
   * - Quantum ESPRESSO
     - 電子バンド構造
     - ``band_structure``
     - 自己無撞着電子状態計算（SCF） → 固定ポテンシャル電子状態計算（バンド） → 電子バンド構造
   * - Quantum ESPRESSO
     - NEB（Nudged Elastic Band）
     - ``neb``
     - NEB（Nudged Elastic Band）
   * - DFT-1/2
     - DFT-1/2 擬ポテンシャル生成（UPF）
     - ``dft12_upf``
     - DFT-1/2 擬ポテンシャル生成（UPF）
   * - Quantum ESPRESSO
     - 状態密度計算（DOS）
     - ``dos``
     - 自己無撞着電子状態計算（SCF） → 固定ポテンシャル電子状態計算 → 状態密度計算（DOS）
   * - Quantum ESPRESSO
     - 投影状態密度（PDOS）
     - ``projected_dos``
     - 自己無撞着電子状態計算（SCF） → 固定ポテンシャル電子状態計算 → 投影状態密度（PDOS）
   * - Quantum ESPRESSO
     - フォノンバンド分散（matdyn）
     - ``matdyn_disp``
     - 構造最適化 → フォノン計算 → 力定数計算（q2r） → フォノンバンド分散（matdyn）
   * - Quantum ESPRESSO
     - フォノン状態密度（matdyn）
     - ``matdyn_dos``
     - 構造最適化 → フォノン計算 → 力定数計算（q2r） → フォノン状態密度（matdyn）
   * - Quantum ESPRESSO
     - X線吸収スペクトル（XSpectra）
     - ``xspectra``
     - X線吸収スペクトル用 SCF → X線吸収スペクトル（XSpectra）
   * - OpenMX
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 自己無撞着電子状態計算（SCF）
   * - OpenMX
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - OpenMX
     - 格子定数最適化
     - ``lattice_opt``
     - 格子定数最適化
   * - OpenMX
     - 電子バンド構造
     - ``band_structure``
     - 電子バンド構造
   * - OpenMX
     - 状態密度計算（DOS）
     - ``dos``
     - 状態密度計算（DOS）
   * - OpenMX
     - 第一原理分子動力学
     - ``fp_md``
     - 分子動力学
   * - OpenMX
     - NEB（Nudged Elastic Band）
     - ``neb``
     - NEB（Nudged Elastic Band）
   * - OpenMX
     - 交換結合パラメータ
     - ``exchange_coupling``
     - 自己無撞着電子状態計算（SCF） → 交換結合パラメータ
   * - RSDFT
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 自己無撞着電子状態計算（SCF）
   * - RSDFT
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - RSDFT
     - 格子定数最適化
     - ``lattice_opt``
     - 格子定数最適化
   * - RSDFT
     - 電子バンド構造
     - ``band_structure``
     - 電子バンド構造
   * - RSDFT
     - 状態密度計算（DOS）
     - ``dos``
     - 状態密度計算（DOS）
   * - RSDFT
     - 第一原理分子動力学
     - ``fp_md``
     - 分子動力学
   * - ASE-MD
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - ASE-MD
     - 格子定数最適化
     - ``lattice_opt``
     - 格子定数最適化
   * - ASE-MD
     - 機械学習ポテンシャル MD
     - ``ml_md``
     - 機械学習ポテンシャル MD
   * - ASE-MD
     - NEB（Nudged Elastic Band）
     - ``neb``
     - NEB（Nudged Elastic Band）
   * - LAMMPS
     - 古典分子動力学
     - ``classical_md``
     - 古典分子動力学
   * - LAMMPS
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - FLARE + Quantum ESPRESSO
     - On-the-fly 機械学習ポテンシャル生成
     - ``ml_ff``
     - 機械学習ポテンシャル MD → 自己無撞着電子状態計算（SCF）
   * - Quloud-Mag
     - LLG ダイナミクス
     - ``llg_dynamics``
     - LLG ダイナミクス
   * - Quloud-Mag
     - モンテカルロ磁性計算
     - ``monte_carlo_mag``
     - モンテカルロ磁性計算
   * - SPRKKR
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 自己無撞着電子状態計算（SCF）
   * - SPRKKR
     - 交換結合パラメータ
     - ``exchange_coupling``
     - 交換結合パラメータ
   * - GROMACS
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - GROMACS
     - 古典分子動力学
     - ``classical_md``
     - 古典分子動力学
   * - HybMD
     - 機械学習ポテンシャル MD
     - ``ml_md``
     - 機械学習ポテンシャル MD → 自己無撞着電子状態計算（SCF）
   * - RadonPy
     - 高分子密度
     - ``polymer_density``
     - QM構造最適化 / RESP電荷 → 高分子平衡化MD
   * - RadonPy
     - 溶解度パラメータ
     - ``polymer_sp``
     - QM構造最適化 / RESP電荷 → 高分子平衡化MD → 溶解度パラメータ
   * - RadonPy
     - ガラス転移温度
     - ``polymer_tg``
     - QM構造最適化 / RESP電荷 → 高分子平衡化MD → ガラス転移温度
   * - RadonPy
     - 熱伝導率
     - ``polymer_tc``
     - QM構造最適化 / RESP電荷 → 高分子平衡化MD → 熱伝導率
   * - RadonPy
     - ヤング率（機械特性）
     - ``polymer_elong``
     - QM構造最適化 / RESP電荷 → 高分子平衡化MD → ヤング率（機械特性）
   * - RadonPy
     - 複素誘電率
     - ``polymer_dielectric``
     - QM構造最適化 / RESP電荷 → 高分子平衡化MD → 複素誘電率
   * - Psi4
     - 自己無撞着電子状態計算（SCF）
     - ``scf``
     - 自己無撞着電子状態計算（SCF）
   * - Psi4
     - 構造最適化
     - ``geometry_opt``
     - 構造最適化
   * - Psi4
     - 分子振動解析
     - ``frequency``
     - 構造最適化 → 分子振動解析
