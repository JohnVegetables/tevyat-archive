from __future__ import annotations

import re

from .common import config

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
CARD_TYPES = ("character", "npc", "historical_figure")
DESCRIPTION_ORDER = ["summary", "appearance", "background", "relationships", "abilities", "status", "knowledge",
                     "roleplay", "speech", "mistakes", "chronology", "trivia"]
CARD_ONLY_FIELDS = {"personality", "scenario", "first_mes", "alternate_greetings", "mes_example", "post_history"}


def _labels():
    return config("tier-policy")["character_sections"]["labels"]


def label_for(field_name: str, cutoff: str) -> str:
    lab = _labels().get(field_name)
    if lab:
        return lab.replace("the canon cutoff", cutoff)
    return field_name.replace("_", " ").capitalize()


def _names(ids, names):
    return [names.get(i, i) for i in ids or []]


def birthday_text(mmdd):
    if not mmdd:
        return None
    m, d = mmdd.split("-")
    return f"{MONTHS[int(m) - 1]} {int(d)}"


def identity_line(rec, names) -> str:
    h, f = rec["header"], rec["header"].get("facts") or {}
    parts = []
    if f.get("full_name") and f["full_name"] != h["name"]:
        parts.append(f"Full name: {f['full_name']}")
    if h.get("aliases"):
        parts.append("Also known as: " + ", ".join(h["aliases"][:12]))
    if f.get("title"):
        parts.append(f"Title: {f['title']}")
    if f.get("species"):
        parts.append(f"Nature: {f['species']}")
    if f.get("pronouns"):
        parts.append(f"Pronouns: {f['pronouns']}")
    if f.get("origin") or h.get("nation"):
        parts.append(f"From: {names.get(f.get('origin') or h.get('nation'), f.get('origin') or h.get('nation'))}")
    if f.get("residence"):
        parts.append(f"Lives in: {names.get(f['residence'], f['residence'])}")
    if f.get("occupation"):
        parts.append(f"Occupation: {f['occupation']}")
    if f.get("affiliations"):
        parts.append("Affiliations: " + ", ".join(_names(f["affiliations"], names)))
    if f.get("vision"):
        parts.append(f"Vision / power source: {f['vision']}")
    if f.get("element") and f.get("element") != f.get("vision"):
        parts.append(f"Element: {f['element']}")
    if f.get("weapon"):
        parts.append(f"Weapon: {f['weapon']}")
    if f.get("constellation"):
        parts.append(f"Constellation: {f['constellation']}")
    if f.get("birthday"):
        parts.append(f"Birthday: {birthday_text(f['birthday'])}")
    if f.get("age"):
        parts.append(f"Age: {f['age']}")
    if f.get("height"):
        parts.append(f"Height: {f['height']}")
    if f.get("era"):
        parts.append(f"Era: {f['era']}")
    return ". ".join(parts) + ("." if parts else "")


def knowledge_block(rec) -> str:
    if rec["tier"] == "LITE":
        return ""
    k = rec["header"].get("knowledge") or {}
    lines = []
    for item in k.get("knows", []):
        tag = "" if item["visibility"] == "public" else f" ({item['visibility']})"
        lines.append(f"- Knows{tag}: {item['fact']}")
    for item in k.get("does_not_know", []):
        lines.append(f"- Does NOT know: {item['fact']}" + (f" ({item['note']})" if item.get("note") else ""))
    for item in k.get("believes", []):
        lines.append(f"- Believes: {item['belief']} (actually: {item['reality']}; {item['classification']})")
    return "\n".join(lines)


def card_description(rec, names, cutoff) -> str:
    fields = rec["fields"]
    out = [f"[{rec['name']}: {rec['header']['summary_line']}]"]
    ident = identity_line(rec, names)
    if ident:
        out.append(ident)
    used = set()
    for name in DESCRIPTION_ORDER:
        if name in fields:
            text = fields[name]["text"]
            if name == "knowledge":
                kb = knowledge_block(rec)
                if kb:
                    text = text + "\n" + kb
            out.append(f"{label_for(name, cutoff)}:\n{text}")
            used.add(name)
    for name, val in fields.items():
        if name not in used and name not in CARD_ONLY_FIELDS:
            out.append(f"{label_for(name, cutoff)}:\n{val['text']}")
    return "\n\n".join(out)


def split_greetings(text):
    if not text:
        return []
    return [g.strip() for g in re.split(r"^\s*===\s*$", text, flags=re.M) if g.strip()]


def card_fields(rec, names, cutoff) -> dict:
    f = rec["fields"]
    get = lambda k: f[k]["text"] if k in f else ""
    return {
        "description": card_description(rec, names, cutoff),
        "personality": get("personality"),
        "scenario": get("scenario"),
        "first_mes": get("first_mes"),
        "alternate_greetings": split_greetings(get("alternate_greetings")),
        "mes_example": get("mes_example"),
        "post_history_instructions": get("post_history"),
    }


def main_entry_text(rec, names, cutoff) -> str:
    h, fields = rec["header"], rec["fields"]
    aka = f" (also: {', '.join(h['aliases'][:8])})" if h.get("aliases") else ""
    if rec["entity_type"] in CARD_TYPES:
        parts = [f"{rec['name']}{aka}: {fields['summary']['text'] if 'summary' in fields else h['summary_line']}"]
        if "status" in fields:
            parts.append(f"Status as of {cutoff}: {fields['status']['text']}")
        return "\n\n".join(parts)
    parts = []
    for name, val in fields.items():
        if name == "summary":
            parts.insert(0, f"{rec['name']}{aka}: {val['text']}")
        else:
            parts.append(f"{label_for(name, cutoff)}: {val['text']}")
    if not parts:
        parts = [f"{rec['name']}{aka}: {h['summary_line']}"]
    return "\n\n".join(parts)


def book_for(rec, names, kind="main") -> str:
    wi = config("world-info-defaults")
    books, h = wi["books"], rec["header"]
    if (h.get("wi") or {}).get("book"):
        return h["wi"]["book"]
    t = rec["entity_type"]
    if t in CARD_TYPES:
        return books["character_index"] if kind == "main" else books["character_own"].format(name=rec["name"])
    nation = None
    if t == "location" and (h.get("facts") or {}).get("location_type") == "nation":
        nation = rec["name"]
    elif h.get("nation"):
        nation = names.get(h["nation"])
    return books[t].format(nation=nation or wi["nation_fallback"])


def entity_keys(rec):
    h = rec["header"]
    wi = h.get("wi") or {}
    if wi.get("keys"):
        return list(dict.fromkeys(wi["keys"]))
    keys = [rec["name"]] + list(h.get("aliases") or [])
    return list(dict.fromkeys(k for k in keys if k and k.strip()))
