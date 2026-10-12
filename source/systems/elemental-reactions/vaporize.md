---
{
  "id": "system.vaporize",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Vaporize",
  "aliases": ["Vaporize reaction", "Pyro-Hydro reaction"],
  "summary_line": "Vaporize is the elemental reaction between Pyro and Hydro: it deals no damage of its own but multiplies the hit that triggers it, by 2 if Hydro triggers it and 1.5 if Pyro does.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.pyro", "system.hydro", "system.melt", "system.elemental-mastery"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation", "classification": "unknown", "note": "No source read for this entry explains in-world why Pyro meeting Hydro amplifies damage; it appears only in tutorial and gameplay text."}
  ],
  "sources": [
    {"title": "Vaporize", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Vaporize", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, Tutorial", "version": "1.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table; Amplifying Reactions"},
    {"title": "Elemental Reaction Intro (template)", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Template:Elemental_Reaction_Intro", "accessed": "2026-10-12", "confidence": "high", "section": "Vaporize multipliers"},
    {"title": "Damage", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Damage", "accessed": "2026-10-12", "confidence": "high", "section": "Amplifying Reaction Damage"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Vaporize is what happens when Pyro and Hydro meet on a target. It deals no damage by itself; instead the attack that triggers it hits much harder, as if the water flashed to steam under the blow. It is a combat rule rather than a story event.
### STANDARD +
Which element lands second decides the strength: a Hydro hit on a Pyro-affected target is amplified more than a Pyro hit on a Hydro-affected target.

## in_universe
### LITE
Canon presents Vaporize only through the Elemental Trial tutorial and gameplay text. No source read for this entry gives an in-world account of why it amplifies damage, so any in-world explanation is a scene decision.
### STANDARD +
The tutorial wording is simply that when Pyro meets Hydro, the triggering Hydro or Pyro damage receives a bonus, and that the bonus is larger when Hydro is the trigger.

## gameplay
### LITE
Gameplay (not literal lore): Vaporize multiplies the damage of the triggering attack by 2 if Hydro is applied to a Pyro-affected target, and by 1.5 if Pyro is applied to a Hydro-affected target.
### STANDARD +
It is an amplifying reaction, like Melt. The multiplier is further increased by a percentage based on the triggering character's Elemental Mastery plus any Reaction DMG Bonus from effects such as artifact sets. Vaporize deals no damage of its own, so a talent that only applies an element and deals no damage gains nothing from it.
### LARGE +
The 1.5x ("reverse") form consumes less of the original element than the 2x ("forward") form, so it often leaves part of the aura in place. Talents, constellations and artifact sets exist that raise Vaporize damage, and the multiplier can also apply to damage from separate reaction instances, not only direct attacks.

### ULTRA +
The wiki gives the multiplier as the base coefficient (2.0 for Hydro triggering, 1.5 for Pyro triggering) times one plus the Elemental Mastery bonus and any Reaction DMG Bonus, with the Elemental Mastery bonus approximated as 2.78 x EM / (EM + 1400). It multiplies the damage before the reaction is otherwise accounted for.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Vaporize as a burst of hissing steam when water strikes fire, or when flame scorches a wet foe, followed by a visibly harder hit. Keep it about the force of the blow, not extra effects.
### LARGE +
Water on flame, the stronger case, can be narrated as the more dramatic hit. Do not treat the steam as a lingering cloud or a status on the target; canon describes none.

## limits
### LITE
Vaporize needs both Pyro and Hydro, and it never creates damage on its own.
### STANDARD +
It does not turn into another reaction and does not involve Geo, Anemo, Electro, Cryo or Dendro.

## entry: Vaporize
@keys: Vaporize, Vaporize reaction
### STANDARD
Vaporize is the Pyro and Hydro reaction. It amplifies the triggering hit: x2 when Hydro triggers it, x1.5 when Pyro does. It deals no damage of its own.
### LARGE +
Elemental Mastery adds a further percentage to the multiplier, and certain talents, constellations and artifact sets improve it. The sibling reaction for Pyro and Cryo is Melt.
