---
{
  "id": "system.stamina",
  "entity_type": "system",
  "subdir": "gameplay",
  "name": "Stamina",
  "aliases": ["Stamina bar", "stamina meter", "maximum stamina"],
  "summary_line": "Stamina is the shared party resource spent on sprinting, climbing, swimming, gliding and charged attacks; it starts at 100 and rises with Statue of The Seven upgrades, to a cap of 240.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": ["system.statue-of-the-seven", "system.anemo", "system.elemental-resonance", "term.oculus", "item.wind-glider"],
  "facts": {"system_type": "gameplay_mechanic", "lore_status": "gameplay_abstraction", "element": null},
  "uncertainties": [
    {"topic": "Stamina cost of climbing", "classification": "unknown", "note": "The wiki gives only that 5 Stamina is the minimum required to start climbing; the continuous cost is listed as unknown."},
    {"topic": "Total stamina available from Snezhnaya statues", "classification": "unknown", "note": "The wiki flags the exact per-level amounts for statues outside Mondstadt and Liyue as needing verification."}
  ],
  "sources": [
    {"title": "Stamina", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Stamina", "accessed": "2026-10-12", "confidence": "medium", "section": "Overview, Maximum Stamina, Stamina Consumption, Other Source", "version": "1.0"},
    {"title": "Statue of The Seven", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Statue_of_The_Seven", "accessed": "2026-10-12", "confidence": "medium", "section": "Overview, Statue Levels"},
    {"title": "Team Bonus", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Team_Bonus", "accessed": "2026-10-12", "confidence": "high", "section": "Elemental Resonance: Impetuous Winds"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Stamina is the yellow bar that drains when you sprint, dash, climb, swim, glide or make a charged attack. It is one pool shared by the whole party, starts at 100 and regenerates quickly when you stop.
### STANDARD +
Upgrading the Statues of The Seven raises the maximum, up to 240.

## in_universe
### LITE
Stamina is a game mechanic, not something characters mention by name. Gameplay abstraction: it represents the physical effort of running, climbing and swimming.
### STANDARD +
Gliding with a wind glider costs only 3 Stamina per second, far less than sprinting at 18.

## gameplay
### LITE
Gameplay: stamina is a shared party pool shown as a yellow bar beside the active character. It regenerates at 25 per second after 1.5 seconds of not spending it, and the bar hides itself when full. Switching characters does not restore it.
### STANDARD +
The bar is divided into sections of 100 Stamina each. Base costs, before any reduction, include:
- Dash: 18 per movement; sprinting: 18 per second.
- Climbing: continuous cost not listed (5 Stamina is the minimum needed to begin); a climbing jump costs 25 per movement.
- Swimming: 4 per movement; swim dash: 2 to start, then about 10.2 per second.
- Gliding: 3 per second while moving.
- Charged attacks: most sword characters 20; polearm 25; most claymore 40 per second; most catalyst 50.
Many characters' passive talents, some Constellations and certain dishes reduce costs, remove them or restore stamina. The Stamina Flower restores 80 Stamina.
### LARGE +
Maximum Stamina starts at 100. Each nation's Statues of The Seven can be upgraded with oculi; the maximum rises by 7 for each of the first two upgrades and 8 for the following seven, a total of +70 from one nation's statues at Level 10 (cumulative: Level 2 +7, 3 +14, 4 +22, 5 +30, 6 +38, 7 +46, 8 +54, 9 +62, 10 +70). The cap is 240, reachable with 18 upgrades across any two nations' statues or at least 19 upgrades spread across six nations. Statue Levels in a region are shared by all of that region's statues, and the stamina bonus is added until 240 is reached.
Reductions stack additively against the base cost: Impetuous Winds (two or more Anemo characters) takes 15% off; the wiki's example also uses Wolvensprint at 20%; a dish such as Barbatos Ratatouille takes 25%. In that example, sprinting drops from 18 to 7.2 per second. Total reduction is capped at about 92%. Anemograna cuts consumption by 30%. Condensed Ice (a Ley Line Disorder) raises consumption by 100% or 200%.
### ULTRA +
Other listed costs: Jean's Gale Blade hold, 20 per second; Keqing and Shikanoin Heizou, 25 for a charged attack; Tartaglia's Foul Legacy and the Raiden Shogun's Secret Art charged attacks and Arataki Itto, 20; Arlecchino's high-speed movement, 40 per second; Kinich and Mavuika, 50 for a charged attack. Ororon's and Citlali's mid-air Aiming Mode costs 75 for holding jump then 20 per second; the Alternate Sprint costs 10 to start then 15 per second. Two enemies, Abyss Herald: Frost Fall and Iniquitous Baptist, also have stamina costs listed for their frost attacks (50 and 80 respectively on first use).
Food that reduces sprint stamina costs applies to both dash and sprint; a second dish overrides the first, rather than stacking.

## limits
### STANDARD
Gameplay: stamina cannot exceed the current maximum, does not regenerate until 1.5 seconds after you stop spending it, and is not restored by swapping characters. Costs differ by action and, for charged attacks, by weapon type.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): do not quote numbers in scene. Show effort through breathing, slowing pace, and hands slipping on a wall. Characters with stamina-related talents can be shown as lighter on their feet, but do not make them tireless.

## entry: Statue of The Seven stamina upgrades
@keys: max stamina, maximum stamina, stamina upgrade
@keys2: Statue of The Seven, oculi, Oculus, Anemoculus, Geoculus
### STANDARD
Offering oculi at a nation's Statue of The Seven raises that nation's statue level, and each early level also adds to the party's maximum Stamina (7 for the first two upgrades, 8 for the next seven). The maximum possible is 240. See the Statue of The Seven entry for the offering mechanic itself.
