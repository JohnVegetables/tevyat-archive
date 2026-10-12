from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

ROOT = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source"
DATA = ROOT / "data"
CONFIG = ROOT / "config"
SCHEMAS = ROOT / "schemas"
COVERAGE = ROOT / "coverage"
ST_OUT = ROOT / "sillytavern"
BUNDLES = ROOT / "bundles"
REPORTS = ROOT / "reports"

TIERS = ("LITE", "STANDARD", "LARGE", "ULTRA")


def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, obj, indent=2):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=indent) + "\n"
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)


@lru_cache(maxsize=None)
def config(name: str):
    return load_json(CONFIG / f"{name}.json")


def cutoff_version() -> str:
    return config("canon-cutoff")["cutoff_version"]


def vkey(version: str | None):
    if not version:
        return (0, 0)
    m = re.match(r"^(\d+)\.(\d+)", str(version).strip())
    if not m:
        raise ValueError(f"bad version string: {version!r}")
    return (int(m.group(1)), int(m.group(2)))


def entity_types():
    return config("naming-conventions")["entity_types"]


def prefix_for(entity_type: str) -> str:
    return entity_types()[entity_type]["prefix"]


ID_RE = re.compile(r"^[a-z]+\.[a-z0-9]+(?:-[a-z0-9]+)*$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def slug_of(entity_id: str) -> str:
    return entity_id.split(".", 1)[1]


def safe_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", name).strip().rstrip(".")


@dataclass
class Issue:
    level: str
    check: str
    where: str
    message: str

    def __str__(self):
        return f"[{self.level.upper():7}] {self.check:12} {self.where}: {self.message}"


@dataclass
class Report:
    issues: list = field(default_factory=list)

    def add(self, level, check, where, message):
        self.issues.append(Issue(level, check, str(where), message))

    def error(self, check, where, message):
        self.add("error", check, where, message)

    def warn(self, check, where, message):
        self.add("warning", check, where, message)

    def info(self, check, where, message):
        self.add("info", check, where, message)

    @property
    def errors(self):
        return [i for i in self.issues if i.level == "error"]

    @property
    def warnings(self):
        return [i for i in self.issues if i.level == "warning"]

    def extend(self, other: "Report"):
        self.issues.extend(other.issues)

    def print(self, show_info=False, limit=None):
        shown = 0
        for i in sorted(self.issues, key=lambda x: ({"error": 0, "warning": 1, "info": 2}[x.level], x.check, x.where)):
            if i.level == "info" and not show_info:
                continue
            print(i)
            shown += 1
            if limit and shown >= limit:
                rest = len(self.issues) - shown
                if rest > 0:
                    print(f"... {rest} more (use --all)")
                break
        print(f"\n{len(self.errors)} error(s), {len(self.warnings)} warning(s)")


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def force_utf8_stdout():
    import sys
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
