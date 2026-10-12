---
{
  "id": "item.parametric-transformer",
  "entity_type": "item",
  "subdir": "gadgets",
  "name": "Parametric Transformer",
  "aliases": ["Parametric Transformer gadget", "transmutation device"],
  "summary_line": "A mysterious device found in ruins near Liyue Harbor that accelerates material cycles, turning a deposited pile of items into different materials once elemental energy has charged it; the Traveler receives it from the Tianqiu Treasure Trail.",
  "nation": "location.liyue",
  "introduced_in": "1.3",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "location.liyue", "location.liyue-harbor", "location.dunyu-ruins", "location.tianqiu-valley", "npc.lan",
    "faction.adventurers-guild", "character.traveler", "npc.paimon", "cosmology.ley-lines", "item.mora"
  ],
  "facts": {
    "item_type": "gadget",
    "weapon_type": null,
    "rarity": 4,
    "owners": ["character.traveler"],
    "origin": "Found by the Traveler as a 'Strange Box' near Dunyu Ruins during the world quest Tianqiu Treasure Trail; its makers are not stated in canon",
    "gameplay_note": "A placeable, reusable gadget. About 150 quality points of non-event materials are loaded in, elemental attacks charge it, and it then disappears and pays out materials; it has a cooldown of roughly 7 days."
  },
  "uncertainties": [
    {"topic": "Who made the device and why it lay near Dunyu Ruins", "classification": "unknown", "note": "The item text only says it was discovered in the ruins. In the quest Lan is puzzled that such a thing was at Dunyu Ruins, an area that has been searched many times; no maker, age or purpose beyond transmutation is given."},
    {"topic": "Exact reward odds", "classification": "inferred", "note": "The wiki's reward tables and the 5 to 10 sets per use come from community data gathering (Genshin Impact Data Gathering team), not from official text. Treat them as approximate observations."},
    {"topic": "Cooldown length", "classification": "confirmed", "note": "The in-game description says 7 days; the wiki measures it as 6 days 22 hours, rounded up in the description."}
  ],
  "sources": [
    {"title": "Parametric Transformer", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Parametric_Transformer", "accessed": "2026-10-12", "confidence": "high", "section": "Infobox, description, gauge meter, fuel type, possible rewards, notes, Archive description", "version": "1.3"},
    {"title": "Tianqiu Treasure Trail", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Tianqiu_Treasure_Trail", "accessed": "2026-10-12", "confidence": "high", "section": "Steps, Dialogue (Lan, Strange Note, Strange Box)", "version": "1.3"}
  ],
  "status": "drafted",
  "last_verified": null,
  "notes": "Short gadget entry. Quest version is taken from the gadget's wiki change history (1.3); the quest page itself was not checked for a separate version. The wiki page carries a stub note about unconfirmed edge cases (whether limited-event combat dismisses a deployed device); those are omitted. No Nod-Krai or Snezhnaya (6.x/7.x) appearance was found."
}
---

## summary
### LITE
The Parametric Transformer is a gadget the Traveler wins in Liyue by solving an Adventurers' Guild treasure riddle. It is a mysterious device from the ruins that can "transmute" material objects: a heap of ordinary materials goes in, and different materials come out after elemental energy has charged it.
### STANDARD +
It is a placeable device, usable again after about a week. Its Archive text frames transmutation as accelerating the natural cycles of the world, and no maker or origin is given.

## appearance
### STANDARD
In the inventory it is a four-star gadget. It is set down on a flat surface, where it shows a charge gauge. The wiki lists a "Deployed" state and a "Loaded" state. Canon does not describe its build beyond calling it a device.

## lore
### LITE
Lan, who works at the Liyue Harbor Adventurers' Guild, posts a rumour about treasure near Tianqiu Valley. Nobody has found it. The Traveler follows a treasure map to Dunyu Ruins, reads a rhyming note about a giant tree, a road and a flight of stairs, opens three chests, and finds a strange box. Lan has never seen anything like it.
### STANDARD +
Lan says that, by the adventurers' code, whatever is found belongs to the finder, and that the Guild only wanted the experience of solving the riddle. Puzzled that the box was at Dunyu Ruins, a place searched many times, Lan arranges a closer search there.
### LARGE +
The Archive description reads as a small piece of philosophy. Everything is said to be in a cycle: memories and elements surge in the ley lines, rotten fallen fruit returns to the soil, and trees born of the soil one day bear crystal fruit. The device speeds such cycles up.
### ULTRA +
Nothing in canon says who built the device, how it came to be at Dunyu Ruins, or whether it is linked to ley-line research. Do not invent one; in a scene it works best as a puzzling relic that someone has put to practical use.

## owners
### STANDARD
The Traveler holds the only copy shown in canon. Lan hands it over as the finder's reward.

## gameplay
### STANDARD
Game mechanics (not in-world fact). The device is placed on a valid surface and loaded with non-event materials worth a total quality of 150 or more. It must be charged with Elemental damage, either from the player or from an environmental source such as an Electro Crystal. It cannot be used while in combat and is dismissed if the player wanders off or draws enemies, keeping the loaded materials for the next try. After use it has a cooldown of about 7 days. The first use grants the achievement "Transmutation Nuclide".
### LARGE +
The wiki counts about 18 elemental hits to fill the gauge, with a 0.4 second delay between charges, regardless of how large the elemental application is. Material quality is tiered: ordinary produce and ore count as 1, and higher-tier enemy drops count as 1, 2 or 4.
### ULTRA +
Community observation (Genshin Impact Data Gathering team, not official) puts the payout at 5 to 10 sets, most often 5 to 7. Each set is drawn from groups such as 20,000 Mora, character and weapon experience materials, 3-star and 2-star character ascension materials, talent books and weapon ascension materials. The mix of materials fed in appears to shift which groups come up, but never guarantees one.

## entry: Tianqiu Treasure Trail
@keys: Tianqiu Treasure Trail
@version: 1.3
@availability: permanent
### STANDARD
A Liyue Harbor world quest that gives the Parametric Transformer. Lan of the Adventurers' Guild passes on a treasure riddle near Tianqiu Valley. After fighting hilichurls the Traveler gets a treasure map to Dunyu Ruins, finds the Strange Note, opens three chests and returns with a Strange Box. Lan lets the Traveler keep it, with the reward.
