// 7 章「Material 詳細画面」。
//
// 画面は左レールで 4 つのペイン（プロパティ／ジョブ／マテリアル／ファイル）に
// 分かれる。ペインは URL のクエリ `m` で指定できる（`menu` ではない）。
//
// **ジョブが多い Material を使わない。** ジョブ一覧には内部のテスト名が
// そのまま出るので、置換表で追える件数の Material を選ぶ。
// Si2（qe1071-si2-light）はジョブが 39 件あるのでジョブ一覧には使えない。
import { defineShots, settle } from '../../lib/shot'
import type { Page } from '@playwright/test'

/** qe1071-si2-light（表示名 Si2、結晶）。 */
const SI2 = 'mt-63f38596-e00b-418c-b64a-cb70c637c281'
/** hybmd-al-fcc（表示名 Al-fcc）。ジョブは 1 件だけ。 */
const AL_FCC = 'mt-4ca30d54-ad04-482f-aa73-de116345a8fc'
/** ver0908-si2-8x8x8-1024atoms（表示名 Si-8x8x8）。Si2 からモデリングで作られた。 */
const SI_8X8X8 = 'mt-8ddcb016-ad96-4b5b-a914-86572f05ab7c'

const openPane = async (page: Page, mid: string, pane?: string) => {
  await page.goto(pane ? `/materials/${mid}?m=${pane}` : `/materials/${mid}`)
  await settle(page, 2500)
}

defineShots([
  {
    name: 'jobdetail_property_pane',
    chapter: 'jobdetail',
    feature: 'プロパティのペイン',
    state: '初期構造とサマリ',
    expectUrl: /\/materials\//,
    prepare: (page) => openPane(page, SI2),
  },
  {
    name: 'jobdetail_rail_expanded',
    chapter: 'jobdetail',
    feature: '左のメニュー',
    state: 'ホバーで展開した状態',
    expectUrl: /\/materials\//,
    // レールは rail + expand-on-hover。ホバーするまで項目名が出ない。
    clip: '.v-navigation-drawer >> nth=0',
    prepare: async (page) => {
      await openPane(page, SI2)
      await page.locator('.v-navigation-drawer').first().hover()
      await settle(page, 800)
    },
  },
  {
    name: 'jobdetail_job_pane',
    chapter: 'jobdetail',
    feature: 'ジョブのペイン',
    state: 'ジョブ一覧',
    expectUrl: /\/materials\/.*m=job/,
    prepare: (page) => openPane(page, AL_FCC, 'job'),
  },
  {
    name: 'jobdetail_material_relations',
    chapter: 'jobdetail',
    feature: 'マテリアルのペイン',
    state: '作成元マテリアル',
    expectUrl: /\/materials\/.*m=material/,
    prepare: (page) => openPane(page, SI_8X8X8, 'material'),
  },
  {
    name: 'jobdetail_file_pane',
    chapter: 'jobdetail',
    feature: 'ファイルのペイン',
    state: '入力ファイルの一覧',
    expectUrl: /\/materials\/.*m=file/,
    prepare: (page) => openPane(page, AL_FCC, 'file'),
  },
])
