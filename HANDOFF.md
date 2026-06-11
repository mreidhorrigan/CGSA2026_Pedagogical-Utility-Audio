# HANDOFF — QR codes · embedded video · multiplayer

**Date:** 2026-06-02 · **Scope:** three additive extensions to the Walkable
Presentation. All build-free (no npm/Node, Python 3.11 only). **Single-player
still runs from `file://` exactly as before** — every new capability degrades
gracefully when its server/tooling isn't present.

This doc is for **handoff** (what changed, how to run) and **testing** (a copy-
paste verification script + a manual checklist for the things only a human can
confirm). User guide = `README.md`; architecture/contributor guide = `CLAUDE.md`.

---

## 2026-06-10 update — phone support (join QR · tap-to-walk · touch chat) + 5 demo kiosks

This session made the poster **fully usable on a phone** (tap-to-walk confirmed on an
iPhone X) and switched the room to **5 demo kiosks** pending the real slides. All
committed + pushed to `main` (commits **`1da144a`** phone support, **`01b8c9a`** mobile
polish) → auto-deployed to Render. **The next session builds the real slides — see
">>> NEXT SESSION" below.**

| What | Where it lives | Notes |
|------|----------------|-------|
| **Join QR on the start screen** | `game.js` `buildJoinQR`/`shareableUrl`/`makeQRCode`/`qrSvg` (§6); `index.html` `#qrJoin`; new `<script src="tools/qrcode-generator.js">` | "Scan to open on your phone" — encodes the page's own URL. `JOIN_URL` config (§1): `""` = auto (LAN IP locally / Render URL in prod); hidden on `file://`, localhost, and touch. The vendored QR lib is **now used by the game runtime**, not just `tools/qr.html`. |
| **Tap / click to walk** | `game.js` `onCanvasPointer` (§7), `walkToKiosk`/`walkToPoint`, `screenToWorld`/`kioskAtScreen` (§11); `auto` gained a free point + stuck-guard (§8); `canvas{touch-action:none}` | Tap a kiosk → walk over + open it; tap the floor → walk there. Reuses the Space auto-walk. No keyboard needed. |
| **Phone speech bubbles** | `game.js` `#chatBtn` wiring + `updateHUD` toggle; `index.html` `#chatBtn` (💬), `#msgComposer` Post/Cancel | Floating 💬 (touch + `net.on` only) opens the composer (no F key on a phone); **Post/Cancel** buttons (no Enter/Esc on mobile); composer moves to the **top** on touch so the keyboard can't cover it. |
| **Phone-friendly start screen** | `index.html` `@media (pointer:coarse)`, `.touch-controls` | On touch, keyboard chips + join QR hidden, replaced with tap hints. **"Enter the room" moved to the top** (under the intro line) so you can skip the instructions. |
| **Stray-`f` fix** | `game.js` `onKeyDown` `'f'` branch | `preventDefault()` so opening the composer no longer types an `f` into it. |
| **No stale assets** | `serve.py` `end_headers` | Static files now send `Cache-Control: no-cache` (revalidate; cheap 304s via Last-Modified) so a redeploy/edit is picked up at once — mobile Safari was serving a stale `game.js`/`slides.js`. `/net/*` keeps its own `no-store`. |
| **5 demo kiosks** | `slides.js` (emptied on purpose) | `window.SLIDES_MANIFEST = []` → the game falls back to the 5 built-in `PLACEHOLDER_SLIDES`. `slides/placeholder.html` (one bundled md2deck deck) is still on disk, unused. |

### Operating notes
- **Phones self-refresh now** — *except* the first load after this deploy, since the phone still caches the pre-`no-cache` version. Clear it once (Safari **Private tab**, or Settings → Safari → **Clear History and Website Data**); it stays fresh after that.
- Mac LAN IP last seen **10.0.0.186**. Local phone test: `python3 serve.py --port 8001` (8000 was taken by another server) → open `http://10.0.0.186:8001` on the phone (same Wi-Fi; click **Allow** if macOS firewall prompts).

### Manual checks still open (browser/phone — can't be automated here)
- [x] iPhone: tap-to-walk + tap-a-kiosk-to-open — **confirmed working** by the user.
- [ ] iPhone: tap **💬** → keyboard up, composer at top → type → **Post** floats your bubble (desktop sees it); **Cancel** dismisses. *(Deployed but not yet eyeballed — pushed at session end.)*
- [ ] iPhone: **"Enter the room"** reachable at the top of the start screen. *(Same — just pushed.)*
- [ ] One-time: after this deploy, the cache-clear above actually yields the fresh build.

