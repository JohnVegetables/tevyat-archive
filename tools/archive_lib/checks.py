from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

from .common import (COVERAGE, ROOT, ST_OUT, TIERS, Report, config, cutoff_version, load_json, rel, slug_of,
                     vkey, ID_RE)
from .registry import CARD_TYPES, Registry, expected_source_dir, schema_for, slug_matches
from .render import entity_keys
from .schema import errors as schema_errors
from . import stexport

ID_FACTS = ("origin", "residence", "parent", "archon", "headquarters", "parent_org", "region")
ID_LIST_FACTS = ("affiliations", "leaders", "operating_areas", "owners", "characters", "prerequisites", "places",
                 "participants", "learned_in")
PLACEHOLDER = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum|PLACEHOLDER|XXX)\b|\[citation needed\]", re.I)
WIKI_MARKUP = re.compile(r"\[\[|\]\]|\{\{(?!char\}\}|user\}\})[^}]*\}\}|<ref[ >]|'''")
FUTURE_VERSION = re.compile(r"\b(?:Version|v\.?|Ver\.?|patch)\s*(\d+)\.(\d+)\b", re.I)


def check_schema(reg: Registry) -> Report:
    r = Report()
    r.extend(reg.parse_report)
    types = config("naming-conventions")["entity_types"]
    for e in reg.entities:
        where = rel(e.path)
        h = e.header
        for path, msg in schema_errors(h, schema_for(h.get("entity_type", "lore"))):
            r.error("schema", where, f"{path}: {msg}")
        eid, et = h.get("id"), h.get("entity_type")
        if not eid or not ID_RE.match(str(eid)) or et not in types:
            continue
        if eid.split(".", 1)[0] != types[et]["prefix"]:
            r.error("naming", where, f"id {eid} should start with '{types[et]['prefix']}.' for entity_type {et}")
        if e.path.parent.resolve() != expected_source_dir(e).resolve():
            r.error("naming", where, f"file should live in {rel(expected_source_dir(e))}/ (entity_type + subdir)")
        if not slug_matches(e):
            r.warn("naming", where, f"file name '{e.path.stem}' differs from id slug '{slug_of(eid)}'")
        if h.get("introduced_in") and vkey(h["introduced_in"]) > vkey(cutoff_version()):
            r.error("cutoff", where, f"introduced_in {h['introduced_in']} is after the canon cutoff {cutoff_version()}")
        if et == "character" and not (h.get("facts") or {}).get("playable"):
            r.error("schema", where, "entity_type 'character' is for playable characters; use 'npc' instead")
    return r


def _required(entity_type):
    pol = config("tier-policy")
    if entity_type in pol["character_sections"]["required"]:
        return pol["character_sections"]["required"][entity_type]
    return pol["generic_required"]


def check_sections(reg: Registry) -> Report:
    r = Report()
    pol = config("tier-policy")
    for e in reg.entities:
        where = rel(e.path)
        if not e.type:
            continue
        req = _required(e.type)
        acc = []
        for t in TIERS:
            acc += req.get(t, [])
            for name in acc:
                s = e.section(name)
                if s is None or s.resolved()[t] is None:
                    r.error("sections", where, f"tier {t} is missing required section '{name}'")
            if pol.get("each_tier_must_add") and t != "LITE":
                if not any(t in s.blocks for s in e.sections):
                    r.error("tiers", where, f"tier {t} adds nothing over the tier below (needs at least one '### {t}' block)")
        for s in e.sections:
            for t in TIERS:
                text = s.resolved()[t]
                if text is None:
                    continue
                if PLACEHOLDER.search(text):
                    r.error("content", where, f"placeholder text in '{s.name}' ({t}): {PLACEHOLDER.search(text).group(0)!r}")
                    break
                if WIKI_MARKUP.search(text):
                    r.warn("content", where, f"wiki markup left in '{s.name}' ({t}): {WIKI_MARKUP.search(text).group(0)!r}")
                    break
            if s.kind == "entry" and not s.attrs.get("keys") and not s.attrs.get("constant"):
                r.warn("worldinfo", where, f"entry '{s.title}' has no @keys; its title will be used as the only key")
        if e.type in CARD_TYPES and e.section("first_mes"):
            fm = e.section("first_mes").resolved()["ULTRA"] or ""
            if "{{user}}" not in fm and "{{User}}" not in fm:
                r.warn("card", where, "first_mes never mentions {{user}}")
        if e.type in CARD_TYPES and e.section("mes_example"):
            ex = e.section("mes_example").resolved()["ULTRA"] or ""
            if "<START>" not in ex:
                r.error("card", where, "mes_example must contain <START> separators")
            if "{{char}}:" not in ex:
                r.error("card", where, "mes_example should use '{{char}}:' speaker labels")
    return r


