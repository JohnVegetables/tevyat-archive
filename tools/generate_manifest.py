#!/usr/bin/env python3
"""Generate data/indexes/*.json and the coverage dashboard (reports/coverage.md).

    python tools/generate_manifest.py

Indexes: entity, character, location, faction, relationship, chronology, source, alias.
All numbers in the dashboard are computed from the files on disk and coverage/*.json.
"""
import argparse
import sys
from collections import Counter, defaultdict

import _cli
from archive_lib.checks import check_exports, coverage_state
from archive_lib.common import DATA, REPORTS, ROOT, TIERS, cutoff_version, dump_json, load_json, rel, vkey
from archive_lib.compiler import load_compiled_by_id
from archive_lib.registry import CARD_TYPES, Registry, data_path


def build_indexes(reg, compiled):
    idx = DATA / "indexes"
    ents = {}
    for e in sorted(reg.entities, key=lambda x: x.id or ""):
        h = e.header
        ents[e.id] = {"name": e.name, "type": e.type, "aliases": h.get("aliases", []), "nation": h.get("nation"),
                      "introduced_in": h.get("introduced_in"), "spoiler_level": h.get("spoiler_level"),
                      "status": h.get("status"), "source": rel(e.path),
                      "tiers": {t: rel(data_path(e, t)) for t in TIERS if t in compiled.get(e.id, {})}}
    dump_json(idx / "entity-index.json", {"canon_cutoff": cutoff_version(), "count": len(ents), "entities": ents})
    chars = {k: {**v, "facts": reg.by_id[k].header.get("facts", {})} for k, v in ents.items() if v["type"] in CARD_TYPES}
    dump_json(idx / "character-index.json", {"count": len(chars), "characters": chars})
    locs = {k: {**v, "parent": (reg.by_id[k].header.get("facts") or {}).get("parent"),
                "location_type": (reg.by_id[k].header.get("facts") or {}).get("location_type")}
            for k, v in ents.items() if v["type"] == "location"}
    tree = defaultdict(list)
    for k, v in locs.items():
        tree[v["parent"] or "(root)"].append(k)
    dump_json(idx / "location-index.json", {"count": len(locs), "locations": locs, "children": dict(sorted(tree.items()))})
    facs = {k: {**v, "facts": reg.by_id[k].header.get("facts", {})} for k, v in ents.items() if v["type"] == "faction"}
    dump_json(idx / "faction-index.json", {"count": len(facs), "factions": facs})
    rels = []
    for e in reg.entities:
        for r in e.header.get("relationships") or []:
            rels.append({"from": e.id, "to": r["target"], "type": r["type"], "summary": r["summary"],
                         "classification": r.get("classification", "confirmed")})
    dump_json(idx / "relationship-index.json", {"count": len(rels), "relationships": rels})
    chrono = []
    for e in reg.entities:
        f = e.header.get("facts") or {}
        if e.type == "timeline_event" or e.type == "quest":
            chrono.append({"id": e.id, "name": e.name, "type": e.type, "when": f.get("when"),
                           "in_world_order": f.get("sort_key", f.get("story_order")),
                           "release_version": f.get("version") or e.header.get("introduced_in"),
                           "learned_in": f.get("learned_in", [])})
    chrono.sort(key=lambda x: (x["in_world_order"] is None, x["in_world_order"] or 0, vkey(x["release_version"])))
    release = sorted(chrono, key=lambda x: vkey(x["release_version"]))
    dump_json(idx / "chronology-index.json", {"note": "in_world_order = when it happened (null = unknown); release_version = when players learned it.",
                                              "by_in_world_order": chrono, "by_release": [x["id"] for x in release]})
    srcs = defaultdict(lambda: {"title": None, "type": None, "cited_by": []})
    for e in reg.entities:
        for s in e.header.get("sources") or []:
            key = s.get("url") or s["title"]
            srcs[key]["title"], srcs[key]["type"] = s["title"], s["type"]
            srcs[key]["cited_by"].append(e.id)
    dump_json(idx / "source-index.json", {"count": len(srcs), "sources": dict(sorted(srcs.items()))})
    amap = reg.alias_map()
    dump_json(idx / "alias-index.json", {"note": "lowercased name/alias -> entity ids. More than one id = ambiguous; disambiguate by context.",
                                         "aliases": {k: sorted(v) for k, v in sorted(amap.items())}})
    return ents


