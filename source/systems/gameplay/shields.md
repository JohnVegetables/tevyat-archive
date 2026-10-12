---
{
  "id": "system.shields",
  "entity_type": "system",
  "subdir": "gameplay",
  "name": "Shield",
  "aliases": ["Shields", "character shield", "Crystallize shield"],
  "summary_line": "A shield is a protective barrier that absorbs damage before a character's HP; party shields come from Crystallize shards, talents, Constellations and some weapons, while enemy shields are separate wards.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": ["system.crystallize", "system.elemental-resonance", "system.elemental-mastery", "system.talents", "system.constellations", "character.kachina", "creature.geovishap"],
  "facts": {"system_type": "gameplay_mechanic", "lore_status": "mixed", "element": null},
  "uncertainties": [
    {"topic": "In-world nature of shields", "classification": "unknown", "note": "Canon text describes barriers and protective elemental constructs individually but does not define 'shield' as one system; the numerical rules are gameplay only."}
  ],
  "wi": {"keys": ["Shield Strength", "Crystallize shield", "elemental shield", "character shield"]},
  "sources": [
    {"title": "Shield", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Shield", "accessed": "2026-10-12", "confidence": "medium", "section": "Character Shields, Improving Shields, Enemy Shields", "version": "1.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
A shield is a barrier that takes damage in place of a character's HP. Characters gain them by collecting Crystallize shards or through certain talents, Constellations and weapons. Most are elemental and resist their own element especially well. Enemies have separate shields called wards.
### STANDARD +
Shield Strength is the stat that makes a character's shields hold up better.

## in_universe
### LITE
In the world, shields appear as protective barriers: a wall of crystal or stone, a sheath of an element, or a bubble of energy. Characters do not speak of Shield Strength or absorption bonuses.
### STANDARD +
Crystallize shards come from a Crystallize reaction, and the Geovishap Hatchling is a creature whose Geo shards give a Geo shield on contact.

## gameplay
### LITE
Gameplay: damage hits the shield's health first, and only the excess reaches the character. A shield that times out is destroyed, which can trigger effects such as Kachina's Constellation. If a character has several shields, one hit affects all of them at once.
### STANDARD +
Elemental shields absorb their own element at 250 percent, so they take only 40 percent as much damage from it. Geo shields absorb every damage type at 150 percent. Crystallize shields get health from the level and Elemental Mastery of whoever caused the reaction. Talent and Constellation shields usually scale with DEF, ATK, Max HP or Elemental Mastery, and some add further absorption that multiplies with the base bonus.
### LARGE +
Shield Strength of the active character scales incoming damage down further, and the same factor applies to excess damage. Some shields cover nearby party members, including in Co-Op Mode. Improvements include the Geo Elemental Resonance Enduring Rock (15 percent more shield strength), plus certain talents, Constellations, food, artifacts and weapons.
### ULTRA +
Enemy shields behave differently. They appear as an extra durability bar called a ward; a few are elementless and act as extra HP, but most are elemental and are broken most efficiently (or only) with elemental reactions. Some wards decay over time, while others only reduce the damage the enemy takes instead of blocking it all.

## roleplay
### STANDARD
Roleplay (this project's interpretation, not canon): describe a shield as a visible barrier of crystal, stone or elemental energy that breaks and fades. Avoid percentages in character.

## limits
### STANDARD
Gameplay: absorption bonuses and Shield Strength figures are mechanics. They do not appear in character dialogue, and canon never states how much a barrier can take.
