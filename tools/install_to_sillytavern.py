#!/usr/bin/env python3
"""Copy a built bundle straight into a local SillyTavern install (optional convenience).

    python tools/install_to_sillytavern.py --st "C:/path/to/SillyTavern" --tier STANDARD
    python tools/install_to_sillytavern.py --st ~/SillyTavern --tier MIX-focus-mondstadt --user default-user --dry-run

For a point-and-click version with per-character choices and custom greetings, run the desktop importer:
    python tools/importer_app.py

What it does
- World Info files -> <ST>/data/<user>/worlds/  (same-named books are replaced: that is how tiers swap)
- Character cards  -> <ST>/data/<user>/characters/<Name>.png, using a generated plain-colour avatar
  (no game art is ever bundled). An existing PNG with the same name is backed up to *.bak first.
- --activate switches the shared lorebooks on globally in settings.json (backed up first).
Stop SillyTavern first, then refresh the browser tab afterwards.
Build the bundle first with tools/build_bundles.py.
"""
import argparse
import sys
from pathlib import Path

import _cli
from archive_lib.common import ST_OUT
from archive_lib.installer import check_st, install, load_bundle


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--st", required=True, help="SillyTavern folder (the one containing server.js)")
    ap.add_argument("--tier", required=True, help="LITE, STANDARD, LARGE, ULTRA or a MIX-<label>")
    ap.add_argument("--user", default="default-user")
    ap.add_argument("--no-cards", action="store_true")
    ap.add_argument("--activate", action="store_true", help="switch the shared lorebooks on globally")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    st = Path(args.st).expanduser()
    err = check_st(st, args.user)
    if err:
        print(err)
        return 1
    if not (ST_OUT / "manifests" / f"{args.tier}.json").exists():
        print(f"no manifest for {args.tier}; run: python tools/build_bundles.py --tier {args.tier}")
        return 1
    man = load_bundle(args.tier)
    cards = set() if args.no_cards else {c["id"] for c in man["cards"]}
    books = {b["book"] for b in man["world_info"]}
    if args.dry_run:
        print(f"would install {len(books)} world books and {len(cards)} cards into {st / 'data' / args.user}")
        return 0
    res = install(st, args.user, man, cards, books, {}, activate_books=[b["book"] for b in man["shared_books"]] if args.activate else None)
    print(f"\n{res['books']} world books, {res['cards']} cards installed into {st / 'data' / args.user}")
    print("Restart SillyTavern (or refresh the page), then enable the books you want under World Info.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
