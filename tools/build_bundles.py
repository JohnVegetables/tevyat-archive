#!/usr/bin/env python3
"""Build installable SillyTavern bundles (cards + World Info + manifest), optionally zipped.

    python tools/build_bundles.py --tier STANDARD
    python tools/build_bundles.py --tier all --zip
    python tools/build_bundles.py --mix mixes/example-focus-mondstadt.json --zip
    python tools/build_bundles.py --tier STANDARD --max-version 4.2 --permanent-only   # spoiler-limited build

Outputs
    sillytavern/character-cards/<LABEL>/<group>/<Name>.json   Character Card V2 JSON
    sillytavern/world-info/<LABEL>/<Book>.json                 World Info files
    sillytavern/manifests/<LABEL>.json                         what is inside, tier per entity
    bundles/teyvat-archive-<LABEL>-v<cutoff>.zip               (with --zip; git-ignored)

A mix file selects a tier per entity:
    {"label": "focus-mondstadt", "default": "LITE",
     "rules": [{"match": "nation:nation.mondstadt", "tier": "LARGE"},
               {"match": "character.venti", "tier": "ULTRA"},
               {"match": "type:system", "tier": "STANDARD"}]}
Later rules win. 'match' is an id glob, 'type:<entity_type>' or 'nation:<nation id>'.
"""
import argparse
import json
import sys
from pathlib import Path

import _cli
from archive_lib.common import ROOT, TIERS
from archive_lib.compiler import load_compiled_by_id
from archive_lib.exporter import tier_selection, write_exports
from archive_lib.common import vkey
from archive_lib.compiler import compile_entity, names_from_registry
from archive_lib.registry import Registry


def compile_filtered(max_version, permanent_only):
    reg = Registry.load()
    names = names_from_registry(reg)
    out = {}
    for e in reg.entities:
        if max_version and vkey(e.header.get("introduced_in")) > vkey(max_version):
            continue
        if permanent_only and e.header.get("availability") == "limited":
            continue
        out[e.id] = compile_entity(e, names, max_version, permanent_only)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tier", choices=list(TIERS) + ["all"])
    ap.add_argument("--mix", help="JSON mix file for a mixed-tier bundle")
    ap.add_argument("--zip", action="store_true", help="also write bundles/*.zip")
    ap.add_argument("--max-version", help="leave out entities/sections revealed after this version (spoiler-limited build)")
    ap.add_argument("--permanent-only", action="store_true", help="leave out sections from limited-time events")
    args = ap.parse_args(argv)
    if not args.tier and not args.mix:
        args.tier = "all"
    suffix = ""
    if args.max_version or args.permanent_only:
        compiled = compile_filtered(args.max_version, args.permanent_only)
        suffix = (f"-upto-{args.max_version}" if args.max_version else "") + ("-permanent" if args.permanent_only else "")
    else:
        compiled = load_compiled_by_id()
    if not compiled:
        print("data/ is empty - run tools/build_data.py first")
        return 1
    jobs = []
    if args.tier:
        jobs += [(t, tier_selection(compiled, t)) for t in (TIERS if args.tier == "all" else [args.tier])]
    if args.mix:
        mix = json.loads(Path(args.mix if Path(args.mix).is_absolute() else ROOT / args.mix).read_text(encoding="utf-8"))
        label = "MIX-" + mix.get("label", Path(args.mix).stem)
        jobs.append((label, tier_selection(compiled, mix.get("default", "STANDARD"), mix)))
    for label, sel in jobs:
        label += suffix
        m = write_exports(compiled, sel, label, zip_bundle=args.zip)
        t = m["totals"]
        print(f"{label:24} {t['cards']:4} cards | {t['world_books']:3} books | {t['world_info_entries']:5} WI entries | "
              f"~{t['world_info_tokens']:,} WI tokens" + (f" | {m['zip']}" if m.get("zip") else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