### >>> NEXT SESSION — build a basic version of the real slides <<<
**Goal:** replace the 5 demo kiosks with the actual presentation.

- **Room = one kiosk per slide *file*** in `slides/` (one entry in `slides.js` = one
  kiosk). `python3 build_slides.py` regenerates `slides.js` from `slides/` and
  **auto-drops** `placeholder.html` once real slides exist. The empty `slides.js` is
  expected until then — building real slides overrides it.
- **User preference: ONE KIOSK PER SLIDE** (they explicitly wanted this). ⚠️ Gotcha:
  `SLIDES_SYSTEM/md2deck.py` compiles a whole Markdown file into **one** self-contained
  HTML deck = **one** kiosk (slides paged *inside* it). For one-kiosk-per-slide use
  **separate files** (one `image`/`.html`/`.pdf`/`.yt` per slide). **Confirm the
  structure + get the actual content/outline from the user before building.**
- **Slide types** (`renderSlideDOM` §10 / `build_slides.py`): `image` (png/jpg/webp/…),
  `pdf`, `html` (scrollable doc — file or inline), `embed` (`.url`/`.embed`/`.yt` → 16:9).
- **Set the title:** `TALK_TITLE` (`game.js` §1) is still `"Your Presentation"`. Topic
  per the repo/Render name: *pedagogical utility of audio* (CGSA 2026).
- **Ship:** files into `slides/` → `python3 build_slides.py` → inspect `slides.js` →
  commit + **push to `main`** (auto-redeploys Render).
- **Verify (no browser here):** `osascript -l JavaScript game.js` parses;
  `python3 -m py_compile build_slides.py`; serve + curl 200s. Room layout = human-in-browser.

**Rollback for this session:** `git revert 01b8c9a` (mobile polish) and/or `1da144a`
(phone support); both are on `main` (untagged).

---

## 2026-06-07 update — live on Render + controls, lattice, speech bubbles

This session put the poster **online for remote multiplayer** and added three
things on top of the 2026-06-02 work below. Everything is committed to git and
pushed to GitHub (`mreidhorrigan/CGSA2026_Pedagogical-Utility-Audio`, branch
`main`); **pushing to `main` auto-redeploys to Render.** Navigation hub: `INDEX.md`.

**Live:** https://cgsa2026-audio-presentation.onrender.com

| What | Where it lives | Notes |
|------|----------------|-------|
| **Render deployment** | `render.yaml`, `requirements.txt`, `serve.py` (binds `$PORT`) | One **free Python web service** = static site **and** ghost relay on one HTTPS origin. No Node. Full guide + caveats: **`DEPLOY.md`**. |
| **Fullscreen-safe slide controls** | `game.js` §7/§10 | Leave a slide with **E** (toggle), by **walking away** (WASD/arrows), or **Esc** — you're no longer forced onto Esc (which exits browser fullscreen). Same-origin slide iframes forward E/Esc/WASD via `wireSlideIframeKeys()`; cross-origin PDFs/embeds leave via the **✕**. |
| **Cyberpunk lattice floor** | `game.js` `drawFloor()` | Cosmetic: dark void + glowing cyan isometric grid + magenta walkway underglow. |
| **Speech bubbles (F)** | `game.js` + `serve.py` `_clean_msg` | Press **F** to post a ≤100-char message over your ghost for the whole room (it replaces the name tag); **F** again clears. Built for live audience Q&A. Canvas text only — never HTML; the relay caps + sanitizes. |

### Operating it for the talk
- **Warm it first:** the free tier sleeps after ~15 min idle (~50 s cold start). Open the URL a couple of minutes before presenting, or move to Render **Starter** for the day. Keep it **one instance** (relay state is in memory). Capacity / "how many can join": `DEPLOY.md`.
- **Join QR:** open `…onrender.com/tools/qr.html` (optionally point people at `…/?room=cgsa2026`) and drop the QR on a slide.

