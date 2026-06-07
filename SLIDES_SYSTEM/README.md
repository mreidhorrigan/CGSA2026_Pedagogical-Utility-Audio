# SLIDES_SYSTEM — write Markdown, get a slideshow kiosk

Turn a **plain text / Markdown file** into a **beautifully laid-out
presentation** that drops straight into the game as **one walkable kiosk** you
open and arrow through. Pure Python 3 + the project's existing pipeline — **no
Node, no pip, no build step, works from `file://`.**

Each compiled deck is a self-contained `.html` that works **both** as a kiosk
in the game **and as a standalone presentation** you can open on its own (or
hand to someone) — see [Present a deck standalone](#present-a-deck-standalone).

> Why this design (and why not Marp/reveal/Pandoc/etc.): see **`RESEARCH.md`**.

## 60-second quickstart

```bash
# from the project root
python3 SLIDES_SYSTEM/md2deck.py SLIDES_SYSTEM/examples/my-talk.md
```

That writes a self-contained `slides/my-talk.html`, rebuilds `slides.js`, and
(re)generates `SLIDES_SYSTEM/presentations.html` — a launcher listing every deck.
Now open `index.html` (or `python3 -m http.server 8000`), walk to the new kiosk,
press **E**, and use **◀ ▶** to move through the slides. Or open
`SLIDES_SYSTEM/presentations.html` to present any deck **standalone**, no game.

Write your own deck by copying `examples/my-talk.md`. Compile a whole folder of
decks at once with `python3 SLIDES_SYSTEM/md2deck.py path/to/folder/`.

### The placeholder room (default → auto-replaced)

`slides/placeholder.html` ships as the **default room** — a built deck
(`examples/placeholder.md`, marked `placeholder: true`) so the game isn't empty.
The moment you build **any real slide**, `build_slides.py` **drops the placeholder
from the manifest** automatically — your content replaces it. The placeholder file
stays on disk as the fallback, so if you later remove all real slides and rebuild,
the placeholder comes back. (Mechanism: the placeholder carries a
`md2deck-role=placeholder` `<meta>`; `build_slides.drop_placeholder_when_real()`
keeps it only when it would otherwise be the empty room.)

> **The kiosk's label comes from the *filename*** (the project's convention, owned
> by `build_slides.py`): `walkable-posters.md` → a kiosk titled *"Walkable
> Posters"*. To order several decks/kiosks, prefix names: `01_intro.md`,
> `02_method.md`, … (natural sort). The deck's own `title:` / first heading is
> used for the browser tab title.

## Authoring cheat-sheet

A deck is Markdown. Slides are separated by `---`. The first `---…---` block is
optional **front-matter**:

```markdown
---
title: My Talk          # browser tab title (kiosk label still comes from filename)
theme: isometric        # isometric (default) | light | <your theme>
paginate: true          # accepted; the kiosk always shows "n / N"
---

<!-- _class: lead -->
# My Talk
## A subtitle
A one-line tagline.

---

## A content slide
- **bold**, _italic_, `code`, ~~strike~~, [links](https://example.com)
- nested lists, > blockquotes, tables, and fenced code all work

---

<!-- _class: invert -->
# One big idea
```

What you can write **inside a slide** (handled by `mdlite.py`):

- `# … ######` headings, paragraphs, `- * +` and `1.` lists (nested by indent)
- `> blockquote`, ```` ``` ```` fenced code, GFM `| pipe | tables |`, `***` rules
- `**bold**` `_italic_` `` `code` `` `~~strike~~` `[text](url)` `![alt](img.png)`
  `<https://autolinks>`, and a two-space hard line-break
- raw HTML (passes through untouched — a power-tool for the odd custom bit)

**Directives & layout** (Marp-compatible):

| You write | Effect |
|---|---|
| `<!-- _class: lead -->` | centred title layout for *this* slide (auto-applied to heading-only slides) |
| `<!-- _class: center -->` | centre everything on this slide |
| `<!-- _class: invert -->` | spotlight slide (accent background) |
| `<!-- anything else -->` | treated as a **speaker note** — never rendered |
| `![bg](photo.jpg)` on its own line | full-bleed slide background image (with a legibility overlay) |
| front-matter `headingDivider: 2` | auto-start a new slide at every `##` (instead of writing `---`) |

A `.txt` file with no `---` simply becomes a single slide.

## Navigating a deck kiosk

Inside the kiosk: **◀ ▶** / **Space** / **Home** / **End**, the on-screen **‹ ›**
arrows, or **click the left / right edge**. A small **n / N** counter and a
progress bar sit at the bottom.

> **Focus gotcha (same as any HTML/PDF slide here):** while a slide is open, the
> *game* owns the keyboard until you **click into the slide** once — then the
> deck's own ◀ ▶ take over. The on-screen arrows and edge-click work without
> clicking in first, so the keyboard is never required.

