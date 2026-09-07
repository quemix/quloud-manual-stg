// 2 章「サインアップ」。サインイン前の利用申込。
import { expect } from '@playwright/test'
import type { Page } from '@playwright/test'
import { defineShots, settle } from '../../lib/shot'

/**
 * 申込フォームの入力欄を項目名で埋める。
 *
 * 入力欄に label 属性が無く（左の列に項目名のテキストがあるだけ）、
 * getByLabel では掴めない。行を項目名で絞ってからその中の input を取る。
 * 正規表現を前後で固定しているのは「所属団体」が「所属団体郵便番号」
 * などにも前方一致してしまうため。末尾の ` *` は必須マーク。
 */
const fillRow = async (page: Page, label: string, value: string) => {
  const row = page.locator('.v-form .v-row').filter({
    has: page.locator('.v-col', { hasText: new RegExp(`^${label}\\s*\\*?\\s*$`) }),
  })
  await row.locator('input, textarea').first().fill(value)
}

/** 掲載用の架空の申込内容。実在の氏名・社名・住所は使わない。 */
const SAMPLE = [
  ['姓', '山田'],
  ['名', '太郎'],
  ['姓カナ', 'ヤマダ'],
  ['名カナ', 'タロウ'],
  ['メールアドレス', 'user@example.com'],
  ['役職', '担当者'],
  ['所属団体郵便番号', '100-0001'],
  ['所属団体住所', '東京都千代田区千代田1-1'],
  ['所属団体', 'サンプル株式会社'],
  ['所属団体（部・研究室）', 'サンプル部門'],
] as const

const fillApplicantForm = async (page: Page) => {
  for (const [label, value] of SAMPLE) await fillRow(page, label, value)
  await page.getByLabel('同意する').check()
}

defineShots([
  {
    name: 'signup_applicant_form',
    chapter: 'signup',
    feature: '利用申込フォーム',
    state: '初期表示',
    expectUrl: /\/applicant$/,
    fullPage: true,
    prepare: async (page) => {
      await page.goto('/applicant')
      await settle(page)
    },
  },
  {
    name: 'signup_applicant_filled',
    chapter: 'signup',
    feature: '利用申込フォーム',
    state: '入力後',
    expectUrl: /\/applicant$/,
    fullPage: true,
    prepare: async (page) => {
      await page.goto('/applicant')
      await settle(page)
      await fillApplicantForm(page)
      await settle(page, 300)
    },
  },
  {
    name: 'signup_applicant_confirm',
    chapter: 'signup',
    feature: '利用申込の確認画面',
    state: '入力内容の確認',
    expectUrl: /\/applicant$/,
    fullPage: true,
    prepare: async (page) => {
      await page.goto('/applicant')
      await settle(page)
      await fillApplicantForm(page)
      // 「確認」は validate_only: true で投げるだけなので申込レコードは作られない
      // （API::ApplicantsController#create が valid? だけ見て head :ok を返す）。
      // 「申込」は押さない。押すと開発 DB に申込が残る。
      await page.getByRole('button', { name: '確認' }).click()
      await expect(page.getByRole('button', { name: '申込' })).toBeVisible()
      await settle(page, 300)
    },
  },
  {
    name: 'signup_applicant_complete',
    chapter: 'signup',
    feature: '利用申込の完了画面',
    state: '送信後',
    expectUrl: /\/applicant\/complete$/,
    prepare: async (page) => {
      // 静的なページなので直接開ける。実際に申込を送ると遷移してくる先。
      await page.goto('/applicant/complete')
      await settle(page)
    },
  },
])
