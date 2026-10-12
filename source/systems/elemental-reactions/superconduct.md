---
{
  "id": "system.superconduct",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Superconduct",
  "aliases": ["Superconduct reaction", "Electro-Cryo reaction"],
  "summary_line": "Superconduct is the elemental reaction between Electro and Cryo: it bursts in a small area for Cryo damage and leaves nearby enemies more vulnerable to Physical attacks for a time.",
  "introduced_in": "1.0",
  "spoiler_level": "minor",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.electro", "system.cryo", "system.frozen", "system.elemental-mastery",
    "system.stellar-conduct", "system.stellar-glimmer-reaction", "system.physical", "system.overloaded"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation", "classification": "unknown", "note": "No source read for this entry explains in-world why Electro meeting Cryo weakens Physical resistance. The reaction is described only in tutorial and gameplay text."},
    {"topic": "Lore of Stellar-Conduct", "classification": "unknown", "note": "Stellar-Conduct (7.0) replaces Superconduct under certain party conditions; the wiki attributes the introduction of Stellar Glimmer reactions to ancient Snezhnaya (via Saarelainen, citing the 7.0 Special Program) but gives no mechanism."}
  ],
  "sources": [
    {"title": "Superconduct", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Superconduct", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, Damage, Environment, Tutorial", "version": "1.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table; Transformative Reactions"},
    {"title": "Elemental Reaction Intro (template)", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Template:Elemental_Reaction_Intro", "accessed": "2026-10-12", "confidence": "high", "section": "Superconduct: 5 m radius, 40% Physical RES for 12 seconds"},
    {"title": "Damage", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Damage", "accessed": "2026-10-12", "confidence": "high", "section": "Transformative Reaction Damage"},
    {"title": "Stellar-Conduct", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Stellar-Conduct", "accessed": "2026-10-12", "confidence": "high", "section": "Intro; Starlight Prism", "version": "7.0"},
    {"title": "Stellar Glimmer Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Stellar_Glimmer_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Lore", "version": "7.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Superconduct is the reaction that happens when Electro meets Cryo on a target, in either order. It is a burst of Cryo energy that damages everything in a small area and strips Physical resistance from the enemies it touches, so that sword, spear and fist hurt more for a while. It is a combat rule rather than a story event.
### STANDARD +
The damage is fixed by the reaction itself (the level and Elemental Mastery of whoever triggers it), not by the attack that set it off. The Cryo is not left on the target, so Superconduct cannot lead to a second reaction.

## in_universe
### LITE
Canon does not explain Superconduct as a phenomenon of the world; it is introduced only through the game's Elemental Trial tutorial. Treat any in-world explanation as a scene decision, not as lore.
### STANDARD +
Outside battle the game shows the same pairing in the environment. Electro on water that Cryo has frozen shortens the freeze and leaves the water Electro-Charged, without area damage or Physical RES loss. Cryo on an Electro Crystal, or Electro on a Mist Flower, triggers a full Superconduct and hurts enemies nearby.
### ULTRA +
Version 7.0 added Stellar-Conduct, a Stellar Glimmer reaction that replaces Superconduct when a character with a matching Stellar Jubilee passive is in the party. The wiki credits the introduction of Stellar Glimmer reactions to ancient Snezhnaya, through Saarelainen, citing the 7.0 Special Program. Ordinary Superconduct is unchanged outside that condition.

## gameplay
### LITE
Gameplay (not literal lore): Superconduct deals AoE Cryo damage in a 5 m radius and reduces the Physical RES of enemies in the area by 40% for 12 seconds.
### STANDARD +
It is a transformative reaction with base coefficient 1.5 (from the wiki's Damage page), scaled by the triggering character's level and Elemental Mastery. It ignores the attack's ATK and cannot CRIT by default. Target resistance applies; DEF is practically ignored. Only the party applying the second element counts.
### LARGE +
Electro on a Frozen target triggers Superconduct and consumes the Freeze. One target can take at most 2 instances of Superconduct damage every 0.5 seconds from the same attacker, and several Superconducts on the same target within 0.1 seconds deal damage only once. Talents, constellations and artifact sets exist that raise Superconduct damage.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Superconduct as a sharp crack of frost and static, a ring of shards or a snap of ice-blue lightning, followed by armour, hides or bone visibly weakening. Describe the effect as a short-lived weakness to blows, not a permanent wound.
### LARGE +
Because the damage is Cryo and the lasting benefit is Physical, narrate it as setting up the next strike. Do not claim Superconduct leaves lingering frost on the target; the reaction does not.

## limits
### LITE
Superconduct needs both Electro and Cryo; no other element pair produces it.
### STANDARD +
It applies no Cryo, so it cannot chain into Frozen, Melt or another Cryo reaction. Cryo on Electro-Charged water does not trigger it in the environment.
### LARGE +
The Physical RES reduction applies to enemies in the burst, not to the reaction's source. Under the Stellar-Conduct conditions (7.0) the reaction becomes a different one.

## entry: Superconduct
@keys: Superconduct, Superconduct reaction
### STANDARD
Superconduct is the Electro and Cryo reaction. It bursts with Cryo damage in a 5 m radius and lowers Physical RES by 40% for 12 seconds for enemies in the area. It leaves no Cryo behind.
### LARGE +
Environmental forms: Electro on frozen water shortens the freeze and electrifies the water without area damage or Physical RES loss, while Cryo on an Electro Crystal or Electro on a Mist Flower triggers a full Superconduct. In 7.0, Stellar-Conduct can replace it if a character with the matching passive is in the party.
