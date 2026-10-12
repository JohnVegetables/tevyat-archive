---
{
  "id": "historical.izmaylov",
  "entity_type": "historical_figure",
  "name": "Izmaylov",
  "aliases": ["Nikolay Izmaylov", "Nikolay \"Pakhan\" Izmaylov", "Pakhan Izmaylov", "Old Sire", "President of the Royal Energy Commission"],
  "summary_line": "A Domovoy of Kitezhgrad who began as a spy in Hvergelmir, became Aksinya's devoted apprentice, seized the presidency of the Royal Energy Commission, founded the High Table and died, probably at his adopted son's hand.",
  "nation": "location.snezhnaya",
  "tags": ["Snezhnaya", "Domovoy", "fae", "Hvergelmir", "Royal Energy Commission", "High Table", "Izmaylov family"],
  "introduced_in": "6.6",
  "spoiler_level": "major",
  "availability": "permanent",
  "related": [
    "npc.aksinya", "historical.alvis", "faction.hvergelmir", "faction.royal-energy-commission", "faction.high-table",
    "faction.izmaylov-family", "creature.domovoy", "creature.snowland-fae", "npc.vasiliy", "npc.zmei", "npc.tsaritsa",
    "npc.pulcinella", "historical.belyi-tsar", "historical.burner-of-cities", "cosmology.shadow-realm", "lore.cataclysm",
    "location.novokitezhgrad", "location.hyperborea", "location.snezhnograd", "location.train-boneyard",
    "faction.snezhnaya-royal-railway-transport-bureau", "item.heart-of-the-furnace", "item.disenchantment-in-deep-shadow",
    "npc.koshchei", "npc.pavlina", "item.eye-of-graeae"
  ],
  "relationships": [
    {"target": "npc.aksinya", "type": "teacher and the loyalty of his life", "summary": "Sent to spy on her, he was won over by her kindness, followed her into the Shadow Realm, and spent centuries searching for her after her supposed death; when she returned he gave back the pen she had once given him.", "classification": "confirmed", "since": "7.0"},
    {"target": "historical.alvis", "type": "former patron turned bitter rival", "summary": "The Domovoy Grand Duke who posted him to Hvergelmir as a spy; Izmaylov turned against him after Aksinya's reported death and took the Commission presidency from under him.", "classification": "confirmed", "since": "7.0"},
    {"target": "npc.vasiliy", "type": "adopted son; suspected killer", "summary": "Head of the Izmaylov gang and the 'Young Sire'; resentful of his father's Law, he was among the last to see the Old Sire alive. The wiki records Vasiliy as the one who killed him; the quest only shows the gangs suspecting it.", "classification": "strongly_supported", "since": "7.0"},
    {"target": "npc.zmei", "type": "adopted son", "summary": "Raised with a surname to lead the Luchkin gang and later Speaker of the High Table.", "classification": "confirmed", "since": "7.0"},
    {"target": "faction.high-table", "type": "founder", "summary": "Swore the founding oath with the surviving Luchkin heroes after the Burner of Cities' plot was crushed.", "classification": "confirmed", "since": "7.0"},
    {"target": "npc.tsaritsa", "type": "sovereign who granted his post", "summary": "He bargained for the Commission presidency in a private audience on her enthronement; the price is not stated.", "classification": "confirmed", "since": "7.0"}
  ],
  "knowledge": {
    "knows": [
      {"fact": "Alvis lied when announcing Aksinya's death in the Shadow Realm.", "learned": "Aftermath of the Cataclysm", "version": "7.0", "visibility": "secret"},
      {"fact": "The Tsaritsa dislikes the old fae nobility and favours humans.", "learned": "Court politics", "version": "7.0", "visibility": "public"}
    ],
    "does_not_know": [
      {"fact": "Anything after his death, including Vasiliy's Shadow Realm scheme and the events of the Traveler's visit", "note": "dead before the Traveler arrives"}
    ],
    "believes": []
  },
  "facts": {
    "full_name": "Nikolay \"Pakhan\" Izmaylov",
    "title": "President of the Royal Energy Commission of Snezhnaya",
    "pronouns": "he/him",
    "species": "Domovoy (fae)",
    "origin": "location.snezhnaya",
    "residence": "location.snezhnograd",
    "occupation": "President of the Royal Energy Commission; head of the Izmaylov family and founder of the High Table",
    "affiliations": ["faction.hvergelmir", "faction.royal-energy-commission", "faction.high-table", "faction.izmaylov-family"],
    "vision": "none",
    "element": null,
    "weapon": null,
    "rarity": null,
    "constellation": null,
    "birthday": null,
    "age": null,
    "height": null,
    "body_type": null,
    "playable": false,
    "release_version": null,
    "card": false,
    "status_flag": "dead",
    "era": "Born in Kitezhgrad in the reign of the Belyi Tsar; president under the Tsaritsa; died a few months before the Traveler's visit",
    "identity_notes": "'Pakhan' is part of his name as given; the Izmaylov gang calls him the Old Sire and his son the Young Sire."
  },
  "uncertainties": [
    {"topic": "Who killed him", "classification": "strongly_supported", "note": "The wiki infobox says Vasiliy killed him in a rage while he was ill. In Disputes Without Honor and Humanity, the gangs only say he suddenly fell ill and died, that the Young Sire and the Butcher were the last to see him, and that the death does not add up. No scene shows the act."},
    {"topic": "The bargain with the Tsaritsa", "classification": "unknown", "note": "The Foundryman's Calculus text says only the few present in the chamber know the price he paid."},
    {"topic": "Whether his feud with Alvis was partly theatre", "classification": "disputed", "note": "Foundryman's Magnanimity says some thought it a performance, then shows real malice."},
    {"topic": "Age and dates", "classification": "unknown", "note": "Canon gives no age. He was slightly older than Aksinya, and the wait for her lasted about five centuries by his own reckoning."},
    {"topic": "Version of first mention", "classification": "unknown", "note": "The wiki lists him as introduced in Luna VII (6.6); the artifact set and the quest that carry his story are 7.0."}
  ],
  "sources": [
    {"title": "Izmaylov", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Izmaylov", "accessed": "2026-10-11", "confidence": "medium", "section": "Profile, Story"},
    {"title": "Foundryman's Conjecture (Heart of the Furnace)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Foundryman%27s_Conjecture", "accessed": "2026-10-11", "confidence": "high", "version": "7.0"},
    {"title": "Foundryman's Observation (Heart of the Furnace)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Foundryman%27s_Observation", "accessed": "2026-10-11", "confidence": "high", "version": "7.0"},
    {"title": "Foundryman's Calculus (Heart of the Furnace)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Foundryman%27s_Calculus", "accessed": "2026-10-11", "confidence": "high", "version": "7.0"},
    {"title": "Foundryman's Magnanimity (Heart of the Furnace)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Foundryman%27s_Magnanimity", "accessed": "2026-10-11", "confidence": "high", "version": "7.0"},
    {"title": "Foundryman's Legacy (Heart of the Furnace)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Foundryman%27s_Legacy", "accessed": "2026-10-11", "confidence": "high", "version": "7.0"},
    {"title": "Sharpness That Ceased Upon Wondrous Creation (Disenchantment in Deep Shadow)", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Sharpness_That_Ceased_Upon_Wondrous_Creation", "accessed": "2026-10-11", "confidence": "high"},
    {"title": "Disputes Without Honor and Humanity (Mean Streets of the Despicable)", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Disputes_Without_Honor_and_Humanity", "accessed": "2026-10-11", "confidence": "high", "version": "7.0", "section": "Dialogue"},
    {"title": "Mean Streets of the Despicable", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Mean_Streets_of_the_Despicable", "accessed": "2026-10-11", "confidence": "medium", "version": "7.0"}
  ],
  "status": "drafted",
  "last_verified": null,
  "notes": "Adopted-children and family structure and the Burner of Cities episode are cross-referenced from the wiki Story section and the Magnanimity text; the manner of death rests on the wiki infobox plus quest suspicion. No voiced scene or portrait appearance exists, so no card."
}
---

## summary
### LITE
A Domovoy of old Kitezhgrad who rose from spy to President of the Royal Energy Commission, founded the gangs' High Table and stayed loyal to his teacher Aksinya. He died months before the Traveler's visit.
### STANDARD +
The gangs call him the Old Sire. His death, officially sudden illness, is widely suspected to have been murder by his adopted son Vasiliy.

## background
@version: 7.0
### LITE
Born in Kitezhgrad under the Belyi Tsar, he went to the Energy Commission's furnace, but Grand Duke Alvis made him a spy in Aksinya's institute, Hvergelmir.
### STANDARD +
He was a poor spy. Aksinya knew where his loyalties lay, treated him kindly and became his mentor, and on an expedition into Hyperborean ruins in the Shadow Realm she gave him her pen. That made him a true believer in Hvergelmir's work.
### LARGE +
He was skilled with the city's furnaces, the energy supply and Kresnik Kristall, with hearing keen enough to diagnose machinery by sound. The artifact texts say he went in awe of the furnace but felt only dread in the Shadow Realm, and buried it in zeal. After the Cataclysm destroyed Kitezhgrad, Aksinya was announced dead in the Shadow Realm. He recognised Alvis's lie, declined his invitation and, while Alvis went to build Novokitezhgrad to win the new sovereign's favour, obtained an audience with the Tsaritsa through a fellow Domovoy in her service. What he gave her is not recorded, but he left as President of the Commission, with Alvis as an enemy. He then fought Alvis in council, and backed human candidates for the Transport Bureau, knowing the Tsaritsa preferred them.
### ULTRA +
When Vila raiders known as the Burner of Cities struck along the new railway, Alvis withdrew from the Transport Bureau nomination, hoping the rebels would humiliate Izmaylov. Instead, Izmaylov forged weapons for the heroes of the Luchkin, who crushed the plot; he took the credit and swore an oath with the survivors in narrow alleys, founding the High Table and its Law. Over the years he adopted human and fae children, gave them surnames and meant them to inherit the gangs: Vasiliy for the Izmaylov gang, Zmei and Iryna for the Luchkin. He also directed Commission commissions toward the Shadow Realm in search of Aksinya, which wore down his body. After about five hundred years she was rescued. By then he was aged and frail; she asked what she had missed, and he had prepared every answer; bowed, and returned her pen, telling her neither owed the other anything. Afterwards he turned the Commission away from the Shadow Realm and left the Speaker's seat to Zmei.

## relationships
@version: 7.0
### LITE
Aksinya, his teacher; Alvis, his patron turned rival; Vasiliy, the adopted son who probably killed him.
### STANDARD +
He raised Vasiliy, Zmei, Iryna and Lyubov as his own, giving them his name or a surname to lead the gangs of the High Table. Vasiliy resented his father's reliance on the Energy Commission and the Law.
### LARGE +
Alvis and he clashed in the Snezhnograd council. Rumour called it theatre; the texts show real malice. He relied on a fellow Domovoy in the Tsaritsa's service to reach her.

## status
@version: 7.0
### LITE
Dead; he died suddenly, and his gang passed to his adopted son Vasiliy.
### STANDARD +
In Disputes Without Honor and Humanity the High Table suspects that Vasiliy and the Butcher were the last to see him and that the cause was not illness. Gureva, a Luchkin agent captured by Vasiliy's second-in-command, tells her captor the Old Sire's death does not add up. The wiki records Vasiliy as the killer. Vasiliy later tried to open the Shadow Realm, was defeated by the Traveler and left blind and calling for Zmei as the device shut down; his fate is not stated.
### LARGE +
Izmaylov guards will not discuss the death. The Luchkin keep the friendships he built, such as a rented train, but doubt how long they will last without him.

## entry: Aksinya and the pen
@keys: Izmaylov pen, Aksinya's pen, Sharpness That Ceased Upon Wondrous Creation
@version: 7.0
@spoiler: major
### STANDARD
Aksinya placed her pen in the young Domovoy's hand among the frozen ruins of Hyperborea inside the Shadow Realm. The artifact text says she was a girl no longer, spoke of seeing by the fire's light rather than inheriting it, and offered her bones as a step for those who came after. The pen made his devotion real. Centuries later, when she returned, he handed it back and released them both from debt.
### LARGE +
The farewell speech calls his life ordinary and says he spent it repaying the brief dream she gave him. It ends by calling her by name, not by title.

## entry: Rivalry with Alvis
@keys: Alvis Izmaylov, Domovoy Grand Duke, Izmaylov and Alvis
@version: 7.0
### STANDARD
Alvis posted Izmaylov to Hvergelmir to spy. After Aksinya's reported death, Izmaylov refused to believe it and used the Tsaritsa's new regime to take the Energy Commission presidency before Alvis could. From then on they opposed each other in council. Their disagreement over the first Director of the Transport Bureau ended with Alvis stepping back and Izmaylov being proved right by the Luchkin.

## entry: The High Table
@keys: High Table, Fae Gang Federation
@version: 7.0
### STANDARD
After crushing the Burner of Cities, Izmaylov and the surviving heroes swore to live under the Law amid soot and rust, which formed the High Table. He meant his adopted children to take the gangs. The Speaker's seat passed to Zmei when he withdrew.
