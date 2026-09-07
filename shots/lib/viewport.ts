/**
 * 掲載画像のビューポート。
 *
 * source/introduction.rst の「動作環境」に「ウィンドウ幅 1440 px」と明記して
 * いるので、ここを変えるなら章も直す。lib/shot.ts が撮影ごとに実際の
 * ビューポートと突き合わせて、食い違ったら撮影を失敗させる。
 *
 * playwright.config.ts の projects[].use に devices['Desktop Chrome'] を
 * 展開すると、その中の viewport (1280x720) が全体の use.viewport を
 * 上書きする。実際にそれで 9 枚とも 1280x720 で撮れていた。
 * 展開の**後ろ**に viewport を置くこと。
 */
export const SHOT_VIEWPORT = { width: 1440, height: 900 } as const
