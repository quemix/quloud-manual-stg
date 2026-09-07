==============================
入出力ファイルとログ
==============================

ここでは、Job の入出力ファイルと計算ログについて、ソフトウェアごとに説明します。入出力ファイルの確認方法は ７章３節、計算ログの確認方法は７章２節をご参照ください。

|
|

--------------------------------------------------------------
Quantum ESPRESSO
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.scf.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SCF 計算を行うためのファイルです。例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

|

**Single-Point SCF、Electron Band Structure、Electron DOS の場合**

::

    &control
     calculation = 'scf'
     prefix = 'QuloudJob'
     tstress = .true.
     tprnfor = .true.
     pseudo_dir = './'
     outdir = './work'
     verbosity = 'high'
    /
    &system
     nat = 5
     ntyp = 3
     ecutwfc = 52.0
     ecutrho = 575.0
     ibrav = 0
     tot_charge = 0
     occupations = 'smearing'
     smearing = 'gauss'
     degauss = 0.01
     nspin = 1
    /
    &electrons
     mixing_beta = 0.7
     conv_thr = 1e-10
     electron_maxstep = 100
    /
    ATOMIC_SPECIES
    Ba 137.327 Ba.pbe-spn-rrkjus_psl.1.0.0.UPF
    Ti 47.867 Ti.pbe-spn-rrkjus_psl.1.0.0.UPF
    O 15.999 O.pbe-nl-rrkjus_psl.1.0.0.UPF
    ATOMIC_POSITIONS {crystal}
    Ba 0.5 0.5 0.58254146
    Ti 0.0 0.0 0.1000427
    O 0.0 0.5 0.06422054
    O 0.5 0.0 0.06422054
    O 0.0 0.0 0.54897175
    CELL_PARAMETERS {angstrom}
    3.99037921 0.0 2.443402563455322e-16
    6.417019188399763e-16 3.99037921 2.443402563455322e-16
    0.0 0.0 4.10265539
    K_POINTS {automatic}
    4 4 4 0 0 0

入力パラメータの詳細は以下の通りです。

-	&control

    -	calculation：計算内容を設定します。デフォルトでは 'scf' となっています。
    -	prefix：入出力ファイルの先頭につける文字列を設定します。デフォルトでは 'QuloudJob' となっています。
    -	tstress： .true. の場合、圧力が計算されます。デフォルトでは .true. となっています。
    -	tprnfor： .true. の場合、力が計算されます。デフォルトでは .true. となっています。
    -	pseudo_dir：擬ポテンシャルファイルが置かれているディレクトリを入力します。
    -	outdir：入出力ファイルやテンポラリを置くディレクトリを指定します。
    -	verbosity：ログ出力の量を設定します。デフォルトでは 'high' となっています。

-	&system

    -	nat：モデルに含まれる原子の総数が表示されます。
    -	ntyp：モデルに含まれる原子の種類の総数が表示されます。
    -	ecutwfc：波動関数のエネルギーカットオフを設定します（単位は Ry）。
    -	ecutrho：電荷密度とポテンシャルのエネルギーカットオフを設定します（単位は Ry）。デフォルトでは ecutwfc の４倍となっています。
    -	ibrav：ブラべ格子の種類を指定します。0 の場合、後述する CELL_PARAMETERS で格子ベクトルを具体的に記述する必要があります。デフォルトでは 0 となっています。
    -	tot_charge：モデル全体の電荷量を設定します。電気的に中性の場合は 0、電子が１つ抜ける場合は +1、電子が１つ追加される場合は -1 とします。デフォルトでは 0 となっています。
    -	occupations：電子の状態数を計算する方法を設定します。デフォルトでは 'smearing' となっています。
    -	smearing：平滑化法の種類を指定します。デフォルトでは 'gauss' となっています。
    -	degauss：ガウシアン平滑化関数の広がりを指定します（単位は Ry）。デフォルトでは 0.01 となっています。
    -	nspin：スピン軌道相互作用を考慮するかどうか設定します。デフォルトでは 1（考慮しない）となっています。

-	&electrons

    -	mixing_beta：SCF 計算で、直前の計算で出てきた電子密度を、次の計算でどの割合で混ぜるかを設定します。デフォルトでは 0.7 となっています。
    -	conv_thr：SCF 計算で、エネルギー誤差がこの数値より小さくなったら、収束したと判定されます。デフォルトでは 1e-10 Ry となっています。
    -	electron_maxstep：SCF 計算での最大繰り返し回数を設定します。デフォルトでは 100 となっています。

-	ATOMIC_SPECIES：元素記号、質量数、擬ポテンシャルファイル名を記載します。

-	ATOMIC_POSITIONS：原子の位置を記載します。デフォルトでは、格子ベクトルを基準とした相対座標で表示されています。

-   CELL_PARAMETERS：前述した ibrav が 0 の場合、ここで格子ベクトルを具体的に記載します。デフォルトではオングストローム（Å）単位で表示されています。

-   K_POINTS：デフォルトでは k 点グリッドが自動生成されます。左の３つの数字は各方向の k 点グリッドの数を表しています。また、右の３つの数字はグリッドオフセットに関する情報で、デフォルトでは 0（オフセットなし）となっています。

|

**Atomic Structure Opt. の場合**

::
    
    &control
     calculation = 'relax'
     prefix = 'QuloudJob'
     tstress = .true.
     tprnfor = .true.
     pseudo_dir = './'
     outdir = './work'
     verbosity = 'high'
     etot_conv_thr = 0.00001
     forc_conv_thr = 0.0001
     nstep = 50
    /
    &system
     nat = 5
     ntyp = 3
     ecutwfc = 52.0
     ecutrho = 575.0
     ibrav = 0
     tot_charge = 0
     occupations = 'smearing'
     smearing = 'gauss'
     degauss = 0.01
     nspin = 1
    /
    &electrons
     mixing_beta = 0.7
     conv_thr = 1e-10
     electron_maxstep = 100
    /
    &ions
    /
    &cell
    /
    ATOMIC_SPECIES
    Ba 137.327 Ba.pbe-spn-rrkjus_psl.1.0.0.UPF
    Ti 47.867 Ti.pbe-spn-rrkjus_psl.1.0.0.UPF
    O 15.999 O.pbe-nl-rrkjus_psl.1.0.0.UPF
    ATOMIC_POSITIONS {crystal}
    Ba 0.5 0.5 0.58254146
    Ti 0.0 0.0 0.1000427
    O 0.0 0.5 0.06422054
    O 0.5 0.0 0.06422054
    O 0.0 0.0 0.54897175
    CELL_PARAMETERS {angstrom}
    3.99037921 0.0 2.443402563455322e-16
    6.417019188399763e-16 3.99037921 2.443402563455322e-16
    0.0 0.0 4.10265539
    K_POINTS {automatic}
    4 4 4 0 0 0

Atomic Structure Opt. では、以下のように設定が変更・追加されています。

-	&control

    -   calculation：計算内容を設定します。デフォルトでは 'relax' となっています。
    -	etot_conv_thr：（原子構造または格子定数の）最適化計算で、エネルギー値の変動がこの数値より小さくなったら、収束したと判定されます。デフォルトでは 0.00001 Ry となっています。
    -   forc_conv_thr：最適化計算で、力の値の変動がこの数値より小さくなったら、収束したと判定されます。デフォルトでは 0.0001 Ry/Bohr となっています。

    なお、上記２つの条件がともに満たされた場合にのみ、計算は収束したと判定されます。

    -   nstep：最適化計算のステップ数を設定します。デフォルトでは 50 となっています。

|

**Lattice Opt. の場合**

::

    &control
     calculation = 'vc-relax'
     prefix = 'QuloudJob'
     tstress = .true.
     tprnfor = .true.
     pseudo_dir = './'
     outdir = './work'
     verbosity = 'high'
     etot_conv_thr = 0.00001
     forc_conv_thr = 0.0001
     nstep = 50
    /
    &system
     nat = 5
     ntyp = 3
     ecutwfc = 52.0
     ecutrho = 575.0
     ibrav = 0
     tot_charge = 0
     occupations = 'smearing'
     smearing = 'gauss'
     degauss = 0.01
     nspin = 1
    /
    &electrons
     mixing_beta = 0.7
     conv_thr = 1e-10
     electron_maxstep = 100
    /
    &ions
    /
    &cell
     press = 0.0
     press_conv_thr = 0.5
    /
    ATOMIC_SPECIES
    Ba 137.327 Ba.pbe-spn-rrkjus_psl.1.0.0.UPF
    Ti 47.867 Ti.pbe-spn-rrkjus_psl.1.0.0.UPF
    O 15.999 O.pbe-nl-rrkjus_psl.1.0.0.UPF
    ATOMIC_POSITIONS {crystal}
    Ba 0.5 0.5 0.58254146
    Ti 0.0 0.0 0.1000427
    O 0.0 0.5 0.06422054
    O 0.5 0.0 0.06422054
    O 0.0 0.0 0.54897175
    CELL_PARAMETERS {angstrom}
    3.99037921 0.0 2.443402563455322e-16
    6.417019188399763e-16 3.99037921 2.443402563455322e-16
    0.0 0.0 4.10265539
    K_POINTS {automatic}
    4 4 4 0 0 0

Lattice Opt. では、以下のように設定が変更・追加されています。

-	&control

    -   calculation：計算内容を設定します。デフォルトでは 'vc-relax' となっています。
    -	etot_conv_thr：（原子構造または格子定数の）最適化計算で、エネルギー値の変動がこの数値より小さくなったら、収束したと判定されます。デフォルトでは 0.00001 Ry となっています。
    -   forc_conv_thr：最適化計算で、力の値の変動がこの数値より小さくなったら、収束したと判定されます。デフォルトでは 0.0001 Ry/Bohr となっています。

    なお、上記２つの条件がともに満たされた場合にのみ、計算は収束したと判定されます。

    -   nstep：最適化計算のステップ数を設定します。デフォルトでは 50 となっています。

-   &cell

    -   press：格子定数の最適化計算で、モデルに加わる圧力の目標値を設定します。デフォルトでは 0.0 Kbar となっています。
    -   press_conv_thr：格子定数の最適化計算で、圧力の値の変動がこの数値より小さくなったら、収束したと判定されます。デフォルトでは 0.5 Kbar となっています。

        なお、上記２つの条件（etot_conv_thr と forc_conv_thr）も併せて満たされた場合にのみ、計算は収束したと判定されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.nscf.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SCF 計算により求められたポテンシャルを用いて、電子バンド計算や電子状態密度計算を行うためのファイルです。例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

|

**Electron Band Structure の場合**

::

    &control
     calculation = 'bands'
     prefix = 'QuloudJob'
     tstress = .true.
     tprnfor = .true.
     pseudo_dir = './'
     outdir = './work'
     verbosity = 'high'
    /
    &system
     nat = 5
     ntyp = 3
     nosym = .true.
     ecutwfc = 52.0
     ecutrho = 575.0
     ibrav = 0
     tot_charge = 0
     occupations = 'smearing'
     smearing = 'gauss'
     degauss = 0.01
     nspin = 1
    /
    &electrons
     mixing_beta = 0.7
     conv_thr = 1e-10
     electron_maxstep = 100
    /
    ATOMIC_SPECIES
    Ba 137.327 Ba.pbe-spn-rrkjus_psl.1.0.0.UPF
    Ti 47.867 Ti.pbe-spn-rrkjus_psl.1.0.0.UPF
    O 15.999 O.pbe-nl-rrkjus_psl.1.0.0.UPF
    ATOMIC_POSITIONS {crystal}
    Ba 0.5 0.5 0.58254146
    Ti 0.0 0.0 0.1000427
    O 0.0 0.5 0.06422054
    O 0.5 0.0 0.06422054
    O 0.0 0.0 0.54897175
    CELL_PARAMETERS {angstrom}
    3.99037921 0.0 2.443402563455322e-16
    6.417019188399763e-16 3.99037921 2.443402563455322e-16
    0.0 0.0 4.10265539
    K_POINTS {crystal_b}
    12 #auto
    0.0 0.0 0.0 20 !G
    0.0 0.5 0.0 20 !X
    0.5 0.5 0.0 20 !M
    0.0 0.0 0.0 20 !G
    0.0 0.0 0.5 20 !Z
    0.0 0.5 0.5 20 !R
    0.5 0.5 0.5 20 !A
    0.0 0.0 0.5 20 !Z
    0.0 0.5 0.0 20 !X
    0.0 0.5 0.5 20 !R
    0.5 0.5 0.0 20 !M
    0.5 0.5 0.5 20 !A
    #KPT  G  0.0 0.0 0.0 /
    #KPT  A  0.5 0.5 0.5 /
    #KPT  M  0.5 0.5 0.0 /
    #KPT  R  0.0 0.5 0.5 /
    #KPT  X  0.0 0.5 0.0 /
    #KPT  Z  0.0 0.0 0.5 /

"QuloudJob.scf.in" と異なる点は以下の通りです。

-	&control

    -	calculation：計算内容を設定します。デフォルトでは 'bands' となっています。

-	&system

    -	nosym：.true. の場合、k 点の対称化は行われず、入力ファイルの k 点リストがそのまま用いられます。また、電荷密度の対称化も行われません。デフォルトでは .true. となっています。

-   K_POINTS：電子バンドを計算する際の k 点の経路を設定します。上の例では G → X → M → G → Z → R → A → Z → X → R → M → A の経路に沿って電子バンド計算が行われます。各 k 点の座標は、逆格子ベクトルを基準とした相対座標で表示されています。なお、k 点座標の右の数字は、次の k 点とを結ぶ線上で何点サンプリングするかを表します。例えば最初の G 点の場合、座標の右の数字は 20 なので、G → X 間の k 点サンプリング数は 20 となります。

|

**Electron DOS の場合**

::

    &control
     calculation = 'nscf'
     prefix = 'QuloudJob'
     tstress = .true.
     tprnfor = .true.
     pseudo_dir = './'
     outdir = './work'
     verbosity = 'high'
    /
    &system
     nat = 5
     ntyp = 3
     ecutwfc = 52.0
     ecutrho = 575.0
     ibrav = 0
     tot_charge = 0
     occupations = 'tetrahedra'
     nspin = 1
    /
    &electrons
     mixing_beta = 0.7
     conv_thr = 1e-10
     electron_maxstep = 100
    /
    ATOMIC_SPECIES
    Ba 137.327 Ba.pbe-spn-rrkjus_psl.1.0.0.UPF
    Ti 47.867 Ti.pbe-spn-rrkjus_psl.1.0.0.UPF
    O 15.999 O.pbe-nl-rrkjus_psl.1.0.0.UPF
    ATOMIC_POSITIONS {crystal}
    Ba 0.5 0.5 0.58254146
    Ti 0.0 0.0 0.1000427
    O 0.0 0.5 0.06422054
    O 0.5 0.0 0.06422054
    O 0.0 0.0 0.54897175
    CELL_PARAMETERS {angstrom}
    3.99037921 0.0 2.443402563455322e-16
    6.417019188399763e-16 3.99037921 2.443402563455322e-16
    0.0 0.0 4.10265539
    K_POINTS {automatic}
    4 4 4 0 0 0

"QuloudJob.scf.in" と異なる点は以下の通りです。

-	&control

    -	calculation：計算内容を設定します。デフォルトでは 'nscf' となっています。

-	&system

    -	occupations：電子の状態数を計算する方法を設定します。デフォルトでは 'tetrahedra' となっています。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.bands.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

電子バンド計算（Electron Band Structure）に用いるファイルです。

::

    &bands
     outdir = './work'
     prefix='QuloudJob'
     filband='QuloudJob.bands'
    /

入力パラメータの詳細は以下の通りです。

