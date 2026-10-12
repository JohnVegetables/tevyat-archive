---
{
  "id": "system.lunar-charged",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Lunar-Charged",
  "aliases": ["Lunar Charged", "Lunar-Charged reaction", "thundercloud reaction"],
  "summary_line": "Lunar-Charged is the Lunar Reaction that replaces Electro-Charged when Electro meets Hydro and a party member has a matching Moonsign Benediction; it spawns a thundercloud and can crit.",
  "nation": "location.nod-krai",
  "introduced_in": "5.8",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.lunar-reaction", "system.lunar-bloom", "system.lunar-crystallize", "system.electro-charged", "system.electro", "system.hydro",
    "system.moonsign", "system.moonsign-benediction-passive", "system.elemental-reaction", "system.elemental-mastery",
    "system.elemental-resonance", "character.ineffa", "character.flins", "character.columbina", "location.nod-krai"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Electro"},
  "uncertainties": [
    {"topic": "In-universe explanation of Lunar-Charged", "classification": "unknown", "note": "The Lunar-Charged page, its tutorial, the 5.8 patch notes and Ineffa's page are all gameplay text. No source read explains the thundercloud as something that exists in the story world."},
    {"topic": "Thundercloud range", "classification": "disputed", "note": "The wiki gives about 5 m for the cloud's reach but marks the figure with a verification flag, so it is treated as approximate."},
    {"topic": "Release version versus Moonsign", "classification": "confirmed", "note": "Lunar-Charged was introduced in 5.8 with Ineffa, ahead of the Moonsign party bonus and Nod-Krai region, which arrived in Version 6.0 (Luna I)."}
  ],
  "sources": [
    {"title": "Lunar-Charged", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Lunar-Charged", "accessed": "2026-10-12", "confidence": "high", "section": "Damage; Talents", "version": "5.8"},
    {"title": "Tutorial: Elemental Reaction: Lunar-Charged", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Tutorial/Elemental_Reaction:_Lunar-Charged", "accessed": "2026-10-12", "confidence": "high", "section": "Tutorial text", "version": "5.8"},
    {"title": "Version 5.8", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Version/5.8", "accessed": "2026-10-12", "confidence": "high", "section": "New Systems; Lunar-Charged", "version": "5.8"},
    {"title": "Ineffa", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Ineffa", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Lunar-Charged passive", "version": "5.8"},
    {"title": "Damage", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Damage", "accessed": "2026-10-12", "confidence": "high", "section": "Lunar and Stellar Glimmer Reaction Damage; Indirect; Direct"},
    {"title": "Moonsign", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Moonsign", "accessed": "2026-10-12", "confidence": "high", "section": "Elemental Resonance: High Voltage", "version": "6.0"},
    {"title": "Thundercloud", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Thundercloud", "accessed": "2026-10-12", "confidence": "medium", "section": "Genius Invokation TCG summon created by Lunar-Charged"},
    {"title": "Version Luna I", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Version/6.0", "accessed": "2026-10-12", "confidence": "high", "section": "Limited-time mode boosts to Lunar-Charged", "version": "6.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Lunar-Charged is the Lunar Reaction between Electro and Hydro. When the two meet on a target and the party includes a character whose Moonsign Benediction passive enables it, the usual Electro-Charged is replaced by Lunar-Charged. The reaction forms a thundercloud that keeps firing lightning at nearby enemies carrying both Electro and Hydro. Its damage can crit. It was the first Lunar Reaction, arriving in Version 5.8 alongside Ineffa.
### STANDARD +
Unlike Electro-Charged, the damage is based on every character who applied an element during the reaction, so the whole party shares in it. The damage is Electro.

## in_universe
### LITE
Canon offers no in-world explanation. The thundercloud is shown only in tutorial and combat material. Treat it as a gameplay abstraction that a scene may borrow as a storm gathering over a fight.
### STANDARD +
Related setting: Ineffa, the character who introduced the reaction, is a 5-star Electro polearm user, and the reaction came out in 5.8, before the Nod-Krai region opened in 6.0. The wiki also lists a Genius Invokation TCG summon called Thundercloud created by Lunar-Charged; that is a card game effect, not a story event.

## gameplay
### LITE
Gameplay (not literal lore): the thundercloud deals Electro damage to all Wet enemies who are also affected by Electro within roughly 5 m, every 2 seconds. A target that has not been hit in the last 2 seconds and is Wet or Electro-affected is struck at once when the other aura lands on it.
### STANDARD +
- Each strike uses up 0.4 gauge units of the Wet and Electro auras together.
- The cloud lasts 6 seconds, which resets if another Lunar-Charged triggers. Only one cloud exists at a time; triggering outside its range makes a new one and removes the old one.
- Thunderclouds try to position themselves between active targets and the triggering party.
### LARGE +
- Lunar-Charged shares all other properties of Electro-Charged, including damaging the wards of Hydrogunner Legionnaires at a higher rate.
- Damage is dealt indirectly (by applying elements) or directly by a talent. The base reaction coefficient is 3 in both cases. The elemental mastery bonus is 6 x EM / (EM + 2000).
- A party member with a Moonsign Benediction turns the reaction on; the wiki lists Ineffa (Assemblage Hub), Flins (Old World Secrets) and Columbina as providing a Lunar-Charged base damage bonus, up to 14% for the first two and up to 7% for Columbina.
- Artifact sets and weapons such as Night of the Sky's Unveiling, Silken Moon's Serenade and Bloodsoaked Ruins increase Lunar-Charged damage.
### ULTRA +
- High Voltage resonance (two Electro characters) gives Lunar-Charged a 100% chance to generate an Electro particle, with a 5-second cooldown.
- Event and mode buffs have boosted it: the 5.8 notes show a 75% increase to Electro-Charged and Lunar-Charged damage in one half of a limited-time mode, and the 6.0 notes show similar 75% boosts in two halves of another.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show a small, low thundercloud that follows the fight, flickers when Electro and water are on the same enemy, and drops short bolts. Keep it a visible, compact storm rather than a weather event. Reserve it for scenes with an Electro user and a Hydro user.
### LARGE +
Because everyone who applied an element contributes, narrate it as a team effort: one person soaks, another sparks, and the cloud answers both. No named character in the sources read calls the effect by its game name in dialogue.
### ULTRA +
Do not give the cloud a will or intelligence, and do not present it as Ineffa's personal invention; the wiki ties its availability to Moonsign Benediction talents, not to a story event.

## limits
### LITE
The cloud only strikes enemies that carry both Electro and Hydro (Wet), and only one cloud can exist at a time.
### STANDARD +
Without a Moonsign Benediction character who enables it, Electro meeting Hydro simply makes the ordinary Electro-Charged.
### LARGE +
The 5 m reach is flagged on the wiki as unconfirmed. Range and tick figures belong to the game mechanic and should not be quoted in story as exact distances.

## entry: Thundercloud
@keys: thundercloud, Thundercloud
@keys2: Lunar-Charged, Ineffa, Electro
@spoiler: none
### STANDARD
A thundercloud is the object created by a Lunar-Charged reaction. It lasts 6 seconds, drifts between targets and the triggering party, and fires Electro damage at nearby enemies that are both Wet and affected by Electro. A Genius Invokation TCG summon shares the name.
