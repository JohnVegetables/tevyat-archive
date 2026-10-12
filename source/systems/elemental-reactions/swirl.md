---
{
  "id": "system.swirl",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Swirl",
  "aliases": ["Swirl reaction", "Anemo Swirl", "Pyro Swirl", "Hydro Swirl", "Electro Swirl", "Cryo Swirl"],
  "summary_line": "Swirl is the elemental reaction in which Anemo meets Pyro, Hydro, Electro or Cryo and carries that element outward to nearby targets, dealing damage and sometimes setting off further reactions.",
  "introduced_in": "1.0",
  "spoiler_level": "minor",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.anemo", "system.pyro", "system.hydro", "system.electro", "system.cryo",
    "system.stellar-swirl", "system.stellar-glimmer-reaction", "system.elemental-mastery", "system.frozen",
    "system.vaporize", "system.melt", "system.overloaded", "system.aggravate", "creature.hypostasis"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Anemo"},
  "uncertainties": [
    {"topic": "In-universe explanation", "classification": "unknown", "note": "No source read for this entry explains in-world why wind spreads other elements; Swirl is described only in tutorial and gameplay text."},
    {"topic": "Stellar Swirl and Cryo Swirl", "classification": "unknown", "note": "Stellar Swirl (7.0) replaces Cryo Swirl when a character with a matching Stellar Jubilee passive is in the party. The wiki credits the introduction of Stellar Glimmer reactions to ancient Snezhnaya through Saarelainen (7.0 Special Program), but no mechanism is given."}
  ],
  "sources": [
    {"title": "Swirl", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Swirl", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, Damage, Tutorial", "version": "1.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table; Transformative Reactions"},
    {"title": "Elemental Reaction Intro (template)", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Template:Elemental_Reaction_Intro", "accessed": "2026-10-12", "confidence": "high", "section": "Swirl: 6 m radius; Frozen interaction; Anemo Hypostasis note"},
    {"title": "Damage", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Damage", "accessed": "2026-10-12", "confidence": "high", "section": "Transformative Reaction Damage"},
    {"title": "Stellar Glimmer Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Stellar_Glimmer_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Lore", "version": "7.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Swirl is what happens when Anemo meets another element on a target: the wind catches that element and flings it outward, so everything nearby is hit or soaked with it. It works with Pyro, Hydro, Electro and Cryo, but not with Geo or Dendro. It is a combat rule rather than a story event.
### STANDARD +
Swirl deals its own damage in the swirled element (except Hydro, which only spreads Wet), based on the Anemo user's level and Elemental Mastery rather than ATK. Because it re-applies the element, it can set off further reactions on neighbouring targets.

## in_universe
### LITE
Canon presents Swirl only through the Elemental Trial tutorial and gameplay text; no source read gives an in-world account of why wind spreads elements. Treat any explanation as a scene decision.
### STANDARD +
The tutorial wording is that when Anemo touches Hydro, Pyro, Cryo or Electro, the element in contact affects a larger area and can trigger other reactions.
### ULTRA +
Version 7.0 introduced Stellar Swirl, a Stellar Glimmer reaction that replaces Cryo Swirl when a character with a matching Stellar Jubilee passive is in the party. Ordinary Cryo Swirl is unchanged outside that condition (see its own entry).

## gameplay
### LITE
Gameplay (not literal lore): Swirl applies the non-Anemo element to targets within a 6 m radius, except the target the reaction was triggered on. Pyro, Electro and Cryo Swirl also deal AoE damage of that element; Hydro Swirl spreads Wet and deals damage only to the triggering target.
### STANDARD +
It is a transformative reaction with base coefficient 0.6 (from the wiki's Damage page), scaled by the Anemo character's level and Elemental Mastery. It cannot CRIT by default and ignores ATK. The wiki separates this from Elemental Absorption, where an Anemo skill absorbs an element and deals ordinary damage of it; that damage uses normal attack stats.
### LARGE +
Secondary reactions caused by a Swirl take their damage from the Anemo user: swirled Pyro onto an Electro target triggers Overloaded using the Anemo character's level and EM, and swirl-induced Melt, Vaporize or Aggravate are likewise scaled by them. One target takes at most 2 Swirl instances every 0.5 seconds from the same attacker, and several Swirls of one element on a target within 0.1 seconds count once, with limits separate for each swirled element.
### ULTRA +
Players cannot apply a lasting Anemo aura, so Swirl is normally triggered by an Anemo attack landing on a target already affected by another element. The one exception noted on the wiki is the Anemo Hypostasis, which keeps Anemo on itself while its core is exposed. An Anemo hit on a Frozen target consumes the Freeze to trigger Swirl.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Swirl as a gust that grabs the burning, dripping, crackling or frosted thing and throws it out in a ring, with a scatter of sparks, spray or frost. The wind should visibly carry the element.
### LARGE +
Hydro Swirl is the gentlest form: spray and dampness that leaves neighbours Wet, with no burst. Do not have the wind create an element that was not already present on the target.

## limits
### LITE
Swirl does not work with Geo or Dendro, and Anemo has no reaction with itself.
### STANDARD +
It spreads an element already present; it does not create one. The swirled element is not applied back to the triggering target, which lets the original target keep its own state.
### LARGE +
Hydro Swirl does no area damage. Swirl damage is unaffected by ATK, CRIT or general damage bonuses; only Swirl-specific bonuses raise it.

## entry: Swirl
@keys: Swirl, Swirl reaction, Pyro Swirl, Hydro Swirl, Electro Swirl, Cryo Swirl
### STANDARD
Swirl is the Anemo reaction with Pyro, Hydro, Electro or Cryo. It spreads that element to everything within 6 m of the target and deals the element's damage (Hydro only spreads Wet).
### LARGE +
It scales with the Anemo character's level and Elemental Mastery, and secondary reactions it causes borrow those stats. In 7.0, Stellar Swirl can replace Cryo Swirl when the matching passive is in the party.
