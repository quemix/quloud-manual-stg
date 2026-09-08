// 11 章「Property」。
//
// 登録のダイアログは Si2 × Quantum ESPRESSO「電子バンド構造」の実行済み Job から、
// 登録後の見え方は既に Property が登録されている結晶マテリアル Si (mp-149) から撮る。
//
// **「登録」は押さない。** 押すと開発 DB に PropertyEntry が残る。
// ダイアログの見た目だけを撮る（グループ一覧の取得は GET だけなので副作用が無い）。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

const SI2 = 'mt-63f38596-e00b-418c-b64a-cb70c637c281'
const QID_SUCCEEDED = '7f6bdb5a-b051-4035-9fb2-547e23e60c42'
/**
 * water（分子）。プロパティグループ「振動解析」に 2 件が登録済み。
 *
 * Property が登録されている Material は他にもあるが、Si (mp-149) と
 * Si (conventional) は **別テナント（group 4）** のもので、撮影に使う
 * アカウント（group 1）からは開けない。開こうとすると auth ミドルウェアが
 * /dashboard へ飛ばすだけで、エラーにはならない。
 */
const MATERIAL_WITH_PROPERTIES = 'mt-78cb60ff-6df8-4234-97dd-e882083eb039'

const openResults = async (page: Page) => {
  await page.goto(`/materials/${SI2}?m=job&qid=${QID_SUCCEEDED}`)
  await settle(page, 2000)
  await page.locator('#section-results-summary').waitFor()
  await page.evaluate(() => {
    const el = document.getElementById('section-results-summary')
    if (!el) return
    window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 72 })
  })
  await settle(page, 900)
}

/** Material 詳細画面のプロパティペイン。既定のペインなのでクエリは要らない。 */
const openPropertyPane = async (page: Page) => {
  await page.goto(`/materials/${MATERIAL_WITH_PROPERTIES}`)
  await settle(page, 2500)
}

defineShots([
  {
    name: 'property_pin_dialog',
    chapter: 'property',
    feature: 'Property に登録するダイアログ',
    state: '表示名とグループの指定',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openResults(page)
      await page.locator('.v-sheet .position-relative').first()
        .locator('button:has(.mdi-dots-vertical)').click()
      await settle(page, 400)
      await page.getByRole('listitem').filter({ hasText: 'Propertyに登録' }).first().click()
      await page.getByRole('dialog').waitFor()
      await settle(page, 800)
    },
  },
  {
    name: 'property_material_pane',
    chapter: 'property',
    feature: 'Material 詳細画面のプロパティ',
    state: '登録済みのグループとカード',
    expectUrl: /\/materials\//,
    prepare: async (page) => {
      await openPropertyPane(page)
      // 初期構造の下にある登録済み Property まで送る。
      await page.locator('[id^="section-group-"]').first().evaluate((el) => {
        window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 72 })
      })
      await settle(page, 1500)
    },
  },
  {
    name: 'property_card_menu',
    chapter: 'property',
    feature: 'Property カードのメニュー',
    state: 'Property から削除',
    expectUrl: /\/materials\//,
    prepare: async (page) => {
      await openPropertyPane(page)
      const group = page.locator('[id^="section-group-"]').first()
      await group.evaluate((el) => {
        window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 72 })
      })
      await settle(page, 1500)
      // カードは result_type ごとに別コンポーネントで、共通の目印が無い。
      // カード内の Property 名で特定する（置換は撮影直前なのでここでは元の名前）。
      await page.locator('.v-card:has-text("振動モード")').first()
        .locator('button:has(.mdi-dots-vertical)').first().click()
      await settle(page, 600)
    },
  },
  {
    name: 'property_dashboard_list',
    chapter: 'property',
    feature: 'ダッシュボードのプロパティ一覧',
    state: '初期表示',
    expectUrl: /\/dashboard/,
    prepare: async (page) => {
      await page.goto('/dashboard?tab=properties')
      await settle(page, 2000)
    },
  },
])
