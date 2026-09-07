// 3 章「サインイン・サインアウト」。サインイン後の画面。
import { defineShots, settle } from '../../lib/shot'

defineShots([
  {
    name: 'signin_dashboard_after_signin',
    chapter: 'signin',
    feature: 'サインイン直後のダッシュボード',
    state: 'プロジェクトタブ',
    expectUrl: /\/dashboard/,
    prepare: async (page) => {
      await page.goto('/dashboard')
      await page.getByRole('tab', { name: 'プロジェクト' }).waitFor()
      await settle(page)
    },
  },
  {
    name: 'signin_account_menu_signout',
    chapter: 'signin',
    feature: 'アカウントメニュー',
    state: 'サインアウトの位置',
    expectUrl: /\/dashboard/,
    prepare: async (page) => {
      await page.goto('/dashboard')
      await page.getByRole('tab', { name: 'プロジェクト' }).waitFor()
      await settle(page)
      await page.getByRole('button', { name: 'アカウント' }).click()
      await page.getByText('サインアウト').waitFor()
      await settle(page, 300)
    },
  },
])
