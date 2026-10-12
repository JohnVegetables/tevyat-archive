---
{
  "id": "system.hyperbloom",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Hyperbloom",
  "aliases": ["Hyperbloom reaction", "Electro Bloom reaction", "Sprawling Shot"],
  "summary_line": "Hyperbloom is the elemental reaction in which Electro strikes a Dendro Core, turning it into a homing Sprawling Shot that hits the nearest enemy with a small, strong Dendro burst.",
  "introduced_in": "3.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.bloom", "system.burgeon", "system.electro", "system.dendro", "system.hydro",
    "system.lunar-bloom", "system.quicken", "system.elemental-mastery", "system.elemental-resonance", "character.traveler"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Dendro"},
  "uncertainties": [
    {"topic": "In-universe cause of Hyperbloom", "classification": "unknown", "note": "The pages read describe Hyperbloom only as a combat rule and tutorial text; no story source explains why lightning turns a Dendro Core into a projectile."},
    {"topic": "Separate page", "classification": "unknown", "note": "The wiki has no page of its own for Hyperbloom; the name redirects to the Bloom page, where it is a section. Bloom is its own entity (system.bloom)."},
    {"topic": "Lunar-Bloom cores", "classification": "inferred", "note": "The wiki says Lunar-Bloom spawns a Dendro Core or Bountiful Core as well as granting Verdant Dew. The pages read do not state whether Hyperbloom is possible on a core made that way; only the Bountiful Core exclusion is stated."}
  ],
  "sources": [
    {"title": "Bloom", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Bloom", "accessed": "2026-10-12", "confidence": "high", "section": "Dendro Core, Bountiful Core, Damage, Talents, Trivia", "version": "3.0"},
    {"title": "Elemental Reactions", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reactions", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table, Transformative Reactions"},
    {"title": "Version 3.0", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Version/3.0", "accessed": "2026-10-12", "confidence": "high", "section": "New Dendro reactions; Sprawling Greenery and High Voltage resonance changes", "version": "3.0"},
    {"title": "Lunar-Bloom", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Lunar-Bloom", "accessed": "2026-10-12", "confidence": "medium", "section": "Damage, Verdant Dew"},
    {"title": "Elemental Reaction: Bloom (tutorial)", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Bloom", "accessed": "2026-10-12", "confidence": "medium", "section": "Tutorial (as summarised in the Version 3.0 reaction list)", "version": "3.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Hyperbloom is a Dendro elemental reaction. When Electro touches a Dendro Core (the orb a Bloom leaves behind), the core becomes a homing projectile, a Sprawling Shot, which flies to the closest enemy and bursts in a small area for strong Dendro damage. It is the Electro counterpart of Burgeon.
### STANDARD +
It debuted in Version 3.0 with Bloom, Burgeon, Quicken, Spread and Aggravate, the reactions introduced for Dendro. A Bloom, from Dendro and Hydro, has to make the core first.

## in_universe
### LITE
Canon gives no in-world explanation for Hyperbloom. The pages read treat it only as a combat rule, so it is best understood as a charged seed of plant energy flung at a foe.

## gameplay
### LITE
Gameplay: when Electro is applied to a Dendro Core, Hyperbloom triggers. The core turns into a Sprawling Shot that homes in on the nearest enemy and deals Dendro area damage on impact.
### STANDARD +
- The shot hits in a small radius of 1 m, compared with the 5 m burst of Burgeon, and the wiki lists it with increased damage over an ordinary Bloom core.
- If an enemy or the environment triggers it, the shot homes in on the closest ally instead. The wiki adds that the Lea Lotus Lamp made by the Dendro Traveler's Elemental Burst counts as a target for Hyperbloom in that case.
- The damage hits enemies and players alike; damage to players from Bloom-related reactions is 2% of the damage to enemies.
- It can be triggered by a party other than the one that made the Bloom, including the environment, and its damage scales with the party that applied the Electro.
- Hyperbloom is a transformative reaction: it does its own damage, based on the triggering character's level and Elemental Mastery, and ignores ATK and cannot critically strike unless a talent or constellation allows it.
### LARGE +
- A target can take only two instances of damage from each Bloom-related reaction per source every 0.5 seconds, separately for each triggering character.
- Hyperbloom cannot be triggered on Bountiful Cores, the quick-bursting cores some abilities and event buffs make in place of ordinary Dendro Cores. They share the limit of five cores with normal ones.
- Electro is also the other half of the Quicken family: Electro on a Dendro-affected target starts Quicken, and Spread and Aggravate follow (own entries).
### ULTRA +
- Version 3.0 added the Dendro Elemental Resonance Sprawling Greenery, which gives nearby party members 20 Elemental Mastery for 6 seconds after Hyperbloom (or Spread, Aggravate, Burgeon), against 30 for Burning, Quicken or Bloom. The same patch adjusted the Electro Resonance High Voltage so that Hyperbloom has a guaranteed chance to generate an Electro Elemental Particle, with a 5-second cooldown.
- The wiki lists talents, constellations and artifacts that raise Hyperbloom damage, let it critically strike or add flat damage; these are character-specific and not detailed here.
- Lunar-Bloom (the Moonsign version of the Dendro-Hydro reaction, which the wiki says replaces Bloom) also spawns a core. Treat Lunar-Bloom as a separate reaction.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show a green, lumpy seed of energy hanging in the air, a crackle of lightning touching it, and the seed lunging away in a streak of sparking vines to strike a target. Keep it quick and precise rather than a huge blast.
### LARGE +
It reads best as a team move: one person coaxes the seed out with water and plants, another sends a bolt into it. The seed seeks its target by itself, so it suits enemies that are spread out or hard to reach. Scale it to a skirmish.
### ULTRA +
Avoid having Hyperbloom work with no core present, avoid claiming a Dendro-only or Electro-only user can do it alone, and avoid giving it an origin story. Do not have the shot chase a target indefinitely or across a battlefield; it is a short-range homing burst.

## limits
### LITE
Hyperbloom needs a Dendro Core, so it needs Bloom first. It does nothing to a Bountiful Core.
### STANDARD +
The shot can hurt the party too, though far less than it hurts enemies. The core vanishes after its duration if its creator has left the party.

## examples
### STANDARD
Gameplay example: Hydro and Dendro together leave a Dendro Core. An Electro attack on it triggers Hyperbloom at once and a Sprawling Shot homes in on the nearest enemy.

## entry: Sprawling Shot
@keys: Sprawling Shot
### STANDARD
The Sprawling Shot is the homing projectile that a Dendro Core becomes when Electro triggers Hyperbloom. It deals Dendro area damage in a small radius on impact and seeks the nearest enemy, or ally if an enemy or the environment set it off.

## entry: Dendro Core
@keys: Dendro Core, Dendro Cores
@keys2: Hyperbloom, Burgeon, Bloom
### STANDARD
A Dendro Core is what the Bloom reaction (Dendro with Hydro) leaves behind. If left alone it bursts after about six seconds. Pyro on it triggers Burgeon, Electro triggers Hyperbloom. No more than five can exist at a time.
