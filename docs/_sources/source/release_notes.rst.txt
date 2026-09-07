========================================
変更履歴
========================================

.. note::

   本章は Quloud Ver.7.0 を対象としています。
   Ver.7.0 の項には、本番稼働中の Ver.6.1.2 と比べて利用者から見える変化のみを記載しています。


|
|

.. include:: _generated/release_notes_v70.rst

**Ver.6.1.2（2026.4.20）**

|

-   招待画面

    -   一度追加した新規ユーザーのメールアドレスを「Deny」ボタンで却下する機能を、Tenant 内のすべての Owner 権限ユーザーが使用できるよう変更

    |

-   画面の自動更新

    -   画面の自動更新を停止

    |

-   Project、Material、Job の名前の重複制限

    -   Project、Material、Job の作成時、名前の重複制限によるエラーが発生した場合でも、作成ダイアログ自体が消えないように修正
    -   作成した Job を、Job 詳細ページの「Copy Job」ボタンでコピーする際にも、Job 名の重複禁止の制御が有効となるよう修正
    -   Job 詳細ページの「Delete Job」ボタンから削除した Job については、名前の重複制限の対象外とし、同一 Material 内で削除した Job と同じ名前の Job が作成できるよう修正

    |

-   Material 作成ダイアログ、Job 作成 / 編集ダイアログでの loading 表示

    -   「Create」もしくは「Save」ボタンをクリックしてから実際に作成 / 編集が完了するまでの間、loading 表示が出て、ユーザーが他の操作を行えないように変更

    |

-   Material 詳細画面

    -   ブラウザリロード時の画面遷移を下記のように変更

        - Property ページでリロード → Property ページに遷移
        - File ページでリロード → File ページに遷移
        - Job 一覧ページでリロード → Job 一覧ページに遷移
        - Job 詳細ページでリロード → Job 詳細ページに遷移

        |

-   Material / Job のファイル編集

    -   Job が存在する Material では、File ページでファイルが編集できないよう変更
    -   ファイル編集時に全角文字を入力し「Save」ボタンで保存すると、その後「Edit」ボタンをクリックしても中身が表示されなくなる問題を解消

    |

-   モデリング画面

    -   Surface 項目にある「Reorient lattice」チェックボックスを削除

    |

-   入力ファイル直接アップロードによる Job 実行

    -   RSDFT の Job 詳細ページの「Site property settings」表示欄を削除
    -   LAMMPS の入力ファイルでの設定内容が Job 詳細ページに反映されるよう修正

    |

-   「Run Job」ボタンからの Job 実行

    -   一度「Run Job」ボタンから Job を実行した直後に、再度「Run Job」ボタンから Job を実行できてしまう問題を解消
    -   一度「Run Job」ボタンから Job を実行した直後に、「Delete Job」ボタンがクリックできてしまう問題を解消

    |

-   Site property settings

    -   Quantum ESPRESSO・OpenMX・RSDFT・FLARE の Edit Job ダイアログに Site property settings 項目を追加
    -   Quantum ESPRESSO・OpenMX・RSDFT・FLARE で、Site property settings 項目の Charge 設定欄を削除
    
    |

