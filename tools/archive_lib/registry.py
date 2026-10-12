from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .common import DATA, SOURCE, TIERS, Report, entity_types, rel, slug_of
from .source import Entity, SourceError, iter_source_files, parse_file

SCHEMA_FOR_TYPE = {
    "character": "character.schema.json",
    "npc": "npc.schema.json",
    "historical_figure": "npc.schema.json",
    "location": "location.schema.json",
    "faction": "faction.schema.json",
    "item": "item.schema.json",
    "system": "ability.schema.json",
    "quest": "quest.schema.json",
    "timeline_event": "timeline-event.schema.json",
}
CARD_TYPES = ("character", "npc", "historical_figure")


def schema_for(entity_type: str) -> str:
    return SCHEMA_FOR_TYPE.get(entity_type, "lore-entry.schema.json")


def type_root(entity_type: str) -> str:
    return entity_types()[entity_type]["root"]


def expected_source_dir(e: Entity) -> Path:
    root = type_root(e.type)
    sub = e.header.get("subdir")
    return SOURCE / root / sub if sub else SOURCE / root


def data_path(e: Entity, tier: str) -> Path:
    relative = e.path.parent.relative_to(SOURCE)
    return DATA / relative / f"{e.path.stem}-{tier}.json"


def has_card(e: Entity) -> bool:
    if e.type not in CARD_TYPES:
        return False
    flag = (e.header.get("facts") or {}).get("card")
    if flag is None:
        return e.type in ("character", "npc")
    return bool(flag)


@dataclass
class Registry:
    entities: list = field(default_factory=list)
    by_id: dict = field(default_factory=dict)
    parse_report: Report = field(default_factory=Report)

    @classmethod
    def load(cls, root: Path = SOURCE) -> "Registry":
        reg = cls()
        for p in iter_source_files(root):
            try:
                e = parse_file(p)
            except SourceError as ex:
                reg.parse_report.error("parse", rel(p), str(ex))
                continue
            except UnicodeDecodeError as ex:
                reg.parse_report.error("parse", rel(p), f"not UTF-8: {ex}")
                continue
            reg.entities.append(e)
            if e.id in reg.by_id:
                reg.parse_report.error("duplicate", rel(p), f"id {e.id} already used by {rel(reg.by_id[e.id].path)}")
            elif e.id:
                reg.by_id[e.id] = e
        return reg

    def name_of(self, entity_id) -> str | None:
        e = self.by_id.get(entity_id)
        return e.name if e else None

    def nation_name(self, e: Entity) -> str | None:
        nid = e.header.get("nation")
        if e.type == "location" and (e.header.get("facts") or {}).get("location_type") == "nation":
            return e.name
        return self.name_of(nid) if nid else None

    def alias_map(self):
        out = {}
        for e in self.entities:
            for a in [e.name] + list(e.header.get("aliases") or []):
                out.setdefault(a.strip().lower(), set()).add(e.id)
        return out


def manifest_names() -> dict:
    import json
    from .common import COVERAGE
    out = {}
    for p in sorted(COVERAGE.glob("*.json")):
        try:
            for it in json.loads(p.read_text(encoding="utf-8")).get("items", []):
                out[it["id"]] = it["name"]
        except Exception:
            continue
    return out


def tiers():
    return TIERS


def slug_matches(e: Entity) -> bool:
    try:
        return e.path.stem == slug_of(e.id)
    except Exception:
        return False
