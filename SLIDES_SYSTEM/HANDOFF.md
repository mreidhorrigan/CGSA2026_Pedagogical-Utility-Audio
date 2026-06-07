# SLIDES_SYSTEM — session close & handoff (2026-06-05)

This is the wrap-up for the **text → presentation** system added under
`SLIDES_SYSTEM/`. It explains, above all, **how you use it day to day starting
from plain text**, then records the end-of-session state, how to verify it, the
gotchas, and what was intentionally left for later.

- Deep "why": `RESEARCH.md`  ·  Full reference: `README.md`  ·  This file: workflow + handoff.

---

## 1 · Your workflow — starting from text

You write a talk as a **plain text / Markdown file** and run one command. That's it.

```bash
# 1. Write a file, e.g. mytalk.md  (see the template just below)
# 2. Compile it:
python3 SLIDES_SYSTEM/md2deck.py mytalk.md
# 3. View it — either way:
#    • in the game:  open index.html  → walk to the kiosk → press E → ◀ ▶
#    • standalone:   open slides/mytalk.html   (or SLIDES_SYSTEM/presentations.html)
```

What step 2 does, automatically and deterministically:

1. writes a **self-contained** `slides/mytalk.html` (one slideshow = one kiosk),
2. **replaces the placeholder** and rebuilds `slides.js` (the game's manifest),
3. refreshes `SLIDES_SYSTEM/presentations.html` (the standalone launcher).

### The only Markdown you need to know

```markdown
---
title: My Talk          # browser-tab title (the *kiosk* label = the filename)
theme: isometric        # isometric (default) or light
---

# My Talk
## A subtitle           # a heading-only slide auto-centres as a title slide

---                     # <- three dashes separate slides

## First point
- bullet one
- **bold**, _italic_, `code`, [a link](https://example.com)

---

## Thanks
Questions? me@example.com
```

- **Slides are split by a line of `---`.** The first `---…---` block is front-matter.
- Inside a slide you can use headings, lists, `> quotes`, ```` ``` ```` code,
  `| tables |`, images `![alt](path.png)`, and raw HTML. Full cheat-sheet +
  directives (`<!-- _class: lead|center|invert -->`, `![bg](img)`, speaker notes,
  `headingDivider`) are in **`README.md`**; a worked example is
  **`examples/my-talk.md`**.
- It stays **mostly textual**: images/video are optional. (For a video kiosk, the
  game's own `embed` slide type — a `.url` file in `slides/` — is the simplest path;
  see the top-level `README.md`.)

### Naming & ordering (important)

- The **kiosk's label comes from the filename** (project convention, owned by
  `build_slides.py`): `walkable-posters.md` → kiosk *"Walkable Posters"*.
- Multiple decks = multiple kiosks. Order them by prefixing: `01_intro.md`,
  `02_method.md`, … (natural sort). Compile a whole folder at once:
  `python3 SLIDES_SYSTEM/md2deck.py path/to/folder/`.

### Presenting standalone (no game)

- Open `slides/<name>.html` directly, or open the launcher
  `SLIDES_SYSTEM/presentations.html` and click a deck.
- Controls: **← →** / Space / Home / End, on-screen **‹ ›**, edge-click, and
  **F = fullscreen**. The deck auto-detects standalone vs. in-game and adjusts its
  hint. (In-game, click the slide once to give it the keyboard — a documented
  iframe quirk; the arrows/edge-click work without clicking.)

---

## 2 · State of the repo at session close

**New subsystem (all under `SLIDES_SYSTEM/`):**

```
md2deck.py        compiler:  deck.md -> slides/<name>.html  (+ rebuild slides.js + launcher)
mdlite.py         stdlib Markdown-subset -> HTML engine (reusable; python3 mdlite.py < x.md)
selftest.py       one-command pipeline smoke test (21 checks) — see §3
themes/_base.css  shared deck layout (container-query scaling + chrome)
themes/isometric.css   default palette (matches the game)
themes/light.css       clean "conference" palette
template/deck.html     self-contained deck shell (placeholders filled at compile time)
template/runtime.js    in-deck navigator (←→, click, fullscreen, standalone/embedded)
examples/my-talk.md    worked example exercising every feature
examples/placeholder.md the default-room deck (marked `placeholder: true`)
README.md  RESEARCH.md  HANDOFF.md (this)
presentations.html     GENERATED standalone launcher (lists every deck) — not a kiosk
```

**Generated/committed artifacts now in the repo:**

- `slides/placeholder.html` — the **default room** (built placeholder deck).
- `slides.js` → currently the single `Placeholder` kiosk.
- `SLIDES_SYSTEM/presentations.html` — launcher listing the placeholder.

**One core file was changed (by design, for this request):**

- `build_slides.py` gained `drop_placeholder_when_real()` + `_is_placeholder_html()`.
  A placeholder deck (carrying `<meta name="md2deck-role" content="placeholder">`)
  is kept in the manifest **only when it would otherwise be the empty room**; any
  real slide drops it (the file stays on disk as the fallback). This applies to
  **both** `python3 build_slides.py` and `md2deck.py` (which calls it).
- **`game.js` and `index.html` were *not* modified.** Decks render through the
  existing `type:"html"` slide path. The JS `PLACEHOLDER_SLIDES` fallback remains
  as a deeper safety net for when `slides.js` is empty.

**Also changed this session (separate task):** `.claude/settings.json` was created
with **12 read-only permission-allow entries** (e.g. `mcp__zotero__zotero_search_items`,
`Bash(shasum *)`, `Bash(pdfinfo *)`) to cut prompts. Your `.claude/settings.local.json`
was left untouched.

---

## 3 · How to verify it still works (no browser automation here)

```bash
python3 SLIDES_SYSTEM/selftest.py     # 21 checks; exit 0 = all good. Builds the
                                      # placeholder through mdlite→md2deck→build_slides
                                      # in a TEMP dir; never touches real slides/.
```

Spot checks:

```bash
python3 -m py_compile build_slides.py SLIDES_SYSTEM/md2deck.py SLIDES_SYSTEM/mdlite.py
osascript -l JavaScript SLIDES_SYSTEM/template/runtime.js     # ReferenceError=parsed OK, SyntaxError=bad
python3 SLIDES_SYSTEM/md2deck.py SLIDES_SYSTEM/examples/my-talk.md --stdout | shasum  # run twice → identical
```

**Only a human in a browser can confirm the visuals & room layout.** The default
room already shows the placeholder, so just open `index.html` and walk in.

---

## 4 · Gotchas & things to know

- **Placeholder is the default and self-healing.** Build a real deck → it replaces
  the placeholder in the room; delete all real decks and rebuild → placeholder
  returns. The file is never auto-deleted.
- **Kiosk title = filename**, not the deck's `title:` (which is the tab title).
  Name files accordingly; for a title that must start with a number, set it by
  hand in `slides.js`.
- **Don't put the launcher in `slides/`.** Plain `.html` there becomes a kiosk;
  `md2deck` guards against `--index-out` inside the slides dir and skips it with a
  warning.
- **Self-contained except referenced media.** Theme CSS + navigator JS are inlined,
  but an `![alt](pic.png)` still points at a file — keep such assets next to the
  deck (e.g. in `slides/`) if you move it.
- **Determinism matters here** (the whole pipeline relies on it) — no timestamps or
  randomness in output; same input ⇒ identical bytes.

---

## 5 · Intentionally not done (future hooks)

- Math typesetting, syntax-highlight **colouring** (code is styled, not tokenised),
  and multi-column layout — all addable in `mdlite.py` / `themes/`.
- PDF / PPTX export — not needed: a deck is HTML, so the browser's **Print → PDF**
  works on any standalone deck.
- No pointer to SLIDES_SYSTEM was added to the top-level `CLAUDE.md` / `README.md`
  (left out on purpose). If you want the next contributor to discover it
  automatically, add one line to `CLAUDE.md`'s file map.

---

## 6 · One-line restart for the next session

> "The `SLIDES_SYSTEM/` text→slides system is complete and tested
> (`python3 SLIDES_SYSTEM/selftest.py` = 21/21). Author a deck as Markdown and run
> `python3 SLIDES_SYSTEM/md2deck.py yourfile.md`; it becomes a kiosk **and** a
> standalone deck, and replaces the default placeholder room. Start at
> `SLIDES_SYSTEM/HANDOFF.md`."
