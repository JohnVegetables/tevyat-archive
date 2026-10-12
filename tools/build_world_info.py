#!/usr/bin/env python3
"""Build only the World Info (lorebook) exports for one tier, or all tiers.

    python tools/build_world_info.py --tier LITE
    python tools/build_world_info.py --tier all

Output: sillytavern/world-info/<TIER>/*.json. Use tools/build_bundles.py for cards + manifests + zips.
"""
import argparse
import sys

import _cli
from archive_lib.common import TIERS
from archive_lib.compiler import load_compiled_by_id
from archive_lib.exporter import tier_selection, write_exports


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tier", default="all", choices=list(TIERS) + ["all"])
    args = ap.parse_args(argv)
    compiled = load_compiled_by_id()
    if not compiled:
        print("data/ is empty - run tools/build_data.py first")
        return 1
    for t in (TIERS if args.tier == "all" else [args.tier]):
        m = write_exports(compiled, tier_selection(compiled, t), t, only_world=True)
        print(f"{t:9} {m['totals']['world_books']:3} books, {m['totals']['world_info_entries']:5} entries, "
              f"~{m['totals']['world_info_tokens']:,} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main())
