from __future__ import annotations

import base64
import json
import struct
import zlib

from .common import config

LOGIC = {"and_any": 0, "not_all": 1, "not_any": 2, "and_all": 3}


def wi_entry(uid: int, entry: dict) -> dict:
    """entry: {title, keys, keys2, logic, content, constant, order, comment_extra}."""
    d = config("world-info-defaults")["entry_defaults"]
    constant = bool(entry.get("constant"))
    return {
        "uid": uid,
        "key": [k for k in entry.get("keys", []) if k.strip()],
        "keysecondary": [k for k in entry.get("keys2", []) if k.strip()],
        "comment": entry["title"],
        "content": entry["content"].strip(),
        "constant": constant,
        "vectorized": False,
        "selective": bool(d["selective"]),
        "selectiveLogic": LOGIC[entry.get("logic") or "and_any"],
        "addMemo": True,
        "order": int(entry.get("order", 100)),
        "position": int(d["position"]),
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": bool(d["exclude_recursion"]),
        "preventRecursion": bool(d["prevent_recursion"]),
        "delayUntilRecursion": False,
        "probability": int(d["probability"]),
        "useProbability": True,
        "depth": int(d["depth"]),
        "group": entry.get("group", ""),
        "groupOverride": False,
        "groupWeight": 100,
        "scanDepth": None,
        "caseSensitive": bool(d["case_sensitive"]),
        "matchWholeWords": bool(d["match_whole_words"]),
        "useGroupScoring": None,
        "automationId": "",
        "role": None,
        "sticky": 0,
        "cooldown": 0,
        "delay": 0,
        "displayIndex": uid,
    }


def world_book(entries: list) -> dict:
    return {"entries": {str(i): wi_entry(i, e) for i, e in enumerate(entries)}}


def embedded_book(name: str, entries: list) -> dict:
    out = []
    for i, e in enumerate(entries):
        out.append({
            "id": i, "keys": e.get("keys", []), "secondary_keys": e.get("keys2", []),
            "comment": e["title"], "name": e["title"], "content": e["content"].strip(),
            "constant": bool(e.get("constant")), "selective": True,
            "insertion_order": int(e.get("order", 100)), "enabled": True, "position": "before_char",
            "case_sensitive": False, "priority": 10,
            "extensions": {"position": 0, "depth": 4, "probability": 100, "useProbability": True,
                           "prevent_recursion": True, "exclude_recursion": False, "display_index": i,
                           "selectiveLogic": LOGIC[e.get("logic") or "and_any"], "group": "",
                           "match_whole_words": True, "case_sensitive": False},
        })
    return {"name": name, "entries": out}


def character_card(name, fields: dict, tags, creator_notes, version, world_name="", book_entries=None) -> dict:
    data = {
        "name": name,
        "description": fields["description"],
        "personality": fields.get("personality", ""),
        "scenario": fields.get("scenario", ""),
        "first_mes": fields.get("first_mes", ""),
        "mes_example": fields.get("mes_example", ""),
        "creator_notes": creator_notes,
        "system_prompt": "",
        "post_history_instructions": fields.get("post_history_instructions", ""),
        "alternate_greetings": fields.get("alternate_greetings", []),
        "tags": tags,
        "creator": "Teyvat Archive contributors",
        "character_version": version,
        "extensions": {"talkativeness": "0.5", "fav": False, "world": world_name,
                       "depth_prompt": {"prompt": "", "depth": 4, "role": "system"}},
    }
    if book_entries:
        data["character_book"] = embedded_book(world_name, book_entries)
    card = {"spec": "chara_card_v2", "spec_version": "2.0", "data": data}
    for k in ("name", "description", "personality", "scenario", "first_mes", "mes_example"):
        card[k] = data[k]
    card["tags"] = tags
    return card


