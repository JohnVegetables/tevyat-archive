#!/usr/bin/env python3
"""Report token counts per tier, per entity type and against the budget guidelines.

    python tools/estimate_tokens.py                 # totals per tier and type
    python tools/estimate_tokens.py --entity character.amber
    python tools/estimate_tokens.py --over          # entities outside their budget range

Uses tiktoken (cl100k_base) if installed, otherwise a heuristic (see archive_lib/tokens.py).
Counts are of the generated SillyTavern text, so they include labels and identity lines.
"""
import argparse
import sys
from collections import defaultdict

import _cli
from archive_lib import tokens
from archive_lib.common import TIERS, config, cutoff_version
from archive_lib.compiler import load_compiled_by_id
from archive_lib.render import CARD_TYPES, card_fields, main_entry_text


def measure(rec, names):
    cutoff = cutoff_version()
    main = tokens.count(main_entry_text(rec, names, cutoff))
    entries = sum(tokens.count(x["text"]) for x in rec["entries"])
    out = {"main": main, "entries": entries, "card": 0, "greetings": 0, "examples": 0}
    if rec["entity_type"] in CARD_TYPES:
        cf = card_fields(rec, names, cutoff)
        out["card"] = tokens.count(cf["description"]) + tokens.count(cf["personality"]) + tokens.count(cf["scenario"])
        out["greetings"] = tokens.count(cf["first_mes"]) + sum(tokens.count(g) for g in cf["alternate_greetings"])
        out["examples"] = tokens.count(cf["mes_example"])
    out["budget"] = out["card"] if rec["entity_type"] in CARD_TYPES else main
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entity")
    ap.add_argument("--over", action="store_true")
    args = ap.parse_args(argv)
    compiled = load_compiled_by_id()
    names = {eid: next(iter(v.values()))["name"] for eid, v in compiled.items()}
    budgets = config("tier-policy")["token_budgets"]
    types = config("naming-conventions")["entity_types"]
    print(f"token method: {tokens.METHOD}\n")
    if args.entity:
        by = compiled.get(args.entity)
        if not by:
            print("unknown entity", args.entity)
            return 1
        for t in TIERS:
            m = measure(by[t], names)
            lo, hi = budgets[types[by[t]['entity_type']]['budget']][t]
            print(f"{t:9} budget-text {m['budget']:6} (guideline {lo}-{hi}) | sub-entries {m['entries']:6} | "
                  f"greetings {m['greetings']:5} | examples {m['examples']:5}")
        return 0
    totals = defaultdict(lambda: defaultdict(int))
    counts = defaultdict(int)
    outside = []
    for eid, by in sorted(compiled.items()):
        et = by["LITE"]["entity_type"]
        counts[et] += 1
        for t in TIERS:
            m = measure(by[t], names)
            totals[t][et] += m["budget"] + m["entries"]
            totals[t]["_all"] += m["budget"] + m["entries"]
            lo, hi = budgets[types[et]["budget"]][t]
            if args.over and not (lo <= m["budget"] <= hi):
                outside.append((eid, t, m["budget"], lo, hi))
    if args.over:
        for eid, t, n, lo, hi in outside:
            print(f"{eid:45} {t:9} {n:6}  (guideline {lo}-{hi})")
        print(f"\n{len(outside)} tier variants outside the guideline range")
        return 0
    print(f"{'entity type':20}{'count':>7}" + "".join(f"{t:>12}" for t in TIERS))
    for et in sorted(counts):
        print(f"{et:20}{counts[et]:7}" + "".join(f"{totals[t][et]:12,}" for t in TIERS))
    print(f"{'TOTAL':20}{sum(counts.values()):7}" + "".join(f"{totals[t]['_all']:12,}" for t in TIERS))
    print("\n(Total = card/main text + sub-entries; this is the whole archive, not what is active at once.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
