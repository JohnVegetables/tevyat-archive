#!/usr/bin/env python3
"""Compile source/**/*.md into the four-tier database in data/.

    python tools/build_data.py            # write data/ (and remove stale compiled files)
    python tools/build_data.py --check    # fail if data/ is out of date with source/ (used by CI)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_lib.common import DATA, TIERS, dump_json, force_utf8_stdout, rel
from archive_lib.compiler import compile_entity, iter_compiled, names_from_registry
from archive_lib.registry import Registry, data_path


def main(argv=None):
    force_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="verify data/ matches source/ without writing")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    reg = Registry.load()
    names = names_from_registry(reg)
    for i in reg.parse_report.errors:
        print(i)
    expected, stale, changed = set(), [], []
    for e in reg.entities:
        if not e.id or not e.type:
            continue
        try:
            recs = compile_entity(e, names)
        except Exception as ex:
            print(f"[ERROR  ] compile      {rel(e.path)}: {ex}")
            reg.parse_report.error("compile", rel(e.path), str(ex))
            continue
        for t in TIERS:
            p = data_path(e, t)
            expected.add(p.resolve())
            new = json.dumps(recs[t], ensure_ascii=False, indent=2) + "\n"
            old = p.read_text(encoding="utf-8") if p.exists() else None
            if old != new:
                changed.append(p)
                if not args.check:
                    dump_json(p, recs[t])
    for p, _ in iter_compiled():
        if p.resolve() not in expected:
            stale.append(p)
            if not args.check:
                p.unlink()
    if not args.check:
        for d in sorted(DATA.rglob("*"), key=lambda x: -len(x.parts)):
            if d.is_dir() and d.name != "indexes" and not any(d.iterdir()):
                d.rmdir()
    n = len(reg.entities)
    if args.check:
        if changed or stale:
            for p in changed[:20]:
                print("out of date:", rel(p))
            for p in stale[:20]:
                print("stale (no source):", rel(p))
            print(f"data/ is out of date: {len(changed)} changed, {len(stale)} stale. Run: python tools/build_data.py")
            return 1
        if not args.quiet:
            print(f"data/ is up to date ({n} entities, {n * 4} tier files)")
    elif not args.quiet:
        print(f"compiled {n} entities -> {len(expected)} tier files ({len(changed)} written, {len(stale)} stale removed)")
    return 1 if reg.parse_report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
