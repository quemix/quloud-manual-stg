import { defineConfig, devices } from '@playwright/test'
import { SHOT_VIEWPORT } from './lib/viewport'

// 撮影対象はローカル Docker の Nuxt（~/v6.0 の docker compose）。
// 本番や stg を叩いて撮ることはしない。実データが写るし、マニュアルの
// 基準環境をローカルに固定するのが設計上の決定事項（設計書 D3）。
const BASE_URL = process.env.QULOUD_BASE_URL ?? 'http://localhost:3000'

export default defineConfig({
  testDir: '.',
  // Nuxt の dev サーバーは初回アクセスするルートを都度 SSR コンパイルするので
  // 通常の E2E より余裕を持たせる。
  timeout: 120_000,
  expect: { timeout: 20_000 },
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  // 既定を 2 に抑えている。撮影は dev サーバーの初回コンパイルを何本も
  // 同時に走らせることになり、並列を上げるとタイムアウトで落ちやすい。
  workers: Number(process.env.QULOUD_SHOTS_WORKERS ?? 2),
  reporter: [['list']],
  use: {
    baseURL: BASE_URL,
    navigationTimeout: 90_000,
    actionTimeout: 20_000,
    trace: 'retain-on-failure',
    // 失敗時の Playwright 自動スクリーンショットは撮らない。撮影物と
    // 混ざると source/images/v70 に置いた画像との区別がつかなくなる。
    screenshot: 'off',
    locale: 'ja-JP',
    timezoneId: 'Asia/Tokyo',
    // マニュアルの掲載画像はこの幅で撮る。lib/viewport.ts を参照。
    // projects[].use にも同じものを置く必要がある（devices の展開が
    // ここの viewport を上書きするため）。
    viewport: SHOT_VIEWPORT,
  },
  projects: [
    {
      name: 'setup',
      testMatch: /setup\/auth\.setup\.ts$/,
      use: { ...devices['Desktop Chrome'], viewport: SHOT_VIEWPORT },
    },
    {
      // サインイン前の画面（申込・サインイン・パスワード再設定・お問い合わせ）。
      name: 'anon',
      testMatch: /specs\/anon\/.*\.shot\.ts$/,
      use: { ...devices['Desktop Chrome'], viewport: SHOT_VIEWPORT },
    },
    {
      // サインイン後の画面。storageState を setup から受け取る。
      name: 'auth',
      testMatch: /specs\/auth\/.*\.shot\.ts$/,
      dependencies: ['setup'],
      use: {
        ...devices['Desktop Chrome'],
        viewport: SHOT_VIEWPORT,
        storageState: '.auth/user.json',
      },
    },
  ],
})