def check_card(card: dict) -> list:
    errs = []
    if card.get("spec") != "chara_card_v2" or card.get("spec_version") != "2.0":
        errs.append("spec/spec_version must be chara_card_v2 / 2.0")
    d = card.get("data")
    if not isinstance(d, dict):
        return errs + ["missing data object"]
    for k in ("name", "description", "personality", "scenario", "first_mes", "mes_example", "creator_notes",
              "system_prompt", "post_history_instructions", "creator", "character_version"):
        if not isinstance(d.get(k), str):
            errs.append(f"data.{k} must be a string")
    if not d.get("name", "").strip():
        errs.append("data.name is empty")
    if not d.get("first_mes", "").strip():
        errs.append("data.first_mes is empty")
    if d.get("mes_example") and "<START>" not in d["mes_example"]:
        errs.append("data.mes_example should separate examples with <START>")
    for k in ("alternate_greetings", "tags"):
        if not isinstance(d.get(k), list) or not all(isinstance(x, str) for x in d.get(k, [])):
            errs.append(f"data.{k} must be a list of strings")
    if not isinstance(d.get("extensions"), dict):
        errs.append("data.extensions must be an object")
    book = d.get("character_book")
    if book is not None:
        if not isinstance(book.get("entries"), list):
            errs.append("character_book.entries must be a list")
        else:
            ids = [e.get("id") for e in book["entries"]]
            if len(ids) != len(set(ids)):
                errs.append("character_book entry ids are not unique")
            for e in book["entries"]:
                if not isinstance(e.get("keys"), list) or not isinstance(e.get("content"), str):
                    errs.append(f"character_book entry {e.get('id')} needs keys[] and content")
                elif not e["keys"] and not e.get("constant"):
                    errs.append(f"character_book entry '{e.get('comment')}' has no keys and is not constant")
    try:
        json.dumps(card, ensure_ascii=False)
    except Exception as ex:
        errs.append(f"not serialisable: {ex}")
    return errs


REQUIRED_WI = {"uid": int, "key": list, "keysecondary": list, "comment": str, "content": str, "constant": bool,
               "selective": bool, "selectiveLogic": int, "order": int, "position": int, "disable": bool,
               "probability": int, "useProbability": bool, "depth": int, "displayIndex": int}


def check_world(book: dict) -> list:
    errs = []
    if not isinstance(book.get("entries"), dict):
        return ["top level must be {\"entries\": {...}}"]
    for k, e in book["entries"].items():
        for field, typ in REQUIRED_WI.items():
            if not isinstance(e.get(field), typ) or (typ is int and isinstance(e.get(field), bool)):
                errs.append(f"entry {k}: '{field}' must be {typ.__name__}")
        if str(e.get("uid")) != k:
            errs.append(f"entry {k}: uid does not match its key")
        if not e.get("constant") and not e.get("key"):
            errs.append(f"entry {k} '{e.get('comment')}': no activation keys and not constant")
        if not str(e.get("content", "")).strip():
            errs.append(f"entry {k} '{e.get('comment')}': empty content")
    return errs


def _chunk(typ, body):
    return struct.pack(">I", len(body)) + typ + body + struct.pack(">I", zlib.crc32(typ + body) & 0xFFFFFFFF)


def placeholder_png(seed: str, size=256) -> bytes:
    h = zlib.crc32(seed.encode("utf-8"))
    r, g, b = (h & 255) // 2 + 64, ((h >> 8) & 255) // 2 + 64, ((h >> 16) & 255) // 2 + 64
    rows = b"".join(b"\0" + bytes([int(r * (1 - y / (size * 1.6))), int(g * (1 - y / (size * 1.6))),
                                   int(b * (1 - y / (size * 1.6)))]) * size for y in range(size))
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", zlib.compress(rows, 9)) + _chunk(b"IEND", b"")


def png_card(card: dict, seed: str) -> bytes:
    png = placeholder_png(seed)
    text = b"chara\0" + base64.b64encode(json.dumps(card, ensure_ascii=False).encode("utf-8"))
    iend = png.rfind(b"\0\0\0\0IEND")
    return png[:iend] + _chunk(b"tEXt", text) + png[iend:]