-   Quantum ESPRESSO

    -   Electron Band Structure で、計算結果の Effective Mass (Table) の表が、Job 作成者のみしか閲覧できない問題を解消
    -   X-Spectra の一部の入力パラメータの表示桁数を変更
    -   X-Spectra の一部の入力パラメータを指数表記に変更
    -   X-Spectra の Job 作成時、吸収原子用の GIPAW 擬ポテンシャルファイルがない場合にエラーメッセージが表示されるよう修正
    -   X-Spectra の Job 作成時、吸収サイト以外にも吸収原子用の GIPAW 擬ポテンシャルファイルが設定されてしまう問題を解消
    -   X-Spectra の Job 作成時、入力ファイル「xspectra.in」の末尾に、吸収サイトに関する情報「QULOUD_ABS_SITE_INDEX」が追加されるよう修正
    -   下記の Job で、Create Job ダイアログや Edit Job ダイアログで 設定・編集した通りの情報が、Job 詳細ページの「Settings」項目、および Edit Job ダイアログに正しく表示されない場合がある問題を解消

        -   Energy Barrier (NEB)
        -   X-Spectra
        -   Phonon (ph.x)

        |
    
    -   Energy Barrier (NEB) の計算結果の Atomic Structure Trajectory で、モデル図がマウスで回転できるように修正
    -   Energy Barrier (NEB) で、Create Job ダイアログで終期構造を選択してからすぐに「Create」ボタンをクリックすると、選択した終期構造が入力ファイルに正しく設定されない問題を解消
    -   Energy Barrier (NEB) で、Edit Job ダイアログで終期構造の情報を変更して保存しても、その変更が入力ファイルに反映されない問題を解消
    -   Energy Barrier (NEB) の入力ファイル「neb.in」が、File ページの「Edit」アイコンから編集できない問題を解消
    -   Phonon (ph.x) の Job 作成後、Edit Job ダイアログで Calculation（Phonon Band Dispersion / Phonon DOS）を変更して「Save」ボタンで保存すると、どちらの Calculation の入力ファイルも生成されてしまう問題を解消
    -   Phonon (ph.x) の ph.in 項目の入力パラメータ「epsil」を削除

    |

-   OpenMX

    -   Electron Band Structure で、計算結果の Effective Mass (Table) の表が、Job 作成者のみしか閲覧できない問題を解消
    -   Energy Barrier (NEB) で、Create Job ダイアログで終期構造を選択してからすぐに「Create」ボタンをクリックすると、選択した終期構造が入力ファイルに正しく設定されない問題を解消
    -   Energy Barrier (NEB) で、Create Job ダイアログや Edit Job ダイアログで 設定・編集した終期構造の情報が、Edit Job ダイアログに正しく表示されない問題を解消
    -   Energy Barrier (NEB) で、Edit Job ダイアログを開いて「Save」ボタンで保存すると、終期構造の情報が、強制的に初期構造と同じものに置き換わってしまう問題を解消
    -   下記の Job の計算結果の Atomic Structure Trajectory で、モデル図がマウスで回転できるように修正

        -   Energy Barrier (NEB)
        -   Molecular Dynamics

        |

-   RSDFT

    -   Electron Band Structure の Job 作成時、入力ファイル「rsdft.in」の KPTDIVNUM の行の末尾にスラッシュが追加されるよう修正
    -   Molecular Dynamics の計算結果の Atomic Structure Trajectory で、モデル図がマウスで回転できるように修正
    -   Site property settings 項目での初期スピンの設定が無視されてしまう問題を解消

    |

-   LAMMPS

    -   Molecular Dynamics の計算結果のグラフの縦軸・横軸に単位を追加
    -   Molecular Dynamics で、Create Job ダイアログで 設定した通りの情報が、Job 詳細ページの「Settings」項目に表示されない場合がある問題を解消
    -   Molecular Dynamics で、msd を計算する元素や rdf を計算する元素ペアを限定して Job を作成しても、Edit Job ダイアログではすべての元素や元素ペアにチェックがついてしまう問題を解消
    -   Molecular Dynamics の計算結果の Atomic Structure Trajectory で、モデル図がマウスで回転できるように修正
    -   Molecular Dynamics の計算結果の Atomic Structure Trajectory で、モデル図が強制的に直方体になってしまう問題を解消
    -   Molecular Dynamics の計算結果の Atomic Structure Trajectory で、格子ベクトル a2 と a3 が逆に表示されてしまう問題を解消
    -   Molecular Dynamics の計算結果の Atomic Structure Trajectory で、元素と原子球のカラー / サイズの対応が違ってしまう場合がある問題を解消

    |

-   ASE

    -   Energy Barrier (NEB) で、Create Job ダイアログで終期構造を選択してからすぐに「Create」ボタンをクリックすると、選択した終期構造が入力ファイルに正しく設定されない問題を解消
    -   Energy Barrier (NEB) で、一度作成した Job を、Job 詳細ページの「Edit Job」ボタンから編集する機能が無効となっていた問題を解消
    -   下記の Job の計算結果の Atomic Structure Trajectory で、モデル図がマウスで回転できるように修正

        -   Energy Barrier (NEB)
        -   Molecular Dynamics

        |

