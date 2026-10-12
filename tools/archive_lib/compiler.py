from __future__ import annotations

from .common import DATA, ROOT, TIERS, config, cutoff_version, load_json, rel
from .registry import Registry, data_path
from .render import CARD_TYPES, card_fields, main_entry_text
from .source import Entity, resolve
from . import tokens


def compile_entity(e: Entity, names: dict, max_version=None, permanent_only=False) -> dict:
    cutoff = max_version or cutoff_version()
    schema_version = config("schema-version")["schema_version"]
    out = {}
    for tier in TIERS:
        fields, entries = resolve(e, tier, max_version, permanent_only)
        rec = {
            "id": e.id, "entity_type": e.type, "name": e.name, "tier": tier,
            "schema_version": schema_version, "canon_cutoff": cutoff_version(),
            "source_file": rel(e.path), "source_hash": e.raw_hash,
            "header": e.header, "fields": fields, "entries": entries,
            "stats": {},
        }
        rec["stats"] = stats_for(rec, names, cutoff)
        out[tier] = rec
    return out


def stats_for(rec, names, cutoff) -> dict:
    main = main_entry_text(rec, names, cutoff)
    st = {"main_entry_tokens": tokens.heuristic(main),
          "entries_tokens": sum(tokens.heuristic(x["text"]) for x in rec["entries"]),
          "entries": len(rec["entries"]),
          "words": sum(tokens.words(v["text"]) for v in rec["fields"].values()) + sum(tokens.words(x["text"]) for x in rec["entries"]),
          "token_method": "heuristic"}
    if rec["entity_type"] in CARD_TYPES:
        cf = card_fields(rec, names, cutoff)
        st["card_tokens"] = tokens.heuristic(cf["description"]) + tokens.heuristic(cf["personality"]) + tokens.heuristic(cf["scenario"])
        st["greeting_tokens"] = tokens.heuristic(cf["first_mes"]) + sum(tokens.heuristic(g) for g in cf["alternate_greetings"])
        st["example_tokens"] = tokens.heuristic(cf["mes_example"])
        st["budget_tokens"] = st["card_tokens"]
    else:
        st["budget_tokens"] = st["main_entry_tokens"]
    st["total_tokens"] = st["budget_tokens"] + st["entries_tokens"] + st.get("greeting_tokens", 0) + st.get("example_tokens", 0)
    return st


def names_from_registry(reg: Registry) -> dict:
    from .registry import manifest_names
    names = manifest_names()
    names.update({e.id: e.name for e in reg.entities if e.id})
    return names


def iter_compiled():
    for p in sorted(DATA.rglob("*-*.json")):
        if p.parent.name == "indexes":
            continue
        stem = p.stem
        if not any(stem.endswith("-" + t) for t in TIERS):
            continue
        yield p, load_json(p)


def load_compiled_by_id():
    out = {}
    for p, rec in iter_compiled():
        out.setdefault(rec["id"], {})[rec["tier"]] = rec
    return out


def expected_data_files(reg: Registry):
    for e in reg.entities:
        for t in TIERS:
            yield e, t, data_path(e, t)


__all__ = ["compile_entity", "names_from_registry", "iter_compiled", "load_compiled_by_id", "expected_data_files", "ROOT"]
