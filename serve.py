#!/usr/bin/env python3
"""Serve the Walkable Presentation locally AND relay ghost positions (multiplayer).

Pure standard library — no pip, no Node, no build. ONE process both serves the
static files (index.html, game.js, slides/, tools/qr.html, …) and runs a tiny
position relay so visitors see each other's ghosts move around the room.

Single-player still needs nothing at all (double-click index.html, file://).
Multiplayer just *adds* shared positions on top, and only switches on when the
page is opened from this server.

    python3 serve.py                      # http://localhost:8000  (+ your LAN URL)
    python3 serve.py --port 8000 --host 0.0.0.0
    python3 serve.py --room demo          # optional room code (goes in the QR link)

The relay (same origin, plain HTTP — fine on a LAN/hotspot, no HTTPS required):
    GET  /net/info               -> {"multiplayer": true, "now": <ms>}     (probe)
    POST /net/sync  {id,name,…}  -> {"now": <ms>, "players": [ …others… ]}

Reachability for attendees (LAN IP / iPhone hotspot / Cloudflare tunnel) is
covered in README.md → "Serve it for an audience (multiplayer)". Ctrl-C to stop.
"""
import argparse
import json
import os
import socket
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, quote

ROOT = os.path.dirname(os.path.abspath(__file__))   # serve this project, whatever the cwd

PLAYER_TTL = 6.0     # seconds: drop a ghost we haven't heard from in this long
MAX_PLAYERS = 80     # per room — a sane cap so one room can't grow without bound
MAX_BODY = 4096      # bytes: reject larger POST bodies outright
NAME_MAX = 24        # characters of a visitor name we keep

_lock = threading.Lock()
_rooms = {}          # rooms[name][id] = {name, sheet, x, y, fx, fy, t}


def _now_ms():
    return int(time.time() * 1000)


def _clampf(v, lo, hi, default=0.0):
    """Coerce v to a float within [lo, hi]; default for junk/NaN (don't trust clients)."""
    try:
        v = float(v)
    except (TypeError, ValueError):
        return default
    if v != v:                       # NaN
        return default
    return lo if v < lo else hi if v > hi else v


def _clean_name(s):
    s = "".join(ch for ch in str(s or "") if ch.isprintable())[:NAME_MAX].strip()
    return s or "Ghost"


def _sync(payload):
    """Apply one player's update and return the list of *other* players in its room."""
    now = time.time()
    pid = str(payload.get("id", ""))[:64]
    if not pid:
        return []
    roomname = (str(payload.get("room", "main"))[:40] or "main")
    rec = {
        "name": _clean_name(payload.get("name")),
        "sheet": int(_clampf(payload.get("sheet"), 0, 999, 0)),
        "x": _clampf(payload.get("x"), -2, 200),
        "y": _clampf(payload.get("y"), -2, 200),
        "fx": _clampf(payload.get("fx"), -1, 1),
        "fy": _clampf(payload.get("fy"), -1, 1),
        "t": now,
    }
    with _lock:
        room = _rooms.setdefault(roomname, {})
        for dead in [k for k, p in room.items() if now - p["t"] > PLAYER_TTL]:
            del room[dead]                       # prune the departed
        if pid in room or len(room) < MAX_PLAYERS:
            room[pid] = rec
        others = [(k, dict(p)) for k, p in room.items() if k != pid]
    return [{"id": k, "name": p["name"], "sheet": p["sheet"],
             "x": round(p["x"], 3), "y": round(p["y"], 3),
             "fx": round(p["fx"], 3), "fy": round(p["fy"], 3),
             "age": int((now - p["t"]) * 1000)} for k, p in others]


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def log_message(self, fmt, *args):
        if self.path.startswith("/net/"):        # don't spam the console with polling
            return
        super().log_message(fmt, *args)

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_OPTIONS(self):                         # CORS preflight (only if served cross-origin)
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if urlparse(self.path).path == "/net/info":
            self._json({"multiplayer": True, "now": _now_ms()})
            return
        super().do_GET()                          # everything else = a static file

    def do_POST(self):
        if urlparse(self.path).path != "/net/sync":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
        except (TypeError, ValueError):
            length = 0
        if length <= 0 or length > MAX_BODY:
            self._json({"error": "bad-length"}, 400)
            return
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError
        except (ValueError, UnicodeDecodeError):
            self._json({"error": "bad-json"}, 400)
            return
        self._json({"now": _now_ms(), "players": _sync(payload)})


def lan_ip():
    """Best-guess LAN IP (the source IP for the default route); 127.0.0.1 if offline."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))                # UDP 'connect' sends nothing; just picks a route
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def main():
    ap = argparse.ArgumentParser(description="Serve the game + multiplayer ghost relay.")
    ap.add_argument("--host", default="0.0.0.0", help="bind address (0.0.0.0 = reachable on your LAN / a PaaS)")
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")),
                    help="listen port; defaults to $PORT when set (Render/Heroku/etc.), else 8000")
    ap.add_argument("--room", default="", help="optional room code; advertised in the printed QR link")
    args = ap.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    room_q = ("?room=" + quote(args.room)) if args.room else ""
    render_url = os.environ.get("RENDER_EXTERNAL_URL", "").rstrip("/")
    if render_url:                                   # on Render: one public HTTPS origin, no LAN IP
        public = f"{render_url}/{room_q}"
        qr_link = f"{render_url}/tools/qr.html?url={quote(public, safe='')}"
        print("\n  Walkable Presentation — serving with multiplayer (Render)")
        print("  ---------------------------------------------------------")
        print(f"  Public URL  : {public}")
        print(f"  Make a QR   : {qr_link}")
        if args.room:
            print(f"  Room code   : {args.room}")
        print("  Put that QR on a slide so people can scan to join.\n")
    else:                                            # local: localhost + best-guess LAN IP
        ip = lan_ip()
        lan_url = f"http://{ip}:{args.port}/{room_q}"
        qr_link = f"http://{ip}:{args.port}/tools/qr.html?url={quote(lan_url, safe='')}"
        print("\n  Walkable Presentation — serving with multiplayer")
        print("  ------------------------------------------------")
        print(f"  On this Mac : http://localhost:{args.port}/{room_q}")
        print(f"  Attendees   : {lan_url}")
        if args.room:
            print(f"  Room code   : {args.room}")
        print(f"  Make a QR   : {qr_link}")
        print("  Put that QR on a slide so people can scan to join. Ctrl-C to stop.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