-   FLARE

    -   On-the-Fly MD の計算結果の Atomic Structure Trajectory で、モデル図がマウスで回転できるように修正

|
|

**Ver.6.1.1（2026.3.30）**

|

-   入力ファイル直接アップロードによる Job 実行

    -   FLARE の入力ファイルがアップロード不可となっていた問題を修正
    -   Quantum ESPRESSO (PW) で、入力ファイルの &CONTROL フィールドの calculation が 'scf' でない場合にアップロード不可となっていた問題を修正

    |

-   Quantum ESPRESSO

    -   Spin 有りの計算を行う際、入力ファイルの &system のブロックに starting_magnetization 行がデフォルトで入らなくなっていた問題を修正
    -   Electron Band Structure で、計算結果に有効質量の情報が表示されない問題を修正
    
        **※ Effective Mass (Table) につきましては、Job 作成者のみしか閲覧できなくなっています。（OpenMX でも同様です。）**

    -   X-Spectra の Job を実行するとエラーが出てしまう場合がある問題を一部解消
        
        **※ 計算が走らない場合もございますので、引き続き、試験的運用とさせていただきます。**

    |

-   OpenMX

    -   Create Job ダイアログの Site property settings の spin & charge 項目で各原子の初期電荷の設定を行うと、無効な入力ファイルが生成されてしまう問題を修正
    -   Energy Barrier (NEB) で、初期スピン設定が初期／終期構造で違ってしまう問題を修正

    |

-   LAMMPS

    -   ２つの入力ファイル「QuloudJob.lmp」と「in.QuloudJob」での元素ナンバリングが必ず一致するよう修正
    -   Molecular Dynamics で、Mean-Squared Displacement を計算する元素や、Radial Distribution Function を計算する元素ペアを限定すると「Create」ボタンがクリックできなくなる問題を修正
    -   Molecular Dynamics で、計算結果のAtomic Structure Trajectory が表示されない問題を修正
    -   Molecular Dynamics で、計算結果の Radial Distribution Function のグラフのデータ ラベルに誤りが生じる場合がある問題を修正

|
|

**Ver.6.1.0（2026.3.16）**

|

-   認証タイムアウト

    -   サインインしてから８時間経過後にサインアウトするよう修正

    |

-   UI/UX

    -   ダッシュボード

        -   ダッシュボードのシステムバー（Points、Expiration Date、Storageが表示されていた箇所）を削除
        -   ヘッドメニューにボードアイコンを追加し、クリックすると Points、Expiration Date、Storage をダイアログで表示するよう変更
        -   Project ボタン位置変更（上部 → 下部）
        -   Material 一覧の Edit ボタンを変更（ボタン → アイコン）
        -   Job 一覧の Edit ボタンを変更（ボタン → アイコン）

        |

    -   Material 詳細画面

        -   画面サイズによらずサイドメニューが表示されるよう修正
        -   Property ページ

            -   Job 選択を削除し、Property 選択を追加
            -   Property 選択には、完了しているかつ表示許可されている Job のみ表示
            -   Structure 選択を削除（Job が選択された場合は Final を自動選択）
            -   Job Detail ボタンを追加（クリックで Job 詳細ページに遷移）
            -   Files ボタンを追加（クリックで File ページに遷移）
            -   Modeling/Save As (Save As Matrial)/Create Job の位置とアイコンを調整
            -   ページ内リンク（TABLE OF CONTENT）を削除
            -   Lattice、Chemical、Description の位置を調整

            |

        -   Job ページ

            -   Job 一覧ページを追加

                -   表示データはダッシュボードと同様
                -   View アイコンをクリックすると Property ページでの表示切替を行う
                -   Files アイコンをクリックすると File ページに遷移
                -   Edit ボタンをクリックすると Job の名称と説明を編集するダイアログを表示
                -   Job 名称をクリックすると Job 詳細ページに遷移

                |

            -   Job 詳細ページ

                -   Job 選択、Structure 選択を削除

                |

            -   File ページ

                -   Structure 選択を削除（Job が選択された場合は Final を自動選択）

    |

