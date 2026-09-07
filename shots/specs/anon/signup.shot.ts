// 2 章「サインアップ」。サインイン前の申込フォーム。
import { defineShots, settle } from '../../lib/shot'

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
])
