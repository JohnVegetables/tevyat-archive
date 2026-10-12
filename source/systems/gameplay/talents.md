---
{
  "id": "system.talents",
  "entity_type": "system",
  "subdir": "gameplay",
  "name": "Talent",
  "aliases": ["Talents", "character talents", "Combat Talents", "Passive Talents", "Ascension Passive"],
  "summary_line": "Talents are the abilities a playable character has: Combat Talents (Normal Attack, Elemental Skill, Elemental Burst), Ascension Passives and other Passive Talents. A game-mechanics term with little direct in-world meaning.",
  "introduced_in": "1.0",
  "spoiler_level": "minor",
  "availability": "mixed",
  "related": [
    "system.constellations", "system.ascension", "system.elemental-skill", "system.elemental-burst", "system.energy",
    "system.stamina", "system.elemental-resonance", "system.vision", "system.party", "system.nightsoul",
    "system.phlogiston", "system.moonsign", "system.moonsign-benediction-passive", "system.lunar-reaction",
    "system.stellar-jubilee-passive", "system.stellar-linchpin", "system.stellar-glimmer-reaction",
    "system.hexerei", "system.witchs-homework", "system.witchs-revelation", "location.domain", "character.traveler"
  ],
  "facts": {"system_type": "gameplay_mechanic", "lore_status": "gameplay_abstraction", "element": null},
  "uncertainties": [
    {"topic": "In-world meaning of Talents", "classification": "unknown", "note": "The wiki lists Talent as a Combat / Game Systems term and nothing found shows canon treating Talents as an in-universe category. Treat the split into Combat, Ascension and Passive as an interface convention."},
    {"topic": "Which passive categories a character has", "classification": "confirmed", "note": "Categories such as Night Realm's Gift, Moonsign Benediction, Stellar Jubilee, Witch's Eve Rite and Witch's Revelation apply only to some characters, and the wiki lists change by version; do not assume a given character has one."}
  ],
  "sources": [
    {"title": "Talent", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Talent", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, Combat Talents, Passive Talents, Level scaling", "version": "1.0"},
    {"title": "Constellation", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Constellation", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, Gameplay Notes"},
    {"title": "Character Talent Material", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Character_Talent_Material", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, Talent Books by region"},
    {"title": "1st Ascension Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/1st_Ascension_Passive", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Utility Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Utility_Passive", "accessed": "2026-10-12", "confidence": "high", "section": "Overview, bonus categories"},
    {"title": "Alternate Sprint", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Alternate_Sprint", "accessed": "2026-10-12", "confidence": "high", "section": "Compared to Normal Sprint"},
    {"title": "Night Realm's Gift Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Night_Realm%27s_Gift_Passive", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Moonsign Benediction Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Moonsign_Benediction_Passive", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Stellar Jubilee Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Stellar_Jubilee_Passive", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Witch's Eve Rite Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Witch%27s_Eve_Rite_Passive", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Witch's Homework", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Witch%27s_Homework", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Witch's Revelation", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Witch%27s_Revelation", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Witch's Revelation Passive", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Witch%27s_Revelation_Passive", "accessed": "2026-10-12", "confidence": "high"},
    {"title": "Team Bonus", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Team_Bonus", "accessed": "2026-10-12", "confidence": "high", "section": "Elemental Resonance"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
"Talents" is the game's interface term for the abilities of a playable character. Most characters have three Combat Talents (Normal Attack, Elemental Skill, Elemental Burst), two Ascension Passives and one Utility Passive. It is a gameplay abstraction: in the story people simply use their powers, skills or arts. Never have a character say "my Talent level is 9".
### STANDARD +
Talents are sorted into Combat, Ascension and Passive types. Some characters also carry extra passives tied to later systems (Natlan, Nod-Krai, Snezhnaya and Hexerei content).

## in_universe
### LITE
Nothing found shows canon using "Talents" as an in-world category. What the interface lists as Talents are, in the story, a character's fighting style, Vision or Authority power, trained techniques and personal knacks.
### STANDARD +
The one Talent-adjacent idea with real lore is the Constellation: star signs said to govern the fates of Teyvat's people, whose unlocks upgrade a character's abilities in the game. Their lore and mechanics belong to the Constellation entry; here they matter only because two of them raise Combat Talent levels.

## combat_talents
### LITE
Every character starts with three Combat Talents unlocked at level 1: the Normal Attack (their main attack form), the Elemental Skill (no Energy cost, but a cooldown) and the Elemental Burst (usually costs Energy).
### STANDARD +
Combat Talent levels rise by spending Character Talent Materials ("talent books", from the weekday Domains of Mastery of each nation) up to level 10, with the usable cap set by the character's Ascension phase. Talent levelling starts at Ascension phase 2 (around character level 40 and Adventure Rank 25).
### LARGE +
- The third and fifth Constellations each raise one specific Combat Talent by 3 levels and lift that Talent's cap from 10 to 15. Materials alone cannot go beyond level 10; the final steps to 15 need other effects.
- Some passive Talents raise the level of a category of Talent.
- During certain events, items or Stratagems temporarily raise Skill or Burst levels inside a domain.
- Values scale by a multiplier per Talent level. For most percentage values level 10 is 180% of the base, and Normal Attacks scale slightly differently. Exceptions exist, such as Xiao's and Zhongli's Bursts, which follow their own scaling.
- Talents hit the selected enemy by default, and otherwise the area in front of the character.
### ULTRA +
- Percentage values and flat values scale on different multipliers. A flat value at level 10 is 220% of the base, against 180% for percentages; the Normal Attack multiplier at level 10 is 197.5%.
- Stat effects from most passives are not shown on the Combat Talent screens, even when unconditional. The exception is Witch's Eve Rite and Witch's Revelation passives that give a Combat Talent its own buff tab.
- Alternate Sprints cannot be jumped from, may snag on stairs or rocks, and are not helped by stamina-reduction effects.

## ascension_passives
### LITE
Two passive Talents unlock with Ascension: the 1st Ascension Passive (phase 1, character level 20) and the 4th Ascension Passive (phase 4). Most improve a Combat Talent.
### STANDARD +
Ascension Passives cannot be levelled up. Their effects often do not show on the Combat Talent's own attribute screen.

## passive_talents
### LITE
Besides Ascension Passives, a character has a Utility Passive (also called an Exploration Talent), unlocked on acquisition; the Traveler has none. It does something outside combat: cooking, crafting or forging bonuses, reduced stamina cost, faster movement, expedition bonuses, resource markers on the map, or not startling certain wildlife.
### STANDARD +
Alternate Sprints replace normal sprinting and are listed as an additional passive. They cost 10 Stamina to start and 15 per second afterwards, against 18 and 18 for a normal sprint; they cannot be levelled.
### LARGE +
Special passive categories, each limited to characters tied to a system:
- Night Realm's Gift: Natlan characters, tied to Nightsoul's Blessing and Phlogiston.
- Moonsign Benediction: Nod-Krai characters and Zibai; each raises the party's Moonsign level by 1, and Columbina's and Moon Wheel users' versions also enable Lunar Reactions.
- Stellar Jubilee: Snezhnaya characters with Stellar Linchpins and the Cryo Traveler, enabling Stellar Glimmer Reactions.
- Witch's Eve Rite: Hexerei characters, unlocked by completing their Witch's Homework quest (character level 70 or above). Most effects need at least two Hexerei characters in the party.
- Witch's Revelation: certain characters, unlocked through a Witch's Revelation quest, also at level 70 or above. It enhances Talents and Constellations and lets the character enter a Radiance state inside a Polestar Field.

## gameplay
### STANDARD
Gameplay (labelled mechanics, not lore): the Normal Attack, Skill and Burst buttons use the matching Talent, and an Alternate Sprint is used if the character has one. Talents largely decide a character's role in a team; Elemental Resonance and other team bonuses sit on top of Talents rather than inside them.

## limits
### LITE
Do not give a character a numeric Talent level, a cooldown readout or an Energy bar in dialogue, and do not call story powers "Talents".
### STANDARD +
Talents are not Visions or Constellations. A Vision (or Authority) is the source of an element, while Talents are what a character does with it. The Traveler has no Utility Passive.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon): describe Talents through their fiction, such as a signature move, a technique that needs a pause before reuse (the cooldown), or a finishing move that drains the user (the Burst). A passive can show as a habit or knack. Stay with what canon shows the character doing.

## entry: Talent levels and caps
@keys: talent level, talent books, talent materials, Character Talent Material
### STANDARD
A Combat Talent starts at level 1 and rises to level 10 with Character Talent Materials, limited by Ascension phase. Constellations that raise a Talent by 3 levels lift its cap to 15.

## entry: Utility Passive
@keys: Utility Passive, Exploration Talent
### STANDARD
Each character apart from the Traveler has a Utility Passive from the start, giving a non-combat benefit such as a crafting refund, a stamina reduction, a movement bonus or map markers.
