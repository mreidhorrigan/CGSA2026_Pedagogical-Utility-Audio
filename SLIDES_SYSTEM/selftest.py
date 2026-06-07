#!/usr/bin/env python3
"""selftest — smoke-test the whole text->slides->manifest pipeline.

Connects the built-in placeholder slides (``examples/placeholder.md``, which
mirrors ``PLACEHOLDER_SLIDES`` in ``game.js``) to the *real* build (``mdlite`` +
``md2deck`` + ``build_slides``) so you can verify the system end-to-end with one
command and no browser:

    python3 SLIDES_SYSTEM/selftest.py

Everything is built into a throwaway temp dir — the real ``slides/`` and
``slides.js`` are never touched, and nothing is left behind. Exit code 0 = all
checks passed, 1 = at least one failed. Deterministic; stdlib only.
"""
import contextlib
import io
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)   # build_slides.py
sys.path.insert(0, HERE)   # md2deck.py, mdlite.py
import md2deck              # noqa: E402
import mdlite              # noqa: E402
import build_slides        # noqa: E402

PLACEHOLDER = os.path.join(HERE, "examples", "placeholder.md")
MY_TALK = os.path.join(HERE, "examples", "my-talk.md")

_results = []


def check(name, ok, detail=""):
    _results.append(ok)
    line = ("  \033[32mPASS\033[0m " if ok else "  \033[31mFAIL\033[0m ") + name
    if detail and not ok:
        line += "  — " + detail
    print(line)


def main():
    print("selftest: building the placeholder deck through the real pipeline\n")
    src = md2deck.read(PLACEHOLDER)

    # --- compiler + engine (pure functions, no files) -----------------------
    html, theme = md2deck.compile_deck(src)
    n = html.count('<section class="slide')
    check("placeholder deck compiles to 5 slides", n == 5, "got %d" % n)
    check("resolved theme is isometric (front-matter)", theme == "isometric", theme)

    html2, _ = md2deck.compile_deck(src)
    check("compile is deterministic", html == html2)

    check("theme CSS + navigator JS are inlined", ":root" in html and "window.self" in html)
    ext = re.findall(r'(?:src|href)="(https?://[^"]+)"', html)
    check("deck has no external asset refs (self-contained)", not ext, ", ".join(ext))

    check("title slide uses the lead layout", '<section class="slide lead"' in html)
    check("center directive applied", '<section class="slide center"' in html)
    check("speaker-note comment was stripped", "mirrors PLACEHOLDER_SLIDES" not in html)
    check("deck is standalone-ready (fullscreen + context detection)",
          "toggleFullscreen" in html and "window.self !== window.top" in html)
    check("placeholder deck carries the role marker (so the build can replace it)",
          'name="md2deck-role" content="placeholder"' in html)

    for t in ("isometric", "light"):
        h, _ = md2deck.compile_deck(src, theme_override=t)
        check("theme '%s' compiles" % t, '<section class="slide' in h and ":root" in h)

    md = mdlite.render("# H\n\n- a\n- b\n\n`code` and **bold** and a | b\n|:--|--:|\n| 1 | 2 |")
    check("mdlite renders headings/lists/inline",
          "<h1>H</h1>" in md and "<li>a</li>" in md
          and "<strong>bold</strong>" in md and "<code>code</code>" in md)

    # --- the build (md2deck -> files -> build_slides manifest) --------------
    # Mirror the real layout: the launcher lives OUTSIDE the slides dir, so it is
    # never scanned as a kiosk (md2deck enforces this too).
    tmp = tempfile.mkdtemp(prefix="slides_selftest_")
    tmp_idx = tempfile.mkdtemp(prefix="launcher_selftest_")
    try:
        idx = os.path.join(tmp_idx, "presentations.html")
        with contextlib.redirect_stdout(io.StringIO()):       # hush md2deck's own logging
            md2deck.main([PLACEHOLDER, "--slides-dir", tmp, "--index-out", idx, "--no-build"])

        deck = os.path.join(tmp, "placeholder.html")
        check("md2deck wrote the deck file", os.path.isfile(deck))
        check("launcher lists the deck", os.path.isfile(idx)
              and "placeholder.html" in md2deck.read(idx))

        manifest = build_slides.build_manifest(tmp)             # <- the actual build
        ok = len(manifest) == 1 and manifest[0].get("type") == "html"
        check("build_slides yields 1 html slide", ok, repr(manifest))
        src_field = manifest[0].get("src", "") if manifest else ""
        check("manifest src points at the deck", src_field.endswith("placeholder.html"), src_field)
        check("manifest title derived from filename",
              bool(manifest) and manifest[0].get("title") == "Placeholder",
              manifest[0].get("title") if manifest else "")

        js_path = os.path.join(tmp, "slides.js")
        build_slides.write_slides_js(manifest, js_path)
        js = md2deck.read(js_path)
        check("slides.js shows the placeholder when it's the only slide",
              "window.SLIDES_MANIFEST" in js and "placeholder.html" in js)

        # Add a REAL deck alongside it -> the build replaces the placeholder.
        with contextlib.redirect_stdout(io.StringIO()):
            md2deck.main([MY_TALK, "--slides-dir", tmp, "--index-out", idx, "--no-build"])
        titles = [e.get("title") for e in build_slides.build_manifest(tmp)]
        check("real deck replaces placeholder on build",
              "Placeholder" not in titles and "My Talk" in titles, repr(titles))
        check("placeholder file is kept on disk as the fallback", os.path.isfile(deck))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        shutil.rmtree(tmp_idx, ignore_errors=True)

    passed = sum(_results)
    total = len(_results)
    print("\n%d/%d checks passed — %s" % (passed, total,
          "OK" if passed == total else "FAILURES ABOVE"))
    print("(temp build dir removed; real slides/ and slides.js untouched)")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