def manifest_ids():
    out = {}
    for p in sorted(COVERAGE.glob("*.json")):
        m = load_json(p)
        for it in m.get("items", []):
            out[it["id"]] = (p.stem, it)
    return out


def referenced_ids(h):
    refs = []
    if h.get("nation"):
        refs.append(("nation", h["nation"]))
    for i in h.get("related") or []:
        refs.append(("related", i))
    for rr in h.get("relationships") or []:
        refs.append(("relationships", rr["target"]))
    f = h.get("facts") or {}
    for k in ID_FACTS:
        v = f.get(k)
        if isinstance(v, str) and ID_RE.match(v):
            refs.append((f"facts.{k}", v))
    for k in ID_LIST_FACTS:
        for v in f.get(k) or []:
            refs.append((f"facts.{k}", v))
    return refs


def check_references(reg: Registry) -> Report:
    r = Report()
    planned = manifest_ids()
    for e in reg.entities:
        where = rel(e.path)
        for field, target in referenced_ids(e.header):
            if target == e.id and field != "related":
                r.warn("references", where, f"{field} refers to itself")
            if target in reg.by_id:
                continue
            if target in planned:
                r.warn("references", where, f"{field} -> {target} is planned ({planned[target][0]}) but not written yet")
            else:
                r.error("references", where, f"{field} -> {target} does not exist and is not in any coverage manifest")
        rels = [x["target"] for x in e.header.get("relationships") or []]
        if len(rels) != len(set(rels)):
            r.warn("references", where, "duplicate relationship targets")
    return r


def check_aliases(reg: Registry) -> Report:
    r = Report()
    amap = reg.alias_map()
    for alias, ids in sorted(amap.items()):
        if len(ids) > 1:
            r.warn("aliases", alias, f"shared by {sorted(ids)} - make sure World Info keys disambiguate (use @keys2)")
    for e in reg.entities:
        for a in e.header.get("aliases") or []:
            if a.strip().lower() == (e.name or "").strip().lower():
                r.warn("aliases", rel(e.path), f"alias '{a}' repeats the name")
    return r


def check_sources(reg: Registry) -> Report:
    r = Report()
    today = _dt.date.today().isoformat()
    for e in reg.entities:
        where = rel(e.path)
        srcs = e.header.get("sources") or []
        if not srcs:
            r.error("sources", where, "no sources")
            continue
        if not any(s.get("url") for s in srcs):
            r.error("sources", where, "at least one source needs a URL")
        if all(s.get("confidence") == "low" for s in srcs):
            r.warn("sources", where, "all sources are low confidence")
        for s in srcs:
            if s.get("accessed") and s["accessed"] > today:
                r.error("sources", where, f"accessed date {s['accessed']} is in the future")
            if s.get("version") and vkey(s["version"]) > vkey(cutoff_version()):
                r.error("cutoff", where, f"source '{s['title']}' is from {s['version']}, after the cutoff")
            u = s.get("url") or ""
            if u and not re.match(r"^https?://", u):
                r.error("sources", where, f"bad URL {u!r}")
        if e.header.get("status") == "verified" and not e.header.get("last_verified"):
            r.warn("sources", where, "status is 'verified' but last_verified is empty")
        if len(srcs) == 1 and e.type in CARD_TYPES:
            r.warn("sources", where, "characters should cite more than one source (profile, quests, voice-overs)")
        for s in e.sections:
            if s.attrs.get("version") and vkey(s.attrs["version"]) > vkey(cutoff_version()):
                r.error("cutoff", where, f"section '{s.name}' is tagged @version {s.attrs['version']}, after the cutoff")
            text = s.resolved()["ULTRA"] or ""
            for m in FUTURE_VERSION.finditer(text):
                if (int(m.group(1)), int(m.group(2))) > vkey(cutoff_version()):
                    r.error("cutoff", where, f"'{s.name}' mentions {m.group(0)!r}, after the cutoff")
    return r