-   入力ファイル直接アップロードによる Job 実行

    -   Material 作成ダイアログに Software の項目を追加
    -   Software の項目が選択された場合に File Upload で同時に Job を作成

    **※ 現時点では、FLARE の入力ファイルがアップロード不可となっております。また、Quantum ESPRESSO (PW) では、入力ファイルの &CONTROL フィールドの calculation が 'scf' でない場合にはアップロード不可となっております。ご了承ください。**

    |

-   Project、Material、Job の名前の重複制限

    -   Project 作成、更新に名前重複禁止の制御を追加（Tenant 毎）
    -   Material 作成、更新に名前重複禁止の制御を追加（Project 毎）
    -   Job 作成、更新に名前重複禁止の制御を追加（Material 毎）

    |

-   計算機能

    -   下記の Job を新たに追加

        -   Quantum ESPRESSO

            -   X-Spectra   **（試験的運用）**
            -   Phonon (ph.x)
            -   Energy Barrier (NEB)

            |

        -   ASE

            -   Energy Barrier (NEB)

        |

    -   OpenMX の Lattice Opt. の Optimization Method に以下の選択肢を追加

        -   Lattice Constants Optimization (\|a1\| = \|a2\| ≠ \|a3\|) by Steepest Descent (OptC4)

    |

-   Create Job ダイアログ

    -   作成する Job を選択する際、Types、Software、Workflows のどこからでも絞り込みが行えるよう変更
    -   下記の Software で Site propery settings 項目を追加し、各原子の拘束条件や初期スピンを設定できるよう変更

        -   Quantum ESPRESSO
        -   OpenMX
        -   RSDFT
        -   FLARE

        **※ OpenMX では、spin & charge 項目での各原子の初期電荷の設定を行うと、無効な入力ファイルが生成されてしまいますので、行わないようご注意ください。**

        **※ RSDFT では、spin & charge 項目での各原子の初期スピンの設定が無効となりますので、Initial Spin Difference での設定をお願いいたします。**

        **※ FLARE (On-the-Fly MD) では、constraint 項目での各原子の拘束条件の設定が無効となりますので、ご了承ください。**

    |

-   モデリング

    -   モデリングタイプの分類（Basic、Slab model、Interface、Add Molecule、Add Cell）を廃止し、あらゆる機能を一つの画面に集約
    -   Atomic Coordinates 項目を追加し、各原子の相対座標を設定できるよう変更
    -   Relative atomic position 項目を追加し、各原子を各方向に一括で移動できるよう変更
    -   Interface 項目では、追加する Film を「Add Crystal」で選択するよう変更
    -   Packmol 項目を追加（セルの格子ベクトル間角度がすべて 90 度の Crystal でのみ使用可能）

    |

-   ボタンの名称

    -   「Submit」ボタンの名称を、「Run」「Create」「Save」「Delete」「Copy」など、操作内容に即した名称に変更

|
|

**Ver.6.0.1（2025.12.12）**

|

-   UI/UX

    -   「Edit Job」ボタン表示の不具合を修正
    -   「Delete Job」ボタン表示の不具合を修正
    -   スペルミスを修正
    -   Job 検索時の Software 表示の不具合を修正
    -   ダッシュボードの Job 一覧の Software 名、Job Type 名表示の不具合を修正

    |

-   データベース検索

    -   不要な文字列が表示されていた不具合を修正

    |

-   モデリング

    -   原子サイズの不具合を修正
    -   分子モデリング時の原子移動の不具合を修正

    |

-   Quantum ESPRESSO

    -   擬ポテンシャルに応じたカットオフ推奨値設定の不具合を修正
    -   Job 設定編集・表示の不具合を修正
    -   収束性表示の不具合を修正

    |

-   OpenMX

    -   Job 設定情報表示の不具合を修正
    -   結果表示の不具合を修正
    -   収束性表示の不具合を修正

    |

-   RSDFT

    -   Car-Parrinello MD の Job 設定時の k 点数の上限値を変更（Γ点のみ）
    -   結果表示の不具合を修正
    -   大きすぎる Threads 並列数指定時の Job 実行停止
    -   波動関数（Kohn-Sham Orbitals）プロットの条件変更

    |