### Manual test checklist (browser only — can't be automated here)
- [ ] Fullscreen → open a slide → click *into* it → **E** closes it; **WASD** closes + walks. A PDF/video slide leaves via the **✕**.
- [ ] Two windows side-by-side → **Start** in both → **👻 2 in the room**; walking in one moves that ghost in the other.
- [ ] Press **F**, type a question, **Enter** → a bubble appears over that ghost in *both* windows; **F** again clears it; **Esc** cancels the composer.
- [ ] The floor renders as a glowing cyan lattice on a dark base.

### Rollback points (git tags, pushed to GitHub)
`v1.0` initial Render deploy · `v1.1` + cyberpunk lattice (pre-speech-bubbles) · `v1.2` this complete, verified state. Undo one change with `git revert <hash>`; jump to a checkpoint with `git checkout v1.2`.

---

## TL;DR — run each piece

```bash
cd ~/Documents/GamesDevelopment/Presentation

# Single-player (unchanged):           open index.html  (double-click)
# Serve + multiplayer:                 python3 serve.py        # prints URLs + a QR link
# Make a QR for a slide:               open tools/qr.html      # or the printed /tools/qr.html?url=…
# Add a YouTube/Vimeo slide:           echo 'https://youtu.be/VIDEOID' > slides/1.yt && python3 build_slides.py
```

---

## What changed

### New files
| File | Purpose |
|------|---------|
| `serve.py` | **Stdlib-only** server (no pip): serves the static site **and** a ghost-position relay on one port. CLI: `--host` (default `0.0.0.0`), `--port` (default `8000`), `--room <code>`. Endpoints: `GET /net/info`, `POST /net/sync`. Caps: prune after 6 s, ≤80 players/room, ≤4 KB body, ≤24-char names, all numbers clamped. |
| `tools/qr.html` | Offline QR generator. Prefill via `?url=` / `?text=`. Error-correction L/M/Q/H. Outputs: live SVG, **Download SVG/PNG**, **Print**, **Download as slide** (`join.html`), **Copy slide HTML**. |
| `tools/qrcode-generator.js` | Vendored **qrcode-generator v1.4.4 (MIT, Kazuhiko Arase)**, verbatim + provenance header. The *only* vendored file; used solely by `tools/qr.html`, never by the game runtime. |

### Modified files
| File | Change |
|------|--------|
| `game.js` | New **`§3b NET`** (multiplayer client — inert unless a relay answers); **`embed`** slide type (`guessType`, `toEmbedUrl`, `renderSlideDOM` branch); config `NET_SYNC_MS`, `NET_LERP`; hooks in `init/loop/render/updateHUD`. |
| `index.html` | 16:9 `embed` stage CSS; start-screen name field (`#mpName`, hidden until a relay is found); HUD "👻 N in the room" badge. |
| `build_slides.py` | `embed` type from `.url`/`.embed`/`.video`/`.yt` files via `read_url_file()`. |
| `README.md`, `CLAUDE.md`, `slides/README.md` | Documentation. |

---

## Automated verification (no browser — re-runnable)

Paste this whole block from the project directory; it leaves the repo unchanged.

```bash
PROJ="$PWD"
echo "== parse/compile =="
osascript -l JavaScript "$PROJ/game.js" 2>&1 | head -1          # want ReferenceError (parsed), NOT SyntaxError
osascript -l JavaScript "$PROJ/tools/qrcode-generator.js" 2>&1 | head -1
python3 -m py_compile "$PROJ/serve.py" "$PROJ/build_slides.py" "$PROJ/import_images.py" && echo "py_compile OK"

echo "== live relay on :8099 =="
python3 "$PROJ/serve.py" --port 8099 >/tmp/h.log 2>&1 & SRV=$!
curl -s --retry 15 --retry-delay 1 --retry-connrefused -w '\n' http://localhost:8099/net/info
curl -s -X POST -H 'Content-Type: application/json' -d '{"id":"A","name":"Alice","x":3,"y":4,"fx":1,"fy":0}' http://localhost:8099/net/sync; echo
curl -s -X POST -H 'Content-Type: application/json' -d '{"id":"B","name":"Bob","x":5,"y":6,"fx":0,"fy":1}'   http://localhost:8099/net/sync; echo  # should list Alice
curl -s -o /dev/null -w 'bad-json -> %{http_code}\n' -X POST -H 'Content-Type: application/json' -d 'nope' http://localhost:8099/net/sync
for p in / /game.js /tools/qr.html /tools/qrcode-generator.js; do
  curl -s -o /dev/null -w "  $p -> %{http_code}\n" "http://localhost:8099$p"; done
kill $SRV 2>/dev/null; rm -f /tmp/h.log
```

