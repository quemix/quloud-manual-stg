// 3 章「サインイン・サインアウト」。サインイン前の画面。
//
// Ver.7.0 で気をつける点（実測）:
//   - 「パスワードをお忘れですか？」は target="_blank" で別タブに開く。
//     同じ page で waitForURL しても遷移しないので、直接 goto する。
//   - 「お問い合わせ」はアプリ内のフォームではなく https://www.quemix.com/contact
//     への外部リンク。アプリ内の /inquiry はサインイン後の画面（14 章）。
import { defineShots, settle } from '../../lib/shot'

defineShots([
  {
    name: 'signin_form_initial',
    chapter: 'signin',
    feature: 'サインイン画面',
    state: '初期表示',
    expectUrl: /\/sign_in$/,
    prepare: async (page) => {
      await page.goto('/sign_in')
      await settle(page)
    },
  },
  {
    name: 'signin_reset_password_request',
    chapter: 'signin',
    feature: 'パスワード再設定申請',
    state: '初期表示',
    expectUrl: /\/request_reset_password$/,
    prepare: async (page) => {
      await page.goto('/request_reset_password')
      await settle(page)
    },
  },
])
