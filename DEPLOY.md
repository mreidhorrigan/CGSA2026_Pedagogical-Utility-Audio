# DEPLOY.md — putting the multiplayer poster on Render

This deploys the **existing Python server** (`serve.py`) to [Render](https://render.com)
so attendees can scan a QR code and walk the room **together** over the public
internet — no shared Wi-Fi, no tunnel, no app install.

## Why Python (and not Node)

The multiplayer relay is already written: `serve.py` is a stdlib-only Python
server that serves the static game **and** relays ghost positions on one origin.
The in-game client (`game.js` §3b NET) just POSTs to `/net/sync` on
`location.origin`, so it works unchanged on any `http(s)` host — including
Render's HTTPS URL. Render runs Python natively, so there is **nothing to install
and nothing to rewrite** — and this respects the project's "no Node / build-free"
rule (see `CLAUDE.md`). The only code change deployment needed was teaching
`serve.py` to bind Render's injected `$PORT` (it already binds `0.0.0.0`).

## What was added for deploy

| File | Purpose |
|------|---------|
| `render.yaml` | Blueprint: one free Python web service, start `python serve.py`, health-check `/net/info`. |
| `requirements.txt` | Empty (comment-only) — makes Render detect a Python service. No real deps. |
| `serve.py` (edit) | `--port` now defaults to `$PORT` when set; logs the public URL via `$RENDER_EXTERNAL_URL`. |
| `.gitignore` | Keeps session transcripts, `.claude/`, `.DS_Store` out of the repo. |

## Deploy in ~2 minutes (Blueprint)

1. Push this repo to GitHub (already done if you're reading this there).
2. In the [Render dashboard](https://dashboard.render.com): **New +** → **Blueprint**.
3. Connect the repo **`mreidhorrigan/CGSA2026_Pedagogical-Utility-Audio`** → Render
   reads `render.yaml` → **Apply**.
4. Wait for the first deploy (cold builds take a couple minutes). When it's live
   you get a URL like `https://cgsa2026-audio-presentation.onrender.com`.
5. Open it. Two browser tabs should each show the name field and read
   **👻 2 in the room** after Start. That's multiplayer working.

**Manual alternative (no Blueprint):** New + → **Web Service** → connect the repo →
Runtime **Python 3**, Build `pip install -r requirements.txt`, Start
`python serve.py`, Health check path `/net/info`, Plan **Free** → Create.

## Make the join QR

Open `https://<your-service>.onrender.com/tools/qr.html` and paste the service
URL (the running server also prints a ready-made QR link in the Render logs). Put
that QR on a slide. Optional room code: append `?room=cgsa2026` to the URL so your
talk has its own room (`https://…onrender.com/?room=cgsa2026`).

## Important caveats for a live talk

- **Free tier sleeps after ~15 min idle**, and the next request pays a ~50 s cold
  start. **Open the URL yourself a minute or two before you present** to wake it.
  To remove the spin-down entirely, bump the service to Render's **Starter** plan
  (~$7/mo) for the day of the talk, then drop back to Free.
- **Keep it to ONE instance.** The relay holds room state in memory, so two
  instances wouldn't see each other's ghosts. Free/Starter are single-instance by
  default — just don't enable autoscaling/extra instances.
- **The room is open and unauthenticated** (by design — it's a poster). A room
  code obscures it; the server still validates, clamps and caps everything clients
  send, and remote names are drawn as canvas text (no HTML injection). Fine for a
  conference; don't leave it as your only line of defense for anything sensitive.
- **Region = latency.** `render.yaml` uses `oregon`; switch to the region nearest
  your venue (e.g. `frankfurt`, `singapore`) for snappier ghost movement.

## Capacity and instances (can 10-20 people join?)

**Short answer: yes.** One server comfortably hosts a roomful — you do not need to
"scale up" for 10–20 people, and in fact you specifically should not.

Two things people mix up:

- **Instance** = one running *copy of the server* (`serve.py`). You are running **one**.
- **Player** = one *person* who connected. A single instance serves **many** players.

They're independent — one instance holds many players at once. The relay is built
for up to **80 players per room** (`MAX_PLAYERS` in `serve.py`), so 10–20 is well
within range. Everyone who opens the URL (same `?room=`, or no room = the default
`main`) lands in the **same** room and sees each other.

**Why keep it to exactly one instance:** the list of who's in the room and where
each ghost is lives in that instance's **memory**. If Render ran two instances,
your visitors would be split between them at random, and people on copy A would not
see people on copy B — each copy only remembers its own crowd. For *shared*
multiplayer everyone must hit the **same** instance, so leave the instance count at
1. (Free and Starter are single-instance by default — just don't turn on extra
instances / autoscaling.)

**Will the free tier keep up with 20?** The *software* is fine to 80; the only
question is the free plan's small CPU share (0.1 CPU). Each player pings the relay
about **8×/second**, so 20 players ≈ ~160 tiny requests/second. Around 10 people is
comfortable on **Free**; pushing toward 20 the free CPU can get busy and ghosts may
glide a little less smoothly (it won't break or disconnect anyone). **For a live
talk expecting ~20, run on Render Starter (~$7/mo) for the day** — more CPU and no
spin-down — then drop back to Free afterward. (If you ever needed to lighten the
load without paying, raising `NET_SYNC_MS` in `game.js` from 120 to ~200 ms cuts
the request rate by ~40%, at the cost of slightly steppier ghost motion.)

## Test it locally exactly as Render runs it

```bash
PORT=8077 python3 serve.py          # binds the env port, just like Render
curl -s http://localhost:8077/net/info     # -> {"multiplayer": true, ...}
```

Single-player from `file://` (double-click `index.html`) is completely unaffected
by any of this.
