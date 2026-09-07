// 4 章「新規ユーザーの招待」。管理ユーザー（オーナー）でのみ開ける画面。
import { defineShots, settle } from '../../lib/shot'

defineShots([
  {
    name: 'invitation_users_list',
    chapter: 'invitation',
    feature: 'ユーザー一覧',
    state: '初期表示',
    expectUrl: /\/users$/,
    prepare: async (page) => {
      await page.goto('/users')
      await settle(page)
    },
  },
  {
    name: 'invitation_list_initial',
    chapter: 'invitation',
    feature: '招待一覧',
    state: '初期表示',
    expectUrl: /\/invitations$/,
    prepare: async (page) => {
      await page.goto('/invitations')
      await settle(page)
    },
  },
  {
    name: 'invitation_invite_dialog',
    chapter: 'invitation',
    feature: 'メンバーを招待ダイアログ',
    state: '入力前',
    expectUrl: /\/invitations$/,
    prepare: async (page) => {
      await page.goto('/invitations')
      await settle(page)
      // 招待ダイアログを開くボタンは <v-btn icon="mdi-email-plus-outline"> で、
      // aria-label もテキストも無い（アイコンだけ）。role や文字で掴めないので
      // アイコンのクラスで指定する。ボタン自体はオーナーにしか描かれない。
      await page.locator('button:has(.mdi-email-plus-outline)').click()
      await page.getByRole('dialog').waitFor()
      await settle(page, 300)
    },
  },
])