-	&bands

    -	outdir：入出力ファイルやテンポラリを置くディレクトリを指定します。
    -	prefix：入出力ファイルの先頭につける文字列を設定します。デフォルトでは 'QuloudJob' となっています。
    -	filband：電子バンド計算の結果を出力するファイルの名前を指定します。デフォルトでは 'QuloudJob.bands' となっています。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.dos.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

電子状態密度計算（Electron DOS）に用いるファイルです。

::

    &dos
     outdir = './work'
     prefix='QuloudJob'
     fildos='QuloudJob.dos'
    /

入力パラメータの詳細は以下の通りです。

-	&dos

    -	outdir：入出力ファイルやテンポラリを置くディレクトリを指定します。
    -	prefix：入出力ファイルの先頭につける文字列を設定します。デフォルトでは 'QuloudJob' となっています。
    -	fildos：電子状態密度計算の結果を出力するファイルの名前を指定します。デフォルトでは 'QuloudJob.dos' となっています。

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
neb.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NEB法によるエネルギー障壁計算の入力ファイルです。

::

    BEGIN
    BEGIN_PATH_INPUT
    Si+H1

    &PATH
    string_method = 'neb'
    restart_mode = 'from_scratch'
    nstep_path = 50
    num_of_images = 5
    opt_scheme = 'quick-min'
    CI_scheme = 'no-CI'
    first_last_opt = .false.
    minimum_image = .false.
    temp_req = 0
    ds = 1
    k_min = 0.1
    k_max = 0.1
    path_thr = 0.05
    use_masses = .false.
    use_freezing = .false.
    lfcp = .false.
    /
    END_PATH_INPUT

    BEGIN_ENGINE_INPUT
    &control
    calculation = 'scf'
    prefix = 'QuloudJob'
    tstress = .true.
    tprnfor = .true.
    pseudo_dir = './'
    outdir = './work'
    verbosity = 'high'
    /
    &system
    nat = 9
    ntyp = 2
    ecutwfc = 46.0
    ecutrho = 221.0
    ibrav = 0
    tot_charge = 0
    occupations = 'smearing'
    smearing = 'gauss'
    degauss = 0.01
    nspin = 1
    /
    &electrons
    mixing_beta = 0.7
    conv_thr = 1e-10
    electron_maxstep = 100
    /
    ATOMIC_SPECIES
    Si 28.086 Si.pbe-nl-rrkjus_psl.1.0.0.UPF
    H 1.008 H.pbe-rrkjus_psl.1.0.0.UPF
    CELL_PARAMETERS {angstrom}
    5.44370222 0.0 3.33330624961717e-16
    8.754140838076987e-16 5.44370222 3.33330624961717e-16
    0.0 0.0 5.44370222
    K_POINTS {automatic}
    1 1 1 0 0 0
    BEGIN_POSITIONS
    FIRST_IMAGE
    ATOMIC_POSITIONS {crystal}
    Si 0.5000000000000000 0.5000000000000000 0.5000000000000000
    Si 0.7500000000000000 0.2500000000000000 0.2500000000000000
    Si 0.5000000000000000 0.0000000000000000 0.0000000000000000
    Si 0.7500000000000000 0.7500000000000000 0.7500000000000000
    Si 0.0000000000000000 0.5000000000000000 0.0000000000000000
    Si 0.2500000000000000 0.2500000000000000 0.7500000000000000
    Si 0.0000000000000000 0.0000000000000000 0.5000000000000000
    Si 0.2500000000000000 0.7500000000000000 0.2500000000000000
    H 0.7277860000000000 0.5000000000000000 0.5012250000000000
    LAST_IMAGE
    ATOMIC_POSITIONS {crystal}
    Si 0.5000000000000000 0.5000000000000000 0.5000000000000000
    Si 0.7500000000000000 0.2500000000000000 0.2500000000000000
    Si 0.5000000000000000 0.0000000000000000 0.0000000000000000
    Si 0.7500000000000000 0.7500000000000000 0.7500000000000000
    Si 0.0000000000000000 0.5000000000000000 0.0000000000000000
    Si 0.2500000000000000 0.2500000000000000 0.7500000000000000
    Si 0.0000000000000000 0.0000000000000000 0.5000000000000000
    Si 0.2500000000000000 0.7500000000000000 0.2500000000000000
    H 0.2428220000000000 0.5000000000000000 0.5012250000000000
    END_POSITIONS
    END_ENGINE_INPUT
    END

    &dos
     outdir = './work'
     prefix='QuloudJob'
     fildos='QuloudJob.dos'
    /

主要な入力パラメータは以下の通りです。

-	BEGIN_PATH_INPUT :math:`\sim` END_PATH_INPUT

    -	num_of_images：Initial と Final の構造間に何点構造を配置するか
    -	nstep_path：反復計算回数の上限
    -	path_thr：収束判定条件（Ry/bohr）

-	BEGIN_ENGINE_INPUT :math:`\sim` END_ENGINE_INPUT

    -   各構造に対するエネルギー＆力の自己無撞着計算設定（QuloudJob.scf.in とほぼ同じ内容）

-	BEGIN_POSITIONS :math:`\sim` END_POSITIONS

    -   FIRST_IMAGE：Initial に対応する ATOMIC_POSITIONS を記述
    -   LAST_IMAGE：Final に対応する ATOMIC_POSITIONS を記述

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ph.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

フォノン計算のメインとなる ph.x 用の入力ファイルです。

::

    &inputph
    prefix = 'QuloudJob'
    outdir = './work'
    niter_ph = 100
    tr2_ph = 1e-12
    alpha_mix(1) = 0.7
    nmix_ph = 4
    verbosity = 'default'
    reduce_io = .false.
    max_seconds = 10000000
    dftd3_hess = 'prefix.hess'
    fildyn = 'matdyn'
    epsil = .false.
    lrpa = .false.
    lnoloc = .false.
    trans = .true.
    lraman = .false.
    eth_rps = 1e-9
    eth_ns = 1e-12
    dek = 0.001
    recover = .false.
    low_directory_check = .false.
    only_init = .false.
    qplot = .false.
    q2d = .false.
    q_in_band_form = .false.
    el_ph_nsigma = 10
    el_ph_sigma = 0.02
    lshift_q = .false.
    zue = .false.
    elop = .false.
    fpol = .false.
    ldisp = .true.
    nogg = .false.
    asr = .false.
    ldiag = .false.
    lqdir = .false.
    search_sym = .true.
    nq1 = 4
    nq2 = 4
    nq3 = 4
    diagonalization = 'david'
    read_dns_bare = .false.
    ldvscf_interpolate = .false.
    start_irr = 1
    start_q = 1
    /

主要パラメータは以下になります。

- nq1/nq2/nq3：フォノンを計算するBrillouin Zone 内の波数の点数

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
q2r.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

波数空間でのフォノンの情報を実空間の情報に変換する q2r.x 用の入力

::

    &input
    fildyn = 'matdyn'
    flfrc = 'matdyn.fc'
    zasr = 'simple'
    /

入出力のファイル名と q = 0 点の処理方式（zasr）を指定します。

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
matdyn_dos.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

matdyn.x 用の入力で、フォノンDOSを描く場合の設定。

::

    &input
    flfrc = 'matdyn.fc'
    asr = 'no'
    dos = .true.
    flfrq = ''
    nk1 = 8
    nk2 = 8
    nk3 = 8
    fldos = 'matdyn.dos'
    /

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
matdyn_disp.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

matdyn.x 用の入力で、フォノンバンドを描く場合の設定。

::

    &input
    flfrc = 'matdyn.fc'
    asr = 'no'
    flfrq = 'matdyn.freq'
    flvec = 'matdyn.modes'
    q_in_band_form = .true.
    /
    2
    0 0 0 20
    0.5 0 0 20

|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
xspectra.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

X線吸収計算を行う xspectra.x 用の入力

::

    &input_xspectra
    calculation = 'xanes_dipole'
    edge = 'K'
    lplus = .false.
    lminus = .false.
    prefix = 'QuloudJob'
    outdir = './work'
    verbosity = 'high'
    xiabs = 1
    xkvec(1) = 1
    xkvec(2) = 0
    xkvec(3) = 0
    xepsilon(1) = 0
    xepsilon(2) = 0
    xepsilon(3) = 1
    xcoordcrys = .true.
    xonly_plot = .false.
    x_save_file = 'xanes.sav'
    xe0 = 10000
    xniter = 50
    xcheck_conv = 5
    xerror = 0.01
    show_status = .false.
    time_limit = 100000000
    restart_mode = 'from_scratch'
    /

    &plot
    xnepoint = 100
    xemax = 10
    xemin = 0
    cut_occ_states = .true.
    terminator = .true.
    gamma_mode = 'constant'
    xgamma = 0.1
    xanes_file = 'xanes.dat'
    /

    &pseudos
    filecore = 'Core.wfc'
    /

    &cut_occ
    cut_ierror = 1e-7
    cut_stepu = 0.01
    cut_stepl = 0.001
    cut_startt = 1
    cut_tinf = 0.000001
    cut_tsup = 100
    cut_desmooth = 0.01
    cut_nmemu = 100000
    cut_nmeml = 100000
    /

    6 6 6 0 0 0

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.scf.out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

以下の内容が出力されます。

|

**Single-Point SCF、Electron Band Structure、Electron DOS の場合**

-   入力ファイル "QuloudJob.scf.in" の読み込み結果
-   SCF 計算の各ステップで求められる全エネルギーの値と、その変動の幅（収束状況）

|

**Atomic Structure Opt. の場合**

-   入力ファイル "QuloudJob.scf.in" の読み込み結果
-   SCF 計算の各ステップで求められる全エネルギーの値と、その変動の幅（収束状況）
-   構造最適化計算の各ステップでの原子座標と、求められる全エネルギー・原子に加わる力の値と、それらの変動の幅（収束状況）

|

**Lattice Opt. の場合**

-   入力ファイル "QuloudJob.scf.in" の読み込み結果
-   SCF 計算の各ステップで求められる全エネルギーの値と、その変動の幅（収束状況）
-   構造最適化計算の各ステップでの格子ベクトル・原子座標と、求められる全エネルギー・原子に加わる力・セルに加わる圧力の値と、それらの変動の幅（収束状況）

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.nscf.out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

以下の内容が出力されます。

|

**Electron Band Structure の場合**

-   入力ファイル "QuloudJob.nscf.in" の読み込み結果
-   電子バンド計算用の各 k 点でのエネルギーの値 (eV)

|

**Electron DOS の場合**

-   入力ファイル "QuloudJob.nscf.in" の読み込み結果
-   電子状態密度計算用の各 k 点でのエネルギーの値 (eV)

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.bands.out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron Band Structure の Job が完了したかどうかが確認できます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.bands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron Band Structure での、電子バンド計算結果のデータが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.bands.gnu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron Band Structure での、電子バンド図描画用のデータが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.dos.out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron DOS の Job が完了したかどうかが確認できます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.dos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron DOS での、電子状態密度計算結果のデータが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.dat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NEB 計算のとき、エネルギープロファイルのデータが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.axsf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NEB 計算のとき、構造変化のトラジェクトリーデータが出力されます（XCrysden 形式）

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
matdyn.freq.gp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

フォノンバンド計算結果のプロット用のデータが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
matdyn.dos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

フォノンDOS計算結果のプロット用データが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
xanes.dat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

X-Spectra の計算結果のデータが出力されます。

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

Quantum ESPRESSO では、ログにはほぼ何も出力されませんので、動作状況の確認では出力ファイルをご覧ください。

|
|

--------------------------------------------------------------
OpenMX
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
openmx.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

|

**Single-Point SCF の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 

入力パラメータの詳細は以下の通りです。

-	File Name

    -	System.CurrrentDirectory：出力ファイルを置くディレクトリを指定します。デフォルトでは ./ となっています。
    -	System.Name：出力ファイルのファイル名を指定します。デフォルトでは QuloudJob となっています。
    -	DATA.PATH：VPS および PAO ディレクトリへのパスを指定します。デフォルトでは /usr/local/rsdft/DFT_DATA19 となっています。

-	Definition of Atomic Species

    -	Species.Number：モデルに含まれる原子の種類の総数を指定します。
    -	Definition.of.Atomic.Species：モデルに含まれる原子の種類を指定します。
    
        記述は <Definition.of.Atomic.Species で始まり、Definition.of.Atomic.Species> で終わります。

        １番目の列では原子の種類の名前を指定します。この名前は、後述する Atoms.SpeciesAndCoordinates にて原子座標を指定するのに使います。
        
        ２番目の列では擬原子基底関数の拡張子無しのファイル名と、プリミティブ基底関数の数および縮約された基底関数の数を指定します。このファイルは DFT_DATA19/PAO ディレクトリに置く必要があります。上の例では、Ba の基底関数は Ba10.0-s3p2d2 となっていますが、Ba10.0 が DFT_DATA19/PAO ディレクトリにある擬原子基底関数の拡張子無しのファイル名を示します。s3 は s3>3 の略記であり、３つの s 軌道のプリミティブ軌道から３つの最適化された軌道が作られていることに対応します。つまり縮約は行わないことを意味します。縮約が無い場合、s3>3 と記述する代わりに s3 という簡単な記法を使用できます。p2、d2 も同様で、それぞれ p2>2、d2>2 の略記です。つまり、Ba10.0-s3p2d2 は Ba10.0-s3>3p2>2d2>2 と同等です。
        
        ３番目の列では擬ポテンシャルの拡張子無しのファイル名を指定します。このファイルは DFT_DATA19/VPS ディレクトリに置く必要があります。

-	Atoms

    -	Atoms.Number：モデルに含まれる原子の総数を指定します。
    -   Atoms.SpeciesAndCoordinates.Unit：原子座標の単位を指定します。デフォルトでは FRAC となっています。FRAC の場合には、後述する Atoms.UnitVectors で与えられた格子ベクトル a、b、c を基準とした相対座標になります。その際には 0.0 ～ 1.0 の範囲で座標が設定可能で、この範囲を超える座標は入力ファイルの読み込み後に自動的に調整されます。
    -   Atoms.SpeciesAndCoordinates：原子座標および各スピン毎の電子数を指定します。
        
        記述は <Atoms.SpeciesAndCoordinates で始まり、Atoms.SpeciesAndCoordinates> で終わります。

        １列目には原子を特定する連番を記述します。

        ２列目には事前に Definition.of.Atomic.Species の１列目で定義した原子の種類の名前を指定します。

        ３～５列目には、それぞれ x、y、z 座標を指定します。前述した Atoms.SpeciesAndCoordinates.Unit で FRAC を指定している場合は、３～５列目はそれぞれ a、b、c 軸を基準とした相対座標になり、値は 0.0 ～ 1.0 の範囲で指定します。この範囲を外れる数値は入力ファイルが読み込まれる段階で自動的に調整されます。

        ６および７列目には、各原子のアップスピンとダウンスピン状態のそれぞれの初期電子数を設定します。アップスピン電子数とダウンスピン電子数の合計は原子の価電子の数に等しくなるようにします。原子の価電子数は OpenMX Ver.3.9 ユーザーマニュアル（https://www.openmx-square.org/openmx_man3.9jp/openmx3.9_jp.pdf）の Table 1 と Table 2 に記載されています。LSDA-CA、 LSDA-PW、あるいは GGA-PBE を使用してスピン分極系を計算する場合、６および７列目の指定によって各原子に初期スピンを指定することができます。これにより強磁性状態や反強磁性状態などの計算が可能です。

    -   Atoms.UnitVectors.Unit：格子ベクトルの単位を指定します。デフォルトでは Ang（オングストローム（Å）単位）となっています。

    -   Atoms.UnitVectors：格子ベクトル a、b、c を指定します。
        
        記述は <Atoms.UnitVectors で始まり、Atoms.UnitVectors> で終わります。
        
        第１～３行はそれぞれ格子ベクトル a、b、c に対応します。

