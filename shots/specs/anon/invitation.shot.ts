// 4 章「新規ユーザーの招待」のうち、招待された側の登録画面。
//
// /sign_up は招待メールの URL に付いているトークンが無いと開けない。
// トークン無しで開くと onMounted の fetch_invitation が失敗して
// /sign_in へ飛ぶ（middleware ではなくページ自身の遷移）。
//
// DB の invitations.token は Devise のダイジェストで、生のトークンは
// 発行時にしか手に入らない。承認や再送信を押せば発行できるが、それは
// 開発 DB への書き込みになるのでハーネスからは行わない。
//
// 撮るときは、承認・再送信を手で行ってから letter_opener（Rails 側の
// http://localhost:3001/letter_opener）でメールを開き、URL のトークンを
// 環境変数で渡す。
//
//   QULOUD_SHOTS_SIGNUP_TOKEN=<トークン> npx playwright test --project=anon
import { defineShots, settle } from '../../lib/shot'

const token = process.env.QULOUD_SHOTS_SIGNUP_TOKEN

defineShots([
  {
    name: 'invitation_signup_form',
    chapter: 'invitation',
    feature: '招待された新規ユーザーの登録画面',
    state: '初期表示',
    expectUrl: /\/sign_up/,
    skipIf: () => !token && 'QULOUD_SHOTS_SIGNUP_TOKEN が未設定（招待メールのトークンが要る）',
    prepare: async (page) => {
      await page.goto(`/sign_up?token=${token}`)
      await settle(page)
    },
  },
])