-   LAMMPS

    -   Job 設定情報表示の不具合を修正
    -   Job 設定編集機能の不具合を修正
    -   Atomic Structure Opt. 計算設定の不具合を修正
    -   Radial Distribution Function 計算設定の不具合を修正
    -   Radial Distribution Function および Mean-Squared Displacement 結果表示の不具合を修正

    |

-   FLARE

    -   バージョンを FLARE-1.4.1 に変更
    -   FLARE → LAMMPS の Job 引継ぎの不具合を修正

    |

-   ASE

    -   計算結果表示の不具合を修正

    |

-   Quloud-Mag

    -   パラメータ設定・表示の不具合を修正
    -   計算結果表示の不具合を修正

    |

-   その他

    -   Job 収束性（conv）の表示を第一原理計算（Quantum ESPRESSO, OpenMX, RSDFT）のみに変更

|
|

**Ver.6.0.0（2025.12.1）**

|

本バージョンで利用できる機能の概要と、旧バージョン（Ver. 5.1.5）からの変更点を記載します。

|
|

- Project

    - Project を Tenant のメンバーと共有する機能を新たに追加しました。

    |

- Material

    - 使用データベース

        -   Crystal：Materials Project
        -   Molecule：PubChem

        |

- アップロード可能なファイル形式

    -	CIF
    -	XYZ
    -	POSCAR（VASP 形式）
    -	OpenMX 入力ファイル
    -	Quantum ESPRESSO 入力ファイル

    |

- モデリング機能

    - モデリングのタイプ

        -   Basic（Crystal、Molecule 共通）
        -   Slab model（Crystal のみ）
        -   Interface（Crystal のみ）
        -   Add Molecule（Crystal のみ）
        -   Add Cell（Molecule のみ）

        **構造最適化時の原子移動の拘束条件 （動く方向を制限したり、完全に動かさないようにしたり）の設定（Constraint）と初期スピン差の設定（Spin difference）機能は、本バージョンでは廃止となりました。**

        **また、 Slab model モデリングで追加可能な、終端用の擬水素原子については、結合長や電荷の設定はできなくなりました。**

        |

- 計算 Job

**入力ファイルのアップロードにより計算 Job を登録する機能は、本バージョンでは廃止となりました。**

    - 計算 Job のタイプ

        -   First-Principles Calculation

            -   Single-Point SCF（Quantum ESPRESSO、OpenMX、RSDFT）
            -   Atomic Structure Opt.（Quantum ESPRESSO、OpenMX、RSDFT）
            -   Lattice Opt.（Quantum ESPRESSO、OpenMX、RSDFT）
            -   Electron Band Structure（Quantum ESPRESSO、OpenMX、RSDFT）
            -   Electron DOS（Quantum ESPRESSO、OpenMX、RSDFT）
            -   Energy Barrier (NEB)（OpenMX）
            -   First-Principles MD（OpenMX、RSDFT）
            -   Exchange Coupling Parameters（OpenMX）

            **Band Unfolding は、本バージョンでは廃止となりました。**

            |

        -   Classical Molecular Dynamics Simulation

            -   Atomic Structure Opt.（LAMMPS）
            -   Molecular Dynamics（LAMMPS）
                **※ dipole（双極子モーメント）の計算は、本バージョンではできなくなりました。**

            **Phonon Calculation は、本バージョンでは廃止となりました。**

            |

        -   Advanced Classical MD

            -   On-the-Fly MD（FLARE）
            -   Machine-Learning MD (Pretraind Potential)（ASE-MD）

            |

        -   Quloud-Mag

            -   First-Principles SCF（SPRKKR）
            -   Exchange Coupling Parameters（SPRKKR）
            -   Monte Carlo（Quloud-Mag）
            -   Micro-Magnetic Simulation（Quloud-Mag-LLG）
                **※ Job 登録時の Option Magnetic 選択欄は、本バージョンでは廃止となりました。**

            **Gilbert Damping Parameter、Transport Property、Monte Carlo (Snapshot of magnetic moments)、UppASD は、本バージョンでは廃止となりました。**

|
|

