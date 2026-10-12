from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from .common import TIERS, vkey

HEADING2 = re.compile(r"^##\s+(.+?)\s*$")
HEADING3 = re.compile(r"^###\s+(LITE|STANDARD|LARGE|ULTRA)\s*(\+)?\s*$")
ATTR = re.compile(r"^@([a-z_0-9]+)\s*:\s*(.*?)\s*$")
INLINE_ATTR = re.compile(r"\s@([a-z_0-9]+)\s*:\s*[\w.]+\s*$")
FIELD_NAME =re.compile(r"^[a-z][a-z0-9_]*$")
COMMENT = re.compile(r"<!--.*?-->", re.S)

LIST_ATTRS = {"keys", "keys2", "related"}
ENUMS = {
    "logic": {"and_any", "not_all", "not_any", "and_all"},
    "availability": {"permanent", "limited", "removed"},
    "spoiler": {"none", "minor", "major"},
}
KNOWN_ATTRS = LIST_ATTRS | set(ENUMS) | {"order", "constant", "version", "book", "label", "id"}


class SourceError(Exception):
    pass


@dataclass
class Section:
    name: str
    kind: str
    title: str
    attrs: dict = field(default_factory=dict)
    blocks: dict = field(default_factory=dict)
    line: int = 0

    def resolved(self) -> dict:
        out, cur = {}, None
        for t in TIERS:
            if t in self.blocks:
                text, append = self.blocks[t]
                if append:
                    if cur is None:
                        raise SourceError(f"line {self.line}: '### {t} +' in '{self.name}' has nothing to append to")
                    cur = cur.rstrip() + "\n\n" + text
                else:
                    cur = text
            out[t] = cur
        return out

    def first_tier(self):
        for t in TIERS:
            if t in self.blocks:
                return t
        return None


@dataclass
class Entity:
    path: Path
    header: dict
    sections: list
    raw_hash: str

    @property
    def id(self):
        return self.header.get("id")

    @property
    def type(self):
        return self.header.get("entity_type")

    @property
    def name(self):
        return self.header.get("name")

    def section(self, name):
        for s in self.sections:
            if s.name == name:
                return s
        return None


def _parse_attr(name, value, where):
    if name not in KNOWN_ATTRS:
        raise SourceError(f"{where}: unknown attribute @{name}")
    if name in LIST_ATTRS:
        return [v.strip() for v in value.split(",") if v.strip()]
    if name in ENUMS:
        if value not in ENUMS[name]:
            raise SourceError(f"{where}: @{name} must be one of {sorted(ENUMS[name])}, got {value!r}")
        return value
    if name == "order":
        try:
            return int(value)
        except ValueError:
            raise SourceError(f"{where}: @order must be an integer")
    if name == "constant":
        if value.lower() not in ("true", "false"):
            raise SourceError(f"{where}: @constant must be true or false")
        return value.lower() == "true"
    if name == "version":
        vkey(value)
        return value
    return value


def parse_text(text: str, path: Path) -> Entity:
    raw_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    text = text.replace("\r\n", "\n").lstrip("﻿")
    if not text.startswith("---\n"):
        raise SourceError("file must start with a '---' line followed by the JSON header")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SourceError("JSON header is not closed with a '---' line")
    try:
        header = json.loads(text[4:end])
    except json.JSONDecodeError as e:
        raise SourceError(f"JSON header: {e}")
    if not isinstance(header, dict):
        raise SourceError("JSON header must be an object")
    header_lines = text[: end + 5].count("\n")
    body = COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text[end + 5:])

    sections, cur, tier, buf, seen = [], None, None, [], set()

    def flush():
        nonlocal buf
        if cur is not None and tier is not None:
            content = "\n".join(buf).strip("\n").rstrip()
            if not content.strip():
                raise SourceError(f"line {cur.line}: empty '### {tier}' block in '{cur.name}'")
            cur.blocks[tier] = (content, cur.blocks.get(tier, ("", False))[1])
        buf = []

    for n, line in enumerate(body.split("\n"), start=header_lines + 1):
        m2 = HEADING2.match(line)
        m3 = HEADING3.match(line)
        if m2 and not line.startswith("###"):
            flush()
            name = m2.group(1).strip()
            if name.lower().startswith("entry:"):
                title = name.split(":", 1)[1].strip()
                if not title:
                    raise SourceError(f"line {n}: entry heading needs a title")
                kind, key = "entry", f"entry: {title}"
            else:
                if not FIELD_NAME.match(name):
                    raise SourceError(f"line {n}: section name {name!r} must be lowercase_with_underscores or 'entry: Title'")
                kind, key, title = "field", name, name
            if key in seen:
                raise SourceError(f"line {n}: duplicate section '{key}'")
            seen.add(key)
            cur, tier = Section(key, kind, title, line=n), None
            sections.append(cur)
            continue
        if m3:
            flush()
            if cur is None:
                raise SourceError(f"line {n}: tier heading before any '##' section")
            t, append = m3.group(1), bool(m3.group(2))
            if t in cur.blocks:
                raise SourceError(f"line {n}: duplicate '### {t}' in '{cur.name}'")
            if TIERS.index(t) < max([TIERS.index(x) for x in cur.blocks] or [-1]):
                raise SourceError(f"line {n}: tier blocks in '{cur.name}' must be in order LITE, STANDARD, LARGE, ULTRA")
            tier = t
            cur.blocks[t] = ("", append)
            continue
        if cur is not None and tier is None:
            ma = ATTR.match(line)
            if ma:
                cur.attrs[ma.group(1)] = _parse_attr(ma.group(1), ma.group(2), f"line {n}")
                continue
            if line.strip():
                raise SourceError(f"line {n}: text in '{cur.name}' before any '### TIER' heading")
            continue
        if cur is None:
            if line.strip():
                raise SourceError(f"line {n}: text before the first '##' section")
            continue
        ma = ATTR.match(line.strip()) or INLINE_ATTR.search(line)
        if ma and ma.group(1) in KNOWN_ATTRS:
            raise SourceError(f"line {n}: @{ma.group(1)} inside a '### {tier}' block; attributes go after the '##' heading")
        buf.append(line)
    flush()
    for s in sections:
        if not s.blocks:
            raise SourceError(f"line {s.line}: section '{s.name}' has no tier blocks")
        if s.kind == "entry":
            s.title = s.attrs.get("label", s.title)
        s.resolved()
    return Entity(path=path, header=header, sections=sections, raw_hash=raw_hash)


def parse_file(path: Path) -> Entity:
    return parse_text(path.read_text(encoding="utf-8"), path)


def iter_source_files(root: Path):
    for p in sorted(root.rglob("*.md")):
        if p.name.lower() in ("readme.md",) or p.name.startswith("_"):
            continue
        yield p


def section_visible(attrs: dict, max_version=None, permanent_only=False) -> bool:
    if max_version and attrs.get("version") and vkey(attrs["version"]) > vkey(max_version):
        return False
    if permanent_only and attrs.get("availability") in ("limited", "removed"):
        return False
    return True


def resolve(entity: Entity, tier: str, max_version=None, permanent_only=False):
    fields, entries = {}, []
    for s in entity.sections:
        text = s.resolved()[tier]
        if text is None or not section_visible(s.attrs, max_version, permanent_only):
            continue
        if s.kind == "field":
            fields[s.name] = {"text": text, "attrs": dict(s.attrs)}
        else:
            entries.append({"title": s.title, "text": text, "attrs": dict(s.attrs)})
    return fields, entries
