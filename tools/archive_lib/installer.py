from __future__ import annotations

import json
import shutil
import time
from pathlib import Path

from .common import ST_OUT, load_json, safe_filename
from .art import avatar_png, backgrounds, embed_card, slug_for
from .stexport import png_card

SETTINGS_KEYS = ("world_info_settings", "world_info", "globalSelect")


def available_bundles() -> list[str]:
    return sorted(p.stem for p in (ST_OUT / "manifests").glob("*.json"))


def load_bundle(label: str) -> dict:
    man = load_json(ST_OUT / "manifests" / f"{label}.json")
    card_books = {c.get("world") for c in man["cards"] if c.get("world")}
    man["shared_books"] = [b for b in man["world_info"] if b["book"] not in card_books]
    entity_books = {f"Teyvat Archive - {e['name']}" for e in man["entities"].values()}
    for b in man["shared_books"]:
        b["topic"] = b["book"] not in entity_books
    man["shared_books"].sort(key=lambda b: (not b["topic"], b["book"].lower()))
    man["books_by_name"] = {b["book"]: b for b in man["world_info"]}
    return man


def default_greeting(card_entry: dict) -> str:
    return json.loads((ST_OUT / card_entry["file"]).read_text(encoding="utf-8"))["data"]["first_mes"]


def check_st(st: Path, user: str) -> str | None:
    if not (st / "server.js").exists():
        return f"{st} does not look like a SillyTavern folder (no server.js)"
    return None


def existing_cards(st: Path, user: str, cards: list) -> list[str]:
    chars = st / "data" / user / "characters"
    return [c["name"] for c in cards if (chars / (safe_filename(c["name"]) + ".png")).exists()]


def apply_greeting(card: dict, greeting: str, keep_default: bool) -> dict:
    greeting = greeting.strip()
    if not greeting:
        return card
    data = card["data"]
    old = data.get("first_mes", "")
    alts = list(data.get("alternate_greetings") or [])
    if keep_default and old and old not in alts:
        alts.insert(0, old)
    data["first_mes"] = greeting
    data["alternate_greetings"] = alts
    card["first_mes"] = greeting
    return card


def install(st: Path, user: str, man: dict, card_ids: set, book_names: set, greetings: dict,
            keep_default_greeting=True, backup=True, activate_books: list | None = None, use_art=True,
            log=print) -> dict:
    """Copy the chosen cards (with their character books) and lorebooks. Returns counts."""
    udir = st / "data" / user
    worlds, chars = udir / "worlds", udir / "characters"
    worlds.mkdir(parents=True, exist_ok=True)
    chars.mkdir(parents=True, exist_ok=True)
    books = set(book_names)
    n_cards = n_art = 0
    for c in man["cards"]:
        if c["id"] not in card_ids:
            continue
        card = json.loads((ST_OUT / c["file"]).read_text(encoding="utf-8"))
        if greetings.get(c["id"], "").strip():
            card = apply_greeting(card, greetings[c["id"]], keep_default_greeting)
        dest = chars / (safe_filename(c["name"]) + ".png")
        if dest.exists() and backup:
            shutil.copy2(dest, dest.with_suffix(".png.bak"))
        art_png = avatar_png(slug_for(c["id"])) if use_art else None
        dest.write_bytes(embed_card(art_png, card) if art_png else png_card(card, c["id"]))
        if c.get("world"):
            books.add(c["world"])
        n_cards += 1
        n_art += bool(art_png)
        extras = [x for x, on in (("custom greeting", greetings.get(c["id"], "").strip()), ("your art", art_png)) if on]
        log(f"card   {c['name']}" + (f"  ({', '.join(extras)})" if extras else ""))
    n_books = 0
    for name in sorted(books):
        b = man["books_by_name"].get(name)
        if not b:
            continue
        src = ST_OUT / b["file"]
        shutil.copy2(src, worlds / src.name)
        n_books += 1
    log(f"{n_books} lorebooks copied")
    n_bg = 0
    if use_art:
        bgdir = udir / "backgrounds"
        for p in backgrounds():
            bgdir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, bgdir / p.name)
            n_bg += 1
        if n_bg:
            log(f"{n_bg} backgrounds copied")
    if activate_books:
        activate_global_books(udir, activate_books, log)
    return {"cards": n_cards, "books": n_books, "art": n_art, "backgrounds": n_bg}


def activate_global_books(udir: Path, names: list, log=print):
    p = udir / "settings.json"
    if not p.exists():
        log("settings.json not found (start SillyTavern once first); skipped activating lorebooks")
        return
    shutil.copy2(p, p.with_name(f"settings.json.before-teyvat-{time.strftime('%Y%m%d-%H%M%S')}.bak"))
    s = json.loads(p.read_text(encoding="utf-8"))
    wi = s.setdefault("world_info_settings", {}).setdefault("world_info", {})
    sel = wi.setdefault("globalSelect", [])
    added = [n for n in names if n not in sel]
    sel.extend(added)
    p.write_text(json.dumps(s, indent=4, ensure_ascii=False), encoding="utf-8")
    log(f"{len(added)} lorebooks switched on globally (settings.json backed up)")
