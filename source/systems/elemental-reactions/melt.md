---
{
  "id": "system.melt",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Melt",
  "aliases": ["Melt reaction", "Melt DMG", "Pyro-Cryo reaction"],
  "summary_line": "Melt is the amplifying elemental reaction between Pyro and Cryo: it deals no damage of its own but multiplies the hit that triggers it, more strongly when Pyro is the trigger.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.elements", "system.pyro", "system.cryo", "system.vaporize",
    "system.frozen", "system.elemental-mastery", "system.elemental-resonance", "creature.elemental-lifeforms",
    "creature.slime"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation of Melt", "classification": "unknown", "note": "The pages read give only tutorial text and damage rules; no story source says why fire and frost make a hit stronger instead of cancelling out."}
  ],
  "sources": [
    {"title": "Melt", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Melt", "accessed": "2026-10-12", "confidence": "high", "section": "Introduction, Tutorial, Artifacts, Preview", "version": "1.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table; Amplifying Reactions", "version": "1.0"},
    {"title": "Frozen", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "high", "section": "Pyro consumes a Freeze Aura and triggers Melt; frozen water melts", "version": "1.0"},
    {"title": "Elemental Trial tutorial: Melt", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Melt", "accessed": "2026-10-12", "confidence": "high", "section": "Tutorial (text quoted on the Melt page)", "version": "1.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Melt is the elemental reaction between Pyro and Cryo. It deals no damage itself. Instead, the attack that triggers it hits harder. The bonus is larger when the trigger is Pyro landing on a target already affected by Cryo, and smaller when Cryo lands on a Pyro-affected target. It is a combat rule, so treat it as a gameplay abstraction, not a named law of the world.
### STANDARD +
Melt has existed since Version 1.0. Its sibling amplifying reaction is Vaporize (Pyro with Hydro). Both give damage multipliers, and neither creates a new effect on the target.

## in_universe
### LITE
Canon gives no story explanation for Melt. The in-game tutorial only says that when Pyro meets Cryo, Melt occurs, and the triggering source of damage receives a bonus.
### STANDARD +
Nothing read ties Melt to a character or event. Do not invent an origin. The everyday idea that heat melts ice is a safe image for a scene, but treat it as flavour.

## gameplay
### LITE
Gameplay (not literal lore): Melt happens when Pyro hits a target that already carries Cryo, or when Cryo hits a target that already carries Pyro. The triggering attack's damage is multiplied. Pyro as the trigger gives a 2x multiplier; Cryo as the trigger gives 1.5x.
### STANDARD +
- Elemental Mastery of the triggering character raises the multiplier further, and certain artifact sets raise Melt damage.
- The 2x version consumes more of the first element, usually removing it quickly. The 1.5x version consumes less and often leaves the aura in place.
- Applying Pyro to a Freeze Aura left by Frozen consumes it and triggers Melt. Melt can also dissolve ice on water in the open world instantly.
### LARGE +
- Melt is one of two amplifying reactions with Vaporize. Unlike transformative reactions such as Overloaded, amplifying reactions can CRIT, because they scale the triggering attack's own damage.
- The strength of the reaction comes from whoever triggers it; the stats of whoever left the first aura do not count.
- Because many attacks have an internal cooldown on applying their element, a source cannot reapply Pyro or Cryo on every hit, and so cannot Melt on every hit.
### ULTRA +
- Melt is unchanged by the newer reaction families. As of Version 7.1 the wiki's reaction table still lists Pyro with Cryo as Melt, with the same 2x and 1.5x multipliers.
- The wiki cites the Elemental Gauge Theory page for the amounts of aura consumed by the two directions. This entry does not reproduce its numbers.

## limits
### LITE
Melt cannot happen without a first element in place, and it does nothing to a target with neither Pyro nor Cryo on it.
### STANDARD +
It adds no damage of its own, so a weak hit stays weak. Enemies immune or resistant to Pyro or Cryo reduce the benefit.

## examples
### STANDARD
Gameplay example from the in-game tutorial: use Cryo attacks to coat opponents with Cryo, then switch to a Pyro character and attack; the Pyro attack triggers Melt and hits much harder, so opponents fall faster. The wiki's preview shows Melt being caused on a Cryo Slime.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Melt as a burst of steam and a hiss where flame meets frost, with the strike landing harder than it should. Pyro is the orange-red cue, Cryo the pale-blue cue; keep the effect to one blow, not a lasting area of fire or ice.
### LARGE +
Narratively, Melt rewards teamwork: one person chills a foe and a partner finishes it with fire, or the reverse. It is a nice way to show two characters with opposing Visions working in sync. Do not have ordinary Vision holders melt walls of ice or glaciers with a single spell.
### ULTRA +
Avoid mixing Melt up with Frozen: Frozen locks a target in ice, while Melt boosts a hit. Pyro on a frozen target ends the freeze; do not have it do both at once for free.

## entry: Amplifying reactions
@keys: amplifying reaction, amplifying reactions
@keys2: Melt, Vaporize
### LARGE
Melt and Vaporize are the two amplifying reactions. They multiply the damage of the triggering attack by 2x or 1.5x depending on which element came second, instead of dealing their own damage. The multiplier is raised again by Elemental Mastery. The 1.5x reactions consume less of the first element than the 2x reactions do.
