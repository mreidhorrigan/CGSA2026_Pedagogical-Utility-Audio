#!/usr/bin/env python3
"""md2deck — turn a Markdown/text file into ONE self-contained slideshow .html.

Each compiled deck becomes a single file dropped into ``../slides/`` — i.e. one
kiosk in the game that the visitor opens and arrows through in place (◀ ▶). The
output is fully self-contained (theme CSS + navigator JS inlined), so it works
over ``file://`` and even opens standalone in a browser. No Node, no pip, no
runtime dependencies: stdlib Python + the local ``mdlite.py`` engine.

It is deliberately compatible with the de-facto Markdown-slides conventions
(Marp / Marpit): ``---`` separates slides, the first ``---…---`` block is YAML
front-matter, and ``<!-- directive -->`` / ``<!-- _spot -->`` HTML comments set
per-slide options. See README.md / RESEARCH.md in this folder.

    python3 md2deck.py examples/my-talk.md            # -> ../slides/my-talk.html (+ rebuild slides.js)
    python3 md2deck.py talk.md --theme light          # pick a theme
    python3 md2deck.py decks/                          # compile every .md/.txt in a folder
    python3 md2deck.py talk.md --stdout                # print HTML, don't write (testing)
    python3 md2deck.py talk.md --no-build              # write file, skip the slides.js rebuild

Front-matter keys honoured: title, theme, class, headingDivider, paginate
(accepted). Per-slide directives: class / _class (lead | center | invert | …).
Slide background image: a line that is just ``![bg](path-or-url)``.
"""
import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mdlite  # noqa: E402  (local engine, same folder)

ROOT = os.path.dirname(HERE)                       # the Presentation project root
THEME_DIR = os.path.join(HERE, "themes")
TEMPLATE = os.path.join(HERE, "template", "deck.html")
RUNTIME = os.path.join(HERE, "template", "runtime.js")
DEFAULT_INPUT = os.path.join(HERE, "examples")
DEFAULT_SLIDES = os.path.join(ROOT, "slides")
BUILD_SLIDES = os.path.join(ROOT, "build_slides.py")
DEFAULT_THEME = "isometric"
TEXT_EXTS = (".md", ".markdown", ".mkd", ".mdown", ".txt")


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def natural_key(name):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", name)]


# --- front-matter (a tiny YAML-subset: flat key: value pairs) ---------------

def parse_front_matter(text):
    """Split a leading ``---\\n … \\n---`` block into (dict, body)."""
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return {}, text
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return _parse_kv("\n".join(lines[1:i])), "\n".join(lines[i + 1:])
    return {}, text                                # no closing fence -> not front-matter


def _parse_kv(block):
    fm = {}
    for line in block.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", s)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        elif val.lower() in ("true", "false"):
            val = val.lower() == "true"
        elif re.match(r"^-?\d+$", val):
            val = int(val)
        fm[key] = val
    return fm


# --- slide splitting --------------------------------------------------------

def _heading_divider(body, level):
    """Insert a ``---`` break before every heading of level <= ``level`` (Marp
    ``headingDivider``), skipping inside fenced code and before the first one."""
    out, fence, seen = [], None, False
    for line in body.split("\n"):
        fm = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fm:
            tok = fm.group(1)[0]
            fence = None if fence == tok else (fence or tok)
        is_head = fence is None and re.match(r"^#{1,%d}\s+" % level, line)
        if is_head and seen:
            out.append("---")
        if line.strip():
            seen = True
        out.append(line)
    return "\n".join(out)


def split_slides(body):
    """Split on lines of three-or-more dashes, ignoring dashes inside code fences."""
    slides, cur, fence = [], [], None
    for line in body.split("\n"):
        fm = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fm:
            tok = fm.group(1)[0]
            fence = None if fence == tok else (fence or tok)
            cur.append(line)
            continue
        if fence is None and re.match(r"^-{3,}\s*$", line):
            slides.append("\n".join(cur))
            cur = []
        else:
            cur.append(line)
    slides.append("\n".join(cur))
    return [s for s in (x.strip("\n") for x in slides) if s.strip()]


