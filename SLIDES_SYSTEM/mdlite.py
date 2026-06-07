#!/usr/bin/env python3
"""mdlite — a tiny, deterministic Markdown-subset -> HTML converter (stdlib only).

This is the text-shaping engine behind ``md2deck.py``. It is intentionally small
and readable so you can extend it *locally* — the project ships no Node/npm and
no runtime dependencies, so we own this instead of pulling a Markdown library.
It is NOT a full CommonMark implementation; it covers the subset that makes good
slides:

  Block : # ATX headings, paragraphs, ``- * +`` and ``1.`` lists (nested by
          indent), ``>`` blockquotes, ```` ``` ```` fenced code, GFM ``|`` pipe
          tables, images on their own line, ``***`` / ``___`` thematic breaks,
          and raw-HTML passthrough (a presenter power-tool).
  Inline: ``**bold**`` ``__bold__``, ``*italic*`` ``_italic_``, `` `code` ``,
          ``~~strike~~``, ``[text](url)``, ``![alt](src)``, ``<autolinks>`` and
          two-space hard breaks.

NOTE: ``---`` is NOT handled here — ``md2deck.py`` splits the deck into slides on
it *before* calling :func:`render`, so a lone ``---`` never reaches this module.

Deterministic: the same input always yields the same output (no time/random/dict
ordering leaks into the HTML).

  As a module:  ``from mdlite import render;  html = render(markdown_text)``
  As a CLI    :  ``python3 mdlite.py < input.md > out.html``   (handy for testing)
"""
import re
import sys

__all__ = ["render"]

# ---------------------------------------------------------------------------
# inline
# ---------------------------------------------------------------------------

