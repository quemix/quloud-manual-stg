// 14 章「ヘッダーメニュー」。
//
// ヘッダーは全画面共通。メニューを開いた状態はオーバーレイなので、
// clip で開いた部分だけを撮ると背後の一覧が写らない。
//
// /inquiry は未サインインでは開けない（auth.global.ts の許可リストに無く
// /sign_in へ飛ばされる）。3 章のサインイン前のお問い合わせは
// https://www.quemix.com/contact への外部リンクで、こちらとは別物。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

const openHome = async (page: Page) => {
  await page.goto('/dashboard?tab=projects')
  await settle(page, 1800)
}

const openHeaderMenu = async (page: Page, label: string) => {
  await openHome(page)
  await page.getByRole('button', { name: label }).first().click()
  await settle(page, 700)
}

defineShots([
  {
    name: 'header_icons',
    chapter: 'header',
    feature: 'ヘッダー',
    state: 'アイコンの並び',
    expectUrl: /\/dashboard/,
    clip: 'header',
    prepare: openHome,
  },
  {
    name: 'header_help_menu',
    chapter: 'header',
    feature: 'ヘルプのメニュー',
    state: '項目の一覧',
    expectUrl: /\/dashboard/,
    clip: '.v-overlay__content >> nth=-1',
    prepare: (page) => openHeaderMenu(page, 'ヘルプ'),
  },
  {
    name: 'header_settings_menu',
    chapter: 'header',
    feature: '設定のメニュー',
    state: '項目の一覧',
    expectUrl: /\/dashboard/,
    clip: '.v-overlay__content >> nth=-1',
    prepare: (page) => openHeaderMenu(page, '設定'),
  },
  {
    name: 'header_information_dialog',
    chapter: 'header',
    feature: '「利用情報」ダイアログ',
    state: 'ポイント・有効期限・ストレージ',
    expectUrl: /\/dashboard/,
    clip: '.v-overlay__content >> nth=-1',
    prepare: (page) => openHeaderMenu(page, '利用情報'),
  },
  {
    name: 'header_usage_status',
    chapter: 'header',
    feature: '利用状況',
    state: 'ポイント残高とストレージ',
    expectUrl: /\/usage_status/,
    // ポイント履歴の「ジョブ」列に内部のテスト名（issue 番号を含む）が
    // そのまま出るので、サマリの 2 枚だけを撮る。
    clip: '.summary-row',
    prepare: async (page) => {
      await page.goto('/usage_status')
      await settle(page, 2500)
    },
  },
  {
    name: 'header_orders',
    chapter: 'header',
    feature: '注文履歴',
    state: '初期表示',
    expectUrl: /\/orders/,
    prepare: async (page) => {
      await page.goto('/orders')
      await settle(page, 2000)
    },
  },
  {
    name: 'header_notices',
    chapter: 'header',
    feature: 'お知らせ',
    state: '一覧',
    expectUrl: /\/notices/,
    prepare: async (page) => {
      await page.goto('/notices')
      await settle(page, 2000)
    },
  },
  {
    name: 'header_profile',
    chapter: 'header',
    feature: 'プロフィール',
    state: '初期表示',
    expectUrl: /\/profile/,
    prepare: async (page) => {
      await page.goto('/profile')
      await settle(page, 2000)
    },
  },
  {
    name: 'header_inquiry_form',
    chapter: 'header',
    feature: 'お問い合わせフォーム（サインイン後）',
    state: '初期表示',
    expectUrl: /\/inquiry$/,
    fullPage: true,
    prepare: async (page) => {
      await page.goto('/inquiry')
      await settle(page)
    },
  },
])
