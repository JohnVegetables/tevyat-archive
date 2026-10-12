#!/usr/bin/env python3
import base64
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlencode, urlparse
from urllib.request import Request, urlopen

import _cli
from archive_lib.common import DATA, ST_OUT, cutoff_version, load_json
from archive_lib.art import ART, IMAGE_EXT, all_character_art, character_dir, find_image, needs_png_copy, save_png_copy, slug_for
from archive_lib.installer import available_bundles, check_st, default_greeting, existing_cards, install, load_bundle

UI = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)) / "importer_ui" / "index.html"
CONFIG = Path.home() / ".teyvat-archive" / "importer.json"
APP_VERSION = "1.0.0"
REPO = "JohnVegetables/teyvat-archive"
IDLE_LIMIT = 15 * 60
DEFAULTS = {"st": "", "user": "default-user", "tier": "STANDARD", "cards": None, "books": None,
            "greetings": {}, "keep_default": True, "activate": True, "backup": True}
TYPE_LABELS = {"character": "Playable", "npc": "NPC", "historical_figure": "Historical"}
TIER_INFO = {
    "LITE": "Short and lean. For small models or 4k–8k context.",
    "STANDARD": "The sweet spot. Rich characters that fit 8k–16k context.",
    "LARGE": "Deep lore and history. Best with 32k context.",
    "ULTRA": "Everything we have. For 32k+ context and big models.",
}
LAST_PING = [time.time()]
_update: dict = {}
WIKI_API = "https://genshin-impact.fandom.com/api.php"
UA = {"User-Agent": "TeyvatArchiveImporter/1.0 (local desktop app)"}
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_wiki_cache: dict = {}
_bundles: dict = {}


def load_config():
    try:
        return {**DEFAULTS, **json.loads(CONFIG.read_text(encoding="utf-8"))}
    except (OSError, ValueError):
        return dict(DEFAULTS)


def save_config(cfg):
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    CONFIG.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")


def bundle(tier):
    if tier not in _bundles:
        _bundles[tier] = load_bundle(tier)
    return _bundles[tier]


def port_open(port):
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=0.3):
            return True
    except OSError:
        return False


def bundle_view(tier):
    man = bundle(tier)
    idx = load_json(DATA / "indexes" / "character-index.json")["characters"]
    cards, art = [], all_character_art()
    for c in man["cards"]:
        slug = slug_for(c["id"])
        info = idx.get(c["id"], {})
        f = info.get("facts") or {}
        el = f.get("element") or f.get("vision")
        el = el if el in ("Anemo", "Geo", "Electro", "Dendro", "Hydro", "Pyro", "Cryo") else None
        cards.append({"id": c["id"], "name": c["name"], "kind": TYPE_LABELS.get(info.get("type"), "Other"),
                      "nation": (info.get("nation") or "").replace("location.", "").replace("-", " ").title().replace("Khaenriah", "Khaenri'ah") or None,
                      "element": el, "title": f.get("title"), "rarity": f.get("rarity"),
                      "tokens": man["entities"].get(c["id"], {}).get("tokens"), "slug": slug,
                      "art": art_url(art.get(slug))})
    books = [{"book": b["book"], "label": b["book"].replace("Teyvat Archive - ", ""), "topic": b["topic"],
              "entries": b["entries"], "tokens": b["tokens"]} for b in man["shared_books"]]
    return {"tier": tier, "cards": cards, "books": books, "totals": man.get("totals", {})}


def art_url(path):
    if not path:
        return None
    return "/art/" + quote(path.relative_to(ART).as_posix()) + f"?v={int(path.stat().st_mtime)}"


def wiki(params):
    url = WIKI_API + "?" + urlencode({**params, "format": "json", "formatversion": 2})
    with urlopen(Request(url, headers=UA), timeout=25) as r:
        return json.load(r)


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def wiki_images(query, gallery=True):
    """Pictures from the Genshin Impact wiki: the character's gallery pages, or a free file search."""
    key = (query, gallery)
    if key in _wiki_cache:
        return _wiki_cache[key]
    found = {}

    def add(pages, must=None):
        for p in pages:
            ii = (p.get("imageinfo") or [{}])[0]
            t = p.get("title", "")
            if Path(t).suffix.lower() not in IMAGE_EXT or ii.get("width", 0) < 180:
                continue
            if must and must not in _norm(t):
                continue
            found.setdefault(t, {"title": t[5:].rsplit(".", 1)[0], "thumb": ii.get("thumburl") or ii.get("url"),
                                 "url": ii.get("url"), "w": ii.get("width"), "h": ii.get("height")})

    info = {"prop": "imageinfo", "iiprop": "url|size", "iiurlwidth": 300}
    if gallery:
        must = _norm(query.split("'")[0])[:12]
        for title in (f"{query}/Gallery", query):
            cont = {}
            for _ in range(5):
                d = wiki({"action": "query", "generator": "images", "titles": title, "gimlimit": "max", **info, **cont})
                add(d.get("query", {}).get("pages", []), must)
                if "continue" not in d:
                    break
                cont = d["continue"]
    else:
        d = wiki({"action": "query", "generator": "search", "gsrsearch": query, "gsrnamespace": 6, "gsrlimit": 50, **info})
        add(d.get("query", {}).get("pages", []))
    out = sorted(found.values(), key=lambda x: ((x["h"] or 0) < 1.2 * (x["w"] or 1), x["title"]))
    _wiki_cache[key] = out
    return out


