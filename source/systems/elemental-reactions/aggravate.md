---
{
  "id": "system.aggravate",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Aggravate",
  "aliases": ["Aggravate reaction", "Electro Catalyze reaction"],
  "summary_line": "Aggravate is the Catalyze reaction in which an Electro attack on a target under a Quicken aura gains a flat bonus to its damage; it is the Electro counterpart of Spread.",
  "introduced_in": "3.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.quicken", "system.spread", "system.electro", "system.dendro",
    "system.elemental-mastery", "system.swirl", "system.burning", "system.bloom"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Electro"},
  "uncertainties": [
    {"topic": "In-universe explanation", "classification": "unknown", "note": "No source read for this entry gives an in-world explanation of Aggravate or of the Electro and Dendro pairing. The wiki notes only that the reaction is said to have a deep connection to the history of Sumeru (from the Sumeru Preview Teaser), and speculates about Nabu Malikata; that speculation is fan inference."},
    {"topic": "Whether Aggravate is a separate entity from Quicken", "classification": "unknown", "note": "On the wiki, Aggravate redirects to the Catalyze page, which covers Quicken, Aggravate and Spread together. This entry covers the Aggravate step; the aura it depends on is described under Quicken."}
  ],
  "sources": [
    {"title": "Catalyze (Aggravate redirects here)", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Catalyze", "accessed": "2026-10-12", "confidence": "high", "section": "Duration, Damage Bonus, Trivia", "version": "3.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table"},
    {"title": "Elemental Reaction Intro (template)", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Template:Elemental_Reaction_Intro", "accessed": "2026-10-12", "confidence": "high", "section": "Catalyze: Quicken, Spread, Aggravate"},
    {"title": "Damage", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Damage", "accessed": "2026-10-12", "confidence": "high", "section": "Catalyze Damage Bonus"},
    {"title": "Swirl", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Swirl", "accessed": "2026-10-12", "confidence": "high", "section": "Overview (swirl-induced Aggravate)"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Aggravate is the Electro half of the Catalyze family. First an Electro hit and a Dendro hit meet and put a Quicken aura on the target; after that, further Electro hits on the Quickened target trigger Aggravate, which makes each of them hit harder by a flat amount. It is a combat rule rather than a story event, and the reaction arrived with Version 3.0.
### STANDARD +
Aggravate does not consume the Quicken aura, so it can fire again and again until the aura runs out. Dendro attacks on the same aura trigger Spread instead, which gives a larger bonus.

## in_universe
### LITE
Canon presents Aggravate only through the Elemental Trial tutorial and gameplay text. The wiki records that the Electro and Dendro reaction is said to have a deep connection to the history of Sumeru, but no source read for this entry explains how.
### STANDARD +
Any link between Electro and Dendro in Sumeru's past, including claims about Nabu Malikata, is inference by wiki editors, not stated canon. Keep scenes from asserting one.

## gameplay
### LITE
Gameplay (not literal lore): an Electro attack on a target with a Quicken aura triggers Aggravate and adds an Additive Base DMG Bonus to that attack's damage. Aggravate does not consume the aura.
### STANDARD +
The bonus is 1.15 times the level multiplier of the character, increased by a percentage from Elemental Mastery and any Reaction DMG Bonus, and then added to the attack's base damage before the usual damage bonuses, CRIT, DEF and RES. Spread is the Dendro version, with coefficient 1.25.
### LARGE +
Quicken itself is created when Electro and Dendro meet. Its duration is 6 seconds plus 5 seconds for each gauge unit of the weaker of the two elements involved. Applying Pyro or Hydro to a Quicken aura consumes it and triggers Burning or Bloom instead. A Swirl can also trigger Aggravate secondarily, using the Anemo character's level and EM. Talents and artifact sets exist that increase the bonus.

### ULTRA +
The wiki gives the Elemental Mastery bonus for Catalyze reactions as approximately 5 x EM / (EM + 1200), applied to the base coefficient times the level multiplier. The final Additive Base DMG Bonus is added to any bonus the attack already had. Enemies and the environment use a slightly different level multiplier above level 60 than characters, and the wiki's table lists no character values for level 100.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show a Quickened target as crackling with green-violet energy, so that each Electro strike lands with extra bite as lightning bites into the growing charge. Keep it a rising intensity, not a new effect.
### LARGE +
Narrate Aggravate as repeated strikes getting stronger while the Quicken lasts. Do not describe the plant energy as consumed by the lightning; the aura stays until it decays or Pyro or Hydro ends it.

## limits
### LITE
Aggravate needs an existing Quicken aura and an Electro attack that can apply Electro; Dendro attacks trigger Spread instead.
### STANDARD +
The bonus belongs to the attack that triggers it, so Aggravate does nothing on its own and adds nothing to a skill that deals no damage.
### LARGE +
The two catalyze bonuses depend on the triggering character: the Electro user's stats count for Aggravate. Gameplay values here are as listed by the wiki as of Version 7.1.

## entry: Aggravate
@keys: Aggravate, Aggravate reaction
### STANDARD
Aggravate is the Electro Catalyze reaction (Version 3.0). An Electro attack on a Quickened target gains a flat damage bonus without using up the Quicken aura.
### LARGE +
Quicken lasts 6 seconds plus 5 seconds per gauge unit of the weaker element. Dendro attacks on it trigger Spread (coefficient 1.25) rather than Aggravate (1.15), and Pyro or Hydro would instead consume it into Burning or Bloom.