NAMEISH = re.compile(r"\b(?:[A-Z][a-z'\-]+(?:\s+(?:of|the|de|du|von|no)\s+|\s+)?){1,4}|\b\d{2,}\b")


def check_tier_consistency(compiled: dict) -> Report:
    """compiled: {id: {tier: record}}."""
    r = Report()
    budgets = config("tier-policy")["token_budgets"]
    types = config("naming-conventions")["entity_types"]
    for eid, by_tier in sorted(compiled.items()):
        missing = [t for t in TIERS if t not in by_tier]
        if missing:
            r.error("tiers", eid, f"missing compiled tier(s): {missing}")
            continue
        where = by_tier["LITE"]["source_file"]
        base = by_tier["LITE"]["header"]
        for t in TIERS[1:]:
            if by_tier[t]["header"] != base:
                r.error("tiers", where, f"header differs between LITE and {t}")
        prev = None
        for t in TIERS:
            rec = by_tier[t]
            if prev is not None:
                lost = set(prev["fields"]) - set(rec["fields"])
                if lost:
                    r.error("tiers", where, f"{t} drops fields present in the tier below: {sorted(lost)}")
                lost_e = {x["title"] for x in prev["entries"]} - {x["title"] for x in rec["entries"]}
                if lost_e:
                    r.error("tiers", where, f"{t} drops entries present in the tier below: {sorted(lost_e)}")
                if rec["stats"]["total_tokens"] < prev["stats"]["total_tokens"]:
                    r.warn("tiers", where, f"{t} is smaller than the tier below ({rec['stats']['total_tokens']} < {prev['stats']['total_tokens']} tokens)")
                hi_text = " ".join(v["text"] for v in rec["fields"].values()) + " " + " ".join(x["text"] for x in rec["entries"])
                for fname, fv in prev["fields"].items():
                    if fname in ("first_mes", "alternate_greetings", "mes_example", "scenario"):
                        continue
                    if rec["fields"][fname]["text"].startswith(fv["text"]):
                        continue
                    for m in set(x.group(0).strip() for x in NAMEISH.finditer(fv["text"])):
                        if len(m) > 3 and m not in hi_text and m not in ("The", "This", "When", "After", "Before", "Her", "His", "She", "They", "Their", "Although", "However"):
                            r.info("tiers", where, f"{prev['tier']}->{t} '{fname}': '{m}' is not mentioned in {t} (check for contradictions)")
            prev = rec
        btype = types[by_tier["LITE"]["entity_type"]]["budget"]
        for t in TIERS:
            lo, hi = budgets[btype][t]
            n = by_tier[t]["stats"]["budget_tokens"]
            if n > hi * 1.5:
                r.warn("budget", where, f"{t} card/main text is {n} tokens; guideline {lo}-{hi}")
            elif n < lo * 0.5 and t != "LITE":
                r.info("budget", where, f"{t} card/main text is {n} tokens; guideline {lo}-{hi}")
    return r


def check_keys(compiled: dict) -> Report:
    r = Report()
    kr = config("world-info-defaults")["key_rules"]
    stop = set(kr["generic_stoplist"])
    usage = {}
    for eid, by_tier in compiled.items():
        rec = by_tier.get("ULTRA")
        if not rec:
            continue
        where = rec["source_file"]
        hdr_wi = rec["header"].get("wi") or {}
        groups = []
        if not hdr_wi.get("exclude"):
            groups.append(("main", entity_keys(rec), hdr_wi.get("keys2") or [], hdr_wi.get("constant")))
        for x in rec["entries"]:
            groups.append((x["title"], x["attrs"].get("keys") or [x["title"]], x["attrs"].get("keys2") or [], x["attrs"].get("constant")))
        for title, keys, keys2, constant in groups:
            if not keys and not constant:
                r.error("worldinfo", where, f"'{title}' has no activation keys")
            for k in keys:
                kl = k.strip().lower()
                usage.setdefault(kl, set()).add(eid)
                if len(kl) < kr["min_length"] and not keys2:
                    r.warn("worldinfo", where, f"'{title}': key {k!r} is very short and will over-trigger")
                if kl in stop and not keys2:
                    r.warn("worldinfo", where, f"'{title}': key {k!r} is too generic without @keys2")
    for k, ids in sorted(usage.items()):
        if len(ids) > kr["max_entries_per_key_warn"]:
            r.info("worldinfo", k, f"key used by {len(ids)} entities")
    return r