-   SCF or Electronic System

    -   scf.XcType：交換相関ポテンシャルを指定します。Quloud では LSDA-CA、LSDA-PW、GGA-PBE から選択できます。ここで LSDA-CA は Ceperley-Alder の局所スピン密度関数、LSDA-PW は、その GGA 形式において密度勾配をゼロとした PerdewWang 局所スピン密度関数です。GGA-PBE は Perdew らが提案する GGA 汎関数です。デフォルトでは GGA-PBE となっています。
    -   scf.SpinPolarization：電子系でスピン分極の計算を行う場合は ON を指定し、非スピン分極の計算を行う場合は OFF を指定します。scf.XcType で LDA を使用する場合は OFF に設定して下さい。前述の２つのオプションの他、ノンコリニア DFT 計算を行う場合には NC というオプションを指定して下さい。この計算については OpenMX Ver.3.9 ユーザーマニュアル（https://www.openmx-square.org/openmx_man3.9jp/openmx3.9_jp.pdf）の「ノンコリニア DFT」の章もご参照下さい。デフォルトでは OFF となっています。
    -   scf.ElectronicTemperature：電子温度（K）を設定します。デフォルトでは 300 となっています。
    -   scf.energycutoff：積分グリッド間隔を決定するカットオフエネルギーを指定します（単位は Ryd）。この積分グリッドは差電子クーロンポテンシャルと交換相関ポテンシャルに対する行列要素の計算および高速フーリエ変換（FFT）を用いた Poisson 方程式の解法のために使用されます。
    -   scf.maxIter：SCF の最大反復回数を設定します。SCF 反復ループは、収束条件が満たされない場合でもここで指定した回数で終了します。デフォルト値は 100 です。
    -   scf.EigenvalueSolver：固有値問題の計算手法を指定します。デフォルトでは Band（バンド計算）となっています。
    -   scf.Kgrid：scf.EigenvalueSolver により Band を指定した場合、k 空間の第１ブリルアンゾーンを等間隔メッシュにより離散化するためのグリッド数（n1, n2, n3）を指定する必要があります。ここでは n1 n2 n3 のように指定して下さい。
    -   scf.criterion：SCF 計算の収束条件を指定します（Hartree 単位）。SCF 反復は、dUele < scf.criterion という条件が満たされると終了します。ここで dUele とは、現在の SCF 反復とひとつ前の反復とのバンドエネルギーの絶対差です。デフォルト値は 1e-10 です。
    -   scf.system.charge：電子および正孔のドーピングの量を指定します。プラス・マイナス符号はそれぞれ正孔と電子のドーピングを表します。デフォルト値は 0 です。
    -   scf.Mixing.Type：SCF 計算の次の反復ステップに入力される電子密度（もしくは密度行列）を生成するための電子密度混合法を指定します。Quloud では、単純混合法（Simple）、RMM-DIISK 法のいずれかを指定することができます。RMM-DIISK 法を指定した場合、計算の初めでは Kerker 混合法を用いてある程度まで収束させ、その後 RMM-DIISK 法に切り替えます。切り替えるタイミングは、後述する scf.Mixing.StartPulay で指定することができます。デフォルトでは RMM-DIISK となっています。
    -   scf.Init.Mixing.Weight：初期の電子密度混合比を指定します。RMM-DIISK 法を指定した場合は、計算初期の Kerker 混合法での混合比を指定することになります。有効な範囲は 0 < scf.Init.Mixing.Weight < 1 で、デフォルト値は 0.3 です。
    -   scf.Min.Mixing.Weight：単純混合法および Kerker 混合法における混合比の下限を指定します。デフォルトでは 0.001 に設定されています。
    -   scf.Max.Mixing.Weight：単純混合法および Kerker 混合法における混合比の上限を指定します。デフォルトでは 0.4 に設定されています。
    -   scf.Mixing.History：RMM-DIISK 法では、SCF の次の反復ステップにおける入力電子密度（ハミルトニアン）を、過去の SCF 反復の電子密度（ハミルトニアン）に基づき推定します。scf.Mixing.History は、この推定に使用する過去の SCF 反復ステップ数を指定します。例えば、scf.Mixing.History を 3 に設定した場合、６回目の SCF 反復では過去の第５、４、３ステップの電子密度（ハミルトニアン）が考慮されます。デフォルト値は 30 となっています。
    -   scf.Mixing.StartPulay：RMM-DIISK 法を開始する SCF ステップを指定します。これらの方法を開始するまでの SCF ステップでは Kerker 混合法が使用されます。デフォルトでは 6 に設定されています。
    -   scf.Electric.Field：のこぎり波形で表される外部均一電場を導入することが可能です。例えば、a 軸に沿って 1.0 GV/m（10\ :sup:`9` V/m）の電場を適用するには、次のように指定します。

        ::

            scf.Electric.Field 1.0 0.0 0.0 # default=0.0 0.0 0.0 (GV/m)

        電場の符号は電子に作用するものとして定義されています。デフォルト値は 0 0 0 です。

|

**Atomic Structure Opt. の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    ### 
    ### Opt
    ###
    MD.Type RF
    MD.maxIter 100
    MD.Opt.criterion 0.00029953
    MD.Opt.StartDIIS 10
    MD.Opt.DIIS.History 4

Atomic Structure Opt. では、以下の設定が追加されています。

-   Opt

    -   MD.Type：原子構造最適化のタイプを指定します。Quloud では Opt（最急降下法）、DIIS（反復部分空間法）、BFGS（Broyden-Fletcher-Goldfarb-Shanno 法）、RF（合理的関数法）、EF（固有ベクトル追跡法）が選択できます。デフォルトでは RF となっています。
    -   MD.maxIter：原子構造最適化計算における最大の反復回数を指定します。デフォルトでは 100 となっています。
    -   MD.Opt.criterion：原子構造最適化計算の収束条件を設定します。原子にかかる力の最大絶対値がここで指定した値より小さくなった場合に、最適化計算は終了します。デフォルトでは 0.00029953 Hartree/Bohr となっています。
    -   MD.Opt.StartDIIS：DIIS、BFGS、RF、EF による原子構造最適化を開始するステップを指定します。これらの方法を開始する以前のステップでは最急降下法が使用されます。デフォルトでは 10 となっています。
    -   MD.Opt.DIIS.History：原子構造最適化のために参照する過去のステップ数を指定します。デフォルトでは 4 となっています。

|

**Lattice Opt. の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    level.of.stdout                   1
    level.of.fileout                  1
    ### 
    ### Lattice Opt
    ###
    MD.Type RFC5
    MD.maxIter 100
    MD.Opt.criterion 0.00029953
    MD.Opt.StartDIIS 10
    MD.Opt.DIIS.History 4

Lattice Opt. では、以下の設定が追加されています。

-   Lattice Opt

    -   MD.Type：格子定数最適化のタイプを指定します。Quloud で選択できるオプションは以下の通りです。
                
            -   OptC1：原子座標を固定したまま、格子ベクトルに拘束をかけずに最適化を行います。最適化は、最急降下法によって行われます。
            -   OptC4：原子座標を固定したまま、格子ベクトル間の角度を初期値に固定し、格子ベクトルの長さを以下の拘束条件のもとで最適化します：\|a1\| = \|a2\| ≠ \|a3\|。最適化は、最急降下法によって行われます。
            -   OptC5：原子座標、格子ベクトルともに拘束をかけずに同時に最適化を行います。最適化は、最急降下法によって行われます。
            -   RFC5：原子座標、格子ベクトルともに拘束をかけずに同時に最適化を行います。最適化は、RF 法、DIIS 法、BFGS 法によって行われます。
        
        デフォルトでは RFC5 となっています。

    -   MD.maxIter：格子定数最適化計算における最大の反復回数を指定します。デフォルトでは 100 となっています。
    -   MD.Opt.criterion：格子定数最適化計算の収束条件を設定します。原子にかかる力の最大絶対値がここで指定した値より小さくなった場合に、最適化計算は終了します。デフォルトでは 0.00029953 Hartree/Bohr となっています。
    -   MD.Opt.StartDIIS：RF、DIIS、BFGS による格子定数最適化を開始するステップを指定します。これらの方法を開始する以前のステップでは最急降下法が使用されます。デフォルトでは 10 となっています。
    -   MD.Opt.DIIS.History：格子定数最適化のために参照する過去のステップ数を指定します。デフォルトでは 4 となっています。

|

**Electron Band Structure の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    ### 
    ### Band
    ###
    Band.dispersion on
    Band.Nkpath 11 #auto
    <Band.kpath
      20 0.0 0.0 0.0   0.0 0.5 0.0 G X
      20 0.0 0.5 0.0   0.5 0.5 0.0 X M
      20 0.5 0.5 0.0   0.0 0.0 0.0 M G
      20 0.0 0.0 0.0   0.0 0.0 0.5 G Z
      20 0.0 0.0 0.5   0.0 0.5 0.5 Z R
      20 0.0 0.5 0.5   0.5 0.5 0.5 R A
      20 0.5 0.5 0.5   0.0 0.0 0.5 A Z
      20 0.0 0.0 0.5   0.0 0.5 0.0 Z X
      20 0.0 0.5 0.0   0.0 0.5 0.5 X R
      20 0.0 0.5 0.5   0.5 0.5 0.0 R M
      20 0.5 0.5 0.0   0.5 0.5 0.5 M A
    Band.kpath>
    #KPT  G  0.0 0.0 0.0 /
    #KPT  A  0.5 0.5 0.5 /
    #KPT  M  0.5 0.5 0.0 /
    #KPT  R  0.0 0.5 0.5 /
    #KPT  X  0.0 0.5 0.0 /
    #KPT  Z  0.0 0.0 0.5 /
    #KPTLABEL   G X M G Z R A Z X R M A  /

Electron Band Structure では、以下の設定が追加されています。

-   Band

    -   Band.dispersion：バンド分散を評価する場合、ON に設定します。
    -   Band.Nkpath：バンド分散の計算における経路の数を指定します。
    -   Band.kpath：バンド分散の経路を指定します。

        記述は <Band.kpath で始まり、Band.kpath> で終わります。行数は Band.Nkpath で指定した数と同じにする必要があります。

        第１列には経路上で固有値を計算する格子の数を指定します。
        
        続く n1, n2, n3 および n1’, n2’, n3’ は、逆格子ベクトルを基底とする第１ブリルアンゾーンの経路の開始および終了の k 点を指定します。逆格子ベクトルは Atoms.UnitVectors で指定した格子ベクトルを用いて計算されます。
        
        最後の２つの英文字は経路の開始および終了の k 点の名前を指定します。

|

**Electron DOS の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    ### 
    ### DOS
    ###
    Dos.fileout on
    Dos.Erange -20 20
    Dos.Kgrid 4 4 4 

Electron DOS では、以下の設定が追加されています。

-   DOS

    -   Dos.fileout：状態密度を評価する場合、ON に設定します。
    -   Dos.Erange：状態密度計算におけるエネルギーの範囲を eV 単位で指定します。デフォルトでは -20 eV ～ 20 eV となっています。
    -   Dos.Kgrid：状態密度計算を行う上で、第１ブリルアンゾーンを離散化するために（n1, n2, n3）の格子点を指定します。

|

**Energy Barrier (NEB) の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    <NEB.Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    NEB.Atoms.SpeciesAndCoordinates>
    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    MD.Type NEB
    MD.NEB.Number.Images 10
    MD.NEB.Spring.Const 0.1
    MD.maxIter 100
    MD.Opt.criterion 0.01
    MD.Opt.StartDIIS 5
    MD.Opt.DIIS.History 3

Energy Barrier (NEB) では、以下の設定が追加されています。

-   Atoms

    -   NEB.Atoms.SpeciesAndCoordinates：生成物の原子座標および各スピン毎の電子数を指定します。記述の方法は Atoms.SpeciesAndCoordinates（反応物の場合）と同様です。

-   ファイル最下部のパラメータ

    -   MD.Type：NEB 計算を行う場合、NEB に設定します。
    -   MD.NEB.Number.Images：エネルギー経路中のイメージ数を指定します。ただし、２つの終端構造（反応物と生成物）はイメージの数から除きます。デフォルトでは 10 となっています。
    -   MD.NEB.Spring.Const：バネ定数を設定します。デフォルトでは 0.1 となっています。
    -   MD.maxIter：エネルギー経路の最適化計算における最大の反復回数を指定します。デフォルトでは 100 となっています。
    -   MD.Opt.criterion：エネルギー経路の最適化計算の収束条件を設定します。原子にかかる力の最大絶対値がここで指定した値より小さくなった場合に、最適化計算は終了します。デフォルトでは 0.01 Hartree/Bohr となっています。
    -   MD.Opt.StartDIIS：エネルギー経路の最適化はハイブリッド最適化法（DIIS + BFGS）によって行います。ここでは、ハイブリッド最適化法を開始するステップを指定します。それ以前のステップでは最急降下法が使用されます。デフォルトでは 5 となっています。
    -   MD.Opt.DIIS.History：エネルギー経路の最適化のために参照する過去のステップ数を指定します。デフォルトでは 3 となっています。

|

**First-Principles MD の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    MD.Type NVT_NH
    MD.maxIter 2000
    MD.TimeStep 1
    NH.Mass.HeatBath 20
    <MD.TempControl
      1
      1000 300
    MD.TempControl>
    <MD.InitVelocity
    MD.InitVelocity>

First-Principles MD では、以下の設定が追加されています。

-   ファイル最下部のパラメータ

    -   MD.Type：分子動力学計算のタイプを指定します。デフォルトでは NVT_NH（Nose-Hoover 法による NVT アンサンブル MD）となっています。
    -   MD.maxIter：分子動力学計算における最大の反復回数を指定します。デフォルトでは 2000 となっています。
    -   MD.TimeStep：時間ステップ（fs）を指定します。デフォルトでは 1 fs となっています。
    -   NH.Mass.HeatBath：MD.Type で NVT_NH を指定した場合、熱浴の質量を設定します。次元は「長さ^2 × 質量」で、長さにはボーア半径（Bohr）、質量には統一原子質量単位（炭素原子の主同位体の質量を 12.0 とする単位。記号は u）を用います。デフォルトでは 20 Bohr\ :sup:`2`・u となっています。
    -   MD.TempControl：NVT アンサンブルの分子動力学計算における原子運動の温度を指定します。NVT_NH を選択した場合の記述の方法は以下の通りです。

        記述は <MD.TempControl で開始し、MD.TempControl> で終わります。

        最初の数字で、続く温度指定の行数を指定します。上の例では１行あります。

        後続する行の第１、２列では、それぞれ MD ステップ数と原子運動の温度を指定します。指定された MD ステップ間の温度は線形補完されます。

    -   MD.InitVelocity：分子動力学のシミュレーションでは、各原子に初期速度を与えることができますが、Quloud のデフォルトでは設定されていません。

|

**Exchange Coupling Parameters の場合**

