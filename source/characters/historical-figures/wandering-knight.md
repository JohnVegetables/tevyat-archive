---
{
  "id": "historical.wandering-knight",
  "entity_type": "historical_figure",
  "name": "Wandering Knight",
  "aliases": ["Wolf Knight", "First Knight of Boreas", "Knight of Boreas (first)", "nameless knight of Boreas"],
  "summary_line": "The nameless first Knight of Boreas, who came to Mondstadt a thousand years ago in Vennessa's time with the wolf Boreas, forged the legend of the Wolf Knight and left without a successor.",
  "nation": "location.mondstadt",
  "tags": ["Mondstadt", "Knight of Boreas", "Wolf Knight", "Vennessa's era", "historical"],
  "introduced_in": "1.0",
  "spoiler_level": "minor",
  "availability": "permanent",
  "related": [
    "npc.andrius", "historical.vennessa", "historical.ravenwood", "character.varka", "faction.knights-of-favonius",
    "faction.four-winds", "item.wolfs-gravestone", "item.wolf-fang", "item.gest-of-the-mighty-wolf",
    "historical.rostam", "quest.lupus-majoris-chapter", "location.temple-of-the-wolf", "location.wolvendom",
    "location.mondstadt-city", "location.mondstadt"
  ],
  "relationships": [
    {"target": "npc.andrius", "type": "companion", "summary": "He travelled with Andrius, the wolf god who took the name Boreas; their journey is the heart of the Wolf Knight tales. In the Wolf's Gravestone text he buries his wolf companion and leaves the city.", "classification": "confirmed", "since": "1.0"},
    {"target": "historical.vennessa", "type": "would-be recruiter", "summary": "The first Grand Master never gave up trying to recruit him; he always refused.", "classification": "confirmed", "since": "6.4"},
    {"target": "historical.ravenwood", "type": "informal disciple", "summary": "A blacksmith's son who admired him, followed him around and later took up the title of Knight of Boreas himself.", "classification": "confirmed", "since": "6.4"},
    {"target": "character.varka", "type": "distant successor; echo in the Ley Lines", "summary": "In Varka's 6.4 story the knight's voice is heard as an echo and as a Longing in the Wolf's Gravestone, urging Varka onward.", "classification": "confirmed", "since": "6.4"}
  ],
  "knowledge": {"knows": [], "does_not_know": [], "believes": []},
  "facts": {
    "full_name": null,
    "title": "Knight of Boreas",
    "pronouns": "he/him",
    "species": "human",
    "origin": null,
    "residence": "location.mondstadt-city",
    "occupation": "wandering knight; first Knight of Boreas",
    "affiliations": [],
    "vision": "none",
    "element": null,
    "weapon": "Claymore",
    "birthday": null,
    "age": null,
    "height": null,
    "playable": false,
    "card": false,
    "status_flag": "presumed_dead",
    "era": "Mondstadt, about 1000 years before the main story, in Vennessa's time",
    "identity_notes": "His name is lost. 'Wandering Knight' is the name used for him in Lupus Majoris Chapter credits and dialogue; 'Wolf Knight' and 'Knight of Boreas' are the titles in item texts. In Mondstadt's tales he is nameless, and in some tellings called Andrius."
  },
  "uncertainties": [
    {"topic": "His name", "classification": "unknown", "note": "Jean says his name was lost to history. Wolf-Fang says there is no record at all of him; the name 'Boreas' comes from street tales."},
    {"topic": "How the companion's story ended", "classification": "disputed", "note": "The Wolf's Gravestone text has him bury the wolf and leave the city; the wiki's Boreas page and Venti's 6.4 account say Boreas let his body die and poured his power into the Ley Lines, becoming Mondstadt's North Wind, with the knight present to witness it. Both are in-world tellings of the same events."},
    {"topic": "Where he came from", "classification": "inferred", "note": "The Gest of the Mighty Wolf text says his homeland was not the snow-covered north and that he told of a vanished warrior kingdom. It does not name the place; readers may recognise Khaenri'ah, but canon does not say so."},
    {"topic": "How and when he died", "classification": "unknown", "note": "A thousand years have passed; no text records his death. The 6.4 sword-grave scene lists his sword symbol among past Knights of Boreas and Grand Masters."},
    {"topic": "Whether he was ever formally a Knight of Favonius", "classification": "strongly_supported", "note": "The Knights acknowledged him as Knight of Boreas, but he refused to join and left no succession plan."},
    {"topic": "Whether Wolf-Fang's tale of the snake demon is historical", "classification": "disputed", "note": "The weapon text presents it as the real event behind later stories, an in-world scholar's reconstruction; it is not otherwise confirmed."}
  ],
  "sources": [
    {"title": "Wandering Knight", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Wandering_Knight", "accessed": "2026-10-11", "confidence": "medium"},
    {"title": "Wolf's Gravestone (weapon description)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Wolf%27s_Gravestone", "accessed": "2026-10-11", "confidence": "high", "version": "1.0", "section": "Description"},
    {"title": "Wolf-Fang (weapon description)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Wolf-Fang", "accessed": "2026-10-11", "confidence": "high", "version": "4.0", "section": "Description"},
    {"title": "Gest of the Mighty Wolf (weapon description)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Gest_of_the_Mighty_Wolf", "accessed": "2026-10-11", "confidence": "high", "version": "6.4", "section": "Description"},
    {"title": "Lupus Majoris Chapter: Act I - To Those Who Embark on the Expedition (Triumphant Warrior)", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Triumphant_Warrior", "accessed": "2026-10-11", "confidence": "high", "version": "6.4", "section": "Dialogue (Jean, Venti, Wandering Knight echo)"},
    {"title": "Lonely Warrior", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Lonely_Warrior", "accessed": "2026-10-11", "confidence": "high", "version": "6.4", "section": "Dialogue (Wandering Knight's Longing)"},
    {"title": "Boreas", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Boreas", "accessed": "2026-10-11", "confidence": "medium", "section": "History"}
  ],
  "status": "drafted",
  "last_verified": null,
  "notes": "Thin canon: no profile, voice-overs or model. Built from three weapon texts (1.0, 4.0, 6.4) and the 6.4 Lupus Majoris quests. The wiki's Boreas account of his meeting with Boreas in Nod-Krai is medium confidence and kept to uncertainties. Card not generated. No 7.0-7.1 content found."
}
---

## summary
### LITE
The Wandering Knight was the first Knight of Boreas, a nameless warrior who arrived in Mondstadt about a thousand years ago, in Vennessa's time, with the wolf Boreas as his companion. He drank in taverns, hunted beasts and demons, refused the Knights of Favonius' repeated offers and left without a successor. The tales of the Wolf Knight grew from him.
### STANDARD +
He is known mostly through three weapon texts and a 6.4 echo. Canon never gives his name, face or origin, and Mondstadt's own tellings of him disagree with each other.
### LARGE +
His life gave Mondstadt the Knight of Boreas tradition, the Wolf's Gravestone claymore and an informal disciple, Ravenwood, who made the title a lasting one.

## background
### LITE
He came from the north with Andrius, who took the name Boreas, to see a city freshly freed from the aristocracy. In Mondstadt he lived as an ordinary drinker, paid in unfamiliar gold and silver coins and commissioned a sword from a local blacksmith, who gave him a heavy slab of iron instead of taking payment. He stayed only a few years.
### STANDARD +
He hunted monsters and demons around Mondstadt; one tale credits him with driving off a serpent that threatened the coast for a single silver coin. When a farmer or merchant whose daughter he rescued asked for his name, he told them to toast his companion Boreas instead, which is the likely origin of the title.
The Knights of Favonius, newly founded, tried hard to recruit him; Wolf-Fang suggests the Grand Master finally had him surrounded in the street, and the famous words of the Boreas tale come from that exchange, which the weapon text says was less polite than the bards made it.
### LARGE +
He liked to tell Ravenwood stories at sunset of a faraway land with undying flowers and rivers of mead, where a warrior kingdom once stood and where the warriors who had sung of honor bent the knee to gold and power; the text does not name it.
### ULTRA +
Wolf-Fang records that Falcon Coast's name was said to come from falcons drawn by the demons' corpses he left on the beach, not from Vennessa's legend of the Falcon of the West; the weapon's author treats this as the truth behind the tales.

## status
### LITE
Presumed dead; his time is a millennium past. His sword symbol is among the Knights of Boreas and Grand Masters commemorated in the memorial space Varka crosses in 6.4, and his echo in the Ley Lines still tells Varka that his path is not finished.
### STANDARD +
He left no succession plan. Ravenwood later earned the wolf spirit's recognition and the title passed within the Knights, though few holders were ever truly recognised by Boreas. A wiki search found no 7.0-7.1 content about him.

## relationships
### LITE
Boreas was his constant companion; Vennessa pursued him; Ravenwood adored him; the Knights wanted him. He answered to none of them.
### STANDARD +
The wolf and the knight are the core of the legend: the wolf hunted at his side and followed his scent into battle, and per the Wolf's Gravestone text the knight finally laid the wolf to rest and left the city to live as a lone wanderer. In a Ley-Line echo he asks Varka to be his guide to the modern city.

## appearance
### STANDARD
A man in a dust-stained, tattered cloak over battle-worn, finely made armor with intricate patterns, who carried a heavy iron claymore. Texts give no face, age or hair.

## chronology
### LARGE
- About 1,000 years before the main story: arrives in Mondstadt with Boreas; takes a sword from Ravenwood's father; refuses Vennessa; hunts demons; leaves after a few years.
- 1.0: the Wolf's Gravestone text first tells his story. 4.0: Wolf-Fang adds the reconstruction of the tale.
- 6.4: the Gest of the Mighty Wolf text, and Jean's account of the Boreas lineage, name him formally as the first Knight of Boreas; his echo speaks in Varka's quests.

## entry: Wolf's Gravestone
@keys: Wolf's Gravestone, Wolf Knight
@version: 1.0
@availability: permanent
### STANDARD
A longsword (claymore) first given by the blacksmith. Through friendship with wolves it acquired legendary power. After the wolf died, the knight laid the sword down as its gravestone. In Varka's 6.4 story it appears as the 'Wandering Knight's Longing'.

## entry: Wolf-Fang
@keys: Wolf-Fang, Northwind Wolf
@keys2: knight, Boreas
@version: 4.0
@availability: permanent
### STANDARD
The weapon text says there is no record of the Knight of Boreas; the name comes from tales, and the knight is always nameless. It explains the tale's two famous lines as a heated exchange with the first Grand Master, and identifies the 'Boreas' of the title as his companion's name.

## entry: Gest of the Mighty Wolf
@keys: Gest of the Mighty Wolf
@keys2: Ravenwood, wandering knight
@version: 6.4
@availability: permanent
### STANDARD
A bardic retelling: a wandering knight from the north with a companion named Andrius visits a city freshly freed, hunts with the wolf, drives back the great serpent, and leaves when the wolf's spirit stays in the wilds. Years later, when the knights have drifted back under the old aristocracy, Ravenwood carries a newly forged sword out of the city and is greeted as Andrius.

## entry: First Knight of Boreas
@keys: first Knight of Boreas, Knight of Boreas
@keys2: Jean, Ravenwood, Varka
@version: 6.4
@availability: permanent
### STANDARD
Jean explains that the first wandering knight to claim the title arrived with his wolf, left no succession plan and lost his name. Ravenwood, an informal disciple, then earned the Wolf Spirit's recognition and defended Mondstadt against the returning aristocracy; after that the title was passed within the Knights of Favonius. The lineage nearly died out twice, the second time through Roland.

## entry: The Wandering Knight's echo
@keys: Wandering Knight's Longing, Wandering Knight echo
@keys2: Varka, Ley Lines
@version: 6.4
@availability: permanent
### STANDARD
In Triumphant Warrior and Lonely Warrior Varka hears the knight as a voice from a thousand years ago: first asking Varka to guide him around Mondstadt, then, as a Longing in the Wolf's Gravestone, telling him 'This is not where your path ends. You must continue on.'
