#!/usr/bin/env python3
"""Run every offline check. This is what CI runs.

    python tools/validate.py                 # all checks, exit 1 on any error
    python tools/validate.py --file source/characters/playable/amber.md   # one source file
    python tools/validate.py --strict        # warnings also fail
    python tools/validate.py -v --all        # show info notes, do not truncate

Order: parse+schema -> sections -> sources/cutoff -> references/aliases -> data/ in sync ->
tier consistency + World Info keys -> exports -> coverage -> docs.
Network access is never needed.
"""
import argparse
import sys
from pathlib import Path

import _cli
from archive_lib.checks import (check_aliases, check_coverage, check_docs, check_exports, check_keys, check_manifests,
                                check_references, check_schema, check_sections, check_sources, check_tier_consistency)
from archive_lib.common import Report, rel
from archive_lib.compiler import compile_entity, load_compiled_by_id, names_from_registry
from archive_lib.registry import Registry


def validate_one(path: Path, args):
    """Fast feedback for authors: checks a single file against the whole registry."""
    reg = Registry.load()
    target = path.resolve()
    one = [e for e in reg.entities if e.path.resolve() == target]
    rep = Report()
    rep.extend(Report([i for i in reg.parse_report.issues if Path(i.where).name == path.name]))
    if not one:
        if not rep.issues:
            rep.error("parse", rel(path), "file not found among source files (must be under source/ and end in .md)")
        return _cli.finish(rep, args)
    e = one[0]
    sub = Registry(entities=one, by_id=reg.by_id)
    for fn in (check_schema, check_sections, check_sources, check_references):
        r = fn(sub)
        rep.extend(Report([i for i in r.issues if i.check != "parse"]))
    try:
        recs = compile_entity(e, names_from_registry(reg))
        r = check_tier_consistency({e.id: recs})
        r.extend(check_keys({e.id: recs}))
        rep.extend(r)
        for t, rec in recs.items():
            rep.info("stats", t, f"budget text {rec['stats']['budget_tokens']} tokens, sub-entries {rec['stats']['entries_tokens']} tokens, {rec['stats']['entries']} entries")
    except Exception as ex:
        rep.error("compile", rel(path), str(ex))
    return _cli.finish(rep, args, args.strict)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    _cli.add_common(ap)
    ap.add_argument("--file", help="validate a single source file")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--skip-coverage", action="store_true", help="do not fail on missing roster entries")
    args = ap.parse_args(argv)
    if args.file:
        return validate_one(Path(args.file), args)

    reg = Registry.load()
    rep = Report()
    steps = [("schema", lambda: check_schema(reg)), ("sections", lambda: check_sections(reg)),
             ("sources", lambda: check_sources(reg)), ("references", lambda: check_references(reg)),
             ("aliases", lambda: check_aliases(reg)), ("manifests", check_manifests)]
    for name, fn in steps:
        rep.extend(fn())
    import build_data
    if build_data.main(["--check", "--quiet"]) != 0:
        rep.error("data", "data/", "compiled data is out of date: run python tools/build_data.py")
    compiled = load_compiled_by_id()
    rep.extend(check_tier_consistency(compiled))
    rep.extend(check_keys(compiled))
    ex_rep, export_ok = check_exports()
    rep.extend(ex_rep)
    cov = check_coverage(reg, compiled, export_ok)
    if args.skip_coverage:
        for i in cov.issues:
            if i.level == "error":
                i.level = "warning"
    rep.extend(cov)
    rep.extend(check_docs())
    print(f"checked {len(reg.entities)} source entities, {len(compiled)} compiled entities")
    return _cli.finish(rep, args, args.strict)


if __name__ == "__main__":
    sys.exit(main())
