---
{
  "id": "system.energy",
  "entity_type": "system",
  "subdir": "gameplay",
  "name": "Energy",
  "aliases": ["Elemental Energy", "Energy Recharge", "elemental particles", "elemental orbs"],
  "summary_line": "Energy is the resource needed to use an Elemental Burst, gathered mainly from elemental particles and orbs dropped by Elemental Skills and defeated enemies, and shared in part with the whole party.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": ["system.elemental-burst", "system.elemental-skill", "system.party", "system.elemental-resonance", "system.phlogiston", "system.elements"],
  "facts": {"system_type": "gameplay_mechanic", "lore_status": "mixed", "element": null},
  "uncertainties": [
    {"topic": "Particle and orb lifetimes", "classification": "unknown", "note": "The wiki gives about 30 seconds for particles and 9 seconds for orbs but flags the exact times as needing verification."},
    {"topic": "How game Energy relates to elemental energy in lore", "classification": "inferred", "note": "Canon lore speaks of elemental energy created by the Heavenly Principles from Phlogiston (Natlan Archon Quest, 5.1). The Burst resource is named the same, but canon never describes the mechanic in those terms."}
  ],
  "wi": {"keys": ["Energy Recharge", "elemental particle", "elemental particles", "elemental orb", "elemental orbs", "Elemental Energy"]},
  "sources": [
    {"title": "Energy", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Energy", "accessed": "2026-10-12", "confidence": "medium", "section": "Overview, Particles and Orbs, Direct Energy Generation, Normal Attacks, Enemies", "version": "1.0"},
    {"title": "Elements", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elements", "accessed": "2026-10-12", "confidence": "medium", "section": "Lore: Elemental Energy"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Energy is the resource a character spends on their Elemental Burst. It builds up from elemental particles and orbs, which drop when Elemental Skills hit enemies or when enemies lose HP, and which recharge the whole party. Using the Burst empties it.
### STANDARD +
Characters with special energy, such as Mavuika and Skirk, work differently and are mostly outside the rules below.

## in_universe
### LITE
Characters do not speak of Energy as a number. The nearest in-world idea is elemental energy: pulses of an element a fighter gathers and then releases in a signature technique. Canon lore elsewhere says elemental energy was made by the Heavenly Principles, who divided raw currents of the Light Realm into seven using Phlogiston as a base (revealed 5.1).
### STANDARD +
Treat the particles as flecks of an element shed in a fight and drawn to the character, which fits how they glow and fly toward a fighter.

## gameplay
### LITE
Gameplay: each Burst has its own Energy cost, and a character cannot hold more than their base Burst needs. Being knocked out removes all of a character's Energy; if the active character falls out of bounds or drowns, the whole team loses all Energy.
### STANDARD +
Particles and orbs recharge the entire party, but only when they reach a character. Energy gained depends on element match, Energy Recharge, whether the character is active and party size. Per particle at 100 percent Energy Recharge, an active character gets 3 from a particle of their own element, 1 of a different element and 2 if non-elemental; orbs give three times as much. Inactive characters get 60 percent of the active rate with four in the party, 70 percent with three and 80 percent with two.
### LARGE +
Elemental Skills can drop up to 6 particles at once or fewer at intervals. They may be generated even if the target is immune or shielded, but some coordinated-attack skills will not trigger against targets that cannot take damage. Some skills have a guaranteed count plus a chance of one more, and some have a separate particle cooldown that starts after any attempt. Hitting objects or non-hostile wildlife drops none, with exceptions for Razor's press Skill and Wriothesley's enhanced attacks. Enemies drop particles or orbs at HP thresholds, up to four, and slimes drop their own element while automatons drop non-elemental ones.
Normal and Charged Attacks can sometimes give 1 Energy, with a chance that rises on every failure and resets on success: swords begin at 10 percent and rise 5 per miss; bows 0 and 5; claymores 0 and 10; polearms 0 and 4; catalysts 0 and 10. This and other direct generation, from artifacts, weapons, talents and Constellations, ignores Energy Recharge.
### ULTRA +
Particles disappear if not collected within roughly 30 seconds and orbs within roughly 9. Weapons can also produce particles; the Electro Elemental Resonance, High Voltage, makes an Electro particle with a 5-second cooldown after an Electro-related reaction, and lightning strikes sometimes yield one. In Co-Op Mode, party size for inactive-character rates counts the characters one player controls, so in a two-player game the host counts as having 2. Energy can be drained by certain enemies, by Ley Line Disorders like High Voltage, and by weapons or artifacts such as Katsuragikiri Nagamasa and Shimenawa's Reminiscence. Special energy is unaffected unless explicitly stated. Event domains and events may also grant Energy.

## roleplay
### STANDARD
Roleplay (this project's interpretation, not canon): describe a character building toward a signature technique as they fight, gathering momentum from elemental flecks, and releasing it all at once. Do not quote numbers or conversion rates in character.

## limits
### STANDARD
Gameplay figures in this entry are mechanics, not world facts. Canon has no in-world rule that a hit produces a set amount of energy, nor a "party" that pools it.
