---
{
  "id": "system.frozen",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Frozen",
  "aliases": ["Frozen reaction", "Freeze Aura", "Hydro-Cryo reaction"],
  "summary_line": "Frozen is the elemental reaction between Hydro and Cryo that locks a target in ice and holds it immobile; a blunt or Geo hit then breaks the ice as Shatter.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.elements", "system.hydro", "system.cryo", "system.shattered",
    "system.melt", "system.superconduct", "system.swirl", "system.geo", "system.elemental-resonance",
    "system.elemental-mastery", "creature.elemental-lifeforms", "creature.slime", "location.dragonspine"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction", "element": "Cryo"},
  "uncertainties": [
    {"topic": "In-universe cause of freezing", "classification": "unknown", "note": "The pages read describe Frozen only as a combat rule and tutorial text; no story source explains why Hydro and Cryo together freeze a target solid."},
    {"topic": "Frozen versus Sheer Cold", "classification": "inferred", "note": "The wiki carries a hatnote separating the Frozen reaction from Sheer Cold, the environmental chill of cold climates such as Dragonspine; they are different mechanics, and nothing read links them in the lore."}
  ],
  "sources": [
    {"title": "Frozen", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "high", "section": "Introduction, Duration, Shatter, Immunity, Environment, Tutorial", "version": "1.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table", "version": "1.0"},
    {"title": "Elemental Gauge Theory/Advanced Mechanics", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Gauge_Theory/Advanced_Mechanics", "accessed": "2026-10-12", "confidence": "medium", "section": "Frozen: Freeze Aura gauge and duration"},
    {"title": "Elemental Trial tutorial: Frozen", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Frozen", "accessed": "2026-10-12", "confidence": "high", "section": "Tutorial (text quoted on the Frozen page)", "version": "1.0"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Frozen is the elemental reaction that happens when Hydro and Cryo meet on a target, in either order. It deals no damage by itself. It encases the target in ice and holds it immobile for a short time. A heavy blunt blow or a Geo attack can then break the ice open, which is the Shatter follow-up. It is a combat rule, so treat it as a gameplay abstraction that a scene may borrow from.
### STANDARD +
Frozen has been part of the game since Version 1.0. The in-game tutorial says to wet opponents with Hydro, then switch to a Cryo character to trigger Frozen and control them. Shatter has its own id, system.shattered, and is also described briefly here.

## in_universe
### LITE
Canon does not give a story explanation for Frozen. The in-game text is a plain tutorial: when Cryo meets Hydro the Frozen reaction is triggered, and frozen beings cannot move.
### STANDARD +
Nothing in the sources read ties the reaction to a named character, god or event. Do not invent an origin, for example a Cryo Archon's spell or a Fatui technique.

## gameplay
### LITE
Gameplay (not literal lore): Frozen needs Hydro applied to a target already carrying Cryo, or Cryo applied to a target carrying Hydro. It deals no damage of its own. It gives the target a Freeze Aura that immobilises it for a while.
### STANDARD +
- The Freeze Aura's duration depends on the smaller of the two elemental amounts involved (the wiki's gauge units), and a target with Freeze Resistance stays frozen for less time.
- Shatter is triggered when a Frozen target is hit by a blunt attack or by Geo. It deals Physical damage and removes the Freeze Aura.
- Applying Pyro to a Freeze Aura consumes it and triggers Melt, Electro triggers Superconduct, and Anemo triggers Swirl.
- A blunt hit first uses up part of the Freeze Aura according to its Poise damage, and Shatter occurs only if some Freeze Aura is left afterwards.
### LARGE +
- Immunity: during an Elemental Burst's invincibility frames no character can be frozen, and the wiki lists a few character abilities with the same protection (Fischl's Midnight Phantasmagoria, Mona's Mirror Reflection of Doom hold, the Wanderer's Hanega: Song of the Wind, and Chasca's Nightsoul's Blessing state). On a target immune to freezing, the reaction still triggers but the Freeze Aura does not apply and the target is not immobilised.
- Enemy immunity and resistance: most bosses are always immune, and the wiki lists many individual enemies as immune in certain states, such as Cryo Slimes, Large Cryo Slimes, Cryo Abyss Mages and the Tainted Hydro Phantasm when enraged. Freeze Resistance values are given for a few enemies; most land Local Legends have 90 percent.
- Shatter's damage follows the transformative-reaction model: it depends on the triggering character's level and Elemental Mastery, not on ATK.
- The Elemental Resonance Shattering Ice (two or more Cryo characters) raises CRIT Rate against targets that are Frozen or affected by Cryo; see the Cryo entry.
### ULTRA +
- The wiki's gauge model: the Freeze Aura holds twice the smaller of the two input amounts, and its duration grows more slowly than that amount does (a square-root relationship). This describes the gameplay framework, which the wiki calls Elemental Gauge Theory, not a character's explanation.
- Shatter happens before any elemental damage in the same hit, so it can prevent some reactions, but an element can persist or be reapplied under a Freeze Aura and react afterwards; the wiki's example is Hydro under a Freeze Aura being Crystallized after Shatter.
- Since Version 5.8, Lunar reactions replace Electro-Charged, Bloom and Crystallize in parties with a matching Moonsign passive, and since 7.0 Stellar Glimmer reactions replace Superconduct and Cryo Swirl in parties with a matching Stellar Jubilee passive. Frozen is not replaced by either family; the wiki's table lists it unchanged as of 7.1.

## environment
### STANDARD
Gameplay: in the open world, parts of most bodies of water can be frozen by Cryo attacks, and characters and enemies can stand on the ice. Pyro melts the ice instantly, and Electro on it can cause Superconduct, which the wiki notes also happens near Electro-Charged water.
### LARGE +
The frozen-water duration depends on how strong the Cryo application is, from about 2.5 seconds for a basic application to 8 seconds for the strongest one the wiki lists (Kaeya's Frostgnaw). Cryo Slimes and Cryo Abyss Mages freeze nearby water for about 8 seconds. Some objects can also be frozen, such as the Baron Bunny and Ushi gadgets from Masatsu Zetsugi: Akaushi Burst!, though explosive objects such as Exploding Barrels can only be frozen without being set off by damageless applications of Hydro and Cryo.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Frozen as a visible shell of ice that forms fast around the target, with a sharp crack and a spray of fragments when it breaks. A frozen person or creature is held in place, not killed; keep it a short, temporary combat effect. Frost is the Cryo cue; a blow that cracks the ice should feel heavy, like a hammer or a stone-hard Geo strike.
### LARGE +
Narratively, Hydro first and Cryo second reads as wet things freezing, which is easy to depict. Do not mix up Frozen with the cold of Dragonspine or with Snezhnaya's winter; a frozen target in a warm room is still frozen by the reaction. Pyro frees a frozen ally by melting the ice, since Pyro consumes the Freeze Aura (Melt).
### ULTRA +
Avoid having ordinary Hydro and Cryo users freeze large crowds permanently, kill by freezing, or freeze a god or boss; the wiki lists most bosses as immune. Keep any Shatter damage proportionate.

## limits
### LITE
Frozen does not hurt by itself, and it does not last long. It does not work on every enemy.
### STANDARD +
The Freeze Aura does not react with Hydro. Elemental shields and some innate enemy auras carry a different frozen state of Cryo that is not the same as a reaction-made Freeze Aura.

## examples
### STANDARD
Gameplay example, from the in-game tutorial: soak an opponent with Hydro, then switch to a Cryo character and attack, and the opponent is frozen. A hammer strike or a Geo blow then Shatters it.

## entry: Shatter
@keys: Shatter, Shattered
### STANDARD
Shatter is the follow-up to Frozen. When a Frozen target is hit by a blunt attack or a Geo attack, the ice breaks and the target takes Physical damage; the Freeze Aura is removed. It uses the transformative-reaction damage model. Its own entry is system.shattered. The wiki's main page for it redirects to the Frozen page.

## entry: Freeze Resistance and immunity
@keys: Freeze Resistance, Freeze Aura
@keys2: Frozen, Hydro, Cryo
### LARGE
Some targets resist or ignore freezing. Freeze Resistance shortens the Freeze Aura on a target; the wiki lists the Abyss Herald Wicked Torrents while shielded, the Consecrated Beast, the Canine Bunshin and most land Local Legends among those with it. A target immune to freezing still triggers the reaction, but is not immobilised.
