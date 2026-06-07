# RESEARCH — picking a text→slides system to extend locally

*Goal:* a deterministic, convenient way to turn a **text file into a beautifully
laid-out presentation** for this project, built on the most efficient free /
open-source foundation we can extend **locally**.

## The constraints that decide everything

This repo is deliberately spartan (see `../CLAUDE.md`). Any solution **must**:

1. Run with **no Node / npm / TypeScript / bundlers** — this machine has only
   **Python 3.11**.
2. Add **no runtime dependencies**; ideally **no `pip`** either (the project is
   "build-free vanilla JS" and `serve.py` is stdlib-only).
3. Keep working from **`file://`** (double-click `index.html`) — nothing fetched
   at runtime.
4. Produce output the game **already renders**: a slide is `image` / `pdf` /
   `html` / `embed`, where `html` is shown in an `<iframe>` (`renderSlideDOM`,
   `../game.js`). A self-contained `.html` file is the natural target.
5. Be **deterministic**: same input ⇒ same output (the whole pipeline,
   `build_slides.py` included, is built around this).

## The landscape (what I evaluated)

| System | What it is | Verdict for *this* repo |
|---|---|---|
| **[Marp](https://marp.app/)** (Marpit + marp-cli) | The de-facto Markdown→slides standard: CommonMark + `---` page breaks, YAML front-matter, `<!-- directives -->`, CSS themes. | **Conventions: adopt. Toolchain: reject.** The CLI is a Node package (`@marp-team/marp-cli`) — violates #1/#2. But its *Markdown dialect* is the best-documented, most widely known, and trivially re-implementable. |
| **[reveal.js](https://revealjs.com/)** / remark.js | Big client-side JS presentation frameworks (MIT). | Reject. Heavy JS we'd vendor and maintain; they build one monolithic, framework-driven deck rather than the small self-contained per-kiosk `.html` the game wants. Fights the "tiny, readable, zero-dep" ethos (and the single allowed vendored file is the QR lib). |
| **Pandoc** | Haskell binary; converts MD→reveal/beamer/pptx/S5/… | Reject. Not installed; a heavy non-Python binary dependency for one job. |
| **Landslide / Slidedown / [markdown-to-presentation](https://opensource.com/article/18/5/markdown-slide-generators)** | Python slide generators. | Reject. All need `pip`, several are unmaintained, and most just shell Markdown into remark/reveal — so we'd inherit a JS framework anyway. |
| **Slidev** | Vue + Vite. | Reject (Node). |

**Sources:** [marp.app](https://marp.app/) ·
[Marpit directives](https://marpit.marp.app/directives) ·
[Marp directive spec (GitHub)](https://github.com/marp-team/marp/blob/main/website/docs/guide/directives.md) ·
[Opensource.com — Markdown slide generators](https://opensource.com/article/18/5/markdown-slide-generators).

## Decision

> **Adopt Marp's Markdown *conventions*; implement a tiny *compiler* locally in
> stdlib Python that emits self-contained, themed HTML slideshows — one per kiosk.**

Rationale:

- **Standard syntax, zero lock-in.** Decks use the syntax thousands already know
  (`---` breaks, front-matter, `<!-- _class: … -->`). A deck written for us also
  opens in real Marp, and vice-versa — but we owe nothing to its toolchain.
- **Fits the repo like a glove.** Output is a `type:"html"` slide; the existing
  `build_slides.py` already detects `.html` in `slides/` and writes the manifest.
  **No changes to `game.js`, `index.html`, or `slides.js` semantics.**
- **Most efficient to extend *locally*.** No supply chain, no second vendored
  blob: a ~200-line Markdown engine (`mdlite.py`) you can read and bend, plus a
  thin compiler (`md2deck.py`). Themes are plain CSS variable files; new theme =
  copy a 30-line file.
- **Deterministic & offline.** Pure stdlib, no timestamps/randomness in output;
  the deck is one self-contained file (theme CSS + navigator JS inlined) that
  works from `file://` and even opens standalone in a browser.

The **user chose** the mapping: **one deck → one kiosk**, a slideshow you open and
arrow through in place (◀ ▶ keys, on-screen arrows, edge-click), alongside any
other kiosks. Multiple decks ⇒ multiple kiosks.

## Marp conventions we adopted (and where they live)

| Convention | Adopted? | Implemented in |
|---|---|---|
| `---` splits slides; first `---…---` = YAML front-matter | ✅ | `md2deck.split_slides` / `parse_front_matter` |
| Front-matter `title`, `theme`, `class`, `headingDivider`, `paginate` | ✅ | `md2deck` |
| `<!-- key: value -->` local directives; `<!-- _key: … -->` = current slide only | ✅ | `md2deck.extract_comments` + `slide_classes` |
| Non-directive HTML comments = presenter notes (not rendered) | ✅ (stripped) | `md2deck.extract_comments` |
| `![bg](url)` slide background image | ✅ (basic) | `md2deck.extract_bg` + `.has-bg` in `_base.css` |
| CommonMark body (headings, lists, code, tables, emphasis, …) | ✅ (subset) | `mdlite.py` |
| Built-in CSS themes you can fork | ✅ | `themes/*.css` (`isometric` default, `light`) |
| `class: lead` centred title layout | ✅ (+ auto for heading-only slides) | `_base.css` + `md2deck.slide_classes` |

Deliberately **out of scope** (documented, easy to add later if wanted): math
typesetting, syntax-highlight colouring (code is styled but not tokenised),
multi-column directives, and exporting to PDF/PPTX (the deck is HTML; print-to-PDF
from the browser already works).

See `README.md` for how to author and compile.
