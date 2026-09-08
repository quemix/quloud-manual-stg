/**
 * 撮影前に画面から識別情報を消す。
 *
 * ローカル開発 DB のシードデータには実在の社名・氏名・メールアドレスが入っている
 * （設計書 §10 が「画面キャプチャに含めてはいけないもの」として挙げているもの）。
 * DB を書き換えるのは他人の作業環境を壊すので、撮影直前に DOM のテキストを
 * 差し替える方式を採る。
 *
 * 置換表は非公開リポジトリ側（meta/shots_redactions.json）にある。
 * 表が無い・読めない場合は撮影を止める。素の画面を撮って公開物に混ぜるより、
 * 何も撮らないほうが安全。
 */
import fs from 'node:fs'
import path from 'node:path'
import type { Page } from '@playwright/test'

export type RedactionRules = {
  /** 部分一致で置換する。キーが長いものから適用する。 */
  replace: Record<string, string>
  /** テキストノード全体が一致したときだけ置換する。 */
  replaceExact: Record<string, string>
}

const RULES_PATH = path.resolve(__dirname, '..', '..', 'meta', 'shots_redactions.json')

export function loadRules(): RedactionRules {
  if (!fs.existsSync(RULES_PATH)) {
    throw new Error(
      `置換表が無いので撮影を中止する: ${RULES_PATH}\n` +
      '非公開リポジトリ quemix/quloud-manual-meta を meta/ にクローンしてください。'
    )
  }
  const raw = JSON.parse(fs.readFileSync(RULES_PATH, 'utf-8'))
  const replace = raw.replace ?? {}
  const replaceExact = raw.replaceExact ?? {}
  if (Object.keys(replace).length === 0 && Object.keys(replaceExact).length === 0) {
    throw new Error(`置換表が空なので撮影を中止する: ${RULES_PATH}`)
  }
  return { replace, replaceExact }
}

/** ページ内のテキストと、テキストとして見える属性を置換する。 */
export async function redactPage(page: Page, rules: RedactionRules): Promise<void> {
  // 開いているダイアログやメニューは body 直下の別要素として描かれる（Vuetify の
  // overlay）。document 全体を対象にするので、ここで区別する必要はない。
  await page.evaluate((r: RedactionRules) => {
    // 長いキーから適用する。テナント名はメールアドレスのドメインにも現れる
    // ので、短いキーを先に当てるとアドレスが壊れた形で残る。
    const pairs = Object.entries(r.replace).sort((a, b) => b[0].length - a[0].length)
    const exact = Object.entries(r.replaceExact)

    const applyAll = (s: string): string => {
      let out = s
      for (const [from, to] of pairs) out = out.split(from).join(to)
      return out
    }

    const walker = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_TEXT)
    const texts: Text[] = []
    for (let n = walker.nextNode(); n; n = walker.nextNode()) texts.push(n as Text)
    for (const node of texts) {
      const parent = node.parentElement?.tagName
      if (parent === 'SCRIPT' || parent === 'STYLE') continue
      const original = node.nodeValue ?? ''
      let next = applyAll(original)
      if (next === original) {
        // 部分一致で何も変わらなかったものだけ、全体一致の規則にかける。
        const trimmed = original.trim()
        const hit = exact.find(([from]) => from === trimmed)
        if (hit) next = original.replace(trimmed, hit[1])
      }
      if (next !== original) node.nodeValue = next
    }

    // 入力欄の値と、ツールチップ・代替テキストとして見える属性。
    //
    // 読み取り専用の v-text-field は値を input の value に持つ（プロフィール画面が
    // そう）。テキストノードと同じく、部分一致で変わらなかったものには
    // 全体一致の規則も当てる。ここを抜かすと、名（1 文字）のような
    // replaceExact だけで消せる値が素のまま残る。
    const applyOne = (s: string): string => {
      const next = applyAll(s)
      if (next !== s) return next
      const trimmed = s.trim()
      const hit = exact.find(([from]) => from === trimmed)
      return hit ? s.replace(trimmed, hit[1]) : s
    }
    for (const el of Array.from(document.querySelectorAll('input, textarea'))) {
      const f = el as HTMLInputElement | HTMLTextAreaElement
      if (f.value) f.value = applyOne(f.value)
    }
    for (const attr of ['placeholder', 'title', 'alt', 'aria-label', 'value']) {
      for (const el of Array.from(document.querySelectorAll(`[${attr}]`))) {
        const v = el.getAttribute(attr)
        if (!v) continue
        const next = applyOne(v)
        if (next !== v) el.setAttribute(attr, next)
      }
    }
  }, rules)
}

/**
 * 置換漏れを検査する。1 つでも残っていれば例外を投げ、撮影を失敗させる。
 *
 * replaceExact のキーは本文の一部として正当に現れうる（アバターの頭文字など）ので、
 * 「テキストノード全体が一致するものが残っていないか」だけを見る。
 */
export async function assertRedacted(page: Page, rules: RedactionRules): Promise<void> {
  const leaks = await page.evaluate((r: RedactionRules) => {
    const found: string[] = []

    const all = document.documentElement.innerText ?? ''
    const attrs: string[] = []
    for (const attr of ['placeholder', 'title', 'alt', 'aria-label', 'value']) {
      for (const el of Array.from(document.querySelectorAll(`[${attr}]`))) {
        const v = el.getAttribute(attr)
        if (v) attrs.push(v)
      }
    }
    for (const el of Array.from(document.querySelectorAll('input, textarea'))) {
      const f = el as HTMLInputElement | HTMLTextAreaElement
      if (f.value) attrs.push(f.value)
    }
    const haystack = [all, ...attrs].join('\n')

    for (const from of Object.keys(r.replace)) {
      if (haystack.includes(from)) found.push(`replace: ${from}`)
    }

    const walker = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_TEXT)
    const remaining = new Set<string>()
    for (let n = walker.nextNode(); n; n = walker.nextNode()) {
      const t = (n.nodeValue ?? '').trim()
      if (t) remaining.add(t)
    }
    for (const from of Object.keys(r.replaceExact)) {
      if (remaining.has(from)) found.push(`replaceExact: ${from}`)
    }
    return found
  }, rules)

  if (leaks.length > 0) {
    throw new Error(
      '置換漏れがあるので撮影を中止した。meta/shots_redactions.json に規則を足すこと:\n  ' +
      leaks.join('\n  ')
    )
  }
}
