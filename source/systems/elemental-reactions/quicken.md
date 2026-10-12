---
{
  "id": "system.quicken",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Quicken",
  "aliases": ["Quicken reaction", "Quickened", "Quicken Aura", "Catalyze", "Catalyze reactions", "Dendro-Electro reaction"],
  "summary_line": "Quicken is the elemental reaction between Dendro and Electro. It deals no damage but leaves a Quicken Aura that lets later Dendro and Electro hits trigger Spread and Aggravate for bonus damage.",
  "nation": "location.sumeru",
  "introduced_in": "3.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.elements", "system.dendro", "system.electro", "system.spread",
    "system.aggravate", "system.bloom", "system.burning", "system.hyperbloom", "system.elemental-mastery",
    "system.elemental-resonance", "location.sumeru", "historical.greater-lord-rukkhadevata",
    "historical.nabu-malikata"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation of Quicken", "classification": "unknown", "note": "The pages read give only tutorial text and damage rules; no story source explains why Dendro and Electro together leave a lasting charged state on a target."},
    {"topic": "Connection to Sumeru's history", "classification": "inferred", "note": "The Catalyze page's trivia says the Dendro-Electro reaction is said to have a deep connection to Sumeru's history, citing the Sumeru preview teaser about the Dendro element. Any link to the goddess Nabu Malikata or to Greater Lord Rukkhadevata is the wiki's reading of environmental clues; no character states it."},
    {"topic": "Name of the reaction group", "classification": "unknown", "note": "The wiki groups Quicken, Aggravate and Spread under the page name Catalyze, and the in-game term Catalyze Reactions is used for Spread and Aggravate in Miliastra Wonderland. The in-game tutorial for the group is titled Elemental Reaction: Catalyze."}
  ],
  "sources": [
    {"title": "Catalyze", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Catalyze", "accessed": "2026-10-12", "confidence": "high", "section": "Introduction, Duration, Damage Bonus, Trivia, Change History", "version": "3.0"},
    {"title": "Tutorial/Elemental Reaction: Catalyze", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Tutorial/Elemental_Reaction:_Catalyze", "accessed": "2026-10-12", "confidence": "high", "section": "Tutorial text", "version": "3.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table; Additive Reactions", "version": "3.0"},
    {"title": "Elemental Gauge Theory/Advanced Mechanics", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Gauge_Theory/Advanced_Mechanics", "accessed": "2026-10-12", "confidence": "medium", "section": "Quicken: aura gauge, duration, re-application"},
    {"title": "Sumeru Preview Teaser 01: The Fascinating Dendro Element", "type": "official_video", "url": "https://youtu.be/6DjVUfy_Lng", "accessed": "2026-10-12", "confidence": "low", "section": "Cited by the Catalyze page's trivia for the link to Sumeru's history; not watched directly", "version": "3.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Quicken is the elemental reaction between Dendro and Electro, in either order. It deals no damage itself. It leaves the target Quickened, with a Quicken Aura that decays over time. While the aura lasts, further Dendro or Electro hits on the target trigger the Spread or Aggravate reactions, which add bonus damage to those hits. It is a combat rule, so treat it as a gameplay abstraction, not a named law of the world.
### STANDARD +
Quicken appeared with Version 3.0 and the Dendro element, along with Sumeru. The wiki treats Quicken, Aggravate and Spread as one group called Catalyze. Spread and Aggravate have their own entries (system.spread, system.aggravate).

## in_universe
### LITE
Canon gives no story explanation for Quicken. The in-game tutorial only says that when creatures are affected by Electro and Dendro, Quicken occurs and renders them Quickened, and that Quickened creatures hit by Electro or Dendro suffer additional damage through Aggravate or Spread.
### STANDARD +
Nothing read ties the reaction to a character, god or event. Do not invent an origin or a mechanism.
### LARGE +
The wiki's trivia notes that the reaction between Electro and Dendro is said to have a deep connection to Sumeru's history, referring to Sumeru's preview teaser about the Dendro element. It speculates that this may relate to the goddess Nabu Malikata and the Dendro Archon Greater Lord Rukkhadevata, because environmental clues in Sumeru suggest Nabu Malikata may have been Electro-aligned. That is the wiki's inference: no character or text states that Nabu Malikata held Electro or links her to Quicken. Treat it as unconfirmed.

## gameplay
### LITE
Gameplay (not literal lore): Quicken happens when Dendro hits a target carrying Electro, or Electro hits a target carrying Dendro. It applies a Quicken Aura to the target, and the reaction itself deals no damage.
### STANDARD +
- A target with a Quicken Aura that is hit by Dendro triggers Spread, and by Electro triggers Aggravate. Each gives the hit a flat damage bonus added to its base damage. Spread's bonus is slightly larger than Aggravate's.
- Spread and Aggravate do not consume the Quicken Aura, so a team can keep triggering them while it lasts.
- Pyro or Hydro applied to a Quicken Aura consumes it, triggering Burning or Bloom respectively.
- Quicken Aura can coexist with Electro and Dendro auras on the same target.
### LARGE +
- The aura's duration is the smaller of the two elements' gauge units times 5 seconds, plus 6 seconds, per the wiki's formula. Triggering Quicken again replaces the old aura only if the new one is stronger.
- The bonus is the character's level multiplier times 1.25 for Spread and 1.15 for Aggravate. Elemental Mastery and certain artifacts and talents raise it. It is then affected by DMG bonuses, CRIT, DEF and RES like the rest of the hit.
- The wiki calls this class Additive reactions (an unofficial name); the game calls them Catalyze Reactions in Miliastra Wonderland. Additive bonuses differ from Melt and Vaporize, which multiply the hit.
- The Elemental Resonance Sprawling Greenery (two or more Dendro characters) gives Elemental Mastery after Quicken, Aggravate and Spread (see the Dendro entry).
### ULTRA +
- Quicken is unchanged by the newer reaction families. The Lunar reactions replace other Hydro reactions, and Stellar Glimmer reactions replace Cryo ones; as of Version 7.1 the wiki's table still lists Dendro with Electro as Quicken.
- Enemies and the environment use separate level-scaled bonus tables than characters; the wiki lists higher bonus values for them at level 100, but those numbers are not reproduced here.

## limits
### LITE
Quicken deals nothing by itself and needs both Dendro and Electro to be applied. It does not apply to plants that are not Dendro; "Wood" objects such as vines cannot trigger it.
### STANDARD +
Quicken only helps Dendro and Electro attacks. Pyro or Hydro attacks on the aura end it. Because attacks have an internal cooldown on applying their element, a source cannot apply Dendro or Electro on every hit.

## examples
### STANDARD
Gameplay example: an Electro attack lands on a target already covered in Dendro, and the target is Quickened. A Dendro character then strikes it for Spread, and an Electro character for Aggravate, both for extra damage.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Quicken as purple and green energy crawling over the target, like vines humming with charge, which makes later strikes bite harder. It reads as a setup: an unresolved charge waiting for another strike.
### LARGE +
Narratively, Quicken fits Sumeru and Dendro scenes: lush growth, damp air, crackling sparks. It rewards teamwork between a Dendro and an Electro Vision user. Keep the effect short and local to a target.
### ULTRA +
Avoid claiming that Quicken is a divine technique of the Dendro Archon or of Nabu Malikata. Do not confuse Quicken with Bloom, which Hydro and Dendro create, or with Hyperbloom, which follows Bloom.

## entry: Catalyze
@keys: Catalyze, Quicken, Quickened, Quicken Aura
### STANDARD
Catalyze is the wiki's name for the Dendro-Electro group of reactions: Quicken, which applies the aura, and Spread and Aggravate, which are the bonus-damage reactions triggered by hits on a Quickened target. The tutorial in the game is titled Elemental Reaction: Catalyze. Its English wiki page covers all three.

## entry: Spread and Aggravate
@keys: Spread, Aggravate
@keys2: Quicken, Quickened, Dendro, Electro
### STANDARD
Spread is triggered by a Dendro hit on a Quickened target, and Aggravate by an Electro hit. Both add a flat bonus to the triggering hit's base damage and do not consume the Quicken Aura. Spread's bonus is slightly higher. Each has its own entry (system.spread, system.aggravate).
