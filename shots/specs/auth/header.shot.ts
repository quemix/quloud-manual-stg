// 14 章「ヘッダーメニュー（各種管理）」。
//
// /inquiry は未サインインでは開けない（auth.global.ts の許可リストに無く
// /sign_in へ飛ばされる）。3 章のサインイン前のお問い合わせは
// https://www.quemix.com/contact への外部リンクで、こちらとは別物。
import { defineShots, settle } from '../../lib/shot'

defineShots([
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
