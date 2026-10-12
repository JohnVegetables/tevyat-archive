#!/usr/bin/env python3
"""Compare coverage manifests (coverage/*.json) with the entities on disk.

    python tools/check_coverage.py              # report; exit 1 if a critical/high item is missing
    python tools/check_coverage.py --sync       # write each item's computed status back to the manifests
    python tools/check_coverage.py --summary    # one line per manifest

Effective status is computed, never trusted: an item is 'complete' only when its source file
exists, its header status is 'verified', all four tiers compile, and (for card characters) a
valid SillyTavern export exists. Run tools/build_data.py and tools/build_bundles.py first.
"""
import argparse
import sys
from collections import Counter

import _cli
from archive_lib.checks import check_coverage, check_exports, check_manifests, coverage_state
from archive_lib.common import COVERAGE, dump_json, load_json
from archive_lib.compiler import load_compiled_by_id
from archive_lib.registry import Registry


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    _cli.add_common(ap)
    ap.add_argument("--sync", action="store_true", help="write computed statuses into coverage/*.json")
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args(argv)
    reg = Registry.load()
    compiled = load_compiled_by_id()
    _, export_ok = check_exports()
    rows = coverage_state(reg, compiled, export_ok)
    if args.sync:
        by_file = {}
        for man, it, eff, _ in rows:
            by_file.setdefault(man, {})[it["id"]] = eff
        for man, statuses in by_file.items():
            p = COVERAGE / f"{man}.json"
            m = load_json(p)
            for it in m["items"]:
                if it["id"] in statuses and it["status"] != "blocked":
                    it["status"] = statuses[it["id"]]
            dump_json(p, m)
        print(f"synced statuses in {len(by_file)} manifest(s)")
    if args.summary or args.sync:
        per = {}
        for man, it, eff, _ in rows:
            per.setdefault(man, Counter())[eff] += 1
        for man, c in sorted(per.items()):
            total = sum(c.values())
            print(f"{man:28} {total:4} items | complete {c['complete']:4} | verified {c['verified']:3} | "
                  f"needs_verification {c['needs_verification']:3} | drafted {c['drafted']:3} | "
                  f"not_started {c['not_started']:4} | blocked {c['blocked']:3}")
        return 0
    rep = check_manifests()
    rep.extend(check_coverage(reg, compiled, export_ok))
    return _cli.finish(rep, args)


if __name__ == "__main__":
    sys.exit(main())
