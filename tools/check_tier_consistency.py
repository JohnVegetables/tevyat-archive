#!/usr/bin/env python3
"""Check that the four compiled tiers of every entity agree, grow monotonically and respect budgets.

    python tools/check_tier_consistency.py [-v] [--all]

Run tools/build_data.py first. With -v, lists names/numbers that a lower tier mentions but a
higher tier dropped after replacing a section (worth a human look for contradictions).
"""
import argparse
import sys

import _cli
from archive_lib.checks import check_keys, check_tier_consistency
from archive_lib.compiler import load_compiled_by_id


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    _cli.add_common(ap)
    args = ap.parse_args(argv)
    compiled = load_compiled_by_id()
    rep = check_tier_consistency(compiled)
    rep.extend(check_keys(compiled))
    return _cli.finish(rep, args)


if __name__ == "__main__":
    sys.exit(main())
