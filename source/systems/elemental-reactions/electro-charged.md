---
{
  "id": "system.electro-charged",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Electro-Charged",
  "aliases": ["Electro-Charged reaction", "Electrocharged", "Electro Charged"],
  "summary_line": "Electro-Charged is the reaction between Electro and Hydro: a crackling charge that deals Electro damage over time and arcs to other wet targets nearby.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.electro", "system.hydro", "system.overloaded", "system.vaporize",
    "system.swirl", "system.lunar-charged", "system.lunar-reaction", "system.elemental-mastery", "system.elements",
    "system.crystallize", "system.burning"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation of Electro-Charged", "classification": "unknown", "note": "The wiki page read treats Electro-Charged as a combat rule. It gives no character's in-world account of it, so none is offered."},
    {"topic": "Arc range", "classification": "unknown", "note": "The wiki gives the arcing range as 5 m but marks the figure as needing verification, so it appears here as 'about 5 m'."}
  ],
  "sources": [
    {"title": "Electro-Charged", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Electro-Charged", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Number of Hits; Environment; Immunity Talents; Tutorial; Change History", "version": "1.0"},
    {"title": "Lunar-Charged", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Lunar-Charged", "accessed": "2026-10-12", "confidence": "high", "section": "Damage", "version": "5.8"},
    {"title": "Lunar Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Lunar_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; List of Lunar Reactions", "version": "5.8"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Electro-Charged is what happens when Electro and Hydro meet on a target, in either order. The target keeps both Hydro and Electro on it and takes Electro damage once a second, and the shock jumps to another wet enemy nearby. It continues until one of the two elements is used up.
### STANDARD +
The wiki lists it as a Transformative reaction. A third element can still react with the target, which makes Electro-Charged a good opener for follow-up reactions.

## in_universe
### LITE
Canon offers no in-world explanation. Electro-Charged appears in tutorials and combat, not in character dialogue in the sources read. Treat it as a gameplay abstraction that a scene may borrow from.
### STANDARD +
The in-game tutorial puts it plainly: Electro meeting Hydro causes Electro-Charged, which keeps dealing Electro damage until it wears off and electrifies nearby Wet opponents.

## gameplay
### LITE
Gameplay (not literal lore): Electro-Charged leaves the target with a Hydro aura and an Electro aura at the same time. It deals Electro damage once per second; each tick reduces both auras by 0.4 gauge units, and it ends when either aura is gone. Normal aura decay still applies.
### STANDARD +
- It cannot damage off-field characters. Switching away pauses the ticks; if the character returns while still affected by Electro and Hydro, the ticks resume.
- Each time it deals damage it also hits one other nearby Wet opponent, about 5 m away (the wiki marks that range as unverified), accounting for that opponent's Electro RES. The Wet aura is not consumed by the arc, and an Electro aura is not applied to the arc target.
- If Electro-Charged ends because an aura expires, one more tick can occur if more than 0.5 seconds have passed since the last.
### LARGE +
- Third element: because both auras exist together, other reactions can follow, such as Overloaded and Vaporize, Superconduct and Frozen, or an Electro and a Hydro Swirl. The Electro reaction is resolved first, and the Hydro reaction happens only if some of the triggering element is left after the Electro aura is used up.
- The coexisting elements also allow effects such as Thundersoother to be applied without giving up reactions.
- Environment: if an Electro attack hits a body of water, the water becomes Electro-Charged for a short time and any target walking into it takes Electro damage. Pyro or Cryo applied to that water can cause Overloaded or Superconduct.
- Damage is Transformative: it comes from the triggering character's level and Elemental Mastery and is resisted by the target's Electro RES.
### ULTRA +
Some talents grant immunity to Electro-Charged, and others, constellations and artifact sets raise its damage; the wiki holds those in category tables, which this entry does not copy. The Lunar-Charged page adds that Lunar-Charged shares all other properties of Electro-Charged, including damaging the ward of the Fatui Skirmisher - Hydrogunner Legionnaire at an increased rate.

## lunar_charged
@version: 5.8
### LARGE
Lunar-Charged (own entry) is the Moonsign form of Electro meeting Hydro. It needs a party member with a qualifying Moonsign Benediction passive. According to the wiki, it summons a thundercloud that strikes every Wet, Electro-affected opponent in range every 2 seconds, and a target not struck in the last 2 seconds is hit at once when the second aura lands. Each strike consumes 0.4 gauge units of both auras. The cloud lasts 6 seconds, is reset by another trigger, and only one can exist at a time.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Electro-Charged as lightning crawling over wet surfaces: blue-white arcs skittering across a soaked body, a crackle in the air, hair and cloth standing up. The shock should leap between soaked enemies and puddles.
### LARGE +
Water is the setting that matters. A stream, puddle or rain-soaked courtyard turns every Electro spark into a hazard, and an Electro user fighting there should take care of nearby allies. Do not have characters state tick rates or gauge units.

## examples
### STANDARD
A Hydro slime drenches a group of enemies, then a bolt of lightning strikes one of them. The charge crackles along its wet body and jumps to another soaked enemy a few steps away, repeating until the water or the lightning fades.
### LARGE +
An Electro user wading through a stream is plausibly dangerous for anyone else in the water, matching the wiki's note about Electro-Charged water.

## limits
### STANDARD
It needs Electro and Hydro together: Anemo, Geo, Pyro, Cryo and Dendro do not cause it. Do not describe it as an instant burst; its identity is the sustained shock. Do not have it hit off-field targets, or spread to dry ones, as the wiki shows it arcs only to Wet opponents.
### LARGE +
Do not move Lunar-Charged earlier than Version 5.8. Do not claim all characters or enemies take it; some talents grant immunity to it.

## entry: Electro-Charged water
@keys: Electro-Charged water, electrified water
### LARGE
When an Electro attack hits a body of water, the water becomes Electro-Charged briefly, and anyone who walks into it takes Electro damage. Applying Pyro or Cryo to such water can cause Overloaded or Superconduct.

## entry: Lunar-Charged thundercloud
@keys: thundercloud, Lunar-Charged thundercloud
@keys2: Lunar-Charged, Moonsign
### LARGE
A thundercloud is the effect created by Lunar-Charged. It tries to position itself between active targets and the triggering party, lasts 6 seconds, and strikes Wet, Electro-affected opponents within range every 2 seconds. Only one can exist at a time.
