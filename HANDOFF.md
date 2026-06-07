# HANDOFF — QR codes · embedded video · multiplayer

**Date:** 2026-06-02 · **Scope:** three additive extensions to the Walkable
Presentation. All build-free (no npm/Node, Python 3.11 only). **Single-player
still runs from `file://` exactly as before** — every new capability degrades
gracefully when its server/tooling isn't present.

This doc is for **handoff** (what changed, how to run) and **testing** (a copy-
paste verification script + a manual checklist for the things only a human can
confirm). User guide = `README.md`; architecture/contributor guide = `CLAUDE.md`.

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
A complete pre-change backup is the sibling folder
`../Presentation_backup_20260602-132532/`. This project is **not** a git repo, so
to revert a file just copy it back from there. (Safe to delete the backup once
you're happy.)