::

    #
    #    File Name
    #

    System.CurrrentDirectory ./
    System.Name QuloudJob
    DATA.PATH /usr/local/rsdft/DFT_DATA19

    #
    # Definition of Atomic Species
    #

    Species.Number 3
    <Definition.of.Atomic.Species
     Ba Ba10.0-s3p2d2 Ba_PBE19
     O O6.0-s2p2d1 O_PBE19
     Ti Ti7.0-s3p2d1 Ti_PBE19
    Definition.of.Atomic.Species>

    #
    # Atoms
    #

    Atoms.Number 5
    Atoms.SpeciesAndCoordinates.Unit FRAC
    <Atoms.SpeciesAndCoordinates
     1 Ba 0.5 0.5 0.58254146 5.0 5.0
     2 Ti 0.0 0.0 0.1000427 6.0 6.0
     3 O 0.0 0.5 0.06422054 3.0 3.0
     4 O 0.5 0.0 0.06422054 3.0 3.0
     5 O 0.0 0.0 0.54897175 3.0 3.0
    Atoms.SpeciesAndCoordinates>
    Atoms.UnitVectors.Unit Ang
    <Atoms.UnitVectors
     3.99037921 0.0 2.443402563455322e-16
     6.417019188399763e-16 3.99037921 2.443402563455322e-16
     0.0 0.0 4.10265539
    Atoms.UnitVectors>

    #atomic.orbital Standard 
    ###
    ### SCF or Electronic System
    ###

    scf.XcType GGA-PBE 
    scf.SpinPolarization off 
    scf.ElectronicTemperature  300 
    scf.energycutoff 224.94602771541878 
    # scf.Ngrid 36 36 36 
    scf.maxIter 100 
    scf.EigenvalueSolver band 
    scf.Kgrid 4 4 4 
    scf.criterion 1e-10 
    scf.system.charge 0 
    scf.Mixing.Type rmm-diisk 
    scf.Init.Mixing.Weight 0.3 
    scf.Min.Mixing.Weight 0.001 
    scf.Max.Mixing.Weight 0.4 
    scf.Mixing.History 30 
    scf.Mixing.StartPulay 6 
    scf.Electric.Field 0 0 0 
    HS.fileout  on

Exchange Coupling Parameters では、以下の設定が追加されています。

-   ファイル最下部のパラメータ

    -   HS.fileout：Exchange Coupling Parameters では、SCF 計算の結果をもとに交換結合パラメータを計算します。SCF 計算の出力ファイル「scfout」を生成するために、ここでは ON に設定します。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
jx.config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exchange Coupling Parameters で、交換結合パラメータを計算するための設定ファイルです。

::

    Flag.PeriodicSum off
    Num.Poles 60
    Num.Kgrid 4 4 4
    Num.ij.pairs 1870
    Bunch.ij.pairs 1870
    <ijpairs.cellid
      1 1 -2 -2 -2
      1 1 -2 -2 -1
      1 1 -2 -2 0
        ・・・
        ・・・
      5 5 2 2 0
      5 5 2 2 1
      5 5 2 2 2
    ijpairs.cellid>

入力パラメータの詳細は以下の通りです。

-   Flag.PeriodicSum：バルク系の場合に、交換結合をどのように計算するかを指定します。on/off それぞれの場合に用いられる計算式は OpenMX Ver.3.9 ユーザーマニュアル（https://www.openmx-square.org/openmx_man3.9jp/openmx3.9_jp.pdf）の「交換結合パラメータ」の章をご参照下さい。なお、クラスター系の場合は、on/off にかかわらず同じ計算式が用いられます。
-   Num.Poles：Flag.PeriodicSum で off を選択した場合、計算式に現れるフェルミ関数の有限極近似に対する極の数 *N* \ :sub:`P`\ を指定します。極の数の増加に従い計算精度が向上しますが、計算時間は極の数に比例して増加します。
-   Num.Kgrid：バルク系の場合に、第１ブリルアンゾーンの離散化に対する k 点の数を指定します。ここで指定する k 点数は SCF 計算の際と同じ値、もしくはそれ以上の値を指定して下さい。クラスター計算では自動的にガンマ点のみが考慮されますので、ここでの設定に意味はありません。
-   Num.ij.pairs：計算する交換結合定数 J の数を指定します。この値は、後述する <ijpairs.cellid と ijpairs.cellid> の間の行数と同数でなければなりません。
-   Bunch.ij.pairs：既定の設定ではメモリ消費が多くなり、計算が出来ない場合がありますが、ここでの設定でメモリ消費量を低減させることができます。この値は Num.ij.pairs と同じか、より小さい値であるべきです。小さい値を用いるとメモリ消費量は低減されますが、計算時間が長くなる傾向があります。
-   ijpairs.cellid：このフィールドでは計算する交換結合定数 J のサイト *i* , *j* と *J* \ :sub:`i0, jR`\ のセルベクトル **R** = *l* \ :sub:`1`\ **a** \ :sub:`1`\ + *l* \ :sub:`2`\ **a** \ :sub:`2`\ + *l* \ :sub:`3`\ **a** \ :sub:`3`\を指定します。ここで、**a** \ :sub:`1`\, **a** \ :sub:`2`\ 及び **a** \ :sub:`3`\ は OpenMX 入力での単位格子ベクトルです。このフィールドのデータの並び方は *i* *j* *l* \ :sub:`1`\ *l* \ :sub:`2`\ *l* \ :sub:`3`\ の順です。上の例では *l* \ :sub:`1`\, *l* \ :sub:`2`\, *l* \ :sub:`3`\ の値の範囲は -2 以上 2 以下となっていますが、これは交換結合パラメータ計算で２個先のサイトまで考慮することを意味します。

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SCF 計算の履歴、構造最適化の履歴、Mulliken 電荷、全エネルギー、および双極子モーメントが保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.xyz
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MD または構造最適化により得られた最終的な幾何学的構造が保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.bulk.xyz
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

scf.EigenvalueSolver=Band の場合、コピーされたセルの原子を含む原子座標が出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.md
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

各 MD ステップごとの原子座標が保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.md2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

最終 MD ステップにおける原子座標が保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.cif
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

cif 形式の初期原子座標が保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.ene
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MD ステップごとの計算値が保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.tden.cube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gaussian cube 形式で全電子密度が保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.sden.cube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

LSDA-CA、LSDA-PW、GGA-PBE を使用したスピン分極計算が実行された場合に、スピン電子密度が Gaussian cube 形式で保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.dden.cube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

構成原子の孤立原子状態の電子密度の重ね合わせを基準として計算された差電子密度が Gaussian cube 形式で保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.v0.cube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

アップスピンの非局所ポテンシャルを除く Kohn-Sham ポテンシャルが Gaussian cube 形式で保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.v1.cube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

スピン分極計算における、ダウンスピンの非局所ポテンシャルを除く Kohn-Sham ポテンシャルが Gaussian cube 形式で保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.vhart.cube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

差電子密度から生じる差電子 Hartree ポテンシャルが Gaussian cube 形式で保存されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.Band
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron Band Structure で、Band.Nkpath が 0 以上で、かつ scf.EigenvalueSolver=Band の場合、バンド分散のデータファイルが生成されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.Dos.val
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron DOS で、Dos.fileout=ON の場合、状態密度を計算するための固有値のデータファイルが生成されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.Dos.vec
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron DOS で、Dos.fileout=ON の場合、状態密度を計算するための固有ベクトルのデータファイルが生成されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
jx.log
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exchange Coupling Parameters で、交換結合パラメータの計算結果が保存されます。

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

SCF 計算、構造最適化、MD の計算過程が出力されます。交換結合パラメータ計算についてはほぼ何も出力されません。

|
|

--------------------------------------------------------------
RSDFT
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
rsdft.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

**Single-Point SCF の場合**

::

    XCTYPE GGA_PBE96 /
    PSSET FHI /
    NGRID 36 36 36 /
    KGRID 4 4 4 /
    EKBT 0.001102471005012568 /
    DITER 300 /
    SCFCONV 1e-15 /
    MPVER  0 /
    KINTEG 0 /
    NSWEEP 10 /
    SWSCF 1 /
    OC 2 /

入力パラメータの詳細は以下の通りです。

-   XCTYPE：交換相関汎関数を指定します。デフォルトでは GGA_PBE96 となっています。
-   PSSET：擬ポテンシャルの種類を指定します。デフォルトでは FHI となっています。
-   NGRID：各格子ベクトル方向の実空間グリッド刻み数を指定します。
-   KGRID：各逆格子ベクトル方向の k 空間グリッド刻み数を指定します。
-   EKBT：Methfessel-Paxton 法によるブリルアンゾーン積分を行う際の平滑化の幅を指定します（Hartree 原子単位）。デフォルトでは 0.001102471005012568 となっています。
-   DITER：SCF 反復のループ回数の上限を指定します。デフォルトでは 300 となっています。
-   SCFCONV：SCF 計算の収束判定条件を指定します。判定に用いる量は RSDFT ユーザーガイド（https://www.rsdft.jp/documents/UserGuide1.5-jp.pdf）の「3.5.1 パラメータ一覧」をご参照ください。デフォルトでは 1e-15 となっています。
-   MPVER：平滑化法の種類を指定します。Fermi-Dirac 分布関数を用いる場合は -1、Methfessel-Paxton 法の場合は 0 に設定します。デフォルトでは 0 となっています。
-   KINTEG：Methfessel-Paxton の方法で平滑化によるブリルアンゾーン積分を行う際の、デルタ関数をエルミート多項式で展開する際の次数を指定します。デフォルトでは 0 となっています。
-   NSWEEP：RSDFT では、良い波動関数を得るために、初期ポテンシャルを固定した SCF 計算のようなものを実行しており、これを Sweep と呼んでいます。その Sweep 計算時の反復回数の上限を指定します。デフォルトでは 10 となっています。
-   SWSCF："rsdft.atom" ファイルから読み込んだ初期原子座標で SCF 計算を行うか否かを指定します。デフォルトでは 1（行う）となっています。
-   OC：波動関数や密度・ポテンシャルデータの書き出しを指定します。デフォルトでは 2（密度 & ポテンシャルのみ書き出す）となっています。

|

**Atomic Structure Opt. の場合**

::

    XCTYPE GGA_PBE96 /
    PSSET FHI /
    NGRID 36 36 36 /
    KGRID 4 4 4 /
    EKBT 0.001102471005012568 /
    DITER 300 /
    SCFCONV 1e-15 /
    MPVER  0 /
    KINTEG 0 /
    NSWEEP 10 /
    SWSCF 1 /
    SWOPT 7 /
    ATOMOPT1 100 0.000499865 /
    OC 2 /

Atomic Structure Opt. では、以下の設定が追加されています。

-   SWOPT：原子構造最適化計算のアルゴリズムを指定しています。
-   ATOMOPT1：共役勾配法による原子構造最適化計算の制御を行います。一つ目の数値で CG 反復回数の上限、二つ目の数値で力の収束判定基準（Hartree/Bohr 単位）を指定します。

|

**Lattice Opt. の場合**

::

    XCTYPE GGA_PBE96 /
    PSSET FHI /
    NGRID 36 36 36 /
    KGRID 4 4 4 /
    EKBT 0.001102471005012568 /
    DITER 300 /
    SCFCONV 1e-15 /
    MPVER  0 /
    KINTEG 0 /
    NSWEEP 10 /
    SWSCF 1 /
    SWOPT 7 /
    ATOMOPT1 100 0.000499865 /
    SWOPTLAT 1 /
    OC 2 /

Lattice Opt. では、以下の設定が追加されています。

-   SWOPT：原子構造最適化計算のアルゴリズムを指定しています。
-   ATOMOPT1：共役勾配法による原子構造最適化計算の制御を行います。一つ目の数値で CG 反復回数の上限、二つ目の数値で力の収束判定基準（Hartree/Bohr 単位）を指定します。
-   SWOPTLAT：モデルの原子構造から、格子定数最適化計算の拘束条件（各方向の格子ベクトル長さを揃えるかどうかなど）が自動で決定されます。

|

**Electron Band Structure の場合**

::

    XCTYPE GGA_PBE96 /
    PSSET FHI /
    NGRID 36 36 36 /
    KGRID 4 4 4 /
    EKBT 0.001102471005012568 /
    DITER 300 /
    SCFCONV 1e-15 /
    MPVER  0 /
    KINTEG 0 /
    NSWEEP 10 /
    SWSCF 1 /
    SWBAND 1  /

    KPT  G  0.0 0.0 0.0 /
    KPT  A  0.5 0.5 0.5 /
    KPT  M  0.5 0.5 0.0 /
    KPT  R  0.0 0.5 0.5 /
    KPT  X  0.0 0.5 0.0 /
    KPT  Z  0.0 0.0 0.5 /
    KPTLABEL   G X M G Z R A Z X R M A  /
    OC 2 /

Electron Band Structure では、以下の設定が追加されています。

-   SWBAND：バンド計算を実行するか否かを指定します。デフォルトでは 1（実行する）となっています。
-   KPT：バンド計算で通過する k 点を指定します。１列目には各 k 点のラベル、２～４列目には各 k 点の座標を入力します。
-   KPTLABEL：KPT で入力した k 点ラベルを用いて、バンド計算の k 点経路を指定します。

    各 k 点経路の刻み幅を指定するには、"KPTDIVNUM" パラメータを使用します。例えば各経路を 5 刻みに分割したい場合は、以下のように設定します。

    ::
    
        KPTDIVNUM 5 5 5 5 5 5 5 5 5 5 5

|

**Electron DOS の場合**

::

    XCTYPE GGA_PBE96 /
    PSSET FHI /
    NGRID 36 36 36 /
    KGRID 4 4 4 /
    EKBT 0.001102471005012568 /
    DITER 300 /
    SCFCONV 1e-15 /
    MPVER  0 /
    KINTEG 0 /
    NSWEEP 10 /
    SWSCF 1 /
    SWDOS 1 /
    OC 2 /

Electron DOS では、以下の設定が追加されています。

-   SWDOS：状態密度計算を実行する場合は、ここで 1 に設定します。

|

**First-Principles MD の場合**

::

    XCTYPE GGA_PBE96 /
    PSSET FHI /
    NGRID 36 36 36 /
    KGRID 4 4 4 /
    EKBT 0.001102471005012568 /
    DITER 300 /
    SCFCONV 1e-15 /
    MPVER  0 /
    KINTEG 0 /
    NSWEEP 10 /
    SWSCF 1 /
    SWOPT 3 /
    MDSTEP 2000 /
    MDDT 0.5 /
    MDTEMP 300 /
    MDNHC 200 /
    OC 2 /

First-Principles MD では、以下のように設定が変更・追加されています。

-   SWOPT：分子動力学計算を行う場合、3 に設定します。
-   MDSTEP：分子動力学計算のステップ数を指定します。デフォルトでは 2000 となっています。
-   MDDT：分子動力学計算の１ステップあたりの時間を指定します。デフォルトでは 0.5 fs となっています。
-   MDTEMP：分子動力学計算の温度を指定します。デフォルトでは300 K となっています。
-   MDNHC：分子動力学計算の温度制御で Nose-Hoover Chain 法を選択した場合、振動数を指定します。デフォルトでは 200 cm\ :sup:`-1` となっています。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
rsdft.atom
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

モデルの原子構造の情報を入力するためのファイルで、CIF 形式で記述されています。例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

::

    #kpts  4 4 4
    #ecut 200.00000000000003 212.80243269568317
    #n1 33.945197074108506 36
    #n2 33.945197074108506 36
    #n3 34.90030355804292 36
    #ecut_omx 200.00000000000003 212.80243269568317
    #m1 33.945197074108506 36
    #m2 33.945197074108506 36
    #m3 34.90030355804292 36
    # generated using pymatgen
    data_BaTiO3
    _symmetry_space_group_name_H-M   'P 1'
    _cell_length_a   3.99037921
    _cell_length_b   3.99037921
    _cell_length_c   4.10265539
    _cell_angle_alpha   90.00000000
    _cell_angle_beta   90.00000000
    _cell_angle_gamma   90.00000000
    _symmetry_Int_Tables_number   1
    _chemical_formula_structural   BaTiO3
    _chemical_formula_sum   'Ba1 Ti1 O3'
    _cell_volume   65.32709969
    _cell_formula_units_Z   1
    loop_
     _symmetry_equiv_pos_site_id
     _symmetry_equiv_pos_as_xyz
      1  'x, y, z'
    loop_
     _atom_site_type_symbol
     _atom_site_label
     _atom_site_symmetry_multiplicity
     _atom_site_fract_x
     _atom_site_fract_y
     _atom_site_fract_z
     _atom_site_occupancy
      Ba  Ba0  1  0.50000000  0.50000000  0.58254146  1.0
      Ti  Ti1  1  0.00000000  0.00000000  0.10004270  1.0
      O  O2  1  0.00000000  0.50000000  0.06422054  1.0
      O  O3  1  0.50000000  0.00000000  0.06422054  1.0
      O  O4  1  0.00000000  0.00000000  0.54897175  1.0

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
scfconv.csv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SCF 計算の履歴が出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
optconv.csv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

