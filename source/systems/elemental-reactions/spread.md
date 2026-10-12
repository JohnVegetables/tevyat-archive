---
{
  "id": "system.spread",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Spread",
  "aliases": ["Spread reaction", "Dendro Spread", "Catalyze Spread"],
  "summary_line": "Spread is the Dendro reaction in which a Dendro attack on a Quickened target adds a flat bonus to that attack's damage, larger than the matching Electro bonus of Aggravate.",
  "introduced_in": "3.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.quicken", "system.aggravate", "system.dendro", "system.electro", "system.bloom",
    "system.burgeon", "system.hyperbloom", "system.elemental-mastery", "system.elemental-resonance", "location.sumeru"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Dendro"},
  "uncertainties": [
    {"topic": "In-universe cause of Spread", "classification": "unknown", "note": "The pages read describe Spread only as a combat rule and tutorial text; no story source explains the mechanism."},
    {"topic": "Separate page", "classification": "unknown", "note": "The wiki has no page of its own for Spread; the name redirects to the Catalyze page, where it is a section. Quicken has its own entity (system.quicken)."},
    {"topic": "Link between Electro-Dendro and Sumeru's history", "classification": "disputed", "note": "A Sumeru preview teaser said the reaction between Electro and Dendro has a deep connection to Sumeru's history. The wiki's trivia ties this to Rukkhadevata and Nabu Malikata, but it admits no character or record has suggested such a link; it is fan analysis."}
  ],
  "sources": [
    {"title": "Catalyze", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Catalyze", "accessed": "2026-10-12", "confidence": "high", "section": "Duration, Damage Bonus, Talents, Trivia", "version": "3.0"},
    {"title": "Elemental Reactions", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reactions", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table"},
    {"title": "Version 3.0", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Version/3.0", "accessed": "2026-10-12", "confidence": "high", "section": "New Dendro reactions; Sprawling Greenery resonance", "version": "3.0"},
    {"title": "Sumeru Preview Teaser 01: The Fascinating Dendro Element", "type": "official_video", "url": "https://youtu.be/6DjVUfy_Lng", "accessed": "2026-10-12", "confidence": "low", "section": "Cited by the Catalyze page's trivia", "version": "3.0"},
    {"title": "Elemental Reaction: Catalyze (tutorial)", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Catalyze", "accessed": "2026-10-12", "confidence": "medium", "section": "Tutorial (as summarised in the Version 3.0 reaction list)", "version": "3.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Spread is a Dendro elemental reaction. First, Dendro and Electro meet and make Quicken, which leaves a Quicken Aura on the target. Any later Dendro attack on that target then triggers Spread, which gives that attack a flat damage bonus. The Electro counterpart is Aggravate, and the Dendro bonus is the larger of the two.
### STANDARD +
It debuted in Version 3.0 with Quicken, Aggravate, Bloom, Burgeon and Hyperbloom, the reactions introduced for Dendro. Unlike many reactions, it does not deal damage of its own.

## in_universe
### LITE
Canon gives no in-world explanation for Spread. The pages read treat it as a combat rule, so it is best understood as plant energy riding on lingering charge and spreading through a target.
### LARGE +
A Sumeru preview teaser said the Electro and Dendro reaction has a deep connection to the history of Sumeru. Only that claim is on record; the wiki's connection to Rukkhadevata and Nabu Malikata is its own speculation.

## gameplay
### LITE
Gameplay: Dendro on a target with a Quicken Aura triggers Spread and adds a bonus to the attack that triggered it. Spread does not use up the Quicken Aura.
### STANDARD +
- Spread is a catalyze reaction, with Quicken and Aggravate. It adds an Additive Base DMG Bonus to the attack, so the bonus enters the damage calculation before the attack's other bonuses, CRIT damage, DEF and resistance apply.
- The base bonus is 1.25 times a level multiplier for Spread, against 1.15 for Aggravate. The wiki notes that Dendro attacks therefore receive a greater bonus than Electro ones.
- Elemental Mastery and certain artifacts raise the reaction multiplier; the two sources add together.
- The Quicken Aura lasts a number of seconds equal to five times the smaller gauge of the two elements, plus six.
### LARGE +
- Pyro or Hydro on a Quicken Aura use it up to trigger Burning or Bloom instead.
- For characters, the wiki's table of Spread base bonus values ends at level 90, while enemies and the environment have a value for level 100; the bonus rises steeply with level.
- The Dendro Elemental Resonance Sprawling Greenery in 3.0 gives nearby party members 20 Elemental Mastery for 6 seconds after Spread (or Aggravate, Burgeon, Hyperbloom), against 30 for Burning, Quicken or Bloom.
### ULTRA +
- The wiki lists talents that increase the Additive Base DMG Bonus from Spread; they are character-specific and not detailed here.
- Either element can start the Quicken Aura, but only Dendro attacks on it trigger Spread.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show green energy running along crackling sparks, a vine-like glow spreading across a target and feeding the next strike. The attack hits harder, but nothing explodes by itself.
### LARGE +
It reads as a boost to one attack rather than a spectacle: the plant strike is sharpened by the current already on the target. Pair it with Quicken, so the lingering charge is visible first.
### ULTRA +
Avoid describing Spread as an area attack, as consuming the aura, or as something that happens without an Electro and Dendro pairing first. Do not link it to Sumeru's history as established fact.

## limits
### LITE
Spread needs a Quicken Aura first and only Dendro triggers it. It has no damage of its own.
### STANDARD +
The Quicken Aura fades with time. Bloom or Burning can use it up if Hydro or Pyro is applied.

## examples
### STANDARD
Gameplay example: an Electro attack lands on a Dendro-affected enemy and starts Quicken. The next Dendro attack triggers Spread and hits harder, and the aura stays for more Dendro hits.

## entry: Quicken Aura
@keys: Quicken Aura
@keys2: Spread, Aggravate
### STANDARD
Quicken is the starting reaction of the catalyze family: Dendro on an Electro-affected target, or the other way round. It deals no damage and leaves a Quicken Aura that fades over time. Dendro attacks on it trigger Spread, Electro ones trigger Aggravate, and neither consumes it. See system.quicken.
