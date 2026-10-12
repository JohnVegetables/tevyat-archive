---
{
  "id": "system.overloaded",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Overloaded",
  "aliases": ["Overloaded reaction", "Overloaded DMG", "Pyro-Electro reaction"],
  "summary_line": "Overloaded is the transformative elemental reaction between Pyro and Electro: an explosion that deals area Pyro damage and knocks targets back.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.elements", "system.pyro", "system.electro", "system.shattered",
    "system.frozen", "system.elemental-mastery", "system.elemental-resonance", "system.burning",
    "system.vaporize", "creature.elemental-lifeforms"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation of Overloaded", "classification": "unknown", "note": "The pages read give only tutorial text and damage rules; no story source explains why fire and lightning together explode."}
  ],
  "sources": [
    {"title": "Overloaded", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Overloaded", "accessed": "2026-10-12", "confidence": "high", "section": "Introduction, Damage, Tutorial, Artifacts, Preview", "version": "1.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table; Transformative Reactions", "version": "1.0"},
    {"title": "Frozen", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "high", "section": "Shatter", "version": "1.0"},
    {"title": "Elemental Trial tutorial: Overloaded", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Overloaded", "accessed": "2026-10-12", "confidence": "high", "section": "Tutorial (text quoted on the Overloaded page)", "version": "1.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Overloaded is the elemental reaction between Pyro and Electro, in either order. It causes an explosion that deals area Pyro damage and throws nearby targets back. It is a combat rule, so treat it as a gameplay abstraction that a scene may borrow from, not a named law of the world.
### STANDARD +
Overloaded has existed since Version 1.0. It is a transformative reaction, meaning it deals its own damage separate from the attack that triggered it. The in-game tutorial calls it a powerful explosion and tells players to alternate Pyro and Electro attacks to trigger it.

## in_universe
### LITE
Canon gives no story explanation for Overloaded. The in-game tutorial only says that when Pyro meets Electro, or Electro meets Pyro, Overloaded occurs, causing powerful explosions that deal area Pyro damage.
### STANDARD +
Nothing read ties the reaction to a character, god or event. Do not invent an origin. Fire and lightning causing a blast is a natural image for a scene, but treat it as flavour.

## gameplay
### LITE
Gameplay (not literal lore): Overloaded happens when Electro hits a target carrying Pyro, or Pyro hits a target carrying Electro. The explosion deals area Pyro damage in a roughly 5 metre radius and causes strong knockback.
### STANDARD +
- It does not apply Pyro to the targets it hits, so it cannot set off further reactions by itself.
- Overloaded damage counts as a blunt attack, so it can trigger Shatter on Frozen targets and is more effective against certain enemy shields.
- Like other transformative reactions, its damage depends on the level of the character who triggers it and is raised by that character's Elemental Mastery. It cannot CRIT.
### LARGE +
- One target can take only one instance of Overloaded damage every 0.5 seconds from the same attacker, and several Overloaded reactions on the same target within 0.1 seconds produce damage only once, whatever their source.
- Certain artifact sets raise Overloaded damage.
- The explosion causes significant knockback; the wiki's preview also shows Overloaded damaging ore deposits.
- Elemental Resonance (two or more Electro characters, High Voltage) interacts with Overloaded; see the Electro entry.
### ULTRA +
- Overloaded is unchanged by the newer reaction families. As of Version 7.1 the wiki's reaction table lists Pyro with Electro as Overloaded, alongside Lunar and Stellar Glimmer reactions that replace other Electro reactions in matching parties.
- The Pyro element in the blast is a damage type only: Overloaded does not leave a Pyro aura, unlike Burning, which keeps applying Pyro.

## limits
### LITE
Overloaded needs both elements on the same target and does nothing to a target with only one. The knockback can scatter enemies instead of keeping them together.
### STANDARD +
The explosion is fixed-size and tied to the triggering character's level, so a weak character does not produce a huge blast. Pyro-immune enemies reduce its damage.

## examples
### STANDARD
Gameplay example from the in-game tutorial: switch characters in battle and use Pyro and Electro attacks in turn to trigger Overloaded and defeat opponents quickly. The wiki's preview shows an Overloaded blast on an enemy and one used to break open ore.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Overloaded as a sharp bang of purple lightning and orange flame, with a shockwave that shoves people and loose objects back. Keep it a single blast, loud and brief, not a lasting fire.
### LARGE +
Narratively, Overloaded is chaos: great for a scene where two characters with opposing Visions clash by accident or on purpose. Characters can be knocked off their feet, but the blast should not be lethal for an ordinary person unless the scene calls for it. Cover, ringing ears and scorched cloth are proportionate.
### ULTRA +
Avoid describing Overloaded as a way to demolish buildings or to destroy gods. Do not have it light a lasting fire; that is Burning, a different reaction with Dendro.

## entry: Transformative reactions
@keys: transformative reaction, transformative reactions
@keys2: Overloaded
### LARGE
Overloaded is a transformative reaction, along with Shattered, Electro-Charged, Superconduct, Swirl, Burning, Bloom, Hyperbloom and Burgeon. Each deals its own damage based on its type and the triggering character's level, raised by Elemental Mastery. This damage cannot CRIT, ignores the target's DEF in practice, and is still affected by resistance.