構造最適化の履歴が出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
band.json
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron Band Structure での、電子バンド図描画用のデータが出力されます。エネルギーの値は、ファイル内の "Band #1" などにハートリー原子単位で記載されています。なお、電子バンド図の縦軸では、これらのエネルギーの値を、ファイル３行目のフェルミエネルギー "efermi" で差し引いた値が表示されています。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dos.json
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Electron DOS での、電子状態密度計算結果のデータが出力されます。電子状態密度曲線の横軸のエネルギーの値は、ファイル内の "x" にハートリー原子単位で記載されています。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
info.dat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First-Principles MD での、各ステップにおけるデータが出力されます。出力される項目は下記の通りです。

-   Born-Oppenheimer MD

    -   経過時間
    -   全エネルギー
    -   全エネルギーの変化量
    -   全エネルギー（DFT）
    -   運動エネルギー
    -   熱浴のエネルギー
    -   温度
    -   Kohn-Sham 方程式の固有値の和

    |

-   Car-Parrinello MD

    -   経過時間
    -   全エネルギー
    -   全エネルギーの変化量
    -   全エネルギー（DFT）
    -   運動エネルギー
    -   仮想的な運動エネルギー
    -   熱浴のエネルギー
    -   温度
    -   Kohn-Sham 方程式の固有値の和
    -   電子の熱浴のエネルギー

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TRAJECTORY.cif
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First-Principles MD での、各ステップにおける Material の構造が出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
rsdft.atom.out.cif
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

構造最適化により得られた最終的な Material の構造が出力されます。

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

SCF 計算、構造最適化、電子バンド計算、電子状態密度計算、MD の計算過程が出力されます。

|
|

--------------------------------------------------------------
LAMMPS
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.lmp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

原子構造の情報を入力するためのファイルです。例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

::

    Generated by pymatgen.io.lammps.data.LammpsData

    5  atoms

    3  atom types

    0.000000 3.990379  xlo xhi
    0.000000 3.990379  ylo yhi
    0.000000 4.102655  zlo zhi

    Masses

    1  137.3270
    2   47.8670
    3   15.9994

    Atoms

    1  1 1.995190 1.995190 2.389967
    2  2 0.000000 0.000000 0.410441
    3  3 0.000000 1.995190 0.263475
    4  3 1.995190 0.000000 0.263475
    5  3 0.000000 0.000000 2.252242

２行目にはモデルに含まれる原子の総数、３行目には原子の種類の総数を指定します。

４行目からはモデルの形状を指定します。 BaTiO3 の場合は直方体なので、x, y, z 各方向の最小値は 0 とし、最大値は各方向の格子ベクトル長さを指定すれば良いのですが、例えば Si（ダイヤモンド構造）の場合は少し複雑です。Si のプリミティブセルの形状は以下の通りです。

    -   a = 3.84 Å
    -   b = 3.84 Å
    -   c = 3.84 Å
    -   α（ab 間の角度）= 60°
    -   β（bc 間の角度）= 60°
    -   γ（ca 間の角度）= 60°

これを入力ファイルで表現すると、次のようになります。

::

    0.000000 3.849278  xlo xhi
    0.000000 3.333574  ylo yhi
    0.000000 3.142923  zlo zhi
    1.924639 1.924639 1.111190  xy xz yz

これらの数値は、以下の関係を満たすように定められています。

    -   **a** = (*x*\ :sub:`hi`\ - *x*\ :sub:`lo`\, 0, 0) 
    -   **b** = (*xy*, *y*\ :sub:`hi`\ - *y*\ :sub:`lo`\, 0)
    -   **c** = (*xz*, *yz*, *z*\ :sub:`hi`\ - *z*\ :sub:`lo`\)

詳しくは LAMMPS のドキュメント（https://docs.lammps.org/create_box.html）をご参照ください。

「Masses」の項目では、質量数により原子の種類を指定し、それに番号づけを行います。上の例では１番が Ba、２番が Ti、３番が O です。

「Atoms」の項目では、「Masses」の項目でつけた番号を使って原子の種類を指定し、各原子の座標を入力します。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
in.QuloudJob
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

構造最適化計算や MD シミュレーションの設定を行うためのファイルです。例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

|

**Atomic Structure Opt. の場合**

::

    #Generated by Quloud
    units metal
    boundary p p p
    atom_style atomic
    read_data QuloudJob.lmp
    replicate 1 1 1
    pair_style chgnet ../../../../../../../../CHGNET
    pair_coeff * * 0.3.0 Ba Ti O
    thermo_style custom step etotal temp density vol press
    thermo 10
    dump 1 all atom 50 QuloudJob.lammpstrj
    fix 1 all box/relax aniso 0.0 vmax 0.001
    minimize 1e-15 0.000001 1000 10000
    write_data QuloudJob.out.lmp

入力パラメータの詳細は以下の通りです。

-   units：単位系を指定します。metal の場合、以下の単位系が使用されます。

    -   質量数：g/mol
    -   距離：Å
    -   時間：ps
    -   エネルギー：eV
    -   速度：Å/ps
    -   力：eV/Å
    -   トルク：eV
    -   温度：K
    -   圧力：bar
    -   粘度：Poise（1 Poise = 0.1 Pa・s）
    -   電荷：電気素量を単位とします。プロトンは +1、電子は -1 となります。
    -   電気双極子モーメント：（電荷）× Å を単位とします。
    -   電場：V/Å
    -   密度：g/(cm^dim)（線密度では dim = 1、面密度では dim = 2、体積密度では dim = 3 とします。）

-   boundary：x, y, z 各方向の境界条件を指定します。デフォルトでは p（周期境界条件）となっています。
-   atom_style：シミュレーションの中身に応じて、原子の属性（電荷や角運動量など）をどこまで計算に盛り込むかを指定します。デフォルトでは、最も基本的な設定の atomic となっています。
-   read_data：シミュレーションで読み込むデータファイルの名前を指定します。デフォルトでは、前述した "QuloudJob.lmp" に設定されています。
-   replicate：シミュレーションのモデルのサイズを指定します。例えば 2 2 2 と設定すると、モデルが x, y, z 各方向に２倍拡大され、原子数は８倍になります。デフォルトでは 1 1 1（等倍）となっています。
-   pair_style：原子間ポテンシャルを指定します。デフォルトでは CHGNET となっています。
-   pair_coeff：pair_style で CHGNET を選択した場合、事前学習モデルのバージョンを指定します。デフォルトでは 0.3.0 となっています。
-   thermo_style：出力する熱力学的データの内容と形式を指定します。上の例では時間ステップ、全エネルギー（ポテンシャルエネルギー + 運動エネルギー）、温度、質量密度、体積、圧力が出力されます。
-   thermo：熱力学的データを出力する頻度を指定します。上の例では 10 ステップごとに出力されます。
-   dump：スナップショットに関する設定を行います。上の例では 50 ステップごとに "QuloudJob.lammpstrj" ファイルに出力されます。
-   fix：構造最適化計算での拘束条件を指定します。上の例ではセルの形状やサイズも最適化します。モデルに加える外圧は異方的で、最適化での目標値は 0.0 です。また、１回の最適化で許容される最大の体積変化率は 0.001 です。
-   minimize：構造最適化計算の収束判定条件を指定します。上の例では、次のいずれかの条件が満たされれば、構造最適化計算は終了します。

    -   エネルギーの変化率が 1e-15 を下回る。
    -   力の大きさが 0.000001 eV/Å を下回る。
    -   構造最適化計算の反復回数が 1000 に達する。
    -   力の大きさの算出回数が 10000 に達する。

-   write_data：データをテキストフォーマットで出力するファイルの名前を指定します。デフォルトでは "QuloudJob.out.lmp" となっています。

|

**Molecular Dynamics の場合**

::

    #Generated by Quloud
    units metal
    boundary p p p
    atom_style atomic
    read_data QuloudJob.lmp
    replicate 1 1 1
    pair_style chgnet ../../../../../../../../CHGNET
    pair_coeff * * 0.3.0 Ba Ti O
    thermo_style custom step etotal temp density vol press
    thermo 10
    dump 1 all atom 50 QuloudJob.lammpstrj
    velocity all create 300 345678 dist gaussian
    timestep 0.001
    fix 1 all nvt temp 300 300 0.1
    run 3000
    unfix 1
    fix 2 all nvt temp 300 300 0.1
    run 3000
    run 10000
    write_data QuloudJob.out.lmp

Molecular Dynamics では、以下のように設定が変更・追加されています。

-   velocity：温度と速度分布を指定します。上の例では温度は 300 K、速度分布はガウシアンとなっています。
-   timestep：MD シミュレーションの時間ステップを指定します。上の例では 0.001 ps となっています。
-   fix：MD 法や温度・圧力の制御に関する設定を行います。上の例では NVT アンサンブル法を採用し、開始時と終了時の温度は 300 K、温度の減衰パラメータは 0.1 ps と設定されています。
-   run：MD シミュレーションを実行するステップ数を指定します。上の例では 3000 ステップ実行されます。
-   unfix：fix で指定した条件での MD シミュレーションを終了するためのコマンドです。"unfix 1" は "fix 1" でのシミュレーションが終了することを意味します。

    上の例では、この後 "fix 2" で新たに条件を設定し、シミュレーションをまず 3000 ステップ、次に 10000 ステップ実行します。

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

|
|

--------------------------------------------------------------
FLARE
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On-The-Fly 機械学習、MD 計算、第一原理計算の設定が、この一つのファイルにまとめられます。例えば Material を BaTiO3 として Job を登録すると、以下のようなファイルが作成されます。

::

    dft_calc:
      kwargs:
        command: mpirun -np 1 pw.x -in espresso.pwi > espresso.pwo
        input_data:
          control:
            calculation: scf
            outdir: ./work
            prefix: QuloudJob
            pseudo_dir: ./
            tprnfor: true
            tstress: true
            verbosity: high
          electrons:
            conv_thr: 1.0e-10
            electron_maxstep: 100
            mixing_beta: 0.7
          system:
            degauss: 0.01
            ecutrho: 0
            ecutwfc: 0
            ibrav: 0
            nat: 5
            nspin: 1
            ntyp: 3
            occupations: smearing
            smearing: gauss
            tot_charge: 0
        koffset:
        - 0
        - 0
        - 0
        kpts:
        - 4
        - 4
        - 4
        pseudopotentials:
          Ba: Ba.pbe-spn-rrkjus_psl.1.0.0.UPF
          O: O.pbe-nl-rrkjus_psl.1.0.0.UPF
          Ti: Ti.pbe-spn-rrkjus_psl.1.0.0.UPF
      name: Espresso
    flare_calc:
      cutoff: 5
      descriptors:
      - cutoff_function: quadratic
        lmax: 3
        name: B2
        nmax: 5
        radial_basis: chebyshev
      energy_noise: 0.01
      forces_noise: 0.05
      gp: SGP_Wrapper
      kernels:
      - name: NormalizedDotProduct
        power: 2
        sigma: 2
      max_iterations: 20
      species:
      - 56
      - 22
      - 8
      stress_noise: 0.005
      use_mapping: true
      variance_type: local
    otf:
      dt: 0.001
      force_only: true
      initial_velocity: 800
      max_atoms_added: -1
      md_engine: Langevin
      md_kwargs:
        friction: 0.101805057
        temperature_K: 800
      mode: fresh
      number_of_steps: 2000
      output_name: myotf
      std_tolerance_factor: -0.04
      store_dft_output:
      - - espresso.pwo
      - ./dft_res
      train_hyps:
      - 10
      - inf
      update_style: threshold
      update_threshold: 0.02
      wandb_log: null
      write_model: 4
    supercell:
      file: rsdft.atom
      format: cif
      jitter: 0.0
      replicate:
      - 1
      - 1
      - 1

入力パラメータの詳細は以下の通りです。

-   dft_calc

  -   kwargs

    -   command：Job 実行時のコマンドを入力します。
    -   input_data：第一原理計算のためのパラメータを設定します。記述の方法は Quantum ESPRESSO の入力ファイルと同様です。
    -   koffset：k 点グリッドのオフセットを指定します。
    -   kpts：各方向の k 点グリッドの数を指定します。
    -   pseudopotentials：擬ポテンシャルファイルを指定します。

  -   name：第一原理計算に用いる ASE Calculator の種類を指定します。ここでは Quantum ESPRESSO を使用しているので、Espresso となっています。

-   flare_calc

  -   cutoff：原子近傍を定義する距離を Å 単位で指定します。これ以上の距離での相互作用は無視されます。
  -   descriptors

    -   cutoff_function：原子近傍を定義するための関数形を指定します。
    -   lmax：角度情報を担う球面調和関数の角運動量最大値を指定します。
    -   name：記述子の名前を指定します。
    -   nmax：使用する動径関数の数を指定します。
    -   radial_basis：動径関数の形を指定します。

  -   energy_noise：エネルギーを確率分布とするためのばらつきの程度を指定します。
  -   forces_noise：力を確率分布とするためのばらつきの程度を指定します。
  -   gp：ガウス過程のタイプを指定します。
  -   kernels

    -   name：カーネル関数のタイプを指定します。
    -   power：NormalizedDotPrduct のべきを指定します。有効な値の範囲は ≦2 です。
    -   sigma：variance を指定します。

  -   max_iterations：ハイパーパラメータ最適化のための反復計算上限を指定します。
  -   species：原子の種類を質量数により指定します。
  -   stress_noise：ストレスを確率分布とするためのばらつきの程度を指定します。
  -   use_mapping：true の場合、LAMMPS 用の coefficients ファイルを出力します。
  -   variance_type：local の場合、誤差評価に local energy variance を用います。

-   otf

  -   dt：MD の時間幅（ps）を指定します。
  -   force_only：True の場合は Force のみで学習を行います。False の場合はエネルギーとストレスも学習します。
  -   initial_velocity：温度 (K) で設定します。
  -   max_atoms_added：DFT 計算後に GP モデルに追加する原子数の上限を指定します。 =-1 は「上限なし」を意味します。
  -   md_engine：Langevin または NPT が選択できます。
  -   md_kwargs

    -   friction：Langevin ダイナミクス用の摩擦パラメータを指定します。
    -   temperature_K：温度 (K) を指定します。

  -   mode：fresh / restart（新規計算か継続計算か）を指定します。
  -   number_of_steps：MD を実行するステップ数を指定します。
  -   output_name：出力ファイルの名前を指定します。
  -   std_tolerance_factor：DFT 計算を実行する誤差の閾値を指定します。
  -   store_dft_output：DFT 計算のデータを保存するためのパラメータを指定します。
  -   train_hyps：指定した DFT 計算のタイミングでハイパーパラメータの最適化を行います。
  -   update_style：threshold の場合、全ての原子が誤差の基準を超えたら DFT 計算を実行して更新します。
  -   update_threshold：update_style=threshold のときの誤差評価基準を指定します。
  -   wandb_log：ログデータを WandB のリモートサーバーにアップロードすることもできますが、Quloud ではこの機能は利用しません。
  -   write_model：ログおよびファイルの出力量を指定します。推奨値は 4 です。

