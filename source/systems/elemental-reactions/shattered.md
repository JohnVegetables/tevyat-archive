---
{
  "id": "system.shattered",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Shattered",
  "aliases": ["Shatter", "Shattered reaction", "Shatter reaction"],
  "summary_line": "Shatter (the Shattered reaction) is the follow-up to Frozen: a blunt or Geo hit on a frozen target breaks the ice and deals Physical damage.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.frozen", "system.geo", "system.cryo", "system.hydro", "system.physical",
    "system.melt", "system.superconduct", "system.swirl", "system.crystallize", "system.elemental-mastery"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Physical"},
  "uncertainties": [
    {"topic": "In-universe cause of Shatter", "classification": "unknown", "note": "The pages read describe Shatter only as a combat rule; no story source explains the mechanism beyond the plain image of ice being broken."},
    {"topic": "Separate page", "classification": "unknown", "note": "The wiki has no page of its own for Shatter or Shattered; the names redirect to the Frozen page, where it is a section. Frozen is its own entity (system.frozen)."},
    {"topic": "Name", "classification": "confirmed", "note": "The wiki's reaction list names the reaction Shattered, while the Frozen page calls the event Shatter. Both are used for the same reaction."}
  ],
  "sources": [
    {"title": "Frozen", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "high", "section": "Shatter, Immunity, Tutorial, Change History", "version": "1.0"},
    {"title": "Elemental Reactions", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reactions", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table, Transformative Reactions"},
    {"title": "Elemental Gauge Theory/Simultaneous Reaction Priority", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Gauge_Theory/Simultaneous_Reaction_Priority", "accessed": "2026-10-12", "confidence": "medium", "section": "Cited from the Frozen page for Shatter ordering"},
    {"title": "Elemental Trial tutorial: Frozen", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "medium", "section": "Tutorial text", "version": "1.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Shatter, listed in the wiki's reaction list as Shattered, is the follow-up to Frozen. When a frozen target is hit by a blunt attack or a Geo attack, the ice breaks apart, the Freeze Aura is removed, and the target takes Physical damage.
### STANDARD +
It has been part of the game since 1.0 along with Frozen, which has to happen first. Hydro and Cryo together make a target Frozen; a heavy or Geo strike then shatters it.

## in_universe
### LITE
Canon gives no in-world explanation for Shatter. The pages read treat it as a combat rule, so it is best understood as the ordinary physical fact that frozen things break when hit hard.

## gameplay
### LITE
Gameplay: a Frozen target hit by a blunt attack (a claymore swing, a heavy hammer strike) or by Geo takes Shatter damage, and the Freeze Aura ends.
### STANDARD +
- Shatter deals Physical damage and is a transformative reaction: it has its own base damage set by the reaction type and the level of the character who triggers it, and that damage is raised by Elemental Mastery. It cannot critically strike, is not based on ATK, and is reduced by the target's resistance.
- Shatter happens before any elemental damage in the same hit, which can prevent some other reactions.
### LARGE +
- A blunt attack first uses up part of the Freeze Aura according to its Poise damage. Shatter triggers only if some aura remains afterwards.
- An element can persist or be reapplied underneath the Freeze Aura, so another reaction can follow. The wiki's example is Let the Show Begin, then Kaeya's Frostgnaw, then Starfell Sword: the Geo hit Shatters the ice and then Crystallizes the Hydro beneath it.
- A target that is immune to freezing still triggers Frozen but gets no Freeze Aura, so there is nothing to shatter. The wiki lists most bosses and several enemies as immune in this way.
### ULTRA +
- Shatter is listed among the transformative reactions with Overloaded, Electro-Charged, Superconduct, Swirl, Burning, Bloom, Hyperbloom and Burgeon.
- The wiki's reaction table still shows Frozen and its Shatter follow-up as of 7.1, alongside the Lunar and Stellar Glimmer variants of other reactions.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show a crack running through a coating of ice, a sharp snap, and a spray of fragments flying outwards. A Geo strike should feel like a stone slamming into the ice; a claymore should feel like a heavy hammer blow.
### LARGE +
The blow should be solid and decisive. It ends a short, temporary freeze, so the target is hurt by the impact, not turned to powder. The fragments are loud and sparkle, which suits a dramatic combat beat.
### ULTRA +
Avoid having a Shatter kill by itself, or break a god or a boss that the game treats as freeze-immune. Do not make it a way to smash frozen water or objects at will; keep the scale of a single fight.

## limits
### LITE
Shatter needs a Frozen target and a blunt or Geo hit. Weak physical strikes may not be enough.
### STANDARD +
It removes the Freeze Aura, so it ends the Frozen state. Pyro, Electro or Anemo on a Freeze Aura trigger Melt, Superconduct or Swirl instead.

## examples
### STANDARD
Gameplay example, from the in-game tutorial: soak an opponent with Hydro, switch to a Cryo character to freeze them, then strike with a Geo or blunt attack to Shatter.

## entry: Frozen reaction
@keys: Freeze Aura
@keys2: Shatter, Shattered
### STANDARD
Frozen is the Hydro-Cryo reaction that immobilises a target with a Freeze Aura. Shatter is the follow-up that breaks that aura with a blunt or Geo hit. See system.frozen for the full rule set, resistance and immunity.