# --- per-slide processing ---------------------------------------------------

def extract_comments(md):
    """Pull ``<!-- key: val -->`` directives out of a slide and strip ALL HTML
    comments (directives + presenter notes) from what gets rendered."""
    directives = {}

    def repl(m):
        for line in m.group(1).split("\n"):
            mm = re.match(r"^\s*(_?[A-Za-z][\w-]*)\s*:\s*(.*?)\s*$", line)
            if mm:
                directives[mm.group(1)] = mm.group(2)
        return ""

    return directives, re.sub(r"<!--(.*?)-->", repl, md, flags=re.S)


def extract_bg(md):
    """Find a lone ``![bg](url)`` line; return (url-or-None, body-without-it)."""
    bg, kept = None, []
    for line in md.split("\n"):
        m = re.match(r"^\s*!\[bg[^\]]*\]\(\s*(<[^>]*>|\S+?)\s*\)\s*$", line)
        if m and bg is None:
            url = m.group(1)
            bg = url[1:-1] if url.startswith("<") and url.endswith(">") else url
        else:
            kept.append(line)
    return bg, "\n".join(kept)


def slide_classes(directives, deck_class, body_md):
    """Resolve the CSS classes for a slide (deck-wide + per-slide + auto-lead)."""
    classes = list(deck_class.split()) if deck_class else []
    for key in ("class", "_class"):
        if directives.get(key):
            classes += str(directives[key]).split()
    nonblank = [l for l in body_md.split("\n") if l.strip()]
    if nonblank and all(re.match(r"^#{1,6}\s+", l.strip()) for l in nonblank):
        if "lead" not in classes and "center" not in classes:
            classes.append("lead")                 # a title-only slide centres itself
    return list(dict.fromkeys(classes))            # de-dupe, preserve order


def first_title(slides):
    for s in slides:
        for line in s.split("\n"):
            m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line.strip())
            if m:
                return re.sub(r"[*_`~]", "", m.group(1)).strip()
    return None


def load_theme(name):
    path = os.path.join(THEME_DIR, name + ".css")
    if not os.path.isfile(path):
        avail = sorted(f[:-4] for f in os.listdir(THEME_DIR)
                       if f.endswith(".css") and not f.startswith("_"))
        raise SystemExit("md2deck: unknown theme '%s'. Available: %s" % (name, ", ".join(avail)))
    return read(path) + "\n" + read(os.path.join(THEME_DIR, "_base.css"))


# --- standalone launcher ----------------------------------------------------

