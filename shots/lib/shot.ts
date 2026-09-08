/**
 * 撮影スペックを Playwright のテストに変換する。
 *
 * 1 スペック = 1 枚。保存先は source/images/v70/<name>.png で、名前は
 * <章>_<機能>_<状態>（設計書 §6.2）。台帳（meta/images_assets.csv）は
 * ここでは書かない。worker 並列で CSV に追記すると壊れるので、1 枚ごとに
 * shots/.out/<name>.json を落として、撮影後に tools/shots_ledger.py が
 * まとめて CSV にする。
 */
import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { test, expect } from '@playwright/test'
import type { Page } from '@playwright/test'
import { loadRules, redactPage, assertRedacted } from './redact'
import { SHOT_VIEWPORT } from './viewport'

const REPO_DIR = path.resolve(__dirname, '..', '..')
const IMAGE_DIR = path.join(REPO_DIR, 'source', 'images', 'v70')
const OUT_DIR = path.join(REPO_DIR, 'shots', '.out')

/**
 * 撮影時に動いていたアプリのコミット。
 *
 * 台帳側で撮り直しのたびに現在の HEAD を書くと、**撮り直していない画像の
 * 参照コミットまで今日の値に書き換わる**（shots/.out/*.json は消えないので、
 * 部分実行でも全件が取り込み直される）。撮影の事実は撮影時に記録する。
 */
const CODE_DIR = process.env.QULOUD_CODE_DIR ?? path.join(os.homedir(), 'v6.0')
const CODE_COMMIT = (() => {
  try {
    return execFileSync('git', ['-C', CODE_DIR, 'rev-parse', 'HEAD'], { encoding: 'utf-8' }).trim()
  } catch {
    return ''
  }
})()

export type ShotSpec = {
  /** ファイル名（拡張子なし）。<章>_<機能>_<状態> の形にする。 */
  name: string
  /** 章。source/<章>.rst の <章>。台帳の突き合わせに使う。 */
  chapter: string
  /** 何の機能の画面か。台帳に入る。 */
  feature: string
  /** どの状態か（初期表示・入力後・確認画面など）。台帳に入る。 */
  state: string
  /**
   * 撮影時にいるべき URL。**必須。**
   *
   * nuxt/middleware/auth.global.ts は未サインインのアクセスを /sign_in へ
   * replace で飛ばす。許可されているのは /sign_in /sign_up
   * /request_reset_password(/complete) /reset_password /applicant(/complete) だけ。
   * つまり撮影対象を間違えると、エラーにならずサインイン画面が撮れてしまう。
   * 実際に /inquiry を anon で撮ろうとして、サインイン画面と 1 バイト違わない
   * PNG が 2 枚できた。ここで URL を検査して落とす。
   */
  expectUrl: RegExp
  /**
   * 撮れない条件のとき、その理由を返す。返した場合はそのショットを飛ばす。
   *
   * 有効なトークンが要る画面のように、読み取りだけでは撮れないものがある。
   * 黙って落とすのでも、間違った画面を撮るのでもなく、理由を出して飛ばす。
   */
  skipIf?: () => string | false
  /** ページ全体を撮る。既定はビューポートだけ。 */
  fullPage?: boolean
  /**
   * この CSS セレクタに一致する要素だけを撮る（既定はビューポート全体）。
   *
   * 置換表は**書いてある文字列しか消せない**。画面の一部に、その章と関係の無い
   * 一覧（プロジェクト詳細画面のジョブ一覧など）が写り込むと、内部のテスト名が
   * そのまま公開画像に入る。実際に issue 番号を含むジョブ名が 2 件写っていた。
   * 章に必要な範囲だけを撮れば、その一覧ごと写らない。
   *
   * 要素が 1 つに定まらない場合は撮影を失敗させる（別の場所を撮るより止める）。
   */
  clip?: string
  /** 撮りたい状態まで画面を進める。 */
  prepare: (page: Page) => Promise<void>
}

export function defineShots(specs: ShotSpec[]): void {
  // 置換表が無い時点で落とす。撮ってから気づくのでは遅い。
  const rules = loadRules()

  for (const spec of specs) {
    test(spec.name, async ({ page }, testInfo) => {
      const reason = spec.skipIf?.()
      if (reason) test.skip(true, reason)

      await spec.prepare(page)
      await expect(page).toHaveURL(spec.expectUrl)

      // Vuetify の遷移アニメーションが途中の絵を撮らないようにする。
      await page.waitForLoadState('networkidle').catch(() => { /* 撮影は続ける */ })
      await page.emulateMedia({ reducedMotion: 'reduce' })

      await redactPage(page, rules)
      await assertRedacted(page, rules)

      const file = path.join(IMAGE_DIR, `${spec.name}.png`)
      fs.mkdirSync(IMAGE_DIR, { recursive: true })
      const options = { path: file, animations: 'disabled' as const, caret: 'hide' as const }
      if (spec.clip) {
        const target = page.locator(spec.clip)
        const count = await target.count()
        if (count !== 1) {
          throw new Error(`clip の要素が 1 つに定まらない（${count} 件）: ${spec.clip}`)
        }
        await target.screenshot(options)
      } else {
        await page.screenshot({ ...options, fullPage: spec.fullPage ?? false })
      }

      const viewport = page.viewportSize()
      // 掲載画像の幅は章に書いてある値と一致していなければならない。
      // devices の展開順で 1280x720 になっていたことがあるので毎回検査する。
      if (viewport?.width !== SHOT_VIEWPORT.width || viewport?.height !== SHOT_VIEWPORT.height) {
        throw new Error(
          `ビューポートが掲載前提と違う: ${viewport?.width}x${viewport?.height} ` +
          `(期待 ${SHOT_VIEWPORT.width}x${SHOT_VIEWPORT.height})。` +
          'playwright.config.ts の projects[].use を確認すること。'
        )
      }

      fs.mkdirSync(OUT_DIR, { recursive: true })
      fs.writeFileSync(
        path.join(OUT_DIR, `${spec.name}.json`),
        JSON.stringify({
          asset_id: spec.name,
          file: path.relative(REPO_DIR, file),
          chapter: spec.chapter,
          feature: spec.feature,
          state: spec.state,
          captured_at: new Date().toISOString(),
          // 台帳の「撮影日」に使う。UTC の ISO 文字列を先頭 10 文字で切ると
          // 日本時間の午前 9 時前が前日になる（実際に 09-08 01:10 の撮影が
          // 09-07 と記録された）。sv-SE は YYYY-MM-DD 形式で返る。
          captured_on: new Date().toLocaleDateString('sv-SE', { timeZone: 'Asia/Tokyo' }),
          code_commit: CODE_COMMIT,
          viewport: viewport ? `${viewport.width}x${viewport.height}` : '',
          project: testInfo.project.name,
        }, null, 2) + '\n',
        'utf-8'
      )
    })
  }
}

/** 画面が落ち着くまで待つ。表やビューアの描画が間に合わないまま撮るのを防ぐ。 */
export async function settle(page: Page, ms = 600): Promise<void> {
  await page.waitForLoadState('networkidle').catch(() => { /* 撮影は続ける */ })
  await page.waitForTimeout(ms)
}