def fetch_image(url):
    if not url.startswith(("http://", "https://")):
        raise ValueError("only web addresses can be fetched")
    headers = dict(UA)
    if urlparse(url).hostname in ("static.wikia.nocookie.net", "vignette.wikia.nocookie.net"):
        headers["Referer"] = "https://genshin-impact.fandom.com/"
    try:
        with urlopen(Request(url, headers=headers), timeout=25) as r:
            ctype = r.headers.get("Content-Type", "")
            data = r.read(25_000_001)
    except Exception:
        curl = shutil.which("curl")
        if not curl:
            raise

        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "img"
            args = [curl, "-sL", "--max-filesize", "25000000", "-A", "Mozilla/5.0", "-w", "%{content_type}", "-o", str(dest)]
            if sys.platform == "win32":
                args.append("--ssl-no-revoke")
            if "Referer" in headers:
                args += ["-e", headers["Referer"]]
            out = subprocess.run(args + [url], capture_output=True, text=True, timeout=40)
            if out.returncode or not dest.exists():
                raise ValueError("couldn't download that picture")
            ctype, data = out.stdout.strip(), dest.read_bytes()
    if not ctype.startswith("image/") or len(data) > 25_000_000:
        raise ValueError("that link is not an image (or is larger than 25 MB)")
    return data, ctype.split(";")[0]


def save_art(slug, png_b64):
    if not SLUG.match(slug):
        raise ValueError("bad character id")
    data = base64.b64decode(png_b64.split(",", 1)[-1])
    if not data.startswith(b"\x89PNG"):
        raise ValueError("expected a PNG")
    d = character_dir(slug)
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"portrait-{time.strftime('%Y%m%d-%H%M%S')}.png"
    path.write_bytes(data)
    return art_url(path)


def remove_art(slug):
    if not SLUG.match(slug):
        raise ValueError("bad character id")
    img = find_image(slug)
    if img:
        img.rename(img.with_name(img.name + ".removed"))
    return art_url(find_image(slug))


def open_folder(slug=None):
    d = character_dir(slug) if slug and SLUG.match(slug) else ART
    d.mkdir(parents=True, exist_ok=True)
    if hasattr(os, "startfile"):
        os.startfile(d)
    else:
        subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", str(d)])


def _version_key(v):
    return tuple(int(x) for x in re.findall(r"\d+", v)[:3]) or (0,)


def check_update():
    if _update:
        return _update
    result = {"current": APP_VERSION, "latest": None, "url": f"https://github.com/{REPO}/releases", "newer": False}
    try:
        req = Request(f"https://api.github.com/repos/{REPO}/releases/latest",
                      headers={**UA, "Accept": "application/vnd.github+json"})
        with urlopen(req, timeout=8) as r:
            rel = json.load(r)
        latest = rel.get("tag_name", "").lstrip("vV")
        result.update(latest=latest, url=rel.get("html_url") or result["url"],
                      newer=bool(latest) and _version_key(latest) > _version_key(APP_VERSION))
    except Exception:
        pass
    _update.update(result)
    return result


def pick_folder(out_file):
    import tkinter
    from tkinter import filedialog
    root = tkinter.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    Path(out_file).write_text(filedialog.askdirectory(title="Choose your SillyTavern folder") or "", encoding="utf-8")


def browse_folder():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "folder.txt"
        cmd = [sys.executable] if getattr(sys, "frozen", False) else [sys.executable, str(Path(__file__).resolve())]
        subprocess.run(cmd + ["--pick-folder", str(out)])
        return out.read_text(encoding="utf-8").strip() if out.exists() else ""


def check(body):
    st, user = Path(body.get("st", "").strip()), (body.get("user") or "default-user").strip()
    if not body.get("st", "").strip():
        return {"ok": False, "error": "Choose your SillyTavern folder."}
    err = check_st(st, user)
    if err:
        return {"ok": False, "error": err}
    man = bundle(body["tier"])
    cards = [c for c in man["cards"] if c["id"] in set(body.get("cards", []))]
    return {"ok": True, "clash": existing_cards(st, user, cards), "running": port_open(8000),
            "profile_exists": (st / "data" / user).exists()}


def do_import(body):
    cfg = {**load_config(), **{k: body[k] for k in DEFAULTS if k in body}}
    save_config(cfg)
    log = []
    res = install(Path(cfg["st"]), cfg["user"], bundle(cfg["tier"]), set(cfg["cards"] or []), set(cfg["books"] or []),
                  cfg["greetings"], keep_default_greeting=cfg["keep_default"], backup=cfg["backup"],
                  activate_books=sorted(cfg["books"] or []) if cfg["activate"] and cfg["books"] else None,
                  log=log.append)
    return {"ok": True, **res, "log": log}


