from __future__ import annotations

import fnmatch
import shutil
import zipfile
from pathlib import Path

from .common import BUNDLES, ROOT, ST_OUT, TIERS, config, cutoff_version, dump_json, load_json, rel, safe_filename
from .render import CARD_TYPES, book_for, card_fields, entity_keys, main_entry_text
from .stexport import character_card, world_book
from . import tokens

CARD_GROUP = {"character": "playable", "npc": "major-npcs", "historical_figure": "historical-figures"}


def tier_selection(compiled: dict, default_tier: str, mix: dict | None = None) -> dict:
    sel = {}
    for eid, by_tier in compiled.items():
        tier = (mix or {}).get("default", default_tier)
        rec = by_tier.get("LITE")
        for rule in (mix or {}).get("rules", []):
            m = rule["match"]
            if m.startswith("type:"):
                hit = rec and rec["entity_type"] == m[5:]
            elif m.startswith("nation:"):
                hit = rec and (rec["header"].get("nation") == m[7:] or eid == m[7:])
            else:
                hit = fnmatch.fnmatch(eid, m)
            if hit:
                tier = rule["tier"]
        if tier not in TIERS:
            raise ValueError(f"unknown tier {tier!r}")
        sel[eid] = tier
    return sel


def build(compiled: dict, selection: dict, label: str):
    """Return (cards: {relpath: card}, books: {name: [entries]}, manifest)."""
    from .registry import manifest_names
    names = manifest_names()
    names.update({eid: next(iter(v.values()))["name"] for eid, v in compiled.items()})
    cutoff = cutoff_version()
    wi = config("world-info-defaults")
    orders = wi["default_order"]
    books, cards = {}, {}
    manifest = {"bundle": label, "canon_cutoff": cutoff, "entities": {}, "cards": [], "world_info": [],
                "token_method": "heuristic", "totals": {}}

    for eid in sorted(selection):
        tier = selection[eid]
        rec = compiled[eid].get(tier)
        if rec is None:
            continue
        h = rec["header"]
        hw = h.get("wi") or {}
        t = rec["entity_type"]
        main_book = book_for(rec, names, "main")
        if not hw.get("exclude"):
            default_constant = t == "core"
            books.setdefault(main_book, []).append({
                "title": rec["name"], "keys": entity_keys(rec), "keys2": hw.get("keys2", []), "logic": hw.get("logic"),
                "content": main_entry_text(rec, names, cutoff),
                "constant": hw.get("constant", default_constant),
                "order": hw.get("order", orders["core"] if t == "core" else orders["index"] if t in CARD_TYPES else orders["main"]),
                "id": eid})
        own_book = book_for(rec, names, "own") if t in CARD_TYPES else main_book
        sub = []
        for x in rec["entries"]:
            a = x["attrs"]
            sub.append({"title": f"{rec['name']}: {x['title']}", "keys": a.get("keys") or [x["title"]],
                        "keys2": a.get("keys2", []), "logic": a.get("logic"), "content": x["text"],
                        "constant": a.get("constant", False), "order": a.get("order", orders["entry"]), "id": eid,
                        "book_override": a.get("book")})
        for s in sub:
            books.setdefault(a_book(s, rec, own_book), []).append(s)
        info = {"tier": tier, "type": t, "name": rec["name"], "source": rec["source_file"],
                "tokens": rec["stats"]["total_tokens"]}
        if t in CARD_TYPES and (h.get("facts") or {}).get("card", t != "historical_figure"):
            cf = card_fields(rec, names, cutoff)
            if cf["first_mes"].strip():
                tags = ["Genshin Impact", "Teyvat Archive", f"Tier {tier}"]
                f = h.get("facts") or {}
                for v in [names.get(h.get("nation")) if h.get("nation") else None, f.get("vision"), f.get("weapon")]:
                    if v and v not in tags:
                        tags.append(v)
                notes = (f"{rec['name']} - Teyvat Archive {tier} card, canon through Version {cutoff}. "
                         f"Entity id {eid}. Unofficial fan-made resource; Genshin Impact and its characters belong to "
                         f"HoYoverse. Sources and verification status: see the Teyvat Archive repository ({rec['source_file']}).")
                own_entries = [s for s in sub if a_book(s, rec, own_book) == own_book]
                card = character_card(rec["name"], cf, tags, notes, f"{cutoff}-{tier}",
                                      world_name=own_book if own_entries else "", book_entries=own_entries)
                card["data"]["extensions"]["teyvat_archive"] = {"id": eid, "tier": tier, "canon_cutoff": cutoff,
                                                                "status": h.get("status")}
                path = f"character-cards/{label}/{CARD_GROUP[t]}/{safe_filename(rec['name'])}.json"
                cards[path] = card
                info["card"] = path
                manifest["cards"].append({"id": eid, "name": rec["name"], "file": path, "tier": tier,
                                          "world": own_book if own_entries else None})
        manifest["entities"][eid] = info
    return cards, books, manifest


def a_book(entry, rec, default):
    return entry.get("book_override") or default


def write_exports(compiled: dict, selection: dict, label: str, only_world=False, zip_bundle=False):
    cards, books, manifest = build(compiled, selection, label)
    card_dir = ST_OUT / "character-cards" / label
    wi_dir = ST_OUT / "world-info" / label
    if not only_world and card_dir.exists():
        shutil.rmtree(card_dir)
    if wi_dir.exists():
        shutil.rmtree(wi_dir)
    if not only_world:
        for path, card in cards.items():
            dump_json(ST_OUT / path, card)
    total_entries = 0
    for name, entries in sorted(books.items()):
        fn = safe_filename(name) + ".json"
        dump_json(wi_dir / fn, world_book(entries))
        toks = sum(tokens.heuristic(e["content"]) for e in entries)
        manifest["world_info"].append({"book": name, "file": f"world-info/{label}/{fn}", "entries": len(entries),
                                       "constant_entries": sum(1 for e in entries if e.get("constant")),
                                       "tokens": toks})
        total_entries += len(entries)
    manifest["totals"] = {"entities": len(manifest["entities"]), "cards": len(manifest["cards"]),
                          "world_books": len(manifest["world_info"]), "world_info_entries": total_entries,
                          "world_info_tokens": sum(b["tokens"] for b in manifest["world_info"]),
                          "tiers": {t: sum(1 for v in manifest["entities"].values() if v["tier"] == t) for t in TIERS}}
    if not only_world:
        dump_json(ST_OUT / "manifests" / f"{label}.json", manifest)
    if zip_bundle:
        manifest["zip"] = zip_up(label, manifest)
    return manifest


def zip_up(label, manifest) -> str:
    BUNDLES.mkdir(exist_ok=True)
    out = BUNDLES / f"teyvat-archive-{label}-v{cutoff_version()}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for c in manifest["cards"]:
            z.write(ST_OUT / c["file"], f"characters/{Path(c['file']).relative_to(f'character-cards/{label}').as_posix()}")
        for b in manifest["world_info"]:
            z.write(ST_OUT / b["file"], f"worlds/{Path(b['file']).name}")
        for p in sorted((ST_OUT / "presets").glob("*")):
            if p.is_file():
                z.write(p, f"presets/{p.name}")
        z.write(ST_OUT / "manifests" / f"{label}.json", "manifest.json")
        readme = ROOT / "wiki" / "Manual-Install.md"
        if readme.exists():
            z.write(readme, "INSTALL.md")
        for name in ("LICENSE", "NOTICE"):
            if (ROOT / name).exists():
                z.write(ROOT / name, name)
    return rel(out)
