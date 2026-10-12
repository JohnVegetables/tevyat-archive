import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from archive_lib.common import force_utf8_stdout

force_utf8_stdout()


def finish(report, args, fail_on_warnings=False):
    report.print(show_info=getattr(args, "verbose", False), limit=None if getattr(args, "all", False) else 200)
    if report.errors or (fail_on_warnings and report.warnings):
        return 1
    return 0


def add_common(ap):
    ap.add_argument("-v", "--verbose", action="store_true", help="also show info-level notes")
    ap.add_argument("--all", action="store_true", help="do not truncate the issue list")
