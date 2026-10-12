---
{
  "id": "system.elemental-mastery",
  "entity_type": "system",
  "subdir": "gameplay",
  "name": "Elemental Mastery",
  "aliases": [],
  "summary_line": "Elemental Mastery is a character attribute that strengthens elemental reactions. It is a gameplay stat; in the story, skill with elements is shown through Visions and training.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction",
    "system.elements",
    "system.vision",
    "system.swirl",
    "system.crystallize",
    "system.bloom",
    "system.aggravate",
    "system.spread",
    "system.lunar-charged",
    "system.lunar-bloom",
    "system.lunar-crystallize",
    "system.stellar-conduct",
    "system.moonsign",
    "system.ascension",
    "system.elemental-resonance",
    "system.dendro"
  ],
  "facts": {
    "system_type": "gameplay_mechanic",
    "lore_status": "gameplay_abstraction"
  },
  "uncertainties": [
    {
      "topic": "In-world meaning of Elemental Mastery",
      "classification": "unknown",
      "note": "Canon never gives the stat a number or a narrative definition. Treating high mastery as a character's finesse with reactions is this project's interpretation."
    }
  ],
  "sources": [
    {
      "title": "Elemental Mastery",
      "type": "wiki",
      "url": "https://genshin-impact.fandom.com/wiki/Elemental_Mastery",
      "accessed": "2026-10-12",
      "confidence": "high",
      "section": "Overview, Formula, Enemy Elemental Mastery",
      "version": "1.0"
    },
    {
      "title": "Team Bonus",
      "type": "wiki",
      "url": "https://genshin-impact.fandom.com/wiki/Team_Bonus",
      "accessed": "2026-10-12",
      "confidence": "high",
      "section": "Elemental Resonance: Sprawling Greenery; Moonsign",
      "version": "6.0"
    }
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Elemental Mastery is an attribute that enhances elemental reactions. The higher it is, the stronger the reactions a character triggers. It is a gameplay stat with no direct in-world number.
### STANDARD +
Most playable characters start at 0. The exceptions are Lauma and Nefer, who begin at 200 and 100 respectively. It has existed since version 1.0.

## gameplay
### LITE
Gameplay (not literal lore): on triggering a reaction, Elemental Mastery boosts it. Overloaded, Superconduct, Electro-Charged, Burning, Shattered, Swirl, Bloom, Hyperbloom, Burgeon, Lunar-Charged, Lunar-Bloom, Lunar-Crystallize and Stellar-Conduct deal more damage. Melt and Vaporize multiply the triggering attack. Aggravate and Spread add bonus base damage to the triggering attack. Crystallize shields absorb more damage.
### STANDARD +
Bonus is computed as a percentage that grows with diminishing returns: the formulas are 2.78 x EM / (EM + 1400) for Vaporize and Melt, 16 x EM / (EM + 2000) for the transformative reactions listed above, 5 x EM / (EM + 1200) for Aggravate and Spread, 6 x EM / (EM + 2000) for the Lunar reactions and Stellar-Conduct, and 4.44 x EM / (EM + 1400) for Crystallize shields. The bonus is added to the reaction bonus in a multiplier of 1 + EM bonus + reaction bonus. Every extra point of mastery gives less than the last.
### LARGE +
- Enemies have 0 Elemental Mastery by default, and it is fixed and does not rise with level. Exceptions: Liam at 650 and Rilai (an Iktomisaurus Warrior: Cryocrystal Cannon) at 800.
- Increasing it: Talents, constellations, artifacts and weapons (as a secondary attribute or as part of a passive effect). Some effects raise the whole party's mastery. Certain characters' ascension stats are Elemental Mastery.
- The Dendro Elemental Resonance Sprawling Greenery gives 50 Elemental Mastery and temporary party bonuses after Dendro reactions.
- The Moonsign team bonus (Ascendant Gleam) lets non-Moonsign characters add Lunar reaction damage; for Anemo or Dendro characters this scales with Elemental Mastery at 2.25% per 100, up to the 36% cap, reached at 1,600 Elemental Mastery.
### ULTRA +
Percentages, thresholds and reaction lists are those on the wiki as of 7.1; Lunar and Stellar reactions are recent additions (6.x and 7.x). Several formulas were reverse-engineered by the community (the wiki cites player testing), so treat exact decimals as community-derived rather than officially published.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): a character with a lot of mastery is deft at combining elements and can make reactions blossom larger; show it through precision, timing and a feel for how elements push on each other rather than numbers. Characters tied to reactions in the story, such as Sucrose and Alhaitham, suit this portrayal, but their stat values are not canon facts.
### LARGE +
Do not state EM values in dialogue. A lack of mastery should not imply a character is unskilled or foolish; many strong fighters rely on raw force.

## limits
### LITE
No canon defines the stat outside the game's interface and tutorial text.
### STANDARD +
The attribute does not change Vision type or the elements a person can use.

## entry: Elemental Mastery formula
@keys: Elemental Mastery, EM bonus
@keys2: reaction, damage, formula
### LARGE
Elemental Mastery bonus for reactions: 2.78 x EM/(EM+1400) for Vaporize and Melt; 16 x EM/(EM+2000) for transformative reactions; 5 x EM/(EM+1200) for Aggravate and Spread; 6 x EM/(EM+2000) for Lunar reactions and Stellar-Conduct; 4.44 x EM/(EM+1400) for Crystallize shields. These are community-derived formulas with diminishing returns.
