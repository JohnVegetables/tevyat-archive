---
{
  "id": "system.physical",
  "entity_type": "system",
  "subdir": "elements",
  "name": "Physical",
  "aliases": ["Physical damage", "Physical DMG", "non-elemental damage"],
  "summary_line": "Physical is the eighth damage type: the plain, non-elemental force of blades, blows and impacts, set apart from the seven elements. It is a game category, not an element with an Archon or Vision.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elements", "system.elemental-reaction", "system.vision", "system.frozen", "system.shattered",
    "system.superconduct", "system.geo", "system.cryo",
    "item.weapon-type-sword", "item.weapon-type-claymore", "item.weapon-type-polearm", "item.weapon-type-bow", "item.weapon-type-catalyst",
    "character.eula", "character.xinyan", "character.freminet", "item.skyward-atlas", "item.bloodstained-chivalry"
  ],
  "facts": {"system_type": "gameplay_mechanic", "lore_status": "gameplay_abstraction", "element": null},
  "uncertainties": [
    {"topic": "Physical as an in-world force", "classification": "unknown", "note": "Canon text never names Physical as a power, Authority or element. It is the game's label for damage that carries no elemental energy; no Archon, Vision, Gnosis or Dragon Sovereign is attached to it."}
  ],
  "sources": [
    {"title": "Physical", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Physical", "accessed": "2026-10-12", "confidence": "high", "section": "Intro, weapon types, skills dealing Physical DMG, artifacts", "version": "1.0"},
    {"title": "Element", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Element", "accessed": "2026-10-12", "confidence": "high", "section": "Seven of the eight damage types; Physical is the eighth"},
    {"title": "Damage", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Damage", "accessed": "2026-10-12", "confidence": "high", "section": "Eight damage types; DMG Bonus; Resistance"},
    {"title": "Physical RES", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/RES/Physical", "accessed": "2026-10-12", "confidence": "high", "section": "Protective Canopy; Superconduct", "version": "1.0"},
    {"title": "Frozen (Shatter)", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "high", "section": "Shatter"},
    {"title": "Claymore", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Claymore", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; blunt attacks and Shatter"},
    {"title": "Sword", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Sword", "accessed": "2026-10-12", "confidence": "high", "section": "Normal and Charged Attacks"},
    {"title": "Catalyst", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Catalyst", "accessed": "2026-10-12", "confidence": "medium"},
    {"title": "Stonehide Lawachurl", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Stonehide_Lawachurl", "accessed": "2026-10-12", "confidence": "high", "section": "Attacks dealing Physical DMG"},
    {"title": "Bloodstained Chivalry", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Bloodstained_Chivalry", "accessed": "2026-10-12", "confidence": "high", "section": "2-piece bonus"},
    {"title": "Pale Flame", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Pale_Flame", "accessed": "2026-10-12", "confidence": "high", "section": "2-piece bonus"},
    {"title": "Ocean-Hued Clam", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Ocean-Hued_Clam", "accessed": "2026-10-12", "confidence": "high", "section": "Sea-Dyed Foam"},
    {"title": "Glacial Illumination", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Glacial_Illumination", "accessed": "2026-10-12", "confidence": "medium", "section": "Lightfall Sword"}
  ],
  "notes": "Purely a gameplay category; no lore of its own. Checked against the wiki as of 7.1; no change to the Physical damage type found in 6.x-7.1.",
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Physical is the eighth damage type in Genshin Impact: ordinary force with no element in it, such as a sword cut, a hammer blow or a crushing impact. The other seven damage types are the elements. Physical has no Archon, nation or Vision. It is a game category rather than a power the story names.
### STANDARD +
Elemental reactions are built from the seven elements, so Physical normally sits outside them. The main exception is Shatter, which deals Physical damage.

## in_universe
### LITE
Canon never presents Physical as a force or Authority. In the story, a strike without elemental energy is just a strike: steel, muscle, teeth, claws or falling stone.
### STANDARD +
This is the main difference from the elements. The elements are tied to Visions, Gnoses, Archons and the Dragon Sovereigns, while Physical has nothing comparable. In narration, treat "Physical" as the absence of elemental energy, not as an eighth element.

## gameplay
### LITE
Gameplay (not literal lore): Sword, Claymore and Polearm attacks deal Physical DMG by default. So do Bow Normal Attacks and Aimed Shots that are not fully charged. Catalyst attacks are inherently elemental, so Catalyst users deal Physical DMG only through extra effects.
### STANDARD +
Some Elemental Skills and Bursts also deal Physical DMG. The wiki's examples are Eula's Glacial Illumination, Xinyan's Riff Revolution and Freminet's Pressurized Floe. Physical DMG Bonus is a stat, found as a character ascension stat, a weapon substat or an artifact bonus (for instance the 2-piece bonus of Bloodstained Chivalry or Pale Flame, +25%). Physical RES is the matching defence. Enemies can deal Physical damage too; the Stonehide Lawachurl's punches, charge and slam are examples.
### LARGE +
- Shatter: a Frozen target hit by a blunt attack (Claymore attacks count) or a Geo attack takes Physical Shatter damage and is unfrozen. It is the best-known source of Physical damage inside the reaction system.
- Superconduct (Electro with Cryo) lowers the enemy's Physical RES by 40% for 12 seconds.
- Elemental Resonance: Protective Canopy (a party of four different elements) raises Physical RES together with all Elemental RES by 15%.
- Catalyst exceptions: some Catalyst weapons, such as Skyward Atlas, and artifact sets such as Ocean-Hued Clam (its Sea-Dyed Foam) can add Physical damage to a Catalyst user. Bonuses to Physical DMG do not all apply: Sea-Dyed Foam is affected by enemy Physical RES but not by Physical DMG Bonus.
### ULTRA +
Damage in general: there are eight damage types, and enemy RES is tracked separately for Elemental and Physical damage. Physical damage applies no element, so it cannot start an elemental reaction. A Physical attack can only unfreeze or shatter a target as described above.

## limits
### LITE
Physical does not react with any element and applies no aura.
### STANDARD +
No Vision or Gnosis grants Physical power. A character cannot "have a Physical element".
### LARGE +
Gameplay: the character stat screen lists Physical DMG Bonus beside the seven Elemental DMG Bonuses, which is why the damage type is easy to mistake for an element.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Physical as weight, edge and momentum: a clean cut, a heavy blow, ground shaking from a slam. It has no signature colour or glow, and nothing about it needs special explanation.
### LARGE +
A sword fighter without a Vision is dangerous because of skill and training, not Physical power. When ice cracks under a hammer blow, that is Shatter, so describe the freeze breaking under force.
### ULTRA +
Avoid calling Physical "the eighth element", linking it to an Archon, or inventing a Physical Vision or resonance.

## entry: Shatter
@keys: Shatter, Shattered, shatter reaction
@spoiler: none
### STANDARD
Shatter is the reaction in which a blunt hit (a Claymore attack, for example) or a Geo attack lands on a target frozen by the Frozen reaction. The ice breaks and the hit deals Physical damage. See the Shattered entry for the full reaction.

## entry: Physical RES
@keys: Physical RES, Physical resistance
@spoiler: none
### STANDARD
Physical RES reduces incoming Physical damage. Protective Canopy resonance, certain talents, constellations, artifacts and dishes can raise it. Superconduct lowers an enemy's Physical RES by 40% for 12 seconds, and some talents, constellations and artifacts can lower it too.
