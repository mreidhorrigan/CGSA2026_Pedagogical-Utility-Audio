# Building the timeline as a beautiful PDF **and** HTML deliverable

### Free / open-source methods, ranked for "a human and/or an AI can construct it"

*Companion to `Audio-Performance-Control_Genealogy-and-Accessibility.md`. A runnable scaffold lives in `./timeline/` and already produces real output (see §2).*

---

## 1. TL;DR — what to use

| Need | Use | Why |
|---|---|---|
| **The chart, one source → HTML + PDF, AI-authored** | **Vega-Lite + `vl-convert`** | A single JSON spec renders to interactive HTML (vega-embed) *and* true-vector PDF/SVG (`vl-convert`). JSON is the most reliable thing for an LLM to generate. |
| **The genealogy graph (branching lineages)** | **Graphviz (DOT)** | Tiny text language → auto-laid-out graph → native `-Tpdf` and `-Tsvg`. Perfect for "siblings descended from MIDI." *(This is what `genealogy.dot` uses.)* |
| **A polished document that bundles both, HTML + PDF from one file** | **Quarto** (with the **Typst** PDF engine) | One `.qmd` renders to both formats and embeds `dot`/`mermaid`/Python/Observable natively. See `timeline/report.qmd`. |
| **Batteries-included in pure Python** | **Plotly + Kaleido** | `px.timeline` (Gantt-style lanes) → `write_html()` (interactive) **and** `write_image("x.pdf")` (static). One script, both outputs. |
| **Zero-install, works on your machine *today*** | **matplotlib + Graphviz** | No Node/Quarto needed. This is the fallback I used to render your sample now. |
| **Max-beauty, bespoke, web-first** | **D3.js** or **Observable Plot** | Total control of a custom swim-lane; export SVG → PDF with `rsvg-convert`. More effort. |
| **Narrative, media-rich, web-only** | **TimelineJS (Knight Lab)** | Gorgeous scrolling timelines from a JSON/Google-Sheet — but **no real PDF** (web only). |

**My recommendation for your case:** keep the **data in one JSON file** (done — `timeline/timeline_data.json`), draw the **swim-lane timeline in Vega-Lite** and the **genealogy in Graphviz**, and wrap both in a **Quarto** document so `quarto render` emits the HTML and the (Typst) PDF together. Until you install Node/Quarto, the included **matplotlib + Graphviz** path already gives you both formats.

---

## 2. What I built for you (already runs)

`./timeline/` — a working, data-driven scaffold. Re-render anytime with `bash timeline/render.sh`.

```
timeline/
  timeline_data.json     ← CONTENT: events (year, lane, title, zotero key, convergence/root flags)
  timeline_style.json    ← STYLE: palette, fonts, swimlanes on/off, borders — rebrand here, share with other tools
  make_timeline.py       ← swim-lane (or single-line) timeline → timeline.pdf / .svg / .png
  genealogy.dot          ← lineage graph (Graphviz) → genealogy.pdf / .svg / .png
  timeline.vl.json       ← Vega-Lite spec (the recommended upgrade path)
  report.qmd             ← Quarto single-source → HTML + PDF (recommended wrapper)
  build_index.py         ← assembles a self-contained index.html (inlines both SVGs)
  render.sh              ← orchestrates everything; uses upgrade tools if present
  → OUTPUT: timeline.pdf, genealogy.pdf, index.html  (already generated)
```

**Styling / config (in `timeline_style.json`, no code edits needed):**
- `"swimlanes": false` → switch to a single-line timeline (markers colour-keyed by lane) for reuse on other datasets.
- `"decade_gridlines"`, `"convergence"` (band/label) → toggle background guides (decade lines are **off** by default).
- `"palette"` / `"palette_by_lane"`, `"font"`, `"figure"` → branding; the same palette keys can drive other graphing tools.
- **Visual hierarchy via borders:** `label_box.edge_width_{normal,emphasis,root}` + `tint_fill_emphasis`; convergence items get bold tinted borders + a star marker, roots a diamond.
- **No-overlap guarantee:** labels are measured and packed into stacked rows with leader lines, so text is never drawn over text (e.g., the three 1991 events no longer collide). To change density, edit `font.label_wrap` / `layout.marker_gap_rows`.

- **PDF deliverable:** `timeline/timeline.pdf` (vector swim-lane) + `timeline/genealogy.pdf` (vector graph).
- **HTML deliverable:** `timeline/index.html` — self-contained (SVGs inlined, no external requests), with buttons linking to the PDFs and the data.

