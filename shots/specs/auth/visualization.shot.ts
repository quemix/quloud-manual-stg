// 12 章「計算結果の可視化」。
//
// 題材は 9・10 章と同じ Si2 × Quantum ESPRESSO「電子バンド構造」の実行済み Job
// （v7spec-qebands-si2 / 表示名 Si2-bands-02、Status: Succeeded）。
//
// **「結果を解析」は押さない。** 押すと ParsedResult を作り直して開発 DB を
// 書き換える。既にある解析済みの結果を撮る。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

const SI2 = 'mt-63f38596-e00b-418c-b64a-cb70c637c281'
const QID_SUCCEEDED = '7f6bdb5a-b051-4035-9fb2-547e23e60c42'
/** v7spec-qelat-normal-si2（格子定数最適化・succeeded / 表示名 Si2-latopt-01）。
 *  構造のカード（3D ビューア）と「Materialとして保存」を撮るために使う。 */
const QID_LATTICE_OPT = '4365d281-7caf-4ca2-8f14-4782d158e96d'

const openResults = async (page: Page, qid: string = QID_SUCCEEDED) => {
  await page.goto(`/materials/${SI2}?m=job&qid=${qid}`)
  await settle(page, 2000)
  // 「Results」の節へ送る。左のナビと同じ scrollTo（job/item.vue の 72 px オフセット）。
  await page.locator('#section-results-summary').waitFor()
  await page.evaluate(() => {
    const el = document.getElementById('section-results-summary')
    if (!el) return
    window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 72 })
  })
  await settle(page, 900)
}

defineShots([
  {
    name: 'visualization_results_step1',
    chapter: 'visualization',
    feature: '計算結果（Results）',
    state: 'ステップ 1（SCF）のカード',
    expectUrl: /\/materials\/.*m=job/,
    prepare: openResults,
  },
  {
    name: 'visualization_results_band',
    chapter: 'visualization',
    feature: '計算結果（Results）',
    state: 'ステップ 3（電子バンド構造）のバンド図',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openResults(page)
      // 「入力」の節にも同じステップタブがあるので、Results の節に限定する。
      await page.locator('#section-results-summary')
        .getByRole('tab', { name: /ステップ 3/ }).click()
      await settle(page, 2500)
      await page.locator('#section-results-summary').evaluate((el) => {
        window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 72 })
      })
      await settle(page, 800)
    },
  },
  {
    name: 'visualization_card_menu',
    chapter: 'visualization',
    feature: '結果カードのメニュー',
    state: 'Property に登録・削除',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openResults(page)
      await page.locator('.v-sheet .position-relative').first()
        .locator('button:has(.mdi-dots-vertical)').click()
      await settle(page, 600)
    },
  },
  {
    name: 'visualization_results_structure',
    chapter: 'visualization',
    feature: '計算結果（Results）',
    state: '構造のカード（格子定数最適化）',
    expectUrl: /\/materials\/.*m=job/,
    prepare: (page) => openResults(page, QID_LATTICE_OPT),
  },
])