**Expected:** `game.js`/`qrcode-generator.js` → `ReferenceError … document` (means *parsed OK*); `py_compile OK`; `/net/info` → `{"multiplayer": true,…}`; Bob's response lists Alice; `bad-json -> 400`; all paths `-> 200`.

*Last run here: all of the above passed.*

---

## Manual test checklist (browser / phone — can't be automated here)

### A. Single-player is unaffected
- [ ] Open `index.html` directly (`file://`). Game loads; WASD/arrows move; **E** opens a kiosk slide; **E again** (or **walking away** with WASD/arrows) leaves it; **Esc** still closes too. Console clean. **No** name field and **no** 👻 badge appear.

### B. Embedded video (`embed` slide)
- [ ] `echo 'https://youtu.be/aqz-KE-bpKQ' > slides/1.yt` → `python3 build_slides.py` (prints `[embed] … — Slide 1`).
- [ ] `python3 serve.py`, open the printed URL, walk to the kiosk, press **E** → video appears in a **16:9** frame and **plays**. (Serve it — YouTube often refuses to play from `file://`.)
- [ ] Also try a `.html` slide containing an `<iframe>` — it should scroll as a document.
- [ ] Cleanup: `rm slides/1.yt && python3 build_slides.py`.

### C. QR code
- [ ] Open `tools/qr.html`. Type a URL → QR renders, URL shown beneath it.
- [ ] **Scan with a phone camera** → the phone opens that exact URL. *(This is the one thing nobody could verify without a real scan.)*
- [ ] **Download SVG**, **Download PNG**, **Print** each work; **Download as slide** saves `join.html` → drop it in `slides/`, rebuild, and confirm it shows in-game.
- [ ] Long URL + level **L** still encodes; empty box shows a hint (no crash).

### D. Multiplayer — two tabs, no second device needed
- [ ] `python3 serve.py`. Open the printed URL in **two** browser tabs/windows.
- [ ] Both show the **name field** on the start screen and, after **Start**, the badge reads **👻 2 in the room**.
- [ ] Walk in tab 1 → its ghost (with name tag) moves in tab 2, and vice-versa.
- [ ] Close one tab → the other drops that ghost after ~6 s.
- [ ] Optional: `python3 serve.py --room demo`, open `…/?room=demo` in one tab and `…/?room=other` in another → they should **not** see each other.

### E. Reaching a real audience
- [ ] Phone on the same Wi-Fi/hotspot → open `http://<LAN-IP>:8000` (serve.py prints it). If macOS asks to allow incoming connections for "Python", click **Allow**.
- [ ] If that fails while the phone has internet, the venue Wi-Fi is isolating clients → use a tunnel: `brew install cloudflared` then `cloudflared tunnel --url http://localhost:8000`, and put the printed `https://…trycloudflare.com` URL in the QR. (Full guidance: `README.md` → *Serve it for an audience (multiplayer)*.)

---

## Known limitations & gotchas
- **Embeds want a server.** YouTube/Vimeo may refuse to play from `file://` (referrer is null). Use `serve.py` or `python3 -m http.server`.
- **The relay is an open, unauthenticated room.** Run it only during the talk; prefer an obscure tunnel URL or a `--room` code if exposing publicly; **Ctrl-C** when done. It validates, clamps, and size-caps everything clients send, and remote names are drawn as canvas text (no HTML injection).
- **iPhone hotspot** caps ~5–10 devices and routes attendees' background traffic over your cellular plan.
- **Plain HTTP is not a "secure context."** `fetch`/relay work fine, but camera/mic/geolocation would be gated — the game needs none of those.
- **`crypto.randomUUID`** may be absent on non-HTTPS origins; the code falls back to a random id automatically.

## Rollback
This project **is** now a git repo with a GitHub remote and tagged checkpoints
(`v1.0`, `v1.1`, `v1.2` — see the 2026-06-07 section above). Revert a single change
with `git revert <hash>`, or return to a known-good build with `git checkout v1.2`.
(The old pre-git folder backup `../Presentation_backup_20260602-132532/` predates
all of this and is safe to delete.)
