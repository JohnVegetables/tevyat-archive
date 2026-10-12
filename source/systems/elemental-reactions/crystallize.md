---
{
  "id": "system.crystallize",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Crystallize",
  "aliases": ["Crystallize reaction", "Crystallize shard", "Crystallize shield", "Elemental Shard"],
  "summary_line": "Crystallize is the reaction in which Geo meets Pyro, Hydro, Electro or Cryo and leaves a shard that grants an elemental shield when picked up.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.geo", "system.pyro", "system.hydro", "system.electro", "system.cryo",
    "system.lunar-crystallize", "system.lunar-reaction", "system.shields", "system.elemental-mastery", "system.swirl",
    "system.elements", "creature.geovishap"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation of Crystallize", "classification": "unknown", "note": "The wiki page read treats Crystallize as a combat rule. It gives no character's in-world account of why Geo turns another element into a shard, so none is offered."},
    {"topic": "Shield Strength mechanics", "classification": "inferred", "note": "The wiki's claim that Shield Strength reduces damage taken by a shield, rather than increasing its HP, rests on community analysis cited on the page; it is not an official statement."}
  ],
  "sources": [
    {"title": "Crystallize", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Crystallize", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Shield Health; Tutorial; Change History", "version": "1.0"},
    {"title": "Lunar-Crystallize", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Lunar-Crystallize", "accessed": "2026-10-12", "confidence": "high", "section": "Damage; Moondrifts", "version": "6.3"},
    {"title": "Lunar Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Lunar_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; List of Lunar Reactions", "version": "5.8"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Crystallize is what happens when Geo hits a target already affected by Pyro, Hydro, Electro or Cryo. It deals no damage. It leaves a shard of that element, and a character who picks the shard up gains a shield of the same element.
### STANDARD +
Geo is always the second element in this reaction. Anemo and Dendro are not part of it.

## in_universe
### LITE
Canon offers no in-world explanation. Crystallize shows up in tutorials and combat, not in character dialogue in the sources read. Treat it as a gameplay abstraction that a scene may borrow from.
### STANDARD +
The in-game tutorial describes it simply: Geo contacting Hydro, Pyro, Cryo or Electro creates shards of the matching element that give the character an elemental shield, and good use of it cuts damage taken in battle.

## gameplay
### LITE
Gameplay (not literal lore): the shard (Electro, Pyro, Hydro or Cryo) lasts 15 seconds on the field, with a short delay before it can be picked up. Picking it up grants an elemental shield that also lasts 15 seconds. Enemies cannot pick shards up.
### STANDARD +
- If more than 3 shards are on the field, after about 2 seconds only the 3 newest remain.
- Only one Crystallize shield is active at a time; a new shard's shield overwrites the old one.
- Crystallize can trigger only once per second on the same target.
- A Geo shard from Geovishap Hatchlings or the Pure Geo Hypostasis is a different thing; its shield can coexist with a Crystallize shield instead of replacing it.
### LARGE +
- Shield health: base health comes from the Geo user's level and is raised by a percentage based on the user's Elemental Mastery. The wiki lists base shield HP of about 91 at level 1, about 1,851 at level 90 and about 2,199 at level 100. The Mastery bonus follows 4.44 x EM / (EM + 1400), so 100 EM gives about 29.6% and 1000 EM about 185%.
- Elemental shields are 250% effective against their own element, taking only 40% as much damage from it, and raise Interruption Resistance while active.
- A Crystallize shield can coexist with other shields, but each takes full damage at once. According to the wiki's community sources, a character's Shield Strength reduces damage taken by the shields they have rather than raising the HP of shields they make.
### ULTRA +
Geo cannot be the first element on a target, so Crystallize is always Geo applied second. Several characters, weapons and artifact sets interact with Crystallize shards or shields; the wiki handles those separately and this entry does not copy them.

## lunar_crystallize
@version: 6.3
### LARGE
Lunar-Crystallize (own entry) is the Moonsign form of Geo meeting Hydro, which the wiki records as introduced in Version Luna IV. It needs a party member with a qualifying Moonsign Benediction passive. According to the wiki, triggering it creates three Moondrifts around the target; every third Lunar-Crystallize reaction makes them resonate in Moondrift Harmony, a tracking projectile that deals Geo damage. Moondrifts count as Geo constructs.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Crystallize as a coloured stone shard forming in the air around a struck foe: ember-red from fire, blue from water, pale from frost, violet from lightning. Picking it up wraps the character in a pane of matching light.
### LARGE +
It is a defensive reaction, so it suits support and tank characters: a Geo user turning the enemy's own element into protection. Keep the shard visible and brief, so there is a moment to pick it up. Do not have characters count shield HP or seconds.

## examples
### STANDARD
A Pyro slime is scorched by a sword, then struck by a Geo strike. A red crystal flies loose, and the character who gathers it is wrapped in a shell of fire-coloured light, which takes less harm from flames.
### LARGE +
A Geo user fighting an Electro-soaked foe can make violet shards, while a Hydro foe produces blue ones. They disappear if not collected.

## limits
### STANDARD
Crystallize does not deal damage and does not work with Dendro or Anemo. Enemies cannot pick up the shards.
### LARGE +
Do not call Crystallize shields permanent or stackable; one at a time, and the 15-second duration is the limit. Do not move Lunar-Crystallize earlier than Version Luna IV. As of 7.1, the wiki records only the 1.0 introduction for base Crystallize.

## entry: Crystallize shard
@keys: Crystallize shard, Crystallize shards, Elemental Shard, Elemental Shards
### STANDARD
A Crystallize shard is the pick-up created by the reaction: Electro, Pyro, Hydro or Cryo according to the element that was crystallised. It can be collected after a short delay and lasts 15 seconds on the field. Only the three newest shards stay if more are produced, and enemies cannot take them.

## entry: Crystallize shield
@keys: Crystallize shield, elemental shield
@keys2: Crystallize, shard, Geo
### STANDARD
The shield granted by a Crystallize shard matches the shard's element and lasts 15 seconds. Its health is based on the Geo user's level and Elemental Mastery. It blocks 2.5 times as much damage from its own element, and only one such shield is active at a time.