## Present a deck standalone

Every compiled deck is a **complete, self-contained `.html`** — it works on its
own, no game and no server required. Two ways in:

- **Open one deck directly:** double-click `slides/<name>.html` (or visit it in a
  browser). It fills the window as a real presentation.
- **Browse them all:** open **`SLIDES_SYSTEM/presentations.html`** — an
  auto-generated launcher card-listing every deck. Click one to present it.

Standalone controls: **← →** / **Space** / **Home** / **End** (the keyboard works
immediately — no "click first"), the on-screen **‹ ›** arrows or edge-click, and
**F** to toggle **fullscreen**. The deck detects whether it's standalone or inside
a kiosk and adjusts the on-screen hint accordingly — same file, both contexts.

> The launcher lives in `SLIDES_SYSTEM/` (not `slides/`) on purpose, so it is
> **never** picked up as its own kiosk. It is regenerated on every `md2deck.py`
> run; skip it with `--no-index`, or relocate it with `--index-out PATH`.
> Because each deck `.html` is portable, you can also just copy one file and open
> it anywhere.

## Theming

Themes are just CSS **variables**; all layout lives in `themes/_base.css`.

- **`isometric`** (default) — matches the game: deep navy, teal + coral accents.
- **`light`** — clean white cards for projectors / standalone reading.
- **Add your own:** copy `themes/isometric.css` to `themes/midnight.css`, edit the
  `:root { … }` vars, then `--theme midnight` (or `theme: midnight` front-matter).

The chosen theme is **inlined** into each compiled deck, so every `.html` is fully
self-contained and portable (it even opens on its own in a browser).

## CLI

```text
python3 md2deck.py [inputs ...] [options]

  inputs          deck .md/.txt files or folders   (default: examples/)
  --theme NAME    theme in themes/                  (default: front-matter or isometric)
  --slides-dir D  where decks are written           (default: ../slides)
  --out PATH      explicit output path              (single input only)
  --no-build      write the .html but skip the slides.js rebuild
  --index-out P   standalone launcher path          (default: SLIDES_SYSTEM/presentations.html)
  --no-index      don't (re)generate the standalone launcher page
  --stdout        print the compiled HTML, write nothing   (handy for testing)
```

## Files

```
SLIDES_SYSTEM/
  README.md        this file
  RESEARCH.md      the research + decision behind the design
  HANDOFF.md       session-close handoff + your "from text" workflow
  presentations.html  GENERATED standalone launcher (lists every deck) — not a kiosk
  md2deck.py       compiler: deck.md -> slides/<name>.html  (+ rebuild slides.js + launcher)
  mdlite.py        stdlib Markdown-subset -> HTML engine (reusable; `python3 mdlite.py < x.md`)
  themes/
    _base.css      shared layout (container-query scaling, chrome) — rarely edited
    isometric.css  default palette (game-matched)
    light.css      conference palette
  template/
    deck.html      self-contained deck shell (placeholders inlined at compile time)
    runtime.js     ~70-line in-deck navigator
  selftest.py      one-command pipeline smoke test (builds the placeholder deck)
  examples/
    my-talk.md     a worked deck exercising every feature
    placeholder.md test fixture mirroring PLACEHOLDER_SLIDES (game.js); used by selftest
```

## How it plugs in (no core changes)

`md2deck.py` **writes a `.html` into `slides/` and re-runs `build_slides.py`** —
the same thing you'd do by hand — plus a launcher page inside `SLIDES_SYSTEM/`
(never `slides/`, so it isn't mistaken for a kiosk). The game's `html` slide type
renders the deck in an `<iframe>`; `build_slides.py` remains the single authority
for the manifest and naming. Nothing in `game.js` / `index.html` was modified.

## Verifying changes (no browser automation here)

The fastest check is the **self-test**, which builds the placeholder deck through
the real pipeline (mdlite → md2deck → build_slides) in a throwaway temp dir and
asserts the invariants — it never touches your `slides/` or `slides.js`:

```bash
python3 SLIDES_SYSTEM/selftest.py        # 18 checks; exit 0 = all good
```

Lower-level spot checks:

```bash
python3 -m py_compile SLIDES_SYSTEM/md2deck.py SLIDES_SYSTEM/mdlite.py   # Python OK
osascript -l JavaScript SLIDES_SYSTEM/template/runtime.js                # JS parses (ReferenceError=OK, SyntaxError=bad)
python3 SLIDES_SYSTEM/md2deck.py SLIDES_SYSTEM/examples/my-talk.md --stdout | shasum  # run twice -> identical (deterministic)
```

**The actual look & the room layout can only be confirmed by a human in a
browser** — open `index.html` and walk to the kiosk. The default room already
shows the **placeholder** deck, so there's nothing to set up; build a real deck
and it replaces the placeholder on the next refresh.
