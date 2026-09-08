// 10 章「計算 Job の実行」。
//
// 題材は 9 章と同じ「サンプルプロジェクト」の結晶マテリアル Si2 に対する
// Quantum ESPRESSO の「電子バンド構造」。
//
// **「実行」は押さない。** 押すと開発 DB の Job が投入され、ローカルの
// コンテナで計算が走る。ダイアログの見た目だけを撮る。
//
// Material 詳細画面のペインと Job は URL で指定できる（`?m=job&qid=<quloud_job_id>`）。
// キーは `menu` ではなく `m`。materials/[quloud_material_id]/index.vue の
// onMounted が `check_query_params(route.query, ['m'])` で読み、job/item.vue の
// onMounted が `qid` を読んで Job をロードする。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

const SI2 = 'mt-63f38596-e00b-418c-b64a-cb70c637c281'
/** merge-verify-qebands-si2（Status: Registered）。Run Job ダイアログ用。 */
const QID_REGISTERED = '1f6bedf5-cdec-4a9c-81ee-1c1eaf628dc0'
/** v7spec-qebands-si2（Status: Succeeded）。実行後の画面用。 */
const QID_SUCCEEDED = '7f6bdb5a-b051-4035-9fb2-547e23e60c42'

const openJob = async (page: Page, qid: string) => {
  await page.goto(`/materials/${SI2}?m=job&qid=${qid}`)
  await settle(page, 2000)
}

const openRunDialog = async (page: Page) => {
  await openJob(page, QID_REGISTERED)
  await page.getByRole('button', { name: 'Run Job' }).first().click()
  await page.getByRole('dialog').waitFor()
  await settle(page, 800)
}

defineShots([
  {
    name: 'runjob_detail_registered',
    chapter: 'runjob',
    feature: 'Job 詳細画面',
    state: 'Registered（実行前）',
    expectUrl: /\/materials\/.*m=job/,
    prepare: (page) => openJob(page, QID_REGISTERED),
  },
  {
    name: 'runjob_dialog_cpu',
    chapter: 'runjob',
    feature: 'ジョブ投入ダイアログ',
    state: 'CPU タブ（初期表示）',
    expectUrl: /\/materials\/.*m=job/,
    prepare: openRunDialog,
  },
  {
    name: 'runjob_dialog_hpc',
    chapter: 'runjob',
    feature: 'ジョブ投入ダイアログ',
    state: 'HPC タブ（2 ノード）',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openRunDialog(page)
      await page.getByRole('tablist').getByText('HPC', { exact: true }).click()
      await settle(page, 600)
      // 「配置（2 ノード以上）」は 2 ノード以上を選んだときだけ現れる。
      await page.getByText('2 ノード', { exact: true }).click()
      await settle(page, 600)
    },
  },
  {
    name: 'runjob_dialog_gpu',
    chapter: 'runjob',
    feature: 'ジョブ投入ダイアログ',
    state: 'GPU タブ',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openRunDialog(page)
      await page.getByRole('tablist').getByText('GPU', { exact: true }).click()
      await settle(page, 600)
    },
  },
  {
    name: 'runjob_dialog_advanced',
    chapter: 'runjob',
    feature: 'ジョブ投入ダイアログ',
    state: '詳細設定',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openRunDialog(page)
      await page.getByRole('button', { name: '詳細設定を開く' }).click()
      await settle(page, 600)
    },
  },
  {
    name: 'runjob_summary_succeeded',
    chapter: 'runjob',
    feature: 'Job 詳細画面',
    state: 'Succeeded（ジョブ概要）',
    expectUrl: /\/materials\/.*m=job/,
    prepare: (page) => openJob(page, QID_SUCCEEDED),
  },
  {
    name: 'runjob_compute_resource',
    chapter: 'runjob',
    feature: 'Job 詳細画面',
    state: '計算リソース',
    expectUrl: /\/materials\/.*m=job/,
    prepare: async (page) => {
      await openJob(page, QID_SUCCEEDED)
      // 「計算」は別ページではなく同じページの節。左のナビの項目は
      // v-list-item で role を持たないので、ナビ自身と同じ scrollTo を直接行う
      // （job/item.vue の scrollTo('computation') と同じ 72 px のオフセット）。
      await page.locator('#section-computation').waitFor()
      await page.evaluate(() => {
        const el = document.getElementById('section-computation')
        if (!el) return
        window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 72 })
      })
      await settle(page, 900)
    },
  },
])