STATUS_RANK = {"not_started": 0, "researching": 1, "drafted": 2, "needs_verification": 3, "verified": 4, "complete": 5, "blocked": -1}


def coverage_state(reg: Registry, compiled: dict, export_ok: set):
    rows = []
    for p in sorted(COVERAGE.glob("*.json")):
        m = load_json(p)
        for it in m["items"]:
            reasons, e = [], reg.by_id.get(it["id"])
            if it["status"] == "blocked":
                rows.append((p.stem, it, "blocked", [it.get("blocked_reason") or "blocked"]))
                continue
            if e is None:
                rows.append((p.stem, it, "not_started" if it["status"] in ("not_started", "complete", "verified", "drafted", "needs_verification") else it["status"], ["no source file"]))
                continue
            st = e.header.get("status", "drafted")
            if len(compiled.get(it["id"], {})) != 4:
                reasons.append("tier files missing - run tools/build_data.py")
            if e.type in CARD_TYPES and it["id"] not in export_ok and (e.header.get("facts") or {}).get("card", e.type != "historical_figure"):
                reasons.append("no valid SillyTavern export")
            eff = st
            if st == "verified" and not reasons:
                eff = "complete"
            rows.append((p.stem, it, eff, reasons))
    return rows


def check_coverage(reg: Registry, compiled: dict, export_ok: set) -> Report:
    r = Report()
    planned = manifest_ids()
    for e in reg.entities:
        if e.id not in planned:
            r.warn("coverage", rel(e.path), "entity is not listed in any coverage manifest")
    for man, it, eff, reasons in coverage_state(reg, compiled, export_ok):
        where = f"{man}:{it['id']}"
        if eff == "not_started" and it.get("priority") in ("critical", "high"):
            r.error("coverage", where, f"{it['name']}: required ({it.get('priority')}) entry has no source file")
        elif eff == "not_started":
            r.warn("coverage", where, f"{it['name']}: not started")
        elif eff not in ("complete", "blocked"):
            r.info("coverage", where, f"{it['name']}: {eff}" + (f" ({'; '.join(reasons)})" if reasons else ""))
    return r


def check_exports() -> tuple[Report, set]:
    import json as _json
    r, ok_ids = Report(), set()
    for p in sorted((ST_OUT / "character-cards").rglob("*.json")):
        try:
            card = _json.loads(p.read_text(encoding="utf-8"))
        except Exception as ex:
            r.error("export", rel(p), f"invalid JSON: {ex}")
            continue
        errs = stexport.check_card(card)
        for x in errs:
            r.error("export", rel(p), x)
        eid = (card.get("data", {}).get("extensions", {}) or {}).get("teyvat_archive", {}).get("id")
        if not errs and eid:
            ok_ids.add(eid)
    for p in sorted((ST_OUT / "world-info").rglob("*.json")):
        try:
            book = _json.loads(p.read_text(encoding="utf-8"))
        except Exception as ex:
            r.error("export", rel(p), f"invalid JSON: {ex}")
            continue
        for x in stexport.check_world(book):
            r.error("export", rel(p), x)
    return r, ok_ids


def check_docs() -> Report:
    r = Report()
    for f in ["README.md", "LICENSE", "NOTICE"]:
        if not (ROOT / f).exists():
            r.error("docs", f, "missing")
    return r


def check_manifests() -> Report:
    r = Report()
    seen = {}
    for p in sorted(COVERAGE.glob("*.json")):
        try:
            m = load_json(p)
        except Exception as ex:
            r.error("manifest", rel(p), f"invalid JSON: {ex}")
            continue
        for path, msg in schema_errors(m, "coverage-manifest.schema.json"):
            r.error("manifest", rel(p), f"{path}: {msg}")
        for it in m.get("items", []):
            if it["id"] in seen:
                r.error("manifest", rel(p), f"{it['id']} also listed in {seen[it['id']]}")
            seen[it["id"]] = p.stem
    return r
