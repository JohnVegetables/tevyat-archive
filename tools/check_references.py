#!/usr/bin/env python3
"""Check entity references (nation, related, relationships, id-valued facts) and alias collisions.

    python tools/check_references.py [-v] [--all]
"""
import argparse
import sys

import _cli
from archive_lib.checks import check_aliases, check_references
from archive_lib.registry import Registry


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    _cli.add_common(ap)
    args = ap.parse_args(argv)
    reg = Registry.load()
    rep = reg.parse_report
    rep.extend(check_references(reg))
    rep.extend(check_aliases(reg))
    return _cli.finish(rep, args)


if __name__ == "__main__":
    sys.exit(main())
