import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "schemas"
S = "https://json-schema.org/draft/2020-12/schema"
ID = {"type": "string", "pattern": "^[a-z]+\\.[a-z0-9]+(?:-[a-z0-9]+)*$"}
VER = {"type": "string", "pattern": "^\\d+\\.\\d+$"}
OPT_VER = {"anyOf": [VER, {"type": "null"}]}
OPT_ID = {"anyOf": [ID, {"type": "null"}]}
NS = {"type": ["string", "null"]}
CLASS = ["confirmed", "strongly_supported", "inferred", "disputed", "unknown", "noncanon"]
ID_LIST = {"$ref": "common.schema.json#/$defs/id_list"}


def W(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


W("source.schema.json", {
    "$schema": S, "$id": "source.schema.json", "title": "Source citation",
    "type": "object", "required": ["title", "type", "confidence"], "additionalProperties": False,
    "properties": {
        "title": {"type": "string", "minLength": 3, "description": "Name of the source: quest, page, item, book, announcement."},
        "type": {"enum": ["in_game_quest", "in_game_profile", "in_game_voiceover", "in_game_text", "in_game_item",
                          "in_game_event", "official_announcement", "official_publication", "official_video", "wiki", "other"]},
        "section": {"type": ["string", "null"], "description": "Chapter, act, section or subpage."},
        "version": {**OPT_VER, "description": "Game version that introduced the cited material, if known."},
        "url": {"type": ["string", "null"], "format": "uri"},
        "accessed": {"type": ["string", "null"], "format": "date"},
        "confidence": {"enum": ["high", "medium", "low"]},
        "notes": NS}})

HEADER_PROPS = {
    "id": ID,
    "entity_type": {"enum": ["character", "npc", "historical_figure", "location", "faction", "lore", "cosmology",
                             "system", "item", "creature", "culture", "quest", "timeline_event", "term", "core"]},
    "subdir": {"type": "string", "pattern": "^[a-z0-9-]+(/[a-z0-9-]+)*$",
               "description": "Directory under the type's root, e.g. 'nations' or 'weapons'."},
    "name": {"type": "string", "minLength": 1},
    "aliases": {"type": "array", "items": {"type": "string", "minLength": 1}, "uniqueItems": True},
    "summary_line": {"type": "string", "minLength": 10, "maxLength": 300},
    "nation": OPT_ID,
    "tags": {"type": "array", "items": {"type": "string"}},
    "introduced_in": VER,
    "spoiler_level": {"enum": ["none", "minor", "major"]},
    "availability": {"enum": ["permanent", "limited", "removed", "mixed"]},
    "related": ID_LIST,
    "relationships": {"type": "array", "items": {"$ref": "#/$defs/relationship"}},
    "knowledge": {"$ref": "#/$defs/knowledge"},
    "uncertainties": {"type": "array", "items": {"$ref": "#/$defs/uncertainty"}},
    "sources": {"$ref": "#/$defs/sources"},
    "status": {"enum": ["researching", "drafted", "needs_verification", "verified"]},
    "last_verified": {"type": ["string", "null"], "format": "date"},
    "wi": {"$ref": "#/$defs/wi"},
    "notes": NS,
    "facts": {"type": "object"},
}

W("common.schema.json", {"$schema": S, "$id": "common.schema.json", "title": "Shared definitions", "$defs": {
    "id": ID, "version": VER,
    "id_list": {"type": "array", "items": ID, "uniqueItems": True},
    "classification": {"enum": CLASS},
    "sources": {"type": "array", "minItems": 1, "items": {"$ref": "source.schema.json"}},
    "relationship": {"type": "object", "required": ["target", "type", "summary"], "additionalProperties": False, "properties": {
        "target": ID, "type": {"type": "string", "minLength": 2}, "summary": {"type": "string", "minLength": 5},
        "classification": {"enum": CLASS}, "since": OPT_VER}},
    "uncertainty": {"type": "object", "required": ["topic", "classification", "note"], "additionalProperties": False, "properties": {
        "topic": {"type": "string", "minLength": 3}, "classification": {"enum": CLASS}, "note": {"type": "string", "minLength": 5}}},
    "knowledge": {"type": "object", "additionalProperties": False, "properties": {
        "knows": {"type": "array", "items": {"type": "object", "required": ["fact", "visibility"], "additionalProperties": False, "properties": {
            "fact": {"type": "string", "minLength": 5}, "learned": NS, "version": OPT_VER,
            "visibility": {"enum": ["public", "secret", "restricted", "disputed"]}}}},
        "does_not_know": {"type": "array", "items": {"type": "object", "required": ["fact"], "additionalProperties": False, "properties": {
            "fact": {"type": "string", "minLength": 5}, "note": NS}}},
        "believes": {"type": "array", "items": {"type": "object", "required": ["belief", "reality", "classification"], "additionalProperties": False, "properties": {
            "belief": {"type": "string"}, "reality": {"type": "string"}, "classification": {"enum": CLASS}}}}}},
    "wi": {"type": "object", "additionalProperties": False, "properties": {
        "keys": {"type": "array", "items": {"type": "string", "minLength": 2}},
        "keys2": {"type": "array", "items": {"type": "string", "minLength": 2}},
        "logic": {"enum": ["and_any", "not_all", "not_any", "and_all"]},
        "order": {"type": "integer"}, "constant": {"type": "boolean"}, "book": {"type": "string"},
        "exclude": {"type": "boolean", "description": "Do not emit a main World Info entry for this entity."}}},
    "header_common": {"type": "object",
                      "required": ["id", "entity_type", "name", "aliases", "summary_line", "introduced_in", "spoiler_level", "sources", "status"],
                      "properties": HEADER_PROPS}}})


def entity_schema(fname, title, types, facts_props, facts_required=()):
    W(fname, {"$schema": S, "$id": fname, "title": title,
              "description": f"JSON header of a {title} source file (source/**/<slug>.md).",
              "allOf": [{"$ref": "common.schema.json#/$defs/header_common"}],
              "type": "object", "additionalProperties": False,
              "properties": {**{k: True for k in HEADER_PROPS},
                             "entity_type": {"enum": types},
                             "facts": {"type": "object", "required": list(facts_required), "additionalProperties": False,
                                       "properties": facts_props}}})


PERSON = {
    "full_name": NS,
    "title": {"type": ["string", "null"], "description": "In-game profile title, if any."},
    "pronouns": NS, "species": NS, "origin": OPT_ID, "residence": OPT_ID, "occupation": NS,
    "affiliations": ID_LIST,
    "vision": {"type": ["string", "null"], "description": "Vision element, or e.g. 'none', 'Delusion', 'Gnosis', 'Archon power', 'unknown'."},
    "element": NS,
    "weapon": {"enum": ["Sword", "Claymore", "Polearm", "Bow", "Catalyst", None]},
    "rarity": {"enum": [4, 5, None]},
    "constellation": NS,
    "birthday": {"type": ["string", "null"], "pattern": "^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", "description": "MM-DD, only if official."},
    "age": {"type": ["string", "null"], "description": "Only if canon states it; otherwise null."},
    "height": {"type": ["string", "null"], "description": "Only if verified; the body model category is not a height."},
    "body_type": {"enum": ["tall male", "medium male", "short male", "tall female", "medium female", "short female", "other", None]},
    "playable": {"type": "boolean"},
    "release_version": OPT_VER,
    "card": {"type": "boolean", "description": "Generate a SillyTavern character card."},
    "status_flag": {"enum": ["alive", "dead", "presumed_dead", "missing", "sealed", "unknown", "not_applicable"]},
    "era": NS, "identity_notes": NS}

entity_schema("character.schema.json", "playable character", ["character"], PERSON, ["playable", "release_version", "status_flag"])
entity_schema("npc.schema.json", "major non-playable or historical character", ["npc", "historical_figure"], PERSON, ["status_flag"])
entity_schema("location.schema.json", "location", ["location"], {
    "location_type": {"enum": ["realm", "continent", "nation", "region", "subregion", "city", "district", "settlement", "village",
                               "outpost", "landmark", "building", "institution", "sacred_site", "domain", "ruin", "ancient_city",
                               "underground", "island", "water", "route", "other_realm", "cosmological"]},
    "parent": OPT_ID, "region": NS, "ruler": NS, "archon": OPT_ID, "element": NS, "civilisation": NS, "current_state": NS,
    "release_version": OPT_VER, "accessible_in_game": {"type": ["boolean", "null"]}}, ["location_type"])
entity_schema("faction.schema.json", "faction or organisation", ["faction"], {
    "faction_type": {"enum": ["government", "military", "religious", "scholarly", "criminal", "mercantile", "secret_society",
                              "historical", "guild", "tribe", "household", "other"]},
    "leaders": ID_LIST, "leader_note": NS, "headquarters": OPT_ID, "parent_org": OPT_ID, "founded": NS, "current_status": NS,
    "operating_areas": ID_LIST}, ["faction_type"])
entity_schema("item.schema.json", "item, weapon, artifact or material", ["item"], {
    "item_type": {"enum": ["weapon", "weapon_type", "artifact_set", "relic", "quest_item", "book", "material", "consumable", "food",
                           "gadget", "currency", "instrument", "device", "ceremonial", "other"]},
    "weapon_type": {"enum": ["Sword", "Claymore", "Polearm", "Bow", "Catalyst", None]},
    "rarity": {"type": ["integer", "null"], "minimum": 1, "maximum": 5},
    "owners": ID_LIST, "origin": NS, "gameplay_note": NS}, ["item_type"])
entity_schema("ability.schema.json", "power system, element or mechanic", ["system"], {
    "system_type": {"enum": ["element", "reaction", "power_source", "magic", "technology", "biology", "physics", "gameplay_mechanic", "other"]},
    "lore_status": {"enum": ["in_universe", "gameplay_abstraction", "roleplay_adaptation", "mixed"],
                    "description": "In-universe concept, gameplay abstraction, or this project's roleplay interpretation."},
    "element": NS}, ["system_type", "lore_status"])
entity_schema("quest.schema.json", "quest or event", ["quest"], {
    "quest_type": {"enum": ["archon", "interlude", "story", "world", "hangout", "event", "dainsleif", "other"]},
    "chapter": NS, "act": NS, "region": OPT_ID, "version": OPT_VER,
    "characters": ID_LIST, "prerequisites": ID_LIST,
    "story_order": {"type": ["number", "null"], "description": "Position in in-world chronology, if known."}}, ["quest_type"])
entity_schema("timeline-event.schema.json", "historical or story event", ["timeline_event"], {
    "era": NS, "when": {"type": ["string", "null"], "description": "In-world dating as canon gives it, e.g. '500 years ago'."},
    "sort_key": {"type": ["number", "null"], "description": "Approximate in-world order; larger is later; null when unknown."},
    "places": ID_LIST, "participants": ID_LIST, "learned_in": ID_LIST})
entity_schema("lore-entry.schema.json", "lore, cosmology, culture, creature, term or core entry",
              ["lore", "cosmology", "culture", "creature", "term", "core"], {
                  "subject_type": NS, "classification": {"enum": CLASS}, "element": NS, "region": OPT_ID})

W("compiled-tier.schema.json", {
    "$schema": S, "$id": "compiled-tier.schema.json", "title": "Compiled tier file (data/**/<slug>-<TIER>.json)",
    "type": "object",
    "required": ["id", "entity_type", "name", "tier", "schema_version", "canon_cutoff", "source_file", "source_hash", "header", "fields", "entries", "stats"],
    "properties": {
        "id": ID, "entity_type": {"type": "string"}, "name": {"type": "string"},
        "tier": {"enum": ["LITE", "STANDARD", "LARGE", "ULTRA"]},
        "schema_version": {"type": "string"}, "canon_cutoff": VER, "source_file": {"type": "string"}, "source_hash": {"type": "string"},
        "header": {"type": "object"},
        "fields": {"type": "object", "additionalProperties": {"type": "object", "required": ["text"],
                                                               "properties": {"text": {"type": "string", "minLength": 1}, "attrs": {"type": "object"}}}},
        "entries": {"type": "array", "items": {"type": "object", "required": ["title", "text", "attrs"],
                                               "properties": {"title": {"type": "string"}, "text": {"type": "string", "minLength": 1}, "attrs": {"type": "object"}}}},
        "stats": {"type": "object"}}})

W("coverage-manifest.schema.json", {
    "$schema": S, "$id": "coverage-manifest.schema.json", "title": "Coverage manifest (coverage/*.json)",
    "type": "object", "required": ["category", "criteria", "cutoff", "items"], "additionalProperties": False,
    "properties": {
        "category": {"type": "string"}, "criteria": {"type": "string"}, "cutoff": VER, "notes": NS,
        "sources": {"type": "array", "items": {"$ref": "source.schema.json"}},
        "items": {"type": "array", "items": {"type": "object", "required": ["id", "name", "status"], "additionalProperties": False, "properties": {
            "id": ID, "name": {"type": "string"},
            "status": {"enum": ["not_started", "researching", "drafted", "needs_verification", "verified", "complete", "blocked"]},
            "priority": {"enum": ["critical", "high", "normal", "low"]},
            "entity_type": {"enum": ["character", "npc", "historical_figure", "location", "faction", "lore", "cosmology", "system",
                                     "item", "creature", "culture", "quest", "timeline_event", "term", "core"]},
            "nation": OPT_ID,
            "introduced_in": OPT_VER, "subdir": NS, "wiki": NS, "notes": NS, "blocked_reason": NS, "group": NS}}}}})

print("schemas written to", OUT)