**Higher-polish outputs (now installed & generated — `vl-convert-python` + `typst`):**
- `make_vega.py` → **`timeline_vega.pdf` / `.svg`** (vector Vega-Lite: halo'd labels, tier-shaped markers, zero overlap) and **`timeline_interactive.html`** (interactive vega-embed with tooltips).
- `timeline.typ` → **`timeline_report.pdf`** (camera-ready A3 landscape bundling the Vega timeline + Graphviz genealogy + a summary grid), via **Typst**.
- `bash render.sh` now regenerates *all* of it (matplotlib draft, Graphviz, self-contained HTML, Vega vector+interactive, Typst report) from `timeline_data.json` + `timeline_style.json`.
- **Design principle:** *data ≠ presentation.* To change content, edit only `timeline_data.json`; every renderer reads it. That's exactly what lets a future AI pass regenerate the visuals without touching styling code.

---

## 3. Full comparison

Output: ✅ first-class · ⚠️ via export step · ❌ not really. AI = how reliably an LLM can author it.

| Tool (all FOSS) | HTML | PDF | Beauty / control | AI | Curve | Best for |
|---|:--:|:--:|---|:--:|---|---|
| **Vega-Lite** + vl-convert | ✅ | ✅ | High, themeable | ★★★ | low–med | data-driven charts/timelines, **one spec → both** |
| **Graphviz** (DOT) | ✅ | ✅ | High for graphs | ★★★ | low | **genealogies / DAGs** |
| **Quarto** (+ Typst) | ✅ | ✅ | High (document) | ★★★ | low–med | the **document** that bundles everything |
| **Plotly** + Kaleido | ✅ | ✅ | High | ★★★ | low | pure-Python, `px.timeline` |
| **matplotlib** | ⚠️ | ✅ | Medium (tunable) | ★★★ | low | offline static vector (**used now**) |
| **Mermaid** + mmdc | ✅ | ✅ | Medium (limited) | ★★★ | very low | quick timeline/flow in docs |
| **Observable Plot** | ✅ | ⚠️ | High | ★★★ | low | concise "D3-lite" |
| **D3.js** | ✅✅ | ⚠️ | **Highest / bespoke** | ★★ | high | custom interactive swim-lane |
| **vis-timeline** | ✅ | ⚠️ | Medium | ★★ | low | zoomable interactive web timeline |
| **Typst** | ⚠️ (exp.) | ✅✅ | High (print) | ★★★ | med | fast, beautiful print; Quarto's PDF engine |
| **TikZ / LaTeX** | ❌ | ✅✅ | Highest (print) | ★★ | high | camera-ready print only |
| **TimelineJS** (Knight Lab) | ✅✅ | ❌ | High (web) | ★★ | low | media-rich web narrative (no PDF) |

Takeaways: **TimelineJS** is the prettiest *web* timeline but gives no PDF; **TikZ/Typst** are the prettiest *print* but weak/awkward in HTML. The tools that genuinely do **both well from one source** are **Vega-Lite**, **Plotly**, **Graphviz**, **Mermaid** — and **Quarto** as the wrapper that ties them into one document.

---

## 4. The recommended stack, concretely

**(a) Timeline — Vega-Lite (`timeline/timeline.vl.json`, provided).** Renders from the same `timeline_data.json`.
```bash
pip install vl-convert-python          # self-contained; no internet, no Node
python -c "import vl_convert as v,json; s=json.load(open('timeline/timeline.vl.json')); \
s['data']=json.load(open('timeline/timeline_data.json'))['events']; \
open('timeline/timeline_vega.pdf','wb').write(v.vegalite_to_pdf(s)); \
open('timeline/timeline_vega.svg','w').write(v.vegalite_to_svg(s))"
```
Interactive HTML: drop the spec into a 6-line page using `vega-embed` (CDN) — snippet at the bottom of `timeline.vl.json`'s sibling notes; or just let Quarto do it.

**(b) Genealogy — Graphviz (`timeline/genealogy.dot`, provided & rendered).**
```bash
dot -Tpdf timeline/genealogy.dot -o genealogy.pdf
dot -Tsvg timeline/genealogy.dot -o genealogy.svg
```

**(c) Wrapper — Quarto + Typst (`timeline/report.qmd`, provided).** One source → both formats; embeds the DOT graph natively.
```bash
# install: https://quarto.org (bundles Typst); then:
quarto render timeline/report.qmd --to html
quarto render timeline/report.qmd --to typst   # → beautiful PDF
```

---

## 5. How an AI can (re)build this — the data contract

Hand any capable model the file `timeline_data.json` and this instruction:

> *"Each event has `year`, `lane` (one of `lanes`), `title`, optional `convergence:true`, and a `zotero` key. Render a swim-lane timeline (x = year, y = lane, ★ for convergence) as a Vega-Lite spec, and a Graphviz DOT genealogy that groups lanes into clusters under a `MIDI 1.0 (1983)` root. Output to PDF and HTML."*

Because the data is declarative and separate, the model never has to re-derive the research — it just styles. (This is the same reason the matplotlib and Vega-Lite renderers can coexist over one dataset.)

---

## 6. Install cheat-sheet (macOS / Homebrew)

```bash
# already present on this machine: python3, matplotlib, graphviz (dot), rsvg-convert, pandoc
pip install vl-convert-python plotly kaleido     # Vega-Lite + Plotly static export
brew install --cask quarto                        # one-source HTML+PDF (bundles Typst)
brew install node && npm i -g @mermaid-js/mermaid-cli   # Mermaid → pdf/svg (optional)
```

---

## 7. Sources
- Vega-Lite `vl-convert` (SVG/PDF/PNG, offline, self-contained): https://github.com/vega/vl-convert
- Vega-Lite "Create Figures for Papers": https://vega.github.io/vega-lite/tutorials/figures.html
- Quarto (multi-format, Typst PDF engine, native Mermaid/Graphviz): https://quarto.org/docs/output-formats/typst.html · https://quarto.org/docs/authoring/diagrams.html
- Plotly static export (Kaleido): https://plotly.com/python/static-image-export/
- Graphviz: https://graphviz.org · TimelineJS: https://timeline.knightlab.com · Mermaid CLI: https://github.com/mermaid-js/mermaid-cli · Typst: https://typst.app
