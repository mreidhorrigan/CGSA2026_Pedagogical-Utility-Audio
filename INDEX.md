# 📍 INDEX — start here

Navigation hub for the **CGSA2026 walkable poster** (an in-browser isometric room
where visitors walk around as ghosts and view slides at kiosks — together, in
multiplayer). Pick what you want to do.

## ▶︎ Play it now (live, multiplayer)

**https://cgsa2026-audio-presentation.onrender.com**

Open it in two browser tabs (or send it to a friend) and you'll see each other's
ghosts move. First load after a quiet spell takes ~50 s to wake the free server —
see [DEPLOY.md](DEPLOY.md). Offline single-player: just double-click `index.html`.

## 🗺️ I want to…

| Goal | Go to |
|------|-------|
| **Play / demo it** | the live URL above · or `index.html` (offline, solo) |
| **Deploy / redeploy to Render** | **[DEPLOY.md](DEPLOY.md)** |
| **Know if N people can join** | [DEPLOY.md → Capacity](DEPLOY.md#capacity-and-instances-can-10-20-people-join) |
| **Run multiplayer on my own laptop/LAN** | [README.md → Serve it for an audience](README.md#serve-it-for-an-audience-multiplayer) · `python3 serve.py` |
| **Add / change slides** | [README.md → Slides](README.md#slides--where-they-come-from) · or [SLIDES_SYSTEM](SLIDES_SYSTEM/README.md) for Markdown decks |
| **Make a join QR for a slide** | `tools/qr.html` (or the prefilled link `serve.py` prints) |
| **Understand / edit the code** | **[CLAUDE.md](CLAUDE.md)** — architecture + "how do I…" recipes |
| **See what changed & how to test** | [HANDOFF.md](HANDOFF.md) (QR/embed/multiplayer) · [SLIDES_SYSTEM/HANDOFF.md](SLIDES_SYSTEM/HANDOFF.md) |

## 📚 Every doc, one line each

- **[README.md](README.md)** — the user guide: run it, controls, slides, multiplayer, the ghost avatar, sound.
- **[DEPLOY.md](DEPLOY.md)** — put multiplayer on Render: Blueprint steps, join QR, capacity, talk-day caveats.
- **[CLAUDE.md](CLAUDE.md)** — contributor/AI guide: section-by-section `game.js` map, extension recipes, how to verify without a browser.
- **[HANDOFF.md](HANDOFF.md)** — the QR / embedded-video / multiplayer changes + a copy-paste verification script and manual checklist.
- **[SLIDES_SYSTEM/README.md](SLIDES_SYSTEM/README.md)** — compile Markdown into self-contained kiosk slides (`md2deck.py`).
- **[SLIDES_SYSTEM/HANDOFF.md](SLIDES_SYSTEM/HANDOFF.md)** · **[RESEARCH.md](SLIDES_SYSTEM/RESEARCH.md)** — slides-system handoff + background.

## 🗂️ File map (the essentials)

```
index.html        the page + overlays + styling
game.js           the game (vanilla, type-checked) — CONFIG block at the top
slides.js         GENERATED slide manifest (window.SLIDES_MANIFEST)
serve.py          the server: static files + multiplayer ghost relay (Python, no Node)
render.yaml       Render Blueprint (one free Python web service)
requirements.txt  empty — just tells Render "this is Python"
build_slides.py   slides/  -> slides.js
import_images.py  images/  -> slides/ -> slides.js
tools/qr.html     make a scannable join-QR
SLIDES_SYSTEM/    Markdown-deck compiler (optional, separate pipeline)
```

## 🔑 Key facts

- **Live URL:** https://cgsa2026-audio-presentation.onrender.com
- **Repo:** github.com/mreidhorrigan/CGSA2026_Pedagogical-Utility-Audio — push to `main` → Render **auto-redeploys**.
- **Server:** Python `serve.py` (no Node). **Keep it ONE instance.** Free tier sleeps after ~15 min idle.
- **Capacity:** built for up to **80 players per room**; 10–20 is comfortable. For ~20 in a live talk, use Render **Starter** for the day — details in [DEPLOY.md](DEPLOY.md#capacity-and-instances-can-10-20-people-join).