-   supercell

  -   file：原子構造を読み込むファイル名を指定します。ここでは "rsdft.atom" ファイルから読み込みます。
  -   format：原子構造ファイルのフォーマットを指定します。"rsdft.atom" ファイルは CIF 形式なので、cif となっています。
  -   jitter：完全な結晶構造から計算を始める場合には、原子座標に少しバラツキを与えることが推奨されています。ここではオングストローム（Å）単位でバラツキの大きさを指定できます。Quloud でのデフォルト値は 0.0 Å です。
  -   replicate：シミュレーションのモデルのサイズを指定します。例えば縦に 2 2 2 と記すと、モデルが x, y, z 各方向に２倍拡大され、原子数は８倍になります。デフォルトでは 1 1 1（等倍）となっています。

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

|
|

--------------------------------------------------------------
ASE
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ase.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

**OPT の場合**

::

    {"mode":"opt","opt":{"fmax":0.05,"ntime":100,"latopt":true},"provider":"7net","model_name":"7net-mf-ompa"}

入力パラメータの詳細は以下の通りです。

-   mode：計算のモード（opt あるいは md）を指定します。
-   opt

    -   fmax：構造最適化計算での力の収束条件を eV/Å 単位で指定します。
    -   ntime：構造最適化計算のステップ数を指定します。
    -   latopt：格子定数を最適化する場合には true とします。

-   provider：機械学習ポテンシャルのプロバイダー（SevenNet あるいは fairchem）を指定します。
-   model_name：機械学習ポテンシャルの具体的な名前が表示されます。

**MD の場合**

::

    {"mode":"md","md":{"dtime":0.001,"ntime":2000,"ensemble":"nvt","temperature":300},"provider":"7net","model_name":"7net-mf-ompa"}

入力パラメータの詳細は以下の通りです。

-   mode：計算のモード（opt あるいは md）を指定します。
-   md

    -   dtime：MD シミュレーションの時間ステップを ps 単位で指定します。
    -   ntime：MD シミュレーションのステップ数を指定します。
    -   ensemble：MD シミュレーションのアンサンブル法を指定します。
    -   temperature：MD シミュレーションの温度を指定します。

-   provider：機械学習ポテンシャルのプロバイダー（SevenNet あるいは fairchem）を指定します。
-   model_name：機械学習ポテンシャルの具体的な名前が表示されます。

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
neb_summary.json
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NEB 計算でのエネルギープロファイルのデータが出力されます。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.traj
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NEB 計算での構造変化のトラジェクトリーが出力されます。

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

|
|

--------------------------------------------------------------
SPRKKR
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
occupation.dat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First-Principles SCF で使用するファイルです。モデルの各サイトを、どの原子がどの割合で占有しているかを指定しています。

::

    {"Ba":1}
    {"Ti":1}
    {"O":1}
    {"O":1}
    {"O":1}

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob.pot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

直前の SCF 計算で出力されたポテンシャルデータを保存し、次の計算の入力として使用するためのファイルです。使用手順は下記の通りです。

    １．ダミーのポテンシャルファイル「QuloudJob.pot」を用意して First-Principles SCF の計算を実行する

    ２．First-Principles SCF で出力されたポテンシャルファイル「QuloudJob.pot_new」を、次の Exchange Coupling Parameters の入力ファイル「QuloudJob.pot」として計算を実行する

|

**First-Principles SCF の場合**

下記のようなダミーのポテンシャルファイルを用意して SCF 計算を実行します。

::

    *******************************************************************************
    HEADER      	SPR-KKR potential file, created at 2025-10-24 13:18:50.728285
    *******************************************************************************
    TITLE       	Created by ASE-SPR-KKR wrapper
    SYSTEM      	System: BaTiO3
    PACKAGE     	SPR-KKR
    FORMAT      	 7 (21.05.2007)
    *******************************************************************************
    GLOBAL SYSTEM PARAMETER
    NQ          	5
    NT          	4
    NM          	4
    IREL        	3
    *******************************************************************************
    SCF-INFO
    INFO        	NONE
    SCFSTATUS   	START
    FULLPOT     	F
    BREITINT    	F
    NONMAG      	F
    ORBPOL      	NONE
    EXTFIELD    	F
    BLCOUPL     	F
    BEXT        	0.0
    SEMICORE    	F
    LLOYD       	F
    SCF-ITER    	0
    SCF-MIX     	0.2
    SCF-TOL     	1e-05
    RMSAVV      	999999.0
    RMSAVB      	999999.0
    EF          	999999.0
    VMTZ        	0.7
    *******************************************************************************
    LATTICE
    SYSDIM      	3D
    SYSTYPE     	BULK
    BRAVAIS     	 8 tetragonal primitive 4/mmm D_4h
    ALAT        	7.540723845133523
    A(1)             1.00000000000000       0.00000000000000       0.00000000000000
    A(2)             0.00000000000000       1.00000000000000       0.00000000000000
    A(3)             0.00000000000000       0.00000000000000       1.02813671936708
    *******************************************************************************
    SITES
    CARTESIAN   	T
    BASSCALE    	1.0 1.0 1.0
       IQ                QBAS(X)                QBAS(Y)                QBAS(Z)
        1       0.50000000000000       0.50000000000000       0.59893226557971
        2       0.00000000000000       0.00000000000000       0.10285757337462
        3       0.00000000000000       0.50000000000000       0.06602749531158
        4       0.50000000000000       0.00000000000000       0.06602749531158
        5       0.00000000000000       0.00000000000000       0.56441801407020
    *******************************************************************************
    OCCUPATION
    IQ              IREFQ              IMQ              NOQ        ITOQ CONC
    1                   1                1                1            1 1.0
    2                   2                2                1            2 1.0
    3                   3                3                1            3 1.0
    4                   3                3                1            3 1.0
    5                   4                4                1            4 1.0
    *******************************************************************************
    REFERENCE SYSTEM
    NREF        	4
    IREF                   VREF                 RMTREF
    1                       4.0                    0.0
    2                       4.0                    0.0
    3                       4.0                    0.0
    4                       4.0                    0.0
    *******************************************************************************
    MAGNETISATION DIRECTION
    KMROT       	0
    QMVEC       	0.0 0.0 0.0
    IQ                   MTET_Q                 MPHI_Q
    1                       0.0                    0.0
    2                       0.0                    0.0
    3                       0.0                    0.0
    4                       0.0                    0.0
    5                       0.0                    0.0
    *******************************************************************************
    MESH INFORMATION
    MESH-TYPE   	EXPONENTIAL
       IM             R(1)               DX             JRMT              RMT             JRWS              RWS
        1            1e-06             0.02                0              0.0              721              0.0
        2            1e-06             0.02                0              0.0              721              0.0
        3            1e-06             0.02                0              0.0              721              0.0
        4            1e-06             0.02                0              0.0              721              0.0
    *******************************************************************************
    TYPES
    IT                TXT               ZT            NCORT            NVALT      NSEMCORSHLT
    1                  Ba               56               54                2                0
    2                  Ti               22               18                4                0
    3                   O                8                2                6                0
    4                   O                8                2                6                0

入力パラメータの詳細は以下の通りです。

-   HEADER：ファイル種別と生成日時を表します。
-   TITLE：ファイルの生成元についての記載です。
-   SYSTEM：系の名前を表します。
-   PACKAGE：ファイルの形式・所属パッケージを表します。
-   FORMAT：ファイルのフォーマット版を表します。
-   GLOBAL SYSTEM PARAMETER

    -   NQ：格子サイトの総数を指定します。
    -   NT：原子タイプの総数を指定します。
    -   NM：半径メッシュの総数を指定します。
    -   IREL：このファイルをつくった SCF ポテンシャルが、どのような相対論的枠組みで得られたものかを表します。具体的には、

        -   スカラー相対論（SP-SREL）で得られたポテンシャルの場合：2
        -   完全相対論（FREL）で得られたポテンシャルの場合：3

        となります。初期状態では 3 となります。

-   SCF-INFO

    -   INFO：補足情報があればここに記載されます。
    -   SCFSTATUS：SCF 計算のステータスを表します。これから計算を行うので START となっています。
    -   FULLPOT：full-potential 計算を使ったかどうかを表します。デフォルトでは F（使用せず）となっています。
    -   BREITINT：Breit 相互作用を考慮したかどうかを表します。デフォルトでは F（考慮せず）となっています。
    -   NONMAG：非磁性計算を行ったかどうかを表します。デフォルトでは F（磁性あり）となっています。
    -   ORBPOL：軌道分極補正を入れたかどうかを表します。デフォルトでは NONE（補正なし）となっています。
    -   EXTFIELD：外部磁場を入れたかどうかを表します。デフォルトでは F（なし）となっています。
    -   BEXT：外部磁場の大きさを表します。デフォルトでは 0.0 となっています。
    -   SEMICORE：semicore 状態を特別扱いしたかどうかを表します。デフォルトでは F（特別扱いせず）となっています。
    -   LLOYD：Lloyd formula を使ったかどうかを表します。デフォルトでは F（使用せず）となっています。
    -   SCF-ITER：現在までの SCF 計算の反復回数を表します。まだ計算が始まっていないので 0 となっています。
    -   SCF-MIX：SCF 計算での電荷/ポテンシャルの混合率を表します。デフォルトでは 0.2 となっています。
    -   SCF-TOL：SCF 計算での収束判定のしきい値を表します。デフォルトでは 1e-05 となっています。
    -   RMSAVV：直前の SCF 計算の最終反復での、ポテンシャル関数 V の RMS 誤差を表します。RMS 誤差がまだ評価されていないので、「未定」を表す目印として、極端に大きな数がダミー値として入っています。
    -   RMSAVB：直前の SCF 計算の最終反復での、スピン依存有効磁場 B の RMS 誤差を表します。RMS 誤差がまだ評価されていないので、「未定」を表す目印として、極端に大きな数がダミー値として入っています。

        ポテンシャル関数 V、スピン依存有効磁場 B については、SPRKKR ユーザーマニュアル（https://www.ebert.cup.uni-muenchen.de/index.php/en/repository/SPRKKR/SPRKKR-8.6-Manual/lang,en-gb/）の 1.2 をご参照ください。

    -   EF：フェルミ準位を表します。フェルミ準位がまだ計算されていないので、「未定」を表す目印として、極端に大きな数がダミー値として入っています。
    -   VMTZ：新しく採用した muffin-tin zero というポテンシャルエネルギーの原点が、もとのポテンシャルの基準からみてどこにあるかを表します。デフォルトでは 0.7 となっています。

-   LATTICE

    -   SYSDIM：モデルの次元数を指定します。立体モデルなので 3D とします。
    -   SYSTYPE：モデルのタイプを指定します。バルク系なので BULK とします。
    -   BRAVAIS：ブラべ格子を番号と名称で指定します。対応する番号は、xband ユーザーマニュアル（https://www.ebert.cup.uni-muenchen.de/index.php/en/repository/SPRKKR/xband-manual/lang,en-gb/）の Table II をご参照ください。
    -   ALAT：格子ベクトル長さを Bohr 単位で指定します。
    
        まず、ALAT 項目で基準となる長さ（ここでは 7.540723845133523 Bohr）を記入します。次の A(1)、A(2)、A(3) 項目では、３つの格子ベクトルの各方向成分を、ALAT で定めた長さを基準とした相対値で記入します。例えば、A(1) ベクトルの第１成分は 7.540723845133523 Bohr × 1 = 7.540723845133523 Bohr ≃ 3.99 Å となり、A(3) ベクトルの第３成分は 7.540723845133523 Bohr × 1.02813671936708 = 7.75289507579 Bohr ≃ 4.10 Å となります。

-   SITES

    -   CARTESIAN：座標が Cartesian の場合は T、格子ベクトルを基準とした分率座標の場合は F とします。デフォルトでは T（Cartesian）となっています。
    -   BASSCALE：座標のスケール因子です。ここでの設定に応じて、QBAS(X)、QBAS(Y)、QBAS(Z) の各成分に追加の倍率がかかります。例えば 2.0 3.0 4.0 と設定すると、QBAS(X) を２倍、QBAS(Y) を３倍、QBAS(Z) を４倍した値が使用されます。デフォルトでは 1.0 1.0 1.0 となっています。
    -   IQ：格子サイトの番号を表します。
    -   QBAS(X)：各格子サイト位置の x 成分を表します。
    -   QBAS(Y)：各格子サイト位置の y 成分を表します。
    -   QBAS(Z)：各格子サイト位置の z 成分を表します。

-   OCCUPATION

    -   IQ：格子サイトの番号を表します。
    -   IREFQ：その格子サイトが参照する reference system の番号を表します。
    -   IMQ：その格子サイトが参照する半径メッシュの番号を表します。
    -   NOQ：その格子サイト上の成分数を表します。単一占有の場合は 1 とします。
    -   ITOQ：その成分の原子タイプの番号を表します。
    -   CONC：その成分の濃度を表します。100% の場合は 1.0 とします。

-   REFERENCE SYSTEM

    -   NREF：reference system の総数を表します。
    -   IREF：reference system の番号を表します。

-   MAGNETISATION DIRECTION

    -   KMROT：磁化方向の回転設定に関するフラグです。
    -   QMVEC：結晶中で磁化が空間的にねじれていくパターンの周期と方向を決める波数ベクトルです。
    -   IQ：格子サイトの番号を表します。
    -   MTET_Q：QMVEC = **0** のもとでの、磁化方向の極角 *θ* を表します。
    -   MPHI_Q：QMVEC = **0** のもとでの、磁化方向の方位角 *φ* を表します。

-   MESH INFORMATION

    -   MESH-TYPE：半径メッシュの型を表します。デフォルトでは EXPONENTIAL（指数メッシュ）となっています。
    -   IM：半径メッシュの番号を表します。
    -   R(1)：半径メッシュの一番内側にある、原点に非常に近い最初の半径点を表します。
    -   DX：対数刻みを表します。
    -   JRMT：muffin-tin 半径に対応するメッシュ点番号を表します。
    -   RMT：muffin-tin 半径を表します。
    -   JRWS：Wigner-Seitz 半径に対応するメッシュ点番号を表します。
    -   RWS：Wigner-Seitz 半径を表します。

-   TYPES

    -   IT：原子タイプの番号を表します。
    -   TXT：元素記号を表します。
    -   ZT：原子番号を表します。
    -   NCORT：コア電子数を表します。
    -   NVALT：価電子数を表します。
    -   NSEMCORSHLT：semicore として扱う殻の数を表します。

|

**Exchange Coupling Parameters の場合**

直前の SCF 計算で出力された「QuloudJob.pot_new」ファイルの中身をそのまま使用します。

