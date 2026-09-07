"""RST の整形だけを担うモジュール。マスタデータの意味は知らない。"""
from __future__ import annotations

import re
import unicodedata

_INLINE_MARKUP = re.compile(r"([*`|_\\])")


def escape(text) -> str:
    """表のセルに入れる文字列を RST として安全にする。

    None と空文字は "-" にする。改行はセルを壊すので空白にする。
    """
    if text is None:
        return "-"
    s = str(text)
    if s == "":
        return "-"
    s = s.replace("\r\n", "\n").replace("\n", " ")
    return _INLINE_MARKUP.sub(r"\\\1", s)


def display_width(text: str) -> int:
    """見出し下線の長さ用に、全角を2幅として数える。"""
    return sum(2 if unicodedata.east_asian_width(c) in ("F", "W", "A") else 1 for c in text)


def section(title: str, char: str) -> str:
    """見出しを作る。下線は表示幅に合わせる（短いと Sphinx が警告を出す）。"""
    return f"{title}\n{char * display_width(title)}\n"


def list_table(headers: list[str], rows: list[list[str]], widths: list[int] | None = None) -> str:
    """list-table を作る。

    grid table はセル幅の計算が要るうえ日本語で崩れるので使わない。
    行が無いときは空文字を返す（空の list-table は Sphinx がエラーにする）。
    """
    if not rows:
        return ""
    lines = [".. list-table::", "   :header-rows: 1"]
    if widths:
        lines.append("   :widths: " + " ".join(str(w) for w in widths))
    lines.append("")
    for row in [headers, *rows]:
        for i, cell in enumerate(row):
            prefix = "   * - " if i == 0 else "     - "
            lines.append(prefix + (cell if cell else "-"))
    lines.append("")
    return "\n".join(lines)


def header_comment(dump: dict, script: str) -> str:
    """生成ファイルの先頭に置くコメント。何から作られたかを必ず残す。

    generated_at（dump 実行時刻）と master_synced_at（アプリのマスタが
    最後に DB へ書き込まれた時刻）は別物で、master YAML を編集しただけで
    同期を回していない場合はズレる。両方を残す。
    """
    commit = dump.get("source_commit") or "(不明)"
    branch = dump.get("source_branch") or "(不明)"
    generated = dump.get("generated_at") or "(不明)"
    synced = dump.get("master_synced_at") or "(不明)"
    return "\n".join([
        f".. これは {script} が生成したファイルです。手で編集しないでください。",
        f".. 生成元コミット: {commit} ({branch})",
        f".. マスタ取得日時（dump 実行）: {generated}",
        f".. マスタ同期日時: {synced}",
        ".. 再生成: make dump && make generate",
        "",
        "",
    ])