INDEX_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="generator" content="md2deck index (SLIDES_SYSTEM)">
<title>Presentations</title>
<style>
  :root{ --bg:#0b1322; --fg:#e8eef5; --muted:#9fb0c6; --accent:#4ecdc4; --line:rgba(255,255,255,.12); }
  *{box-sizing:border-box} a{color:var(--accent)}
  body{margin:0;min-height:100vh;color:var(--fg);padding:6vh 6vw;
    background:radial-gradient(125% 125% at 50% 0%,#17243d,#0b1322 70%);
    font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;}
  header,main,footer{max-width:980px;margin-left:auto;margin-right:auto;}
  h1{font-size:clamp(28px,5vw,46px);margin:0 0 .2em;font-weight:800;}
  h1 .dot{color:var(--accent);}
  .sub{color:var(--muted);font-size:clamp(14px,2vw,18px);margin:0 0 4vh;}
  .grid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));}
  .card{display:flex;flex-direction:column;gap:.3em;text-decoration:none;color:inherit;
    background:linear-gradient(165deg,#1c2a45,#121e35);border:1px solid var(--line);border-radius:14px;
    padding:20px 20px 16px;transition:transform .15s,border-color .15s,box-shadow .15s;}
  .card:hover{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 12px 32px rgba(0,0,0,.45);}
  .card .t{font-size:20px;font-weight:800;line-height:1.2;}
  .card .m{color:var(--muted);font-size:13px;}
  .card .go{margin-top:.55em;color:var(--accent);font-weight:700;font-size:14px;}
  .empty{color:var(--muted);}
  code{background:#0d1424;border:1px solid var(--line);padding:2px 6px;border-radius:6px;}
  footer{margin-top:5vh;color:var(--muted);font-size:13px;}
</style>
</head>
<body>
<header>
  <h1>Presentations<span class="dot">.</span></h1>
  <p class="sub">{{COUNT}} standalone deck(s) — open any one to present it on its own
     (← → to move, <b>F</b> for fullscreen), or walk them as kiosks in
     <a href="../index.html">the game</a>.</p>
</header>
<main class="grid">
{{CARDS}}
</main>
<footer>Auto-generated by <code>md2deck.py</code>. Regenerate:
  <code>python3 SLIDES_SYSTEM/md2deck.py &lt;deck&gt;.md</code></footer>
</body>
</html>
"""


def _index_html(decks):
    if decks:
        cards = "\n".join(
            '  <a class="card" href="%s"><span class="t">%s</span>'
            '<span class="m">%d slide%s</span><span class="go">Open &#9656;</span></a>'
            % (mdlite._attr(href), mdlite._esc(title), n, "" if n == 1 else "s")
            for href, title, n in decks)
    else:
        cards = '  <p class="empty">No decks yet — run <code>md2deck.py yourfile.md</code>.</p>'
    return INDEX_TEMPLATE.replace("{{COUNT}}", str(len(decks))).replace("{{CARDS}}", cards)


def write_index(slides_dir, out_path):
    """(Re)generate the standalone launcher listing every md2deck-generated deck
    found in ``slides_dir``. Returns the list of (href, title, slide_count)."""
    decks, out_dir = [], os.path.dirname(os.path.abspath(out_path))
    if os.path.isdir(slides_dir):
        for name in sorted(os.listdir(slides_dir), key=natural_key):
            if name.startswith(".") or not name.lower().endswith((".html", ".htm")):
                continue
            try:
                html = read(os.path.join(slides_dir, name))
            except OSError:
                continue
            if 'content="md2deck (SLIDES_SYSTEM)"' not in html:
                continue                                   # only our decks, not arbitrary html slides
            m = re.search(r"<title>(.*?)</title>", html, re.S)
            title = (m.group(1).strip() if m else "") or os.path.splitext(name)[0]
            href = os.path.relpath(os.path.join(slides_dir, name), out_dir).replace("\\", "/")
            decks.append((href, title, html.count('<section class="slide')))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(_index_html(decks))
    return decks


# --- compile ----------------------------------------------------------------

def compile_deck(text, theme_override=None):
    """Compile deck source text -> (html_string, resolved_theme_name)."""
    fm, body = parse_front_matter(text)
    theme = theme_override or fm.get("theme") or DEFAULT_THEME
    if fm.get("headingDivider"):
        body = _heading_divider(body, int(fm["headingDivider"]))
    deck_class = fm.get("class") if isinstance(fm.get("class"), str) else None

    raw_slides = split_slides(body) or [""]
    sections = []
    for sl in raw_slides:
        directives, sl = extract_comments(sl)
        bg, sl = extract_bg(sl)
        classes = slide_classes(directives, deck_class, sl)
        if bg:
            classes.append("has-bg")
        cls = (" " + " ".join(classes)) if classes else ""
        style = ' style="background-image:url(&quot;%s&quot;)"' % mdlite._attr(bg) if bg else ""
        sections.append('<section class="slide%s"%s>\n%s\n</section>'
                        % (cls, style, mdlite.render(sl.strip("\n"))))

    title = fm.get("title") or first_title(raw_slides) or "Slides"
    out = read(TEMPLATE)
    out = out.replace("{{TITLE}}", mdlite._attr(str(title)))
    out = out.replace("{{THEME_CSS}}", load_theme(theme))
    out = out.replace("{{RUNTIME_JS}}", read(RUNTIME))
    out = out.replace("{{ROLE_META}}",
                      '<meta name="md2deck-role" content="placeholder">\n' if fm.get("placeholder") else "")
    out = out.replace("{{SECTIONS}}", "\n".join(sections))   # last: user content not re-scanned
    return out, theme


# --- CLI --------------------------------------------------------------------

def gather_inputs(paths):
    """Expand the positional args into an ordered list of source files."""
    files = []
    for p in paths:
        if os.path.isdir(p):
            files += [os.path.join(p, n) for n in sorted(os.listdir(p), key=natural_key)
                      if n.lower().endswith(TEXT_EXTS) and not n.startswith(".")
                      and n.lower() != "readme.md"]
        elif os.path.isfile(p):
            files.append(p)
        else:
            raise SystemExit("md2deck: no such file or folder: %s" % p)
    return files


def main(argv=None):
    ap = argparse.ArgumentParser(description="Compile Markdown/text into self-contained slideshow kiosks.")
    ap.add_argument("inputs", nargs="*", help="deck .md/.txt files or folders (default: examples/)")
    ap.add_argument("--theme", help="theme name in themes/ (default: front-matter or '%s')" % DEFAULT_THEME)
    ap.add_argument("--slides-dir", default=DEFAULT_SLIDES, help="where to write decks (default: ../slides)")
    ap.add_argument("--out", help="explicit output path (only valid with a single input)")
    ap.add_argument("--no-build", action="store_true", help="skip rebuilding ../slides.js afterwards")
    ap.add_argument("--index-out", default=os.path.join(HERE, "presentations.html"),
                    help="standalone launcher listing all decks (default: SLIDES_SYSTEM/presentations.html)")
    ap.add_argument("--no-index", action="store_true", help="don't (re)generate the standalone launcher page")
    ap.add_argument("--stdout", action="store_true", help="print compiled HTML instead of writing a file")
    args = ap.parse_args(argv)

    inputs = gather_inputs(args.inputs or [DEFAULT_INPUT])
    if not inputs:
        raise SystemExit("md2deck: nothing to compile (no .md/.txt found).")
    if args.out and len(inputs) != 1:
        raise SystemExit("md2deck: --out only works with a single input file.")

    if args.stdout:
        html, _ = compile_deck(read(inputs[0]), args.theme)
        sys.stdout.write(html)
        return 0

    os.makedirs(args.slides_dir, exist_ok=True)
    written = []
    for src in inputs:
        html, theme = compile_deck(read(src), args.theme)
        stem = os.path.splitext(os.path.basename(src))[0]
        dst = args.out or os.path.join(args.slides_dir, stem + ".html")
        with open(dst, "w", encoding="utf-8") as f:
            f.write(html)
        n = html.count('<section class="slide')
        written.append((src, dst, theme, n))
        print("  %-32s -> %s  [theme: %s, %d slide(s)]"
              % (os.path.basename(src), os.path.relpath(dst, ROOT), theme, n))

    if not args.no_index:
        si, ii = os.path.abspath(args.slides_dir), os.path.abspath(args.index_out)
        if ii == si or ii.startswith(si + os.sep):
            # The launcher is plain .html; inside slides/ it would be scanned as a
            # kiosk. Refuse, so the "launcher is never a kiosk" invariant holds.
            print("Warning: --index-out is inside --slides-dir; skipping the launcher "
                  "so it isn't picked up as a kiosk. Pick a path outside %s." % args.slides_dir)
        else:
            decks = write_index(args.slides_dir, args.index_out)
            print("Launcher: %s  (%d deck(s) — open it to present any deck standalone)"
                  % (os.path.relpath(args.index_out, ROOT), len(decks)))

    if args.no_build:
        print("Skipped slides.js rebuild (--no-build). Run: python3 build_slides.py")
        return 0

    print("Rebuilding slides.js ...")
    # Run build_slides.py exactly as a human would — from the project root with a
    # RELATIVE slides dir — so the manifest's src stays relative (e.g.
    # "slides/my-talk.html"), which is what the game loads over file:// and http.
    r = subprocess.run([sys.executable, BUILD_SLIDES,
                        "--slides-dir", os.path.relpath(args.slides_dir, ROOT),
                        "--out", "slides.js"], cwd=ROOT)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
