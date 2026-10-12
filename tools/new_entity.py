#!/usr/bin/env python3
"""Create a correctly structured source file for a new entity.

    python tools/new_entity.py character amber "Amber" --nation nation.mondstadt
    python tools/new_entity.py location springvale "Springvale" --subdir settlements --nation nation.mondstadt
    python tools/new_entity.py npc dottore "Il Dottore"

The file is written under source/ with every required section stubbed with an HTML comment
(comments are ignored by the compiler, so an unfilled stub fails validation instead of
shipping empty). Fill it in, then run: python tools/validate.py --file <path>
"""
import argparse
import datetime
import json
import sys

import _cli
from archive_lib.common import SOURCE, TIERS, config, cutoff_version


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entity_type", choices=sorted(config("naming-conventions")["entity_types"]))
    ap.add_argument("slug")
    ap.add_argument("name")
    ap.add_argument("--subdir")
    ap.add_argument("--nation")
    args = ap.parse_args(argv)
    types = config("naming-conventions")["entity_types"]
    t = types[args.entity_type]
    folder = SOURCE / t["root"] / (args.subdir or "")
    path = folder / f"{args.slug}.md"
    if path.exists():
        print(f"{path} already exists")
        return 1
    header = {"id": f"{t['prefix']}.{args.slug}", "entity_type": args.entity_type, "name": args.name, "aliases": [],
              "summary_line": "", "nation": args.nation, "introduced_in": "", "spoiler_level": "none",
              "related": [], "relationships": [], "facts": {}, "uncertainties": [],
              "sources": [{"title": "", "type": "wiki", "url": "", "accessed": datetime.date.today().isoformat(),
                           "confidence": "high"}],
              "status": "drafted", "last_verified": None}
    if args.subdir:
        header["subdir"] = args.subdir
    if args.entity_type in ("character", "npc", "historical_figure"):
        header["knowledge"] = {"knows": [], "does_not_know": [], "believes": []}
    pol = config("tier-policy")
    req = pol["character_sections"]["required"].get(args.entity_type, pol["generic_required"])
    lines = ["---", json.dumps(header, ensure_ascii=False, indent=2), "---", ""]
    for tier in TIERS:
        for sec in req.get(tier, []):
            lines += [f"## {sec}", f"### {tier}", f"<!-- write the {tier} {sec} (canon through {cutoff_version()}) -->", ""]
    lines += ["<!-- Add '### STANDARD', '### LARGE +', '### ULTRA +' blocks and '## entry: Title' sections; see docs/authoring-guide.md -->", ""]
    folder.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"created {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
