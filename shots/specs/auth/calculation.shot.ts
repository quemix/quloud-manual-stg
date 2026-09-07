// 9 章「計算 Job の登録」。
//
// 題材は「サンプルプロジェクト」の結晶マテリアル Si2 に対する
// Quantum ESPRESSO の「電子バンド構造」（3 ステップ）。
//
// **「作成」は押さない。** 押すと開発 DB に Job が残る。ダイアログとフォームの
// 見た目だけを撮る。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

const SI2 = 'mt-63f38596-e00b-418c-b64a-cb70c637c281'

const openSelection = async (page: Page) => {
  await page.goto(`/materials/${SI2}`)
  await settle(page, 1500)
  await page.getByRole('button', { name: 'ジョブ作成' }).first().click()
  await page.getByRole('dialog').waitFor()
  await settle(page, 800)
}

const openForm = async (page: Page) => {
  await openSelection(page)
  await page.getByText('Quantum ESPRESSO', { exact: true }).first().click()
  await settle(page, 400)
  await page.getByText('電子バンド構造', { exact: true }).first().click()
  await settle(page, 400)
  await page.getByRole('button', { name: '開く' }).click()
  await settle(page, 1500)
}

defineShots([
  {
    name: 'calculation_selection_initial',
    chapter: 'calculation',
    feature: '計算ソフト／計算機能の選択',
    state: '初期表示',
    expectUrl: /\/materials\//,
    prepare: openSelection,
  },
  {
    name: 'calculation_selection_chosen',
    chapter: 'calculation',
    feature: '計算ソフト／計算機能の選択',
    state: '計算ソフトと計算機能を選んだ状態',
    expectUrl: /\/materials\//,
    prepare: async (page) => {
      await openSelection(page)
      await page.getByText('Quantum ESPRESSO', { exact: true }).first().click()
      await settle(page, 400)
      await page.getByText('電子バンド構造', { exact: true }).first().click()
      await settle(page, 600)
    },
  },
  {
    name: 'calculation_form_step1',
    chapter: 'calculation',
    feature: 'ジョブ作成フォーム',
    state: 'ステップ 1（SCF）',
    expectUrl: /\/materials\//,
    // fullPage は効かない。ダイアログが固定高で内側にスクロールを持つので、
    // ページを伸ばしてもダイアログの中身は切れたままになる。
    // 続きは calculation_form_groups で撮る。
    prepare: openForm,
  },
  {
    name: 'calculation_form_groups',
    chapter: 'calculation',
    feature: 'ジョブ作成フォーム',
    state: '実験パラメータ・装置パラメータ',
    expectUrl: /\/materials\//,
    prepare: async (page) => {
      await openForm(page)
      // ダイアログの中身をスクロールして、物理モデルより下のまとまりを出す。
      await page.getByText('装置パラメータ', { exact: true }).scrollIntoViewIfNeeded()
      await settle(page, 500)
    },
  },
  {
    name: 'calculation_form_step3',
    chapter: 'calculation',
    feature: 'ジョブ作成フォーム',
    state: 'ステップ 3（電子バンド構造）',
    expectUrl: /\/materials\//,
    prepare: async (page) => {
      await openForm(page)
      await page.getByRole('tab', { name: /ステップ 3/ }).click()
      await settle(page, 800)
    },
  },
])
