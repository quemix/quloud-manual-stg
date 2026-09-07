/**
 * 撮影用アカウントでサインインして storageState を保存する。
 *
 * 資格情報はコミットしない。環境変数で渡す（既定値も置かない）。
 * ローカル開発 DB のシードユーザーのアドレスは実在の形をしているので、
 * 公開リポジトリに書けない。値は meta/README を参照。
 *
 *   QULOUD_SHOTS_EMAIL=... QULOUD_SHOTS_PASSWORD=... make shots
 *
 * 新規ユーザーの作成や既存ユーザーのパスワード書き換えはしない。
 * ~/v6.0 は他人の作業環境なので読み取りだけで済ませる。
 */
import { test as setup, expect } from '@playwright/test'

const AUTH_FILE = '.auth/user.json'

setup('authenticate', async ({ page }) => {
  const email = process.env.QULOUD_SHOTS_EMAIL
  const password = process.env.QULOUD_SHOTS_PASSWORD
  if (!email || !password) {
    throw new Error(
      '撮影用アカウントが指定されていない。\n' +
      '  QULOUD_SHOTS_EMAIL=<メールアドレス> QULOUD_SHOTS_PASSWORD=<パスワード> make shots\n' +
      '値は非公開リポジトリ meta/ の README を参照すること。'
    )
  }

  await page.goto('/sign_in')
  await page.getByTestId('signin-email').locator('input').fill(email)
  await page.getByTestId('signin-password').locator('input').fill(password)
  await page.getByTestId('signin-submit').click()

  await page.waitForURL(/\/dashboard/, { timeout: 90_000 })
  await expect(page.getByRole('tab', { name: 'プロジェクト' })).toBeVisible()

  await page.context().storageState({ path: AUTH_FILE })
})