def _esc(s):
    """Escape the three HTML text specials (used on plain-text runs)."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _attr(s):
    """Escape a value destined for a double-quoted HTML attribute."""
    return _esc(s).replace('"', "&quot;")


_CODE = re.compile(r"(`+)(.+?)\1", re.S)
_IMG = re.compile(r"!\[([^\]]*)\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+\"([^\"]*)\")?\s*\)")
_LINK = re.compile(r"\[([^\]]+)\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+\"([^\"]*)\")?\s*\)")
_AUTO = re.compile(r"<((?:https?|mailto):[^>\s]+)>")


def _clean_url(u):
    u = u.strip()
    if u.startswith("<") and u.endswith(">"):
        u = u[1:-1]
    return u


def _inline(text):
    """Render inline Markdown in ``text`` to an HTML fragment."""
    store = []

    def stash(html):
        store.append(html)
        return "\x00%d\x00" % (len(store) - 1)

    # 1. code spans — protected verbatim (escaped, never re-processed)
    text = _CODE.sub(lambda m: stash("<code>%s</code>" % _esc(m.group(2).strip())), text)

    # 2. images
    def img_sub(m):
        alt, url, title = m.group(1), _clean_url(m.group(2)), m.group(3)
        t = ' title="%s"' % _attr(title) if title else ""
        return stash('<img src="%s" alt="%s"%s>' % (_attr(url), _attr(alt), t))
    text = _IMG.sub(img_sub, text)

    # 3. links — the label may itself contain inline markup, so recurse
    def link_sub(m):
        label, url, title = m.group(1), _clean_url(m.group(2)), m.group(3)
        t = ' title="%s"' % _attr(title) if title else ""
        return stash('<a href="%s"%s>%s</a>' % (_attr(url), t, _inline(label)))
    text = _LINK.sub(link_sub, text)

    # 4. autolinks <https://…> / <mailto:…>
    text = _AUTO.sub(lambda m: stash('<a href="%s">%s</a>' % (_attr(m.group(1)), _esc(m.group(1)))), text)

    # 5. escape the remaining plain text, then apply emphasis to the safe text
    text = _esc(text)
    text = re.sub(r"\*\*(\S(?:.*?\S)?)\*\*", r"<strong>\1</strong>", text, flags=re.S)
    text = re.sub(r"__(\S(?:.*?\S)?)__", r"<strong>\1</strong>", text, flags=re.S)
    text = re.sub(r"(?<!\*)\*(\S(?:.*?\S)?)\*(?!\*)", r"<em>\1</em>", text, flags=re.S)
    text = re.sub(r"(?<!\w)_(\S(?:.*?\S)?)_(?!\w)", r"<em>\1</em>", text, flags=re.S)
    text = re.sub(r"~~(\S(?:.*?\S)?)~~", r"<del>\1</del>", text, flags=re.S)

    # 6. hard line break: two or more spaces before a newline
    text = re.sub(r" {2,}\n", "<br>\n", text)

    # 7. restore the protected spans
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], text)


# ---------------------------------------------------------------------------
# blocks
# ---------------------------------------------------------------------------

_FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([\w+-]*)\s*$")
_HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_HR = re.compile(r"^\s*(?:\*\s*){3,}$|^\s*(?:_\s*){3,}$")
_ULI = re.compile(r"^(\s*)([-*+])\s+(.*)$")
_OLI = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
_LI = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+")


def _is_table_sep(line):
    """True if ``line`` is a GFM table delimiter row, e.g. ``| --- | :--: |``."""
    return "-" in line and bool(
        re.match(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$", line))


def _split_row(row):
    """Split one pipe-table row into trimmed cells (ignoring outer pipes)."""
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [c.strip() for c in re.split(r"\s*(?<!\\)\|\s*", row)]


def _aligns(sep):
    out = []
    for c in _split_row(sep):
        l, r = c.startswith(":"), c.endswith(":")
        out.append("center" if l and r else "right" if r else "left" if l else "")
    return out


def _al(aligns, k):
    a = aligns[k] if k < len(aligns) else ""
    return ' style="text-align:%s"' % a if a else ""


def _table(header, aligns, rows):
    head = "".join("<th%s>%s</th>" % (_al(aligns, k), _inline(c))
                   for k, c in enumerate(_split_row(header)))
    body = []
    for r in rows:
        cells = "".join("<td%s>%s</td>" % (_al(aligns, k), _inline(c))
                        for k, c in enumerate(_split_row(r)))
        body.append("<tr>%s</tr>" % cells)
    return ("<table>\n<thead><tr>%s</tr></thead>\n<tbody>\n%s\n</tbody>\n</table>"
            % (head, "\n".join(body)))


def _list(block):
    """Render a collected, blank-free list block into nested ``<ul>``/``<ol>``."""
    base = len(_LI.match(block[0]).group(1))
    tag = "ol" if _OLI.match(block[0]) else "ul"
    out, i = ["<%s>" % tag], 0
    while i < len(block):
        m = _OLI.match(block[i]) or _ULI.match(block[i])
        content = m.group(3)
        i += 1
        children = []
        # everything until the next sibling marker (indent <= base) is this item's
        while i < len(block) and not (_LI.match(block[i])
                                      and len(_LI.match(block[i]).group(1)) <= base):
            children.append(block[i])
            i += 1
        inner = _inline(content)
        if children:
            dedent = min(len(re.match(r"^(\s*)", c).group(1)) for c in children if c.strip())
            inner += "\n" + render("\n".join(c[dedent:] for c in children))
        out.append("<li>%s</li>" % inner)
    out.append("</%s>" % tag)
    return "\n".join(out)


def _starts_block(line, nxt):
    """True if ``line`` begins a new block (so a paragraph must stop before it)."""
    s = line.lstrip()
    return bool(_FENCE.match(line) or _HEAD.match(line) or _HR.match(line)
                or s.startswith(">") or _LI.match(line) or s.startswith("<")
                or ("|" in line and _is_table_sep(nxt)))


def render(text):
    """Convert a block of Markdown (one slide's body) to an HTML fragment."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        m = _FENCE.match(line)
        if m:                                           # fenced code block
            close = re.compile(r"^\s*" + re.escape(m.group(2)[0]) + r"{3,}\s*$")
            lang, buf = m.group(3), []
            i += 1
            while i < n and not close.match(lines[i]):
                buf.append(lines[i])
                i += 1
            i += 1                                      # consume the closing fence
            cls = ' class="language-%s"' % _attr(lang) if lang else ""
            out.append("<pre><code%s>%s</code></pre>" % (cls, _esc("\n".join(buf))))
            continue

        m = _HEAD.match(line)
        if m:                                           # ATX heading
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, _inline(m.group(2)), lvl))
            i += 1
            continue

        if _HR.match(line):                             # thematic break
            out.append("<hr>")
            i += 1
            continue

        if line.lstrip().startswith(">"):               # blockquote (recursive)
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>\n%s\n</blockquote>" % render("\n".join(buf)))
            continue

        if "|" in line and i + 1 < n and _is_table_sep(lines[i + 1]):   # GFM table
            header, aligns = line, _aligns(lines[i + 1])
            i += 2
            rows = []
            while i < n and lines[i].strip() and "|" in lines[i]:
                rows.append(lines[i])
                i += 1
            out.append(_table(header, aligns, rows))
            continue

        if _LI.match(line):                             # list (collected, then nested)
            buf = []
            while i < n and lines[i].strip() and (_LI.match(lines[i])
                                                  or lines[i].startswith((" ", "\t"))):
                buf.append(lines[i])
                i += 1
            out.append(_list(buf))
            continue

        if line.lstrip().startswith("<"):               # raw-HTML passthrough
            buf = []
            while i < n and lines[i].strip():
                buf.append(lines[i])
                i += 1
            out.append("\n".join(buf))
            continue

        buf = []                                        # paragraph
        while i < n and lines[i].strip() and not _starts_block(
                lines[i], lines[i + 1] if i + 1 < n else ""):
            buf.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % _inline("\n".join(buf)))
    return "\n".join(out)


if __name__ == "__main__":
    sys.stdout.write(render(sys.stdin.read()))
