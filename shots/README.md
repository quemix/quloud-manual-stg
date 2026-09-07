# 画面キャプチャの撮影ハーネス

マニュアル掲載用の画面を Playwright で撮る。手で撮らないのは、仕様変更のあとに
**一括で撮り直せる**ようにするため（設計書 §6.1 の前提そのもの）。

撮影対象はローカル Docker の Nuxt（`http://localhost:3000`）。本番や stg は叩かない。

## なぜ `~/v6.0/e2e` に足さずここに置くか

設計書 §6.1 は `~/v6.0/e2e` に撮影スペックを足す案だったが、`CLAUDE.md` は
**`~/v6.0` を読み取り専用**（`log` / `show` / `ls-tree` / `diff` まで）と定めている。
他人の作業リポジトリなので書き込まない。そのため独立した npm プロジェクトとして
マニュアル側に置き、認証も自前で行う。

ブラウザバイナリは共有キャッシュ `~/.cache/ms-playwright` を流用する。
`@playwright/test` を `1.63.0-alpha-2026-08-05` に固定しているのはそのためで、
このバージョンが要求する chromium は revision 1237。**フルの `chromium-1237` は
キャッシュに無く、`chromium_headless_shell-1237` だけがある。**
ヘッドレスなら動くが `--headed` は動かない。

## 前提

- `~/v6.0` で `docker compose ps` の `nuxt` / `rails` / `db` が Up
- `meta/` に非公開リポジトリ `quemix/quloud-manual-meta` がクローンされている
  （置換表 `meta/shots_redactions.json` を読む）

## 使い方

リポジトリ直下から。

```bash
QULOUD_SHOTS_EMAIL=<メールアドレス> QULOUD_SHOTS_PASSWORD=<パスワード> make shots
```

`make shots` は「撮影 → 台帳の更新（`meta/images_assets.csv`）→ 整合の検査」を通しで行う。

一部だけ撮り直すとき。台帳は撮っていない行を消さないので、部分実行してよい。

```bash
cd shots
npx playwright test --project=anon                       # サインイン前の画面だけ
npx playwright test --grep invitation_                   # 名前で絞る
QULOUD_SHOTS_WORKERS=1 npx playwright test               # 並列を落とす
cd .. && make shots-ledger && make shots-check
```

**資格情報はコミットしない。** 既定値も置かない（ローカル開発 DB のシードユーザーの
アドレスは実在の形をしている）。値は `meta/` の README を参照。

## 識別情報の消し方

ローカル開発 DB のシードデータには実在の社名・氏名・メールアドレスが入っている。
設計書 §10 が「画面キャプチャに含めてはいけないもの」として挙げているものそのまま。

DB を書き換えるのは他人の作業環境を壊すので、**撮影直前に DOM のテキストを差し替える**。
置換表は `meta/shots_redactions.json`（非公開リポジトリ側）。

- `replace` … 部分一致。キーが長いものから適用する。テナント名がメール
  アドレスのドメインにも現れるので、短いキーを先に当てるとアドレスが壊れる
- `replaceExact` … テキストノード全体が一致したときだけ置換する。アバターの
  頭文字（1 文字）のように、部分一致だと本文を壊すもの向け

置換のあとに**元の文字列が 1 つも残っていないことを検査**し、残っていれば撮影を
失敗させる。置換漏れが公開画像に混ざることはない。新しい画面を撮って落ちたら、
表に規則を足す。

## スペックの書き方

`specs/anon/` はサインイン前、`specs/auth/` はサインイン後（`storageState` を使う）。
どちらに置くかで認証の有無が決まる。

```ts
import { defineShots, settle } from '../../lib/shot'

defineShots([
  {
    name: 'signin_form_initial',        // ファイル名。<章>_<機能>_<状態>
    chapter: 'signin',                  // source/<章>.rst の <章>
    feature: 'サインイン画面',
    state: '初期表示',
    expectUrl: /\/sign_in$/,            // 必須
    prepare: async (page) => {
      await page.goto('/sign_in')
      await settle(page)
    },
  },
])
```

保存先は `source/images/v70/<name>.png`。

### `expectUrl` を必須にしている理由

`nuxt/middleware/auth.global.ts` は未サインインのアクセスを `/sign_in` へ
`replace` で飛ばす。許可されているのは `/sign_in` `/sign_up`
`/request_reset_password(/complete)` `/reset_password` `/applicant(/complete)` だけ。
**撮影対象を間違えてもエラーにならず、サインイン画面が撮れてしまう。**
実際に `/inquiry` を `anon` で撮ろうとして、サインイン画面と 1 バイト違わない
PNG が 2 枚できた。`expectUrl` はこれを落とすためにある。

### ビューポート

`lib/viewport.ts` の `SHOT_VIEWPORT`（1440x900）で固定し、撮影ごとに実際の値と
突き合わせて違えば失敗させる。`source/introduction.rst` の「動作環境」に
1440 px と書いてあるので、変えるなら章も直す。

`projects[].use` に `devices['Desktop Chrome']` を展開すると、その中の
viewport（1280x720）が全体の `use.viewport` を**上書きする**。実際にそれで
9 枚とも 1280x720 で撮れていた。展開の**後ろ**に viewport を置くこと。

## 掴みにくい要素

アプリの `data-testid` は全体で 4 個しかなく、そのうち 3 個がサインイン画面。
基本は role と日本語ラベル（`nuxt/locals/ja/*.ts` の文言）で掴む。

アイコンだけのボタンには `aria-label` もテキストも無いので、アイコンのクラスで
指定する。例：招待ダイアログを開くボタン。

```ts
await page.locator('button:has(.mdi-email-plus-outline)').click()
```

## 台帳

2 枚に分けている。変わる理由が違うため（設計書 §6.3）。

| ファイル | 誰が書くか | 中身 |
| --- | --- | --- |
| `meta/images_assets.csv` | `make shots-ledger` が機械的に書く | 画像ファイル、章、機能、状態、撮影日、参照コミット、ビューポート |
| `meta/images_placements.csv` | **人が書く** | どの章のどの節で使うか、alt、caption |

`make shots-check` が、画像・`images_assets.csv`・`images_placements.csv` の
食い違い（画像が無い、台帳に無い、存在しない画像を指している、alt / caption が空、
`placement_id` の重複）を検査する。まだ章に貼っていない画像は失敗にしない
（撮影が章より先に進むのは正常な進め方）。