::

    *******************************************************************************
    HEADER    'SPR-KKR dataset created by KKRSCF    '
    *******************************************************************************
    TITLE     'DOS for SCF-start'
    SYSTEM    System:
    PACKAGE   SPR-KKR   
    FORMAT     9 (18.01.2019)
    *******************************************************************************
    GLOBAL SYSTEM PARAMETER
    NQ                 5
    NT                 4
    NM                 4
    IREL               3
    NSPIN              1
    *******************************************************************************
    SCF-INFO  
    INFO      'SPR-KKR-ASA'
    SCFSTATUS 'CONVERGED '
    FULLPOT   F
    BREITINT  F
    NONMAG    F
    ORBPOL    NONE      
    EXTFIELD  F
    BLCOUPL   F
    BEXT        0.00000000000000E+00
    SEMICORE  F
    LLOYD     F
    NE                32         0
    IBZINT             2
    NKTAB            552
    TETDEPPOT F
    XC-POT    VWN       
    SCF-ALG   BROYDEN2  
    SCF-ITER          19
    SCF-MIX     2.00000000000000E-01
    SCF-TOL     1.00000000000000E-05
    RMSAVV      7.26126299506257E-06
    RMSAVB      4.14572487291295E-14
    EF          7.70078753718801E-01
    VMTZ       -7.41852774518500E-01
    *******************************************************************************
    LATTICE   
    SYSDIM    '3D        '
    SYSTYPE   'BULK                          '
    BRAVAIS            8     tetragonal  primitive      4/mmm  D_4h
    ALAT        7.54072384513352E+00
    A(1)        1.00000000000000E+00  0.00000000000000E+00  0.00000000000000E+00
    A(2)        0.00000000000000E+00  1.00000000000000E+00  0.00000000000000E+00
    A(3)        0.00000000000000E+00  0.00000000000000E+00  1.02813671936708E+00
    *******************************************************************************
    SITES     
    CARTESIAN T
    BASSCALE    1.00000000000000E+00  1.00000000000000E+00  1.00000000000000E+00
            IQ        QBAS(X)               QBAS(Y)               QBAS(Z)
            1  5.00000000000000E-01  5.00000000000000E-01  5.98932265579710E-01
            2  1.00000000000000E+00  1.00000000000000E+00  1.02857573374620E-01
            3  1.00000000000000E+00  5.00000000000000E-01  6.60274953115800E-02
            4  5.00000000000000E-01  1.00000000000000E+00  6.60274953115800E-02
            5  1.00000000000000E+00  1.00000000000000E+00  5.64418014070200E-01
    *******************************************************************************
    OCCUPATION
            IQ     IREFQ       IMQ       NOQ  ITOQ  CONC
            1         1         1         1     1 1.00000
            2         2         2         1     2 1.00000
            3         3         3         1     3 1.00000
            4         3         3         1     3 1.00000
            5         4         4         1     4 1.00000
    *******************************************************************************
    REFERENCE SYSTEM FOR TIGHT BINDING MODE
    NREF               4
        IREF       VREF                  RMTREF
            1  4.00000000000000E+00  0.00000000000000E+00
            2  4.00000000000000E+00  0.00000000000000E+00
            3  4.00000000000000E+00  0.00000000000000E+00
            4  4.00000000000000E+00  0.00000000000000E+00
    *******************************************************************************
    HOST MADELUNG POTENTIAL
            IQ      VLMMAD
    NLMTOP-POT         4
            1   1 -7.38780209222572E-01
            1   2  0.00000000000000E+00
            1   3  0.00000000000000E+00
            1   4  0.00000000000000E+00
            2   1  2.67827727693005E+00
            2   2  0.00000000000000E+00
            2   3  0.00000000000000E+00
            2   4  0.00000000000000E+00
            3   1 -1.21710003949274E+00
            3   2  0.00000000000000E+00
            3   3  0.00000000000000E+00
            3   4  0.00000000000000E+00
            4   1 -1.21710003949274E+00
            4   2  0.00000000000000E+00
            4   3  0.00000000000000E+00
            4   4  0.00000000000000E+00
            5   1 -6.11415601463066E-01
            5   2  0.00000000000000E+00
            5   3  0.00000000000000E+00
            5   4  0.00000000000000E+00
    *******************************************************************************
    CHARGE MOMENTS
            IQ      CMNTQ 
    NLMTOP-CHR         4
            1   1  1.30544191044029E-01
            1   2 -1.43264855429539E-19
            1   3  7.82179087843899E-02
            1   4  5.84276265521740E-19
            2   1 -3.27632716349814E-01
            2   2 -1.98986331766841E-20
            2   3  1.05455980839858E-01
            2   4 -6.37231864968248E-20
            3   1  8.89458533030423E-02
            3   2  2.27507558209204E-23
            3   3  4.64470194726833E-03
            3   4  5.43716151224347E-20
            4   1  8.89458533030423E-02
            4   2  5.43716151224347E-20
            4   3  4.64470194726833E-03
            4   4 -2.27507558209204E-23
            5   1  1.91968186997027E-02
            5   2  2.44079477578207E-20
            5   3 -1.44113920770928E-02
            5   4  1.12734559057116E-21
    *******************************************************************************
    MAGNETISATION DIRECTION
    KMROT              0
    QMVEC       0.00000000000000E+00  0.00000000000000E+00  0.00000000000000E+00
            IQ       MTET_Q                MPHI_Q                MGAM_Q
            1  0.00000000000000E+00  0.00000000000000E+00
            2  0.00000000000000E+00  0.00000000000000E+00
            3  0.00000000000000E+00  0.00000000000000E+00
            4  0.00000000000000E+00  0.00000000000000E+00
            5  0.00000000000000E+00  0.00000000000000E+00
            IT       MTET_T                MPHI_T                MGAM_T
            1  0.00000000000000E+00  0.00000000000000E+00  0.00000000000000E+00
            2  0.00000000000000E+00  0.00000000000000E+00  0.00000000000000E+00
            3  0.00000000000000E+00  0.00000000000000E+00  0.00000000000000E+00
            4  0.00000000000000E+00  0.00000000000000E+00  0.00000000000000E+00
    *******************************************************************************
    MESH INFORMATION
    MESH-TYPE EXPONENTIAL 
    IM       R(1)                  DX              JRMT       RMT             JRWS       RWS
        1  1.00000000000000E-06  2.11226382337071E-02  710  3.19258073545723E+00  721  4.02606297956194E+00
        2  1.00000000000000E-06  2.04358001179938E-02  709  1.94703198558424E+00  721  2.45534069354115E+00
        3  1.00000000000000E-06  2.02042400622768E-02  709  1.64803375598263E+00  721  2.07828344647323E+00
        4  1.00000000000000E-06  2.01040588486880E-02  709  1.53334625274198E+00  721  1.93365464949797E+00
    *******************************************************************************
    TYPES
    IT     TXT_T            ZT     NCORT     NVALT    NSEMCORSHLT
        1     Ba              56        48         8            0
        2     Ti              22        18         4            0
        3     O_1              8         2         6            0
        4     O_2              8         2         6            0
    *******************************************************************************
    POTENTIAL
    TYPE               1
    -1.11999469477566E+08 -1.09658544071915E+08 -1.07366546619534E+08 -1.05122454471514E+08 -1.02925266353452E+08
    -1.00774001918701E+08 -9.86677013109542E+07 -9.66054247359731E+07 -9.45862520422699E+07 -9.26092823105519E+07
    -9.06736334517462E+07 -8.87784418134277E+07 -8.69228617944718E+07 -8.51060654677632E+07 -8.33272422107886E+07
        ・・・
        ・・・
    1.23420077058742E-14  1.24703973885994E-14  1.25242460681231E-14  1.24855259732370E-14  1.23250831736239E-14
    1.21662656107035E-14  1.18797166271472E-14  1.15316639465576E-14  1.10606941225236E-14  1.06432370020484E-14
    1.00887584255439E-14  9.56576191802020E-15  9.05961729473247E-15  8.58832306904877E-15  8.05352886577341E-15
    7.52030090613412E-15
    ===============================================================================
    TYPE               2
    -4.39998563820181E+07 -4.31098065844003E+07 -4.22377610738086E+07 -4.13833556522457E+07 -4.05462334888585E+07
    -3.97260449709125E+07 -3.89224475577811E+07 -3.81351056378879E+07 -3.73636903885433E+07 -3.66078796386158E+07
    -3.58673577339821E+07 -3.51418154056979E+07 -3.44309496408361E+07 -3.37344635559378E+07 -3.30520662730228E+07
        ・・・
        ・・・
    1.03608469501841E-13  1.02684543969764E-13  1.01319851117324E-13  9.94317101570969E-14  9.70275818791722E-14
    9.41467233944479E-14  9.07762331834141E-14  8.70347613287822E-14  8.28061024469178E-14  7.84317298408356E-14
    7.37498385033811E-14  6.89116535350524E-14  6.39652189190809E-14  5.89883412755714E-14  5.40471354982090E-14
    4.91594744774126E-14
    ===============================================================================
    TYPE               3
    -1.59999681213153E+07 -1.56799440875867E+07 -1.53663210152309E+07 -1.50589708754056E+07 -1.47577682000378E+07
    -1.44625900306043E+07 -1.41733158679369E+07 -1.38898276230322E+07 -1.36120095688438E+07 -1.33397482930403E+07
    -1.30729326517072E+07 -1.28114537239753E+07 -1.25552047675563E+07 -1.23040811751681E+07 -1.20579804318314E+07
        ・・・
        ・・・
    7.56126405771841E-15  8.03124316556877E-15  8.63713875411746E-15  9.30195913027950E-15  1.00088839585291E-14
    1.08316496867109E-14  1.17703571327370E-14  1.27922728275666E-14  1.39060705283880E-14  1.52019211798420E-14
    1.65864707183789E-14  1.81297978609719E-14  1.98593872920532E-14  2.17569727539044E-14  2.38917825272278E-14
    2.61547011067024E-14
    ===============================================================================
    TYPE               4
    -1.59999681242798E+07 -1.56815150082609E+07 -1.53694001664237E+07 -1.50634974460705E+07 -1.47636832053612E+07
    -1.44698362633387E+07 -1.41818378509494E+07 -1.38995715630379E+07 -1.36229233112982E+07 -1.33517812781599E+07
    -1.30860358715938E+07 -1.28255796808157E+07 -1.25703074328726E+07 -1.23201159500928E+07 -1.20749041083829E+07
        ・・・
        ・・・
    4.56648259705269E-15  5.11014492473585E-15  5.66290707785817E-15  6.32089385567594E-15  6.87701110687314E-15
    7.73619847543746E-15  8.50834430753839E-15  9.45644287397971E-15  1.04611574363904E-14  1.15285224064725E-14
    1.27080431267601E-14  1.39939478804894E-14  1.54455805360826E-14  1.70488927943798E-14  1.87215485512092E-14
    2.05705891348374E-14
    ===============================================================================
    *******************************************************************************
    CHARGE
    TYPE               1
    9.09915773446004E+06  9.06563630338208E+06  9.03223790302782E+06  8.99896207372312E+06  8.96580835848412E+06
    8.93277629979895E+06  8.89986544245292E+06  8.86707533327950E+06  8.83440552015420E+06  8.80185555285638E+06
    8.76942498257043E+06  8.73711336200057E+06  8.70492024536020E+06  8.67284518836969E+06  8.64088774823712E+06
        ・・・
        ・・・
    -2.37625857226148E-14 -2.30332555200751E-14 -2.23524974030677E-14 -2.16560181720625E-14 -2.09173632839180E-14
    -2.02554697254343E-14 -1.96508218702764E-14 -1.90590758695970E-14 -1.84358878838547E-14 -1.77686812068813E-14
    -1.72785247081236E-14 -1.65888750213643E-14 -1.61505434651370E-14 -1.56925879807993E-14 -1.51973225858114E-14
    -1.48396155991761E-14
    ===============================================================================
    TYPE               2
    1.18713170857022E+05  1.18650144596237E+05  1.18587149577196E+05  1.18524185739508E+05  1.18461253044032E+05
    1.18398351405853E+05  1.18335480764440E+05  1.18272641064585E+05  1.18209832221802E+05  1.18147054187318E+05
    1.18084306881051E+05  1.18021590251093E+05  1.17958904211054E+05  1.17896248708729E+05  1.17833623657333E+05
        ・・・
        ・・・
    -4.64674143355363E-13 -4.40716980435499E-13 -4.17563089065838E-13 -3.94981805821850E-13 -3.73095429342592E-13
    -3.51901927271298E-13 -3.31065224703324E-13 -3.11067494049394E-13 -2.91546964818058E-13 -2.72739939392025E-13
    -2.54504062567452E-13 -2.36601650722412E-13 -2.19502624681335E-13 -2.02846026921645E-13 -1.86739979965459E-13
    -1.70976751162668E-13
    ===============================================================================
    TYPE               3
    4.01780428333377E+03  4.01752610141834E+03  4.01724791135457E+03  4.01696971264700E+03  4.01669150558502E+03
    4.01641328873491E+03  4.01613506193621E+03  4.01585682412184E+03  4.01557857498118E+03  4.01530031401882E+03
    4.01502204037641E+03  4.01474375370139E+03  4.01446545304958E+03  4.01418713816837E+03  4.01390880794248E+03
        ・・・
        ・・・
    -4.38491115603422E-14 -4.48634997446923E-14 -4.63308659666804E-14 -4.77724263865018E-14 -4.94303914140138E-14
    -5.13164433474401E-14 -5.33218096179980E-14 -5.55554796947589E-14 -5.81068189423232E-14 -6.06317016379958E-14
    -6.34879145137479E-14 -6.66650492816115E-14 -6.97354966266269E-14 -7.33730882532258E-14 -7.69068114662477E-14
    -8.07483378874411E-14
    ===============================================================================
    TYPE               4
    4.01698893605441E+03  4.01671218342760E+03  4.01643542284545E+03  4.01615865473202E+03  4.01588187826486E+03
    4.01560509231119E+03  4.01532829647505E+03  4.01505149027259E+03  4.01477467303141E+03  4.01449784420744E+03
    4.01422100297871E+03  4.01394414911958E+03  4.01366728162217E+03  4.01339040005025E+03  4.01311350353734E+03
        ・・・
        ・・・
    -2.99238228286046E-14 -3.21696429083602E-14 -3.45592289801610E-14 -3.68811601380678E-14 -3.94966925612787E-14
    -4.19931784952292E-14 -4.46893730805895E-14 -4.73745615527670E-14 -5.04532051670474E-14 -5.33302397992902E-14
    -5.66665407541314E-14 -5.98406432828421E-14 -6.31678333728126E-14 -6.67465566226183E-14 -7.01630814576350E-14
    -7.41546653865533E-14
    ===============================================================================
    *******************************************************************************
    MOMENTS        QEL  NOS  SPN  ORB  HFI
    TYPE               1
    5.64627671082587E+01  8.46276710825868E+00 -4.76079904146277E-13 -4.84814332112910E-14 -2.25251178415955E-05
    ===============================================================================
    TYPE               2
    2.08385722604463E+01  2.83857226044627E+00 -5.05649283918066E-12 -1.11210621370234E-12  1.58436534205542E-05
    ===============================================================================
    TYPE               3
    8.31530484041811E+00  6.31530484041811E+00 -1.85539356157092E-13  4.00077588740545E-14 -7.02160193567428E-06
    ===============================================================================
    TYPE               4
    8.06805095045885E+00  6.06805095045884E+00 -7.30312145062514E-14  7.19267633188792E-13 -6.41694377374235E-06
    ===============================================================================

SCF 計算実行後は、以下のように設定が変更・追加されています。

-   GLOBAL SYSTEM PARAMETER

    -   NSPIN：スピン表現に関する内部情報です。

-   SCF-INFO

    -   INFO：ASA 近似で得られたポテンシャルなので SPR-KKR-ASA となっています。
    -   SCFSTATUS：SCF 計算が収束済みなので CONVERGED となっています。
    -   NE：SCF 計算で使われたエネルギーメッシュ点の数を表します。
    -   IBZINT：既約ブリルアンゾーンでどの積分法を使ったかを表す内部コードです。
    -   NKTAB：special points method によるブリルアンゾーン積分で、実際に使われた k 点の数を表します。
    -   TETDEPPOT：tetrahedron 法に関する内部フラグです。ここでは F（無効）となっています。
    -   XC-POT：SCF 計算で実際に使われた交換相関ポテンシャルの種類を表します。ここでは VWN（Vosko-Wilk-Nusair 型の LSDA 交換相関ポテンシャル）となっています。
    -   SCF-ALG：SCF 計算で実際に使われた混合・収束アルゴリズムを表します。ここでは BROYDEN2（Broyden の第２法）となっています。
    -   SCF-ITER：SCF 計算が収束済みなので、実際の反復回数に更新されています。
    -   RMSAVV：ダミー値から実際の収束誤差に更新されています。
    -   RMSAVB：ダミー値から実際の収束誤差に更新されています。
    -   EF：ダミー値から実際のフェルミ準位に更新されています。
    -   VMTZ：デフォルト値から収束後の値に更新されています。

