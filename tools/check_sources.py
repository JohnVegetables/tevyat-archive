#!/usr/bin/env python3
"""Check source metadata, canon-cutoff compliance and placeholder text.

    python tools/check_sources.py [-v] [--all] [--online]

--online additionally sends a HEAD request to every distinct URL (slow; never required by CI).
"""
import argparse
import sys
import urllib.request

import _cli
from archive_lib.checks import check_sources
from archive_lib.common import Report
from archive_lib.registry import Registry


def online(reg, rep):
    urls = sorted({s["url"] for e in reg.entities for s in e.header.get("sources", []) if s.get("url")})
    print(f"checking {len(urls)} URLs online...")
    for u in urls:
        req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0 teyvat-archive-linkcheck"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status >= 400:
                    rep.warn("links", u, f"HTTP {r.status}")
        except Exception as ex:
            rep.warn("links", u, f"unreachable: {ex}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    _cli.add_common(ap)
    ap.add_argument("--online", action="store_true")
    args = ap.parse_args(argv)
    reg = Registry.load()
    rep = Report()
    rep.extend(reg.parse_report)
    rep.extend(check_sources(reg))
    if args.online:
        online(reg, rep)
    return _cli.finish(rep, args)


if __name__ == "__main__":
    sys.exit(main())
