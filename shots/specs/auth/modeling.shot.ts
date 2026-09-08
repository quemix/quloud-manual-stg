// 8 章「モデリング」。
//
// モデラーは Material 詳細画面から window.open で**別タブ**に開く。撮影では
// 同じタブで URL を直接開く（modeling/index.vue が組み立てているものと同じ形）。
//
//   /viewers/material/modeler?qid=<マテリアル or ジョブ>&sid=<initial|final>&m=<cell|cell_mol>&pid=<プロジェクトの数値 id>
//
// m は母体が結晶なら cell、分子なら cell_mol。
//
// **「保存」は押さない。** 上書きでも新規でも開発 DB の Material を書き換える。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

/** psi4-verify（表示名「サンプルプロジェクト」）の数値 id。 */
const PROJECT_ID = 8
/** qe1071-si2-light（表示名 Si2、結晶）。 */
const SI2 = 'mt-63f38596-e00b-418c-b64a-cb70c637c281'

const openModeler = async (page: Page, qid: string, mode: string) => {
  await page.goto(`/viewers/material/modeler?qid=${qid}&sid=initial&m=${mode}&pid=${PROJECT_ID}`)
  // three.js の初期化と構造の読み込みが終わるまで待つ。通常のページより重い。
  await settle(page, 4000)
}

defineShots([
  {
    name: 'modeling_modeler_initial',
    chapter: 'modeling',
    feature: 'モデラー',
    state: '結晶を開いた初期表示',
    expectUrl: /\/viewers\/material\/modeler/,
    prepare: (page) => openModeler(page, SI2, 'cell'),
  },
  {
    name: 'modeling_supercell_panel',
    chapter: 'modeling',
    feature: 'モデラーの操作パネル',
    state: 'スーパーセル',
    expectUrl: /\/viewers\/material\/modeler/,
    prepare: async (page) => {
      await openModeler(page, SI2, 'cell')
      await page.getByText('スーパーセル', { exact: true }).first().click()
      await settle(page, 1200)
    },
  },
  {
    name: 'modeling_surface_panel',
    chapter: 'modeling',
    feature: 'モデラーの操作パネル',
    state: '表面（スラブ生成）',
    expectUrl: /\/viewers\/material\/modeler/,
    prepare: async (page) => {
      await openModeler(page, SI2, 'cell')
      await page.getByText('表面', { exact: true }).first().click()
      await settle(page, 1200)
    },
  },
  {
    name: 'modeling_view_settings',
    chapter: 'modeling',
    feature: 'モデラーの表示設定',
    state: '設定メニュー',
    expectUrl: /\/viewers\/material\/modeler/,
    prepare: async (page) => {
      await openModeler(page, SI2, 'cell')
      await page.locator('.mdi-cog').first().click()
      await settle(page, 900)
    },
  },
  {
    name: 'modeling_save_dialog',
    chapter: 'modeling',
    feature: '「モデルを保存」ダイアログ',
    state: '名前・説明・上書きの指定',
    expectUrl: /\/viewers\/material\/modeler/,
    clip: '.v-overlay__content >> nth=-1',
    prepare: async (page) => {
      await openModeler(page, SI2, 'cell')
      // 保存アイコンを押すとダイアログが出るだけ。書き込みは
      // ダイアログの「保存」→ window.confirm を通ってから。
      await page.locator('.mdi-content-save').first().click()
      await page.getByRole('dialog').waitFor()
      await settle(page, 800)
    },
  },
  {
    name: 'modeling_site_property',
    chapter: 'modeling',
    feature: 'サイトプロパティ設定',
    state: '原子ごとの拘束条件・初期スピン',
    expectUrl: /\/viewers\/material\/modeler/,
    // ジョブ作成フォームの「拘束条件・初期スピンを設定」から開く画面。
    // 同じモデラーを sp（機能）と sps（セッション）付きで開いた別モード。
    // 保存先は localStorage で、DB には書かない。
    prepare: async (page) => {
      await page.goto(
        `/viewers/material/modeler?qid=${SI2}&sid=initial&m=cell&pid=${PROJECT_ID}` +
        '&sp=fix,spin&sps=manual-shot'
      )
      await settle(page, 4000)
    },
  },
])