class Server(ThreadingHTTPServer):
    allow_reuse_address = False
    daemon_threads = True


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, obj, status=200, ctype="application/json"):
        data = obj if isinstance(obj, bytes) else json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        text = ctype.startswith("text/") or ctype == "application/json"
        self.send_header("Content-Type", ctype + ("; charset=utf-8" if text else ""))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path == "/":
                return self.send(UI.read_bytes(), ctype="text/html")
            if u.path == "/icon.png":
                return self.send((UI.parent / "icon.png").read_bytes(), ctype="image/png")
            if u.path == "/api/state":
                tiers = [{"id": t, "info": TIER_INFO.get(t, "Custom mix."),
                          "totals": load_json(ST_OUT / "manifests" / f"{t}.json").get("totals", {})}
                         for t in sorted(available_bundles(), key=lambda t: (list(TIER_INFO).index(t) if t in TIER_INFO else 9, t))]
                return self.send({"config": load_config(), "tiers": tiers, "cutoff": cutoff_version()})
            if u.path == "/api/update":
                return self.send(check_update())
            if u.path == "/api/bundle":
                return self.send(bundle_view(q["tier"]))
            if u.path.startswith("/art/"):
                p = (ART / unquote(u.path[5:])).resolve()
                if ART.resolve() in p.parents and p.is_file() and p.suffix.lower() in IMAGE_EXT:
                    ctype = {".png": "image/png", ".webp": "image/webp"}.get(p.suffix.lower(), "image/jpeg")
                    return self.send(p.read_bytes(), ctype=ctype)
                return self.send({"error": "not found"}, 404)
            if u.path == "/api/wiki":
                return self.send({"images": wiki_images(q.get("q", ""), q.get("mode", "gallery") == "gallery")})
            if u.path == "/api/proxy":
                data, ctype = fetch_image(q["url"])
                return self.send(data, ctype=ctype)
            if u.path == "/api/art/pending":
                return self.send({"pending": [{"slug": s, "url": art_url(find_image(s))}
                                              for s in all_character_art() if needs_png_copy(s)]})
            if u.path == "/api/greeting":
                card = next(c for c in bundle(q["tier"])["cards"] if c["id"] == q["id"])
                return self.send({"greeting": default_greeting(card)})
        except Exception as e:
            return self.send({"ok": False, "error": str(e)}, 500)
        self.send({"error": "not found"}, 404)

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(n) or b"{}")
        try:
            if self.path == "/api/ping":
                LAST_PING[0] = time.time()
                return self.send({"ok": True})
            if self.path == "/api/config":
                cfg = {**load_config(), **{k: body[k] for k in DEFAULTS if k in body}}
                save_config(cfg)
                return self.send({"ok": True})
            if self.path == "/api/browse":
                return self.send({"path": browse_folder()})
            if self.path == "/api/check":
                return self.send(check(body))
            if self.path == "/api/art/save":
                return self.send({"ok": True, "art": save_art(body["slug"], body["png"])})
            if self.path == "/api/art/remove":
                return self.send({"ok": True, "art": remove_art(body["slug"])})
            if self.path == "/api/art/cache":
                if not SLUG.match(body["slug"]):
                    raise ValueError("bad character id")
                save_png_copy(body["slug"], base64.b64decode(body["png"].split(",", 1)[-1]))
                return self.send({"ok": True})
            if self.path == "/api/art/open":
                open_folder(body.get("slug"))
                return self.send({"ok": True})
            if self.path == "/api/import":
                return self.send(do_import(body))
            if self.path == "/api/bye":
                LAST_PING[0] = time.time() - IDLE_LIMIT + 6
                return self.send({"ok": True})
            if self.path == "/api/quit":
                self.send({"ok": True})
                threading.Thread(target=self.server.shutdown, daemon=True).start()
                return
        except Exception as e:
            return self.send({"ok": False, "error": str(e)}, 500)
        self.send({"error": "not found"}, 404)


def open_window(url):
    for exe in (shutil.which("msedge"), r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                r"C:\Program Files\Microsoft\Edge\Application\msedge.exe", shutil.which("chrome"),
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        if exe and Path(exe).exists():
            profile = Path.home() / ".teyvat-archive" / "browser-profile"
            subprocess.Popen([exe, f"--app={url}", "--window-size=1280,860", f"--user-data-dir={profile}",
                              "--no-first-run", "--no-default-browser-check"])
            return
    webbrowser.open(url)


def watchdog(server):
    while True:
        time.sleep(3)
        if time.time() - LAST_PING[0] > IDLE_LIMIT:
            server.shutdown()
            return


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Teyvat Archive Importer")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--no-window", action="store_true", help="don't open a window (for testing)")
    ap.add_argument("--pick-folder", metavar="FILE", help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    if args.pick_folder:
        pick_folder(args.pick_folder)
        return 0
    if not available_bundles():
        print("No built bundles found. Run: python tools/build_bundles.py --tier all")
        return 1
    server = Server(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{server.server_address[1]}/"
    print(f"Teyvat Archive Importer running at {url} (close the window to quit)")
    LAST_PING[0] = time.time()
    threading.Thread(target=watchdog, args=(server,), daemon=True).start()
    if not args.no_window:
        open_window(url)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
