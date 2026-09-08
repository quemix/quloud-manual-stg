// 6 章「Material の登録」。
//
// 起点はプロジェクト詳細画面（/projects/<quloud_pj_id>）の「新規マテリアル」。
// material/create.vue を描画しているのはこのページだけ。
//
// **「作成」「選択」は押さない。** 押すと開発 DB に Material が残る。
// 外部データベースの検索は読み取りだけなので実行してよい。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

/** psi4-verify（表示名「サンプルプロジェクト」）。 */
const PROJECT = 'pj-ae5d5154-8056-4120-ac83-6c7585845226'

const openCreateDialog = async (page: Page) => {
  await page.goto(`/projects/${PROJECT}`)
  await settle(page, 2000)
  await page.getByRole('button', { name: '新規マテリアル' }).click()
  await page.getByRole('dialog').waitFor()
  await settle(page, 800)
}

defineShots([
  {
    name: 'jobs_and_models_atom_project_materials',
    chapter: 'jobs_and_models_atom',
    feature: 'プロジェクト詳細画面',
    state: 'マテリアル一覧と「新規マテリアル」',
    expectUrl: /\/projects\//,
    // マテリアルの列だけを撮る。同じ画面のジョブ一覧には内部のテスト名
    // （issue 番号を含むもの）がそのまま出ており、置換表では追い切れない。
    clip: '.v-col:has(button:has-text("新規マテリアル"))',
    prepare: async (page) => {
      await page.goto(`/projects/${PROJECT}`)
      await settle(page, 2000)
    },
  },
  {
    name: 'jobs_and_models_atom_create_dialog',
    chapter: 'jobs_and_models_atom',
    feature: '「マテリアルを作成」ダイアログ',
    state: '初期表示',
    expectUrl: /\/projects\//,
    // ダイアログだけを撮る。背後のプロジェクト詳細画面のジョブ一覧に、
    // issue 番号を含む内部のテスト名がそのまま出ている。
    // nth=-1 は最後に開いたオーバーレイ＝いちばん手前のダイアログ。
    clip: '.v-overlay__content >> nth=-1',
    prepare: openCreateDialog,
  },
  {
    name: 'jobs_and_models_atom_crystal_search',
    chapter: 'jobs_and_models_atom',
    feature: '「結晶を検索」ダイアログ',
    state: '初期表示',
    expectUrl: /\/projects\//,
    // ダイアログだけを撮る。背後のプロジェクト詳細画面のジョブ一覧に、
    // issue 番号を含む内部のテスト名がそのまま出ている。
    // nth=-1 は最後に開いたオーバーレイ＝いちばん手前のダイアログ。
    clip: '.v-overlay__content >> nth=-1',
    prepare: async (page) => {
      await openCreateDialog(page)
      await page.getByRole('button', { name: 'Crystal DBで検索' }).click()
      await settle(page, 900)
    },
  },
  {
    name: 'jobs_and_models_atom_molecule_search',
    chapter: 'jobs_and_models_atom',
    feature: '「分子を検索」ダイアログ',
    state: '初期表示',
    expectUrl: /\/projects\//,
    // ダイアログだけを撮る。背後のプロジェクト詳細画面のジョブ一覧に、
    // issue 番号を含む内部のテスト名がそのまま出ている。
    // nth=-1 は最後に開いたオーバーレイ＝いちばん手前のダイアログ。
    clip: '.v-overlay__content >> nth=-1',
    prepare: async (page) => {
      await openCreateDialog(page)
      await page.getByRole('button', { name: 'Molecule DBで検索' }).click()
      await settle(page, 500)
      await page.getByRole('listitem').filter({ hasText: 'PubChemで検索' }).first().click()
      await settle(page, 900)
    },
  },
  {
    name: 'jobs_and_models_atom_polymer_preset',
    chapter: 'jobs_and_models_atom',
    feature: '「ポリマープリセットを選択」ダイアログ',
    state: '初期表示',
    expectUrl: /\/projects\//,
    // ダイアログだけを撮る。背後のプロジェクト詳細画面のジョブ一覧に、
    // issue 番号を含む内部のテスト名がそのまま出ている。
    // nth=-1 は最後に開いたオーバーレイ＝いちばん手前のダイアログ。
    clip: '.v-overlay__content >> nth=-1',
    prepare: async (page) => {
      await openCreateDialog(page)
      await page.getByRole('button', { name: 'Molecule DBで検索' }).click()
      await settle(page, 500)
      await page.getByRole('listitem').filter({ hasText: 'ポリマープリセットから選択' }).first().click()
      await settle(page, 1200)
    },
  },
  {
    name: 'jobs_and_models_atom_file_upload',
    chapter: 'jobs_and_models_atom',
    feature: '「ファイルをアップロード」ダイアログ',
    state: '初期表示',
    expectUrl: /\/projects\//,
    // ダイアログだけを撮る。背後のプロジェクト詳細画面のジョブ一覧に、
    // issue 番号を含む内部のテスト名がそのまま出ている。
    // nth=-1 は最後に開いたオーバーレイ＝いちばん手前のダイアログ。
    clip: '.v-overlay__content >> nth=-1',
    prepare: async (page) => {
      await openCreateDialog(page)
      await page.getByRole('button', { name: 'ファイルアップロード' }).click()
      await settle(page, 900)
    },
  },
])