def dashboard(reg, compiled, export_ok):
    rows = coverage_state(reg, compiled, export_ok)
    per = defaultdict(Counter)
    missing = []
    for man, it, eff, reasons in rows:
        per[man][eff] += 1
        if eff == "not_started":
            missing.append((man, it))
    manifests = {}
    for label in TIERS:
        p = ROOT / "sillytavern" / "manifests" / f"{label}.json"
        if p.exists():
            manifests[label] = load_json(p)
    types = Counter(e.type for e in reg.entities)
    status = Counter(e.header.get("status") for e in reg.entities)
    four = sum(1 for e in reg.entities if len(compiled.get(e.id, {})) == 4)
    L = [f"# Coverage report (canon through {cutoff_version()})", "",
         "Generated by `python tools/generate_manifest.py` from the files on disk. Do not edit by hand.", "",
         "## Totals", "",
         f"- Entities with source files: **{len(reg.entities)}**",
         f"- Entities with all four compiled tiers: **{four}**",
         f"- Header status: " + ", ".join(f"{k}: {v}" for k, v in sorted(status.items(), key=lambda x: str(x[0]))),
         f"- Valid character cards exported (any tier): **{len(export_ok)}** distinct entities",
         "", "| Entity type | Count |", "|---|---:|"]
    L += [f"| {t} | {n} |" for t, n in sorted(types.items())]
    L += ["", "## Bundles", "", "| Tier | Cards | World books | WI entries | WI tokens (heuristic) |", "|---|---:|---:|---:|---:|"]
    for t, m in manifests.items():
        tt = m["totals"]
        L.append(f"| {t} | {tt['cards']} | {tt['world_books']} | {tt['world_info_entries']} | {tt['world_info_tokens']:,} |")
    L += ["", "## Coverage manifests", "",
          "| Manifest | Items | Complete | Verified | Needs verification | Drafted | Not started | Blocked | % complete |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for man, c in sorted(per.items()):
        total = sum(c.values())
        pct = 100 * c["complete"] / total if total else 0
        L.append(f"| {man} | {total} | {c['complete']} | {c['verified']} | {c['needs_verification']} | {c['drafted']} | "
                 f"{c['not_started']} | {c['blocked']} | {pct:.1f}% |")
    L += ["", "'Complete' requires: source file, header status `verified`, four compiled tiers, and (for card characters) a valid export.", ""]
    if missing:
        L += ["## Not started", ""]
        for man, it in missing:
            L.append(f"- `{it['id']}` {it['name']} ({man}, priority {it.get('priority', 'normal')})")
    spots = sorted(REPORTS.glob("spot-check-*.json"))
    if spots:
        s = load_json(spots[-1])
        t = s["totals"]
        pct = lambda k: 100 * t[k] / t["checked"] if t["checked"] else 0
        L += ["", "## Spot-check of unverified entries", "",
              f"Latest: `{rel(spots[-1])}` ({s.get('date', '?')}). {s.get('method', '')}", "",
              f"- Entities sampled: {t['entities']}; claims checked: {t['checked']}",
              f"- Confirmed: {t['correct']} ({pct('correct'):.1f}%) · wrong: {t['wrong']} ({pct('wrong'):.1f}%, fixed) · "
              f"unconfirmable within budget: {t['unsupported']} ({pct('unsupported'):.1f}%)", ""]
    blocked = [(m, it) for m, it, eff, _ in rows if eff == "blocked"]
    if blocked:
        L += ["", "## Blocked", ""] + [f"- `{it['id']}` {it['name']}: {it.get('blocked_reason')}" for m, it in blocked]
    REPORTS.mkdir(exist_ok=True)
    (REPORTS / "coverage.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.parse_args(argv)
    reg = Registry.load()
    compiled = load_compiled_by_id()
    _, export_ok = check_exports()
    ents = build_indexes(reg, compiled)
    dashboard(reg, compiled, export_ok)
    print(f"indexes written for {len(ents)} entities; dashboard: reports/coverage.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