-   HOST MADELUNG POTENTIAL

    -   IQ：格子サイトの番号を表します。
    -   VLMMAD：その格子サイトでの Madelung potential の多極展開係数を表します。
    -   NLMTOP-POT：Madelung potential をどこまでの多極成分で展開しているかを表す上限数です。ここでは、各格子サイトについて４個の成分が保存されています。

    各データ行の

    ::

        IQ   n   value

    は、

        -   １列目　IQ：格子サイトの番号
        -   ２列目　n：多極成分の通し番号
        -   ３列目　value：その多極成分の係数
    
    です。

-   CHARGE MOMENTS

    -   IQ：格子サイトの番号を表します。
    -   CMNTQ：その格子サイトの電荷分布の多極展開係数を表します。
    -   NLMTOP-CHR：電荷分布をどこまでの多極成分で展開しているかを表す上限数です。ここでは、各格子サイトについて４個の成分が保存されています。

    各データ行の

    ::

        IQ   n   value

    は、

        -   １列目　IQ：格子サイトの番号
        -   ２列目　n：多極成分の通し番号
        -   ３列目　value：その多極成分の係数
    
    です。

-   MAGNETISATION DIRECTION

    -   IT：原子タイプの番号を表します。
    -   MTET_T：（原子タイプごとの）QMVEC = **0** のもとでの、磁化方向の極角 *θ* を表します。
    -   MPHI_T：（原子タイプごとの）QMVEC = **0** のもとでの、磁化方向の方位角 *φ* を表します。
    -   MGAM_T：（原子タイプごとの）局所座標系に対する第３の回転角 *γ* を表します。

-   MESH INFORMATION

    -   DX：実際の対数刻みの値に更新されています。
    -   JRMT：実際の muffin-tin 半径に対応するメッシュ点番号が入ります。
    -   RMT：実際の muffin-tin 半径の値に更新されています。
    -   JRWS：実際の Wigner-Seitz 半径に対応するメッシュ点番号が入ります。
    -   RWS：実際の Wigner-Seitz 半径の値に更新されています。

-   TYPES

    -   NCORT：Ba のコア電子数が、初期の推定値 "54" から、実際の計算での分類結果 "48" に更新されています。
    -   NVALT：Ba の価電子数が、初期の推定値 "2" から、実際の計算での分類結果 "8" に更新されています。

-   POTENTIAL

    各原子タイプごとの半径方向ポテンシャル *V* (r) の実データが、メッシュ点ごとの値で保存されています。 

-   CHARGE

    各原子タイプごとの半径方向電荷密度の実データが、メッシュ点ごとの値で保存されています。 

-   MOMENTS

    SCF 計算後の電子状態を積分して得られた実数値が保存されています。内容は下記の通りです。

    -   QEL：各原子タイプに属する総電子数
    -   NOS：各原子タイプの価電子側の占有
    -   SPN：各原子タイプのスピン磁気モーメント
    -   ORB：各原子タイプの軌道磁気モーメント
    -   HFI：各原子タイプの hyperfine field に関係する量

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob_SCF.inp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First-Principles SCF 用の入力ファイルです。

::

    CONTROL
        DATASET=QuloudJob
        ADSI=SCF
        POTFIL=QuloudJob.pot
        KRWS=1
        PRINT=0

    MODE
        FREL

    TAU
        BZINT=POINTS
        NKTAB=300

    ENERGY
        GRID={5}
        NE={32}
        ImE=0
        EMIN=-0.2

    STRCONST
        ETA=1.6
        RMAX=6
        GMAX=6

    SCF
        NITER=200
        MIX=0.2
        VXC=VWN
        ALG=BROYDEN2
        TOL=1e-05
        ISTBRY=1
        ITDEPT=40

    TASK
        SCF

入力パラメータの詳細は以下の通りです。

-   CONTROL

    -   DATASET：データセットの名前を指定します。ここの文字列が出力ファイル名のベースとなります。
    -   ADSI：ここの文字列が DATASET で指定した出力ファイル名の末尾に追加されます。このデータセットは SCF 計算に使われるため、SCF となっています。
    -   POTFIL：使用するポテンシャルファイルの名前を指定します。
    -   PRINT：アウトプットの出力レベルを指定します。

-   MODE

    計算のモードを指定します。デフォルトでは FREL（完全相対論）となっています。

-   TAU

    -   BZINT：ブリルアンゾーン積分のモードを指定します。デフォルトでは POINTS（special points method）となっています。
    -   NKTAB：special points method の k 点数を指定します。

-   ENERGY

    -   NE：エネルギーのメッシュ点の数を指定します。
    -   ImE：エネルギー値の虚数部分を指定します。
    -   EMIN：最小エネルギー値の実数部分を指定します。

-   STRCONST

    -   ETA：Ewald パラメータを指定します。
    -   RMAX：実空間での収束半径を指定します。
    -   GMAX：逆空間での収束半径を指定します。

-   SCF

    -   NITER：SCF 計算の最大反復回数を指定します。
    -   MIX：SCF 計算の混合パラメータを指定します。
    -   VXC：交換相関ポテンシャルを指定します。デフォルトでは VWN（Vosko-Wilk-Nusair）となっています。
    -   ALG：SCF 計算のアルゴリズムを指定します。デフォルトでは BROYDEN2（Broyden の第２法）となっています。
    -   TOL：SCF 計算の収束判定条件を指定します。
    -   ISTBRY：ここで指定した回数だけ SCF 計算を行った後に、Broyden 法が適用されます。
    -   ITDEPT：Broyden 法の iteration depth（最大で過去何回分の SCF 反復履歴を参照して次の混合更新を組み立てるか）を指定します。デフォルトでは 40 となっています。

-   TASK

    SCF 計算を行う場合、SCF と設定します。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QuloudJob_JXC.inp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exchange Coupling Parameters 用の入力ファイルです。

::

    CONTROL
        DATASET=QuloudJob
        ADSI=JXC
        POTFIL=QuloudJob.pot
        PRINT=0

    MODE
        SP-SREL

    TAU
        BZINT=POINTS
        NKTAB=300

    ENERGY
        GRID={5}
        NE={32}
        EMIN=-0.2

    TASK
        JXC
        CLURAD=2

入力パラメータの詳細は以下の通りです。

-   CONTROL

    -   DATASET：データセットの名前を指定します。ここの文字列が出力ファイル名のベースとなります。
    -   ADSI：ここの文字列が DATASET で指定した出力ファイル名の末尾に追加されます。このデータセットは交換結合パラメータ計算に使われるため、JXC となっています。
    -   POTFIL：使用するポテンシャルファイルの名前を指定します。
    -   PRINT：アウトプットの出力レベルを指定します。

-   MODE

    計算のモードを指定します。デフォルトでは SP-SREL（スカラー相対論）となっています。

-   TAU

    -   BZINT：ブリルアンゾーン積分のモードを指定します。デフォルトでは POINTS（special points method）となっています。
    -   NKTAB：special points method の k 点数を指定します。

-   ENERGY

    -   NE：エネルギーのメッシュ点の数を指定します。
    -   EMIN：最小エネルギー値の実数部分を指定します。

-   TASK

    交換結合パラメータ計算を行う場合、JXC と設定します。

    -   CLURAD：交換結合パラメータ計算で使うクラスター半径です。どこまでの近接サイト間相互作用を評価するかの範囲指定を行います。ポテンシャルファイルの ALAT を基準とした相対値で指定します。デフォルトでは 2 となっているので、クラスター半径は 2 × ALAT となります。

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

|
|

--------------------------------------------------------------
Quloud-Mag
--------------------------------------------------------------

|
|

++++++++++++++++++++++++++++
入力ファイル
++++++++++++++++++++++++++++

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
control.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

**Monte Carlo (Quloud-Mag) の場合**

::

    0 0

左の数字は初期状態を指定するパラメータです。Searching Equilibrium の場合は 0、Random Start の場合は 1、入力ファイル "heis.in" に準ずる場合は 2 とします。

右の数字はアルゴリズムを指定するパラメータです。Metropolis の場合は 0、Heat Bath の場合は 1 とします。

|

**Micro-Magnetic Simulation (Quloud-Mag-LLG) の場合**

::

    1 0
    1E-9 1E-13 1E-7

１行目は Monte Carlo と同じです。

２行目では、左から Simulation Time (sec)、Time Step (sec)、Thermalization Time (sec) を指定します。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
heis.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Monte Carlo (Quloud-Mag)

::

    3.990377622196221 3.990377622196221 4.102653757520632 90 90 90
    10 10 10
    4
    1
    0 -5.24561337357568e-13 100
    1
    0 0 100
    1
    0 0 100
    1
    0 0 100
    5
    0.5 0.5 0.582541460000001
    0 1
    1 1 0.10004269999999515
    1 1
    1 0.5 0.06422
    2 1
    0.5 1 0.06422
    2 1
    1 1 0.54897
    3 1
    2
    16 12
    0 0 0 0
    0.00000000 0.00000000 -0.00000000 -0.00000000 -0.00000000 0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    0 0 1 0
    0.00000000 0.00000000 0.00000000 -0.00000000 -0.00000000 -0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    0 0 2 0
    -0.00000000 -0.00000000 -0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 
    0 0 3 0
    0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    1 0 0 0
    0.00000000 0.00000000 -0.00000000 -0.00000000 -0.00000000 -0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    1 0 1 0
    0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    1 0 2 0
    0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 0.0 0.0 
    1 0 3 0
    0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 -0.00000000 0.0 0.0 
    2 0 0 0
    -0.00000000 -0.00000000 -0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 
    2 0 1 0
    0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.0 0.0 
    2 0 2 0
    -0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 -0.00000000 0.00000000 0.0 0.0 
    2 0 3 0
    -0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 
    3 0 0 0
    -0.00000000 -0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    3 0 1 0
    0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 -0.00000000 0.0 0.0 
    3 0 2 0
    -0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 -0.00000000 0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 
    3 0 3 0
    0.00000000 -0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.0 0.0 0.0 0.0 0.0 0.0 
    0 1200 100
    10000 10000 1
    0 0.1 1
    0 0 1
    0 0 0
    0 0 0
    0
    1 1 
    0 0 0 0
    0 0 0 0 0 0

入力ファイルの詳細は以下の通りです。

１行目では、ユニットセルのサイズと形状を指定します。ます格子ベクトルの長さ（Å）を記入し、次にベクトル間の角度（°）を記入します。

２行目では、シミュレーションのモデルのサイズを指定します。例えば 2 2 2 と記すと、１行目で指定したユニットセルが x, y, z 各方向に２個ずつ配置され、モデルのサイズは８倍になります。デフォルトでは 10 10 10 となっています。

３行目では原子サイトのタイプの総数を指定します。

４行目ではサイトタイプ１に入る原子の種類の総数を指定します。５行目からは、サイトタイプ１に入る各原子種の情報を順番に記述していきますが、上の例では１種類のみなので１行で終わっています。一番左の数字は磁性の情報で、Magnetic の場合は 1、Non Magnetic の場合は 0 とします。真ん中の数値は磁気モーメント（μ\ :sub:`B`\）を表します。一番右の数値は濃度（%）を表します。
以下、６～７行目でサイトタイプ２、８～９行目でサイトタイプ３，１０～１１行目でサイトタイプ４の情報を指定します。

１２行目ではユニットセルに含まれる原子の総数を指定します。

１３行目では１番目の原子の相対座標を指定します。１４行目の左の数字はサイトタイプ（0 から始まる）を表します。右の数字は初期スピンの種類を表し、FM の場合は 1、AFM の場合は -1 とします。
以下、１５～１６行目で２番目の原子、１７～１８行目で３番目の原子，１９～２０行目で４番目の原子、２１～２２行目で５番目の原子の情報を指定します。

２３行目ではユニットセル内の相互作用のカットオフ半径を指定します。カットオフ半径が n の場合、(2n + 1) × (2n + 1) × (2n + 1) 個のユニットセルが考慮されます。

２４行目の左の数字は J\ :sub:`ij`\ の相互作用のタイプの総数を表します。右の数字は各タイプの相互作用での最隣接原子の数を表します。

２５行目では相互作用のペアを、サイトタイプと原子種で指定しています。左の 0 0 は、サイトタイプ１の原子種１を表し、右の 0 0 も同じです。この２つの原子の相互作用の J\ :sub:`ij`\ を次の２６行目で記述します。
以下、２７～２８行目で２番目のペア、２９～３０行目で３番目のペア、・・・・・・、５５～５６行目で１６番目のペアの相互作用の情報を指定しています。

５７行目ではシミュレーションでの温度パラメータ（K）を指定します。左から Min、 Max、ΔT を表します。

５８行目ではモンテカルロの設定を行います。左の数値は測定回数、真ん中の数値は平衡に達するまでのモンテカルロステップ数、右の数値はレプリカサンプル数を表します。

５９行目ではシミュレーションでの磁場パラメータ（Tesla）を指定します。左から H \ :sub:`Min`\、H \ :sub:`Max`\、ΔH を表します。

６０行目では磁場の方向を指定します。左から x、y、z 方向の成分を表します。

６１行目では一軸磁気異方性パラメータを設定し、６２行目では立方磁気異方性パラメータを設定します。

６３行目では、DMI 相互作用を考えない場合は 0、考える場合は 1 とします。

６４行目の左の数字は D\ :sub:`ij`\ の相互作用のタイプの総数、右の数字は各タイプの相互作用でのペアの総数を表します。

６５行目では D\ :sub:`ij`\ の相互作用のペアを、サイトタイプと原子種で指定しています。指定方法は J\ :sub:`ij`\ と同様です。

６６行目の左３つの数値はペアの方向、右３つの数値は DMI ベクトルの成分を表します。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
omp.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Monte Carlo (Quloud-Mag)、Micro-Magnetic Simulation (Quloud-Mag-LLG)

::

    1 1 1
    0

１行目では openMP での x、y、z 方向の格子分割数を指定します。

２行目では、openMP での格子分割を行わない場合は 0、行う場合は 1 とします。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
boundary.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Monte Carlo (Quloud-Mag)

::

    1 1 1

x、y、z 方向の境界条件を指定します。Periodic の場合は 1、Free の場合は 0 とします。

|
|

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
structure.in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Micro-Magnetic Simulation (Quloud-Mag-LLG)

::

    50 50 50 10E-9 10E-9 10E-9
    1
    296 99999 100000
    0.47398E+6
    0.7779475927
    0
    8.3845E-12
    0 0 0
    0 0 0
    0.002847469702
    1
    0.1 500E+6
    0 0 1

入力ファイルの詳細は以下の通りです。

１行目では、各方向のグリッド数と空間領域の大きさ（m）を指定します。

３行目の一番左の数値は温度（K）を表します。

４行目では 0 K での飽和磁化 (A/m) を指定します。

５行目では有限温度での規格化された磁化を指定します。

７行目では 0 K での Exchange Stiffness（J/m）を指定します。

８行目では 0 K での一軸異方性パラメータを指定します。

９行目では 0 K での立方異方性パラメータを指定します。

１０行目では Gilbert 減衰定数を指定します。

１２行目では、磁場強度 (A/m) と振動数 (Hz) を指定します。

１３行目では磁場の方向を指定します。

|
|

++++++++++++++++++++++++++++
出力ファイル
++++++++++++++++++++++++++++

|
|

++++++++++++++++++++++++++++
ログ
++++++++++++++++++++++++++++

Quloud-Mag では、ログにはほぼ何も出力されませんので、動作状況の確認では出力ファイルをご覧ください。