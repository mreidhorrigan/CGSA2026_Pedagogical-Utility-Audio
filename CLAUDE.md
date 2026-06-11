# CLAUDE.md — orientation for this project

Read this first. It's written so the next contributor — a human or a later Claude
session — can get productive fast and extend the project **safely**. (`README.md`
is the user-facing guide; this is the contributor/AI guide.)

## What this is
An in-browser conference poster built as an isometric game: a visitor walks a
room as a sheet-ghost and views slides (image / PDF / scrollable HTML / **embed**)
at kiosks. Pure client-side, no framework — plus an **optional** stdlib server
(`serve.py`) that adds **multiplayer** (visitors see each other's ghosts move).

## Environment — read before changing anything
- This machine has **no Node / npm / TypeScript** — only **Python 3.11**. Do NOT
  introduce npm / Vite / webpack / bundlers / runtime dependencies. The game is
  deliberately **build-free vanilla JS**.
- **One vendored static file** exists and is allowed: `tools/qrcode-generator.js`
  (qrcode-generator, MIT) — a plain `<script>` include, the same "ship a static
  file" spirit (no npm/build). It backs the presenter-facing `tools/qr.html` **and**
  the game's own start-screen "scan to open on your phone" QR (`buildJoinQR()`, §6).
  `serve.py` is **stdlib-only** (no pip). Keep both true.
- `game.js` is **plain JS with `// @ts-check` + JSDoc** (not `.ts`), so editors
  type-check it with zero tooling (`jsconfig.json`). Keep it that way.
- It must keep running from **`file://`** (double-click `index.html`) as well as
  over a static server. Nothing is fetched at runtime; browsers can't list a
  directory over `file://`, which is exactly why slides go through a manifest.

## Run / rebuild
- Play: open `index.html`, or `python3 -m http.server 8000`.
- **Play together (multiplayer):** `python3 serve.py` — serves the game + a ghost-
  position relay; single-player still works with no server (see README + §3b NET).
- Slides from a folder of images: drop into `images/`, run `python3 import_images.py`.
- Slides managed directly (incl. PDF / HTML / **embed**): put files in `slides/`, run `python3 build_slides.py`.

## Verify changes (no browser automation is available here)
- **JS syntax:** `osascript -l JavaScript game.js` — a `ReferenceError: … document`
  means it PARSED FINE (it only hit a browser-only global); a `SyntaxError` is a
  real problem to fix.
- **Python:** `python3 -m py_compile build_slides.py import_images.py`.
- **Serving:** `curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/...`.
- **Multiplayer relay:** `python3 serve.py --port 8099 &`, then `curl
  http://localhost:8099/net/info` and POST `/net/sync` as two ids — the second
  should see the first. Kill it after. (True multi-device sync is a human check.)
- **QR tool:** `osascript -l JavaScript tools/qrcode-generator.js` (vendored lib
  parses), and parse the inline `<script>` of `tools/qr.html` the same way.
- **Pipeline:** make dummy files in `images/`/`slides/`, run the scripts, inspect
  `slides.js`, then clean up:
  `find images slides -maxdepth 1 -type f ! -name README.md -delete`.
- **Visual / gameplay can only be confirmed by a human in a browser** — say so
  explicitly rather than claiming it works.

## File map
```
index.html        page, overlays (intro / slide / HUD), CSS; loads qrcode-generator.js, slides.js, then game.js
game.js           the game — sections 1–11 (+ 3b NET), CONFIG block at the top
slides.js         GENERATED manifest (window.SLIDES_MANIFEST) — don't hand-edit casually
build_slides.py   slides/  -> slides.js (deterministic; OWNS the naming convention)
import_images.py  images/ -> slides/ (alphabetical, prefixed) -> slides.js
serve.py          OPTIONAL multiplayer: stdlib server = static files + ghost-position relay
tools/qr.html     standalone QR generator (vendored qrcode-generator.js, MIT) for the serving URL
images/  slides/   raw inputs / game-ready slides (each has its own README)
jsconfig.json     editor type-checking, no build
HANDOFF.md        handoff + manual test checklist for the QR / embed / multiplayer changes
```

## game.js architecture (numbered sections)
| # | Section | What lives there |
|---|---------|------------------|
| 1 | CONFIG | tunables, `KIOSK_PALETTE`, `PLACEHOLDER_SLIDES`, `SHEET_THEMES`, audio `SCALE` |
| 2 | STATE | canvas + run-time vars; `GRID`/`SLIDES`/`EXHIBITS` are `let` (built at load) |
| 3 | AUDIO | `audio.tone()` primitive + `noteFreq()` + `sfx{}`; generative-music hook |
| 3b| NET | optional multiplayer: `netInit/netTick/netSync/lerpPeers/drawPeer` + `net` state; inert unless `serve.py` answers |
| 4 | SLIDE LOADING | `loadSlides()`: manifest → image-probe → placeholders; `normalizeSlide`/`guessType`; `preloadSlideDocs()` (http-only srcdoc warm-up) |
| 5 | ROOM LAYOUT | `buildRoom(count)`: ring of kiosks, grid sized to fit, walkway, player |
| 6 | INIT | DOM refs, random ghost, picker, listeners, async load → `buildRoom` |
| 7 | INPUT | `onKeyDown/Up`; `onCanvasPointer` (tap/click → `walkToKiosk`/`walkToPoint`); `autoPathNext()` (Space); `startGame()` |
| 8 | UPDATE | movement (auto-walk OR keys), collision, active-kiosk detection |
| 9 | RENDER | floor, kiosks, ghost (`paintGhost`), guidance arrow, toast, HUD |
| 10 | SLIDE MODAL | open/close/`setSlide`; `renderSlideDOM()` switches on slide `type` |
| 11 | HELPERS | iso math, draw primitives, colour, escaping |

**Conventions:** one classic-script global scope (no modules/imports); top-level
`function` declarations are hoisted, so call-order is flexible and the file ends
with `init()`. Use `escapeHtml` for element text, `escapeAttr` for attributes
(including the iframe `srcdoc`).

## Extension recipes ("how do I…")
- **Add a slide type:** add a branch in `renderSlideDOM()` (§10), teach
  `guessType()` (§4) the extension, and add the extension to the right set in
  `build_slides.py`. Document it in the READMEs. The **`embed`** type (a 16:9
  YouTube/Vimeo/any-URL iframe) is the worked example: `toEmbedUrl()` in §4
  normalises watch URLs; `EMBED_EXTS` + `read_url_file()` in `build_slides.py`
  turn a `.url`/`.embed`/`.yt` file's URL into an `{type:"embed", src:<url>}` entry.
- **Add / change a ghost look:** edit `SHEET_THEMES` (§1). For a new cloth
  pattern, handle a new `theme.pattern` value in `paintGhost()` (§9). The start
  picker and the `C` cycle update automatically.
- **Add a sound:** add a method to `sfx{}` (§3) built on `audio.tone()`; call it.
- **Generative music (planned):** implement the documented lookahead scheduler in
  §3, start it from `startGame()`, keep its gain low so SFX sit on top.
- **Audio-instruction navigation (planned):** recognise commands, then call
  `autoPathNext()` or set `auto.goal` (§7) — the walk + auto-open already exists.
- **Change the room shape:** edit `buildRoom()` (§5) — currently a ring.
- **Add a control key:** handle it in `onKeyDown()` (§7) and list it in the intro
  controls (`index.html`) + README.
- **Touch / click navigation (phone support):** `onCanvasPointer` (§7) hit-tests
  taps — `kioskAtScreen()` (§11, a screen-space box over each kiosk) routes a tap to
  `walkToKiosk()` (auto-walk + open), else `screenToWorld()` (§11, the inverse iso
  projection) feeds `walkToPoint()` (auto-walk to a floor tile, then stop). Both reuse
  the Space auto-walk machinery in §8 (`auto` now also carries a free point + a stuck
  guard). The canvas has `touch-action:none` so taps navigate instead of scrolling.

## Slide naming convention (single source of truth)
`build_slides.py` defines it. Files are ordered by a natural sort; `title_from()`
strips a leading numeric index (`strip_leading_index()`) and title-cases the rest:
`01_method_chart.png` → "Method Chart", `03.png` → "Slide 3". `import_images.py`
reuses `strip_leading_index()` so the two tools never disagree. If a title must
legitimately start with a number, set it by hand in `slides.js`.

## Multiplayer — `serve.py` + §3b NET
- **Off by default, additive.** game.js networks only when `location.protocol` is
  http(s) **and** `GET /net/info` answers; otherwise `net.on` stays false and
  nothing changes. Never make core gameplay depend on `net`.
- **serve.py is stdlib-only** (no pip): `ThreadingHTTPServer` + `SimpleHTTPRequestHandler`
  serving `ROOT`, plus `GET /net/info` (probe) and `POST /net/sync` (send mine →
  get others, per `room`, pruned after `PLAYER_TTL`). It validates / clamps / caps
  everything clients send — keep it that way; remote **names and speech-bubble
  messages are drawn as canvas text** via `label()` / `speechBubble()`, never
  injected as HTML. The `msg` field is `_clean_msg`'d and capped at `MSG_MAX`.
- **Wire points in game.js:** `netInit()` from `init()`; `netTick()+lerpPeers()`
  in `loop()`; remote ghosts join the depth-sorted actor list in `render()` via
  `drawPeer()` (reuses `paintGhost`); the room count shows in `updateHUD()`.
- **Speech bubbles (F key / 💬 on touch):** `toggleMessage()` (§7) opens
  `#msgComposer` to type `net.msg`; it rides along in `netSync()` and renders as a
  `speechBubble()` over each ghost (replacing the name tag). `net.composing` makes
  `onKeyDown` cede the keyboard to the text input. Phones have no F key, so a floating
  `#chatBtn` (💬) calls the same `toggleMessage()`, and `#msgComposer` carries **Post/
  Cancel** buttons (`postMessage`/`closeComposer`) since there's no Enter/Esc; on touch
  (`@media (pointer:coarse)`) the composer moves to the top, clear of the on-screen
  keyboard, and the button shows only while `net.on`. Mirror any new networked field
  in `serve.py`'s `_sync`.

## Gotchas
- **Leaving a slide is fullscreen-safe by design.** In `onKeyDown()` (§7), the
  `state === "slide"` branch closes the modal on **`E`** (the same key that opened
  it — a toggle), on **any movement key** (which also starts walking — "walk away
  to leave"), and on **`Esc`** (kept for non-fullscreen, but avoidable on purpose:
  browser fullscreen swallows `Esc` as "exit fullscreen"). Slide **browsing** is on
  `<`/`>` (was `←/→`, freed up so arrows can walk you away). If you re-add an
  arrow/WASD binding here, don't reintroduce that conflict.
- **Slide iframes & the keyboard.** HTML/PDF/embed slides are `<iframe>`s that grab
  the keyboard once focused, and the game's keydown listener is on the *parent*
  window (which iframe key events never reach). `wireSlideIframeKeys()` (§10)
  forwards the leave keys (**E/Esc**) and **WASD** from *same-origin* iframes (the
  HTML decks) back to `closeSlide()`, so those keep working even after you click
  into a deck; arrows/Space/F stay with the deck's own navigator. **Cross-origin**
  iframes — the browser's PDF viewer and YouTube/Vimeo embeds — can't be reached, so
  there you leave with the **✕** button or by clicking the backdrop. `closeSlide()`
  refocuses the canvas so movement + `keyup` return to the game (no stuck keys).
- **HTML slides open from memory over http(s).** `preloadSlideDocs()` (§4) fetches
  each html slide once after load and stores it on the slide as `s.html`;
  `renderSlideDOM()` prefers `s.html` → `srcdoc`, so kiosks open with no network
  round-trip (no white frame on slow hosts). A `<base href="slides/">` is injected
  because srcdoc resolves relative URLs against the *page*, not `slides/` — keep
  slide-internal asset paths relative (e.g. `SourceMaterial/...`). srcdoc iframes
  are same-origin, so `wireSlideIframeKeys()` still works. Over `file://` fetch()
  is unavailable: slides keep loading by iframe `src` — keep both paths working.
- The runtime image-probe only finds **plain numeric** names (`slides/1.png`…);
  the importer's prefixed names rely on the manifest (which it rebuilds).
- Keep `MASTER_VOLUME` and any future music gain low so interaction SFX stay clear.
- The local `python3 -m http.server` may already be running on :8000 from a prior
  session; reuse it rather than starting duplicates.
