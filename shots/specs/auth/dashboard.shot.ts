// 5 章「ホーム画面」。
//
// タブは URL のクエリで指定できる（/dashboard?tab=projects|materials|jobs|properties）。
//
// **ジョブのタブは絞り込んでから撮る。** テナントには 109 件のジョブがあり、
// 名前は内部のテスト名のまま。置換表では追い切れないので、検索で 1 件に絞る。
// 検索語もそのまま画面に写るが、置換表に載っている文字列を使えば置換される。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

const openTab = async (page: Page, tab: string) => {
  await page.goto(`/dashboard?tab=${tab}`)
  await settle(page, 2000)
}

/** 検索ボックスを開いて語を入れる。虫眼鏡でフィルターの行が出る。 */
const search = async (page: Page, word: string) => {
  await page.locator('button:has(.mdi-magnify)').first().click()
  await settle(page, 500)
  await page.getByRole('textbox').first().fill(word)
  await settle(page, 1200)
}

defineShots([
  {
    name: 'dashboard_projects_tab',
    chapter: 'dashboard',
    feature: 'ホーム画面',
    state: 'プロジェクトのタブ',
    expectUrl: /\/dashboard/,
    prepare: (page) => openTab(page, 'projects'),
  },
  {
    name: 'dashboard_filter_panel',
    chapter: 'dashboard',
    feature: '一覧の絞り込み',
    state: 'フィルターのパネルを開いた状態',
    expectUrl: /\/dashboard/,
    prepare: async (page) => {
      await openTab(page, 'materials')
      await page.locator('button:has(.mdi-magnify)').first().click()
      await settle(page, 500)
      await page.getByRole('button', { name: 'フィルター' }).click()
      await settle(page, 900)
    },
  },
  {
    name: 'dashboard_project_create',
    chapter: 'dashboard',
    feature: '「プロジェクトを作成」ダイアログ',
    state: '初期表示',
    expectUrl: /\/dashboard/,
    clip: '.v-overlay__content >> nth=-1',
    prepare: async (page) => {
      await openTab(page, 'projects')
      await page.getByRole('button', { name: '新規プロジェクト' }).click()
      await page.getByRole('dialog').waitFor()
      await settle(page, 800)
    },
  },
  {
    name: 'dashboard_jobs_tab',
    chapter: 'dashboard',
    feature: 'ホーム画面',
    state: 'ジョブのタブ（検索で絞り込んだ状態）',
    expectUrl: /\/dashboard/,
    prepare: async (page) => {
      await openTab(page, 'jobs')
      // hybmd-al-fcc は置換表で Al-fcc になる。検索欄の文字も置換される。
      await search(page, 'hybmd-al-fcc')
    },
  },
])
