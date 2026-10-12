---
{
  "id": "faction.fatui",
  "entity_type": "faction",
  "subdir": "fatui",
  "name": "Fatui",
  "aliases": ["Fatuus", "the Fatui", "Fatui of Snezhnaya"],
  "summary_line": "Snezhnaya's combined government, diplomatic corps and military, founded by the Tsaritsa 500 years ago under Pierro and led by the Eleven Fatui Harbingers; feared abroad for collecting the Gnoses by deceit and force.",
  "nation": "location.snezhnaya",
  "introduced_in": "1.0",
  "spoiler_level": "major",
  "availability": "mixed",
  "related": [
    "location.snezhnaya", "location.snezhnograd", "location.glupov", "location.zapolyarny-palace", "location.armory-palace",
    "location.snezhnograd-veche-state-hall", "location.port-belovodye", "location.sanctuary-of-grief", "location.goth-grand-hotel",
    "location.the-chasm-underground-mines", "location.tatarasuna", "location.desert-of-hadramaveth",
    "location.kuuvahki-experimental-design-bureau", "location.nasha-town", "location.nod-krai", "location.northland-bank-liyue",
    "location.northland-bank-fontaine", "location.northland-bank-nod-krai", "location.mondstadt", "location.liyue",
    "location.inazuma", "location.sumeru", "location.fontaine", "location.natlan",
    "npc.tsaritsa", "npc.pierro", "npc.capitano", "npc.dottore", "character.columbina", "character.arlecchino",
    "npc.pulcinella", "character.wanderer", "character.sandrone", "npc.signora", "npc.pantalone", "character.tartaglia",
    "historical.crucabena", "character.odette", "character.vesna", "npc.danica", "npc.mitya", "npc.valeriy", "npc.viktor",
    "npc.javert", "npc.ekaterina", "npc.lyudochka-snezhevna", "npc.efim-snezhevich", "npc.teppei", "npc.crepus",
    "npc.ronova", "npc.hroptatyr", "npc.dainsleif", "npc.paimon", "npc.osial", "npc.goth", "npc.rhinedottir",
    "historical.anton-zarkovich-karnatsky",
    "character.lyney", "character.lynette", "character.freminet", "character.traveler", "character.diluc", "character.jean",
    "character.zhongli", "character.raiden-shogun", "character.nahida", "character.neuvillette", "character.mavuika",
    "character.ororon", "character.yelan", "character.venti",
    "faction.eleven-fatui-harbingers", "faction.house-of-the-hearth", "faction.northland-bank", "faction.fatui-internal-affairs",
    "faction.snezhnograd-veche", "faction.druzhna", "faction.rokot", "faction.knights-of-favonius",
    "faction.northern-intelligence-network", "faction.liyue-qixing", "faction.millelith", "faction.tenryou-commission",
    "faction.kanjou-commission", "faction.shuumatsuban", "faction.sumeru-akademiya", "faction.frostmoon-scions",
    "faction.abyss-order", "faction.crimson-moon-dynasty",
    "system.delusion", "system.kresnik-kristall", "system.stellar-linchpin", "term.fatui-harbinger", "term.oprichnik",
    "cosmology.gnosis", "cosmology.heavenly-principles", "cosmology.four-shades", "cosmology.crimson-moon",
    "cosmology.kuuvahki", "cosmology.shadow-realm", "creature.cicin", "creature.ursa-the-drake", "creature.snowland-fae",
    "item.anemo-gnosis", "item.geo-gnosis", "item.electro-gnosis", "item.dendro-gnosis", "item.hydro-gnosis",
    "item.pyro-gnosis", "item.cryo-gnosis",
    "lore.project-stuzha", "lore.project-mistilteinn", "lore.tsaritsas-plan", "lore.vision-hunt-decree",
    "lore.destruction-of-irminsul", "lore.fall-of-ronova", "lore.cataclysm",
    "quest.everwinter-without-mercy", "quest.white-night-like-a-dream-upon-waking", "quest.a-rekviem-for-the-underworld",
    "quest.true-moon", "quest.truth-amongst-the-pages-of-purana", "quest.a-traveler-on-a-winters-night",
    "quest.incandescent-ode-of-resurrection", "quest.summertime-odyssey", "quest.chapter-vii", "event.snezhnaya-history"
  ],
  "facts": {
    "faction_type": "government",
    "leaders": ["npc.tsaritsa", "npc.pierro"],
    "leader_note": "The Tsaritsa (Anastasya) holds supreme authority. Pierro, 'The Jester', is Director of the Fatui and its first member; he leads the Eleven Fatui Harbingers, who each head their own division. As of 7.1 the active Harbingers are Pierro, Arlecchino, Pulcinella, Sandrone, Pantalone and Tartaglia, and Capitano keeps his seat although he is incapacitated.",
    "headquarters": "location.glupov",
    "parent_org": null,
    "founded": "About 500 years ago, in the third year of the Tsaritsa's reign after the Cataclysm, with Pierro as first member and leader",
    "current_status": "Active and governing Snezhnaya. In 7.1 Pierro used the new 'Eye of the Fatui' Delusion to mortally wound Ronova, Ronova's curse of death was lifted, and Project Mistilteinn could resume. Arlecchino's agreed price for that Delusion is that the House of the Hearth will leave Fatui affairs and stop training children as spies; how that will be carried out has not yet been shown.",
    "operating_areas": ["location.snezhnaya", "location.mondstadt", "location.liyue", "location.inazuma", "location.sumeru", "location.fontaine", "location.natlan", "location.nod-krai"]
  },
  "uncertainties": [
    {"topic": "The Tenth Harbinger", "classification": "unknown", "note": "No holder of the tenth seat has been named through 7.1. The wiki observes that every active Harbinger attended the 7.1 vote, so the seat is either vacant or Pierro's own; canon does not say which. Do not invent a Tenth Harbinger."},
    {"topic": "Who holds Delusions", "classification": "disputed", "note": "Viktor told the Traveler that few Fatui beyond the Harbingers have Delusions and that the Tsaritsa grants them personally. Yet Agents, Cicin Mages, Mirror Maidens, Operatives and Oprichniki officers all use Delusion-like devices, and mass-produced Delusions were handed out in Inazuma. In 7.1 Pierro said Delusions are allocated on a strictly voluntary basis: Fatui may apply for them for important missions or emergencies, and nobody is forced to use one."},
    {"topic": "How Delusions are made", "classification": "inferred", "note": "Production is a guarded secret. Inazuma's Delusion Factory used Crystal Marrow tainted by the dead god Orobashi, and manga material links Crepus's Delusion to the remains of ancient gods. A general method has not been stated."},
    {"topic": "The House of the Hearth after 7.1", "classification": "unknown", "note": "Pierro agreed that the House would become an independent organisation no longer involved in Fatui affairs and that no more children would be trained as spies. Canon through 7.1 does not show this being put into practice."},
    {"topic": "Terms of the Geo Gnosis contract", "classification": "unknown", "note": "Zhongli gave the Geo Gnosis to Signora under a contract with the Tsaritsa whose terms have not been revealed."},
    {"topic": "Pierro's condition", "classification": "strongly_supported", "note": "Using the Eye of the Fatui left Pierro severely depleted. Dainsleif said such power always costs something that cannot be recovered. The full extent of the damage is not stated."},
    {"topic": "Crepus's Delusion", "classification": "strongly_supported", "note": "The wiki says the Fatui were 'presumably' the ones who gave Crepus Ragnvindr his Delusion; Diluc's and Kaeya's stories and the manga support this, and Varka blames Dottore for Crepus's death."},
    {"topic": "Which Harbinger punished Jenck", "classification": "inferred", "note": "In Fontaine the forces of an unnamed Harbinger, most likely Sandrone, worked with Jenck and later broke his mind. The Harbinger is not named."}
  ],
  "sources": [
    {"title": "Fatui", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Fatui", "accessed": "2026-10-11", "confidence": "high", "section": "Description, operations in each nation, Members, Internal Affairs, Trivia", "version": "7.1"},
    {"title": "Eleven Fatui Harbingers", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Eleven_Fatui_Harbingers", "accessed": "2026-10-11", "confidence": "high", "section": "Overview, Members table and notes", "version": "7.1"},
    {"title": "Pierro", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Pierro", "accessed": "2026-10-11", "confidence": "high", "section": "Profile, History, Recruiting Other Harbingers, Present", "version": "7.1"},
    {"title": "Tsaritsa", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Tsaritsa", "accessed": "2026-10-11", "confidence": "high", "section": "Founding of the Fatui, Palestar Edict, Internal Affairs ruling, 7.1 meetings", "version": "7.1"},
    {"title": "Guiding Notes", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Guiding_Notes", "accessed": "2026-10-11", "confidence": "high", "section": "Knowledge: The Fatui, Glupov, The Druzhna, Project Stuzha; People: Valeriy, Sandrone", "version": "7.0"},
    {"title": "Delusion", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Delusion", "accessed": "2026-10-11", "confidence": "high", "section": "Overview, Side Effects, Mass-Produced Delusions", "version": "7.1"},
    {"title": "Project Stuzha", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Project_Stuzha", "accessed": "2026-10-11", "confidence": "high", "section": "Full article", "version": "7.1"},
    {"title": "Armory Palace", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Armory_Palace", "accessed": "2026-10-11", "confidence": "high", "section": "Overview, Special Assignments Battalion", "version": "7.0"},
    {"title": "Glupov", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Glupov", "accessed": "2026-10-11", "confidence": "high", "section": "Description, Lore (A Brief History of the Pale Starborn)", "version": "7.0"},
    {"title": "Snezhnograd Veche", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Snezhnograd_Veche", "accessed": "2026-10-11", "confidence": "high", "section": "Overview", "version": "7.0"},
    {"title": "The Druzhna", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/The_Druzhna", "accessed": "2026-10-11", "confidence": "high", "section": "History (A Brief History of the Pale Starborn)", "version": "7.0"},
    {"title": "House of the Hearth", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/House_of_the_Hearth", "accessed": "2026-10-11", "confidence": "high", "section": "Overview", "version": "7.1"},
    {"title": "Northland Bank", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Northland_Bank", "accessed": "2026-10-11", "confidence": "high", "section": "Descriptions, Lore, Snezhnayan branches", "version": "7.1"},
    {"title": "Fatui Skirmishers", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Fatui_Skirmishers", "accessed": "2026-10-11", "confidence": "high", "section": "Adventurer Handbook description, Types", "version": "1.0"},
    {"title": "Fatui Oprichniki", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Fatui_Oprichniki", "accessed": "2026-10-11", "confidence": "high", "section": "Adventurer Handbook description, Types", "version": "6.0"},
    {"title": "Fatui Cicin Mages", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Fatui_Cicin_Mages", "accessed": "2026-10-11", "confidence": "high", "section": "Adventurer Handbook description", "version": "1.0"},
    {"title": "Fatui Pyro Agent", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Fatui_Agents", "accessed": "2026-10-11", "confidence": "medium", "section": "Enemy page", "version": "1.0"},
    {"title": "Mirror Maiden", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Mirror_Maiden", "accessed": "2026-10-11", "confidence": "medium", "section": "Enemy page", "version": "2.0"},
    {"title": "Everwinter Without Mercy", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Everwinter_Without_Mercy", "accessed": "2026-10-11", "confidence": "high", "section": "Chapter VII Act I summary", "version": "7.0"},
    {"title": "White Night, Like a Dream Upon Waking", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/White_Night,_Like_a_Dream_Upon_Waking", "accessed": "2026-10-11", "confidence": "high", "section": "Chapter VII Act III summary", "version": "7.1"},
    {"title": "One Move Left to Make", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/One_Move_Left_to_Make", "accessed": "2026-10-11", "confidence": "high", "section": "Chapter VII Act III Part 3 (Northland Bank vault)", "version": "7.1"},
    {"title": "A Rekviem for the Underworld", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/A_Rekviem_for_the_Underworld", "accessed": "2026-10-11", "confidence": "high", "section": "Chapter VII Act IV summary (Delusion)", "version": "7.1"},
    {"title": "Etched in Time", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Etched_in_Time", "accessed": "2026-10-11", "confidence": "high", "section": "Dialogue: Harbingers' vote on Hroptatyr's notebook", "version": "7.1"},
    {"title": "Black Feathers Scattered at Parting", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Black_Feathers_Scattered_at_Parting", "accessed": "2026-10-11", "confidence": "high", "section": "Dialogue: Eye of the Fatui, battle with Ronova, Dainsleif", "version": "7.1"},
    {"title": "Tracing the Footsteps of the Past", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Tracing_the_Footsteps_of_the_Past", "accessed": "2026-10-11", "confidence": "medium", "section": "Song of the Welkin Moon Act VII Part 3 (A Traveler on a Winter's Night, Luna IV)", "version": "6.3"},
    {"title": "Truth Amongst the Pages of Purana", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Truth_Amongst_the_Pages_of_Purana", "accessed": "2026-10-11", "confidence": "medium", "section": "Song of the Welkin Moon Act X; aftermath described on the Fatui page", "version": "6.6"},
    {"title": "Tartaglia/Storyline", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Tartaglia/Storyline", "accessed": "2026-10-11", "confidence": "high", "section": "Capitano's will, Veche councillor, Project Stuzha stance", "version": "7.1"},
    {"title": "Odette/Storyline", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Odette/Storyline", "accessed": "2026-10-11", "confidence": "high", "section": "Induction into the Fatui, Lelek of the Rokot", "version": "7.0"},
    {"title": "Rokot", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Rokot", "accessed": "2026-10-11", "confidence": "high", "section": "Overview", "version": "7.0"},
    {"title": "Chapter VII", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Chapter_VII", "accessed": "2026-10-11", "confidence": "high", "section": "Act list", "version": "7.1"},
    {"title": "A Brief History of the Pale Starborn", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/A_Brief_History_of_the_Pale_Starborn", "accessed": "2026-10-11", "confidence": "high", "section": "Years 1-7 of the 799th Cycle (founding of the Fatui, Glupov, Veche)", "version": "7.0"},
    {"title": "Delusion (Chapter VII)", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Delusion_(Chapter_VII)", "accessed": "2026-10-11", "confidence": "high", "section": "Dialogue: Pierro on Delusion allocation; Arlecchino on the authority of Death; House of the Hearth terms; experiment", "version": "7.1"},
    {"title": "Version/7.1", "type": "official_announcement", "url": "https://genshin-impact.fandom.com/wiki/Version/7.1", "accessed": "2026-10-11", "confidence": "high", "section": "New quests: Chapter VII Acts III and IV", "version": "7.1"}
  ],
  "status": "verified",
  "last_verified": "2026-10-11"
}
---

## summary
### LITE
The Fatui (one member is a Fatuus; the name is Latin for "fools") are Snezhnaya's government, diplomatic corps and military in one body. They answer to the Tsaritsa, the Cryo Archon, who founded them 500 years ago with Pierro as their first member and Director. Under him the Eleven Fatui Harbingers each run a division. The Fatui are headquartered in Glupov, a fortress city inside Snezhnograd, and their emblem is the Palestar Banner. Abroad they present themselves as envoys of the Tsaritsa's goodwill, but most nations distrust them: in the Traveler's journey they took Gnoses from one Archon after another, using deceit, extortion, bribery and human experimentation along the way.
### LARGE +
At home the Fatui are simply the state. In-game guide text says they handle all aspects of governance and military affairs. Their members include soldiers, bureaucrats, politicians, bankers and spies, and most rank-and-file Fatui know nothing of the Tsaritsa's true plan but are loyal to her and to Snezhnaya.

## structure
### LITE
The Tsaritsa sits at the top. Below her, Director Pierro relays her appointments, assigns missions and convenes the Harbingers. Each Harbinger leads a division with personal subordinates, and below them are numbered companies and squads.
### STANDARD +
Known parts of the organisation include:
- **Debt Collection**: mostly Pyro Agents. It recovers debts owed to the Northland Bank, using as much force as it takes.
- **The House of the Hearth**: the intelligence arm, an orphanage that raises children as agents under Arlecchino, "Father".
- **The Northland Bank**: the state bank, presided over by Pantalone, which also funds and houses Fatui operations abroad.
- **The Armory Palace**: the royal weapons-development institution in Glupov, managed by Sandrone.
- **Fatui Internal Affairs**: also called the Okhranka. It investigates misconduct among the Fatui and reports to the Tsaritsa.
### LARGE +
Members receive pay, supplies and powerful weapons. In return they choose neither where they are sent nor whom they serve under. Annual leave grows with rank: a sergeant named Wislawa started with about ten days and said she could reach twenty-five through promotions.
### ULTRA +
Communication is a known weakness: Harbingers keep things from one another, from their subordinates and from other divisions. Units are numbered, for example the Sixth Company, the Ninth Company and the 34th Independent Investigative Squad. Ranks seen in the field run from trainee and private through corporal, sergeant and staff sergeant to lieutenant and captain, with naval and specialist ranks (warrant officer, praporshchik, fourrier, drillmaster, field medic, sapper) alongside. A staff sergeant may declare himself brevet captain when his captain is lost. Many Oprichniki officers trained at Snezhnaya's Royal Military Academy.

## leadership
### LITE
**The Tsaritsa (Anastasya)** rules Snezhnaya directly, and the Fatui exist to carry out her will. **Pierro, "The Jester"**, is the Director of the Fatui, the first Harbinger and the Harbingers' leader. Each Harbinger takes a codename from Italian commedia dell'arte, a title and a rank number based on combat power.
### STANDARD +
Status of the seats as of 7.1:
- Director: Pierro, active.
- 1st: Capitano, incapacitated. His life force is merged with the Lord of the Night in Natlan, but the Tsaritsa kept his rank.
- 2nd: Dottore, dead.
- 3rd: Columbina, resigned.
- 4th: Arlecchino, active.
- 5th: Pulcinella, active.
- 6th: Scaramouche, resigned and erased from Irminsul. He now lives as the Wanderer.
- 7th: Sandrone, active.
- 8th: Signora, dead.
- 9th: Pantalone, active.
- 10th: never revealed.
- 11th: Tartaglia (Childe), active.
### LARGE +
Ranks are not shuffled upward when a higher seat empties, and seats can stay vacant indefinitely. Harbingers receive their appointments from the Tsaritsa, either in person at Zapolyarny Palace or through Pierro (it was Pierro who pinned Tartaglia's Delusion on him). Names can be inherited: Arlecchino took the codename of the previous Knave, Crucabena, after killing her. Prospective Harbingers may be invited by the Director to a "wild" and "frenzied banquet" that seems to decide their place. Whether that banquet is literal is unknown. Harbingers have wide autonomy and may act against central policy, but the Tsaritsa forbids them to fight one another unless she lifts the ban.

## members
### LARGE
The Fatui come from many backgrounds. Some are House of the Hearth orphans, some volunteer, and some are drafted, as Tartaglia was. Many are ordinary workers. Some are homesick on foreign postings, others grow fond of them, and they play wargames, buy souvenirs and grumble about their superiors. Playable characters tied to the Fatui include Tartaglia, Arlecchino, Sandrone, Lyney, Lynette, Freminet and Odette, and the Wanderer and Columbina are former Harbingers.
### ULTRA +
Odette, prima ballerina of the Korolevskiy Troupe, was placed in Signora's division as a child after her Fatuus father died on a mission. She is the favoured candidate to inherit Signora's seat, and she was also secretly "Lelek" of the Rokot. Vesna and Danica serve the Tsaritsa directly rather than the Fatui, but both were trained by Capitano. Named rank-and-file Fatui the Traveler meets include Javert (a debt collector in Liyue), Ekaterina (the Northland Bank's Liyue receptionist, who denies any Fatui ties), Viktor (Signora's assistant in Mondstadt, later sent to Sumeru), Staff Sergeant Anton of the Ninth Company, Sergeant Wislawa, Polonsky (who distributes Kristall) and Major Valeriy of the Armory Palace guards.

## goals
### STANDARD
The Fatui serve the Tsaritsa's aim of a "perfect world", which means overthrowing the Heavenly Principles. In the Traveler's journey, that meant collecting the Gnoses: Harbingers were sent to each of the other six nations to obtain them, and by 7.1 the Tsaritsa held every Gnosis except the Pyro Gnosis, which was lost when Irminsul burned. They also develop Delusions and weapons, gain influence in other nations, and strengthen Snezhnaya against Celestia.
### LARGE +
Pierro revealed in 7.0 that Project Stuzha, the energy-rationing policy that saved power for the Armory Palace, was really a lead-up to Project Mistilteinn, a weapon for facing the Heavenly Principles that relies on Stellar Linchpins. The Tsaritsa believes all seven Gnoses are needed to unlock a seal left by the Third Descender. By the end of 7.1 she held six. The Pyro Gnosis burned with Irminsul, and she expects it to be ejected from the Ley Lines eventually. Individual Harbingers add their own aims, for example Pantalone's wish to end the gods' control over Mora.

## methods
### STANDARD
Abroad, the Fatui's usual pattern is to provoke or exploit a crisis and then offer "help" that leaves the local authorities in their debt. They bribe or collude with local elites, lend money through the Northland Bank and collect it ruthlessly, plant sleeper agents raised in the House of the Hearth, and use deniable operatives. Delusions (Vision-like devices that work for anyone and can be stronger than Visions, but drain or even kill their users) give their elite troops elemental power.
### LARGE +
Ordinary troops differ by region. Skirmishers in elemental armour are the common line infantry abroad, while Oprichniki and Landcruiser war machines serve in Nod-Krai and Snezhnaya. Elite Delusion users (Agents, Cicin Mages, Mirror Maidens, Operatives) work alone or in small teams. Harbingers' personal styles shape their subordinates: some Fatui act without orders to advance their Harbinger's goals or to avenge a fallen one. Divisions sometimes work against each other. In Sumeru, another Fatui division had the troublesome Elchingen assassinated. By Capitano's policy, a commanding Harbinger is responsible for the families of Fatui who fall in service.
### ULTRA +
Pierro admitted in 7.1 that the Fatui's Delusions have always been an unfinished product that drains the user's life force, and said they are allocated on a strictly voluntary basis to members who apply for them for important missions or emergencies. They give off the smell of Mist Grass when used. Inazuma's Delusion Factory used Crystal Marrow tainted with the dead god Orobashi's curse, and Watatsumi soldiers who used mass-produced Delusions aged rapidly, some fatally, such as Teppei. People who already have Visions or innate elemental power resist the side effects better. Fatui logistics can also be turned to private ends: Odette used her Fatui connections to distribute Kristall that the Traveler had bought to the locals of Zolnyy.

## history
### LARGE
**Founding.** After the Belyi Tsar died in the Cataclysm 500 years ago, Anastasya became Snezhnaya's Archon. In the second year of her reign the humans of Port Belovodye rebelled against their Fae rulers. In the third year she founded the Fatui with Pierro as first member and leader, choosing them over the Druzhna, and sent them against the port's independent government. On that campaign the Fatui occupied the lands of several Fae clans, whose princes were charged with negligence and condoning rebellion; envoys then talked the port into surrendering its instigators. The next year she ordered the Fatui to build Glupov, "the city of fools", near Snezhnograd, and she replaced the Fae aristocracy with the Snezhnograd Veche.

**The Gnosis campaign.** Shortly before the Traveler's journey began, Pierro briefed the Harbingers on the Tsaritsa's plan to collect the Gnoses. Pantalone was given the finances and Sandrone the technical needs. Signora took the Anemo Gnosis in Mondstadt and the Geo Gnosis in Liyue. Scaramouche took the Electro Gnosis in Inazuma. Dottore secured the Electro and Dendro Gnoses in Sumeru, and Neuvillette gave Arlecchino the Hydro Gnosis in Fontaine as a "diplomatic gift". In Natlan, Capitano declined to take the Pyro Gnosis.

**Nod-Krai (6.x).** After Columbina resigned and fled, the Tsaritsa issued the Palestar Edict and sent Harbingers to Nod-Krai. Dottore turned rogue, Internal Affairs ruled against him, and Arlecchino and Sandrone, with the Traveler and others, brought him down. Sandrone sacrificed herself and was later rebooted in Fontaine. Dottore then died for good when Nahida burned Irminsul, after Pantalone had secretly helped his soul's attack on Sumeru.
### ULTRA +
**Over the centuries.** Pierro, a Khaenri'ahn royal mage cursed with immortality at the Cataclysm, recruited Signora (whom he gave a Cryo Delusion), the expelled scholar Zandik (Dottore, 400 to 450 years ago) and the puppet who became Scaramouche. Four hundred years ago Dottore sabotaged Inazuma's Mikage Furnace on Pierro's orders. The Tsaritsa invited Columbina in three to four centuries ago. Over a decade ago she pardoned the House of the Hearth orphan Peruere for killing Crucabena and made her the new Knave. Later she raised Ajax to Eleventh Harbinger as Tartaglia.

**Nation by nation (1.0-5.x).** The Fatui's actions in each nation are summarised in the sub-entries. In short: Mondstadt (Stormterror, the Holy Lyre, the Anemo Gnosis), Liyue (Osial, the Geo Gnosis, the Ninth Company), Inazuma (the Vision Hunt Decree and Signora's execution), Sumeru (Shouki no Kami and two Gnoses), Fontaine (the House of the Hearth and the Hydro Gnosis), and Natlan (Capitano's sacrifice).

**Snezhnaya (7.0-7.1).** Fatui detachments ran Project Stuzha's Kristall rationing. Many squads posted in the tundra were lost to the Shadow Realm and became shadows. In the Veche, opposition to Stuzha reached 39 percent. Pierro took Paimon to the Armory Palace to shield her, and Odette broke in after them, revealing herself as Lelek. Ronova's curse of death then struck everyone working on Project Mistilteinn, and the project and Stuzha were both put on hold. The Tsaritsa dropped all investigations into the Traveler and gave them free access to Zapolyarny Palace. In 7.1 Pierro and Arlecchino built a new Delusion and the Harbingers unanimously voted to unseal Hroptatyr's notebook. At Rankova Zorya, after the Tsaritsa's tampering with time stalled Rhinedottir, Celestia reclaimed Ronova's authority for abusing it, which ended her curse. Pierro then dealt Ronova fatal damage with the Eye of the Fatui, and Mistilteinn could go ahead.

## relations
### STANDARD
- **Other nations**: Snezhnaya keeps official relations with every nation, but its Fatui are distrusted nearly everywhere. Inazuma expelled them as a friendly party after Signora's plot, and the Liyue Qixing watch them closely.
- **The Traveler**: long a thorn in the Fatui's side, by 7.1 the Traveler is a trusted outsider. The Tsaritsa made them a "Consultant to the Tsaritsa".
### LARGE +
- **Knights of Favonius**: relations are tense. Dottore used Inspector Eroch, and Fatui diplomats tried to exploit the Stormterror crisis.
- **The Rokot**: a non-violent Snezhnayan civic group opposed to Project Stuzha. The Fatui consider it an enemy but tolerate it.
- **Snezhnograd Veche**: Snezhnaya's legislature, chaired by Pulcinella as Speaker. Harbingers may sit in it, and the Fatui can usually get their policies passed. Tartaglia now sits there as the voice of the Fatui armed forces.
- **The Druzhna**: the Tsaritsa's personal guard, mostly Vila. It is separate from the Fatui. In 7.1 the Tsaritsa lent its Third Company to Tartaglia to help review officials accused of corruption.
- **Northern Intelligence Network**: the network Diluc belongs to tracks the Fatui and once foiled a Harbinger attempt on Diluc's life.
- **Celestia and the Shades**: since 7.0 the Fatui have been in open conflict with Ronova, the Ruler of Death.
### ULTRA +
- **Internal rivalries**: Pulcinella and Pantalone put Arlecchino and the House of the Hearth at the front of Project Stuzha, which she read as a move to curb her influence. Arlecchino and Sandrone despised Dottore, while Pantalone was close to him. Capitano's will kept his troops away from Pulcinella and Pantalone.
- **Dainsleif**: in 7.1 Pierro's officers searched hard for Dainsleif, who then fought alongside Pierro against Ronova.

## reputation
### LARGE
Abroad, "Fatui" is close to a curse word. People expect masked soldiers, crooked loans and plots behind diplomatic smiles. At home the picture is more mixed. The Fatui are the state, and Harbingers are wealthy, powerful public figures whose interests can start fashions (Tartaglia's taste in fishing gear made one item a sought-after craze). But Project Stuzha's rationing made many citizens resentful.
### ULTRA +
The Fatui are described as the strongest military force of the seven nations in both power and numbers. Ordinary Snezhnayans meet them as Kristall distributors, officials and bank staff as often as soldiers. In Natlan, Fatui troops suffered heavy losses defending the nation against the Abyss under Capitano, and Mavuika thanked him for it, a rare case of open gratitude.

## secrets
### ULTRA
Few Fatui know the Tsaritsa's real plan. Even Pierro admits he is not told everything. Delusion production is a closely guarded secret. Hroptatyr's notebook was sealed for five centuries by Pierro's own request, with a rule that any decision carrying national-level risk needs a unanimous in-person vote of all active Harbingers. Pierro is a pure-blooded Khaenri'ahn, a former royal mage of the Eclipse Dynasty, cursed with immortality at the Cataclysm.

## status
@version: 7.1
### LITE
As of 7.1 the Fatui remain in power in Snezhnaya. Pierro mortally wounded Ronova with the new Eye of the Fatui but was left badly depleted. Ronova's curse is lifted, and Project Mistilteinn can resume.
### STANDARD +
Six Harbingers are active: Pierro, Arlecchino, Pulcinella, Sandrone, Pantalone and Tartaglia. Capitano's seat is kept, and the seats of Dottore, Columbina, Scaramouche and Signora are empty. Arlecchino's agreed price for helping build the new Delusion is that the House of the Hearth will become independent of Fatui affairs and that no more children will be trained as spies. This has been agreed but not yet shown in practice. Tartaglia commands most of Capitano's former troops, and corruption lists from Pulcinella and the House of the Hearth are being reviewed with the Druzhna's help.

## entry: Fatui troop types
@keys: Fatui Skirmisher, Skirmishers, Cicin Mage, Fatui Agent, Pyro Agent, Electro Agent, Mirror Maiden, Fatui Operative, Landcruiser
### STANDARD
- **Skirmishers**: the common soldiers abroad, wearing mechanical suits that give their weapons and armour elemental power and shields. Variants include Cryogunner and Hydrogunner Legionnaires, Pyroslinger and Geochanter Bracers, and Electrohammer and Anemoboxer Vanguards. Their handbook entry says they advance into foreign lands to scout and lay groundwork without asking whether they will live, and that they rely on teamwork because each is weaker alone.
- **Cicin Mages**: Delusion-wielding mages (Cryo or Electro) who command swarms of small elemental Cicins and enjoy toying with their prey.
- **Agents**: elite Pyro or Electro operatives who blink in and out of sight and fight with blades. Pyro Agents staff Debt Collection.
- **Mirror Maidens**: elite Hydro users who fight through conjured mirrors.
- **Operatives**: covert Wind and Frost agents, seen in Fontaine.
- **Landcruisers**: war machines built by the Armory Palace with the Kuuvahki Experimental Design Bureau.

## entry: Fatui Oprichniki
@keys: Oprichniki, Oprichnik, Fireblade Shock Trooper, Hailstorm Cannoneer, Thunderblitz Gvardiya
@version: 6.0
### STANDARD
Unlike Skirmishers, Oprichniki are formally recruited, rigorously trained volunteers, sent either to the Fatui's most important strongholds or to the deadliest front lines. They serve in Nod-Krai and Snezhnaya with kuuvahki-powered gear. Line Troopers, Vanguards, Grenadiers, Support Troopers, Medics and Bombardiers make up the ranks. Officers such as Fireblade Shock Troopers, Hailstorm Cannoneers and Thunderblitz Gvardiya fight with pure elemental power and mostly come from the Royal Military Academy. Oprichniki guard the Northland Bank's vaults in Snezhnograd with radios and access cards.

## entry: Fatui Debt Collection
@keys: Debt Collection division, Fatui debt collector, debt collection
@keys2: Fatui, Northland Bank, Pyro Agent, debt
### STANDARD
The Northland Bank lends generously and expects repayment in full and on time. When someone defaults, the Fatui's Debt Collection division, made up mostly of Pyro Agents, is usually sent and uses as much force as it takes. The bank sometimes chooses other options: in Nasha Town it turned the debtor Zhuoxin into an informant for ten years instead. Snezhnaya's deep cultural regard for loyalty and promises underlies the bank's claim to be "no ordinary bank".

## entry: Founding of the Fatui
@keys: founding of the Fatui, Port Belovodye rebellion, Glupov fortress
### LARGE
The Fatui began as the Tsaritsa's instrument for securing her throne. In the second year of her reign, the humans of Port Belovodye rebelled against the Snowland Fae ruling class. The next year she founded the Fatui with Pierro as first member and leader, rather than mustering the Druzhna as Emperor Monomakh had done, and sent them against the port's independent government. The Fatui occupied the lands of the Drevogorye, Volkhovan and Cirnareka Fae clans, whose princes were charged with negligence and condoning rebellion and stripped of their titles. Grand Duke Drevogorye accused the Tsaritsa of treason, fought the Fatui and was killed. Her envoys then persuaded Port Belovodye to hand over the rebellion's instigators in return for amnesty for everyone else. The following year (the fourth year of the 799th Cycle) she ordered the Fatui to build the fortress of Glupov near Snezhnograd, and in the sixth year she set up the Snezhnograd Veche.

## entry: Fatui in Mondstadt
@keys: Fatui in Mondstadt, Goth Grand Hotel delegation, Holy Lyre der Himmel theft
### LARGE
In Mondstadt the Fatui stirred up or exploited trouble to embarrass the Knights of Favonius. They lured Ursa the Drake into the attack that killed Crepus Ragnvindr, who died after using a Delusion, and Varka blames Dottore personally. After Stormterror's attack, a Fatui diplomat pressed Jean to let them kill Dvalin. Agents stole the Holy Lyre der Himmel, which was soon recovered. Signora then took the Anemo Gnosis from Venti by force. Some Fatui colluded with Schubert Lawrence to restore the Lawrence Clan, a plot the Knights foiled. They also eyed the heart of the dead dragon Durin on Dragonspine, and they compete with Diluc for a stolen vial of the Anemo Archon's breath. A diplomatic delegation lives in the Goth Grand Hotel, which Pantalone rented in its entirety, though they are apparently under lockdown.

## entry: Fatui in Liyue
@keys: Fatui in Liyue, Fatui embassy in Liyue, Zhiyi plot
### LARGE
The Fatui once had an embassy and a kind of diplomatic immunity in Liyue Harbor, and they invested through the Northland Bank. Tartaglia summoned Osial to draw out Rex Lapis, and Fatui soldiers fought the Millelith on the Jade Chamber. Behind that, Signora's real business was a contract under which Zhongli handed over the Geo Gnosis. Afterwards the remaining Fatui were viewed with suspicion and the Northland Bank paid heavy reparations. Later the Fatui backed Zhiyi's attempt to assassinate and replace Uncle Tian on the Qixing. Yelan foiled it, though Pantalone limited the damage. In a smaller affair, the Fatuus Javert ordered Cor Lapis through Gentry Maocai, whose bullying of merchants the Traveler and Xingqiu turned against him.

## entry: Ninth Company in the Chasm
@keys: Ninth Company, Fatui Ninth Company
### LARGE
Under an agreement Signora negotiated with the Qixing, the Fatui's Ninth Company, 64 soldiers sent by Pulcinella, entered the Chasm's underground mines to cleanse a strange sludge with an experimental device. The device exploded. About half the company, including its captain, died or went missing, and Staff Sergeant Anton took command as brevet captain. After Tartaglia's actions in Liyue Harbor the agreement was voided: the company's supplies were cut off, and the Millelith declared its members criminals while they were still trapped underground. When the Traveler found Anton he had only three men left, and they decided to retreat. Katarina, raised in the House of the Hearth, stayed behind to search for her lost brother.

## entry: Fatui in Inazuma
@keys: Fatui in Inazuma, Delusion Factory, Vision Hunt plot, Tatarasuna Incident
### LARGE
The Fatui masterminded the Vision Hunt Decree and kept Inazuma's civil war going, probably by Pierro's design. Signora had the Tenryou and Kanjou Commissions feed the Raiden Shogun false information and supply materials for a Delusion Factory that used Orobashi's Crystal Marrow. Life-draining mass-produced Delusions went to the Watatsumi Army, and the infiltrator Nathan got the wards on Yashiori Island destroyed, releasing the Tatarigami. Centuries earlier, Dottore's sabotage of the Mikage Furnace caused the Tatarasuna Incident. Scaramouche ran the factory and took the Electro Gnosis. After the Traveler beat Signora in a duel before the throne, the Shogun executed her and expelled the Fatui as a friendly party. Signora loyalists and a breakaway House of the Hearth cell under Efim Snezhevich, still following the dead Crucabena's directives, tried to reignite the war. Lyudochka Snezhevna's defection helped stop it.

## entry: Fatui in Sumeru
@keys: Fatui in Sumeru, Shouki no Kami project, Fatui Desert Expedition
### LARGE
Most Fatui work in Sumeru served Dottore. With corrupt Akademiya sages he turned Scaramouche into the artificial god Shouki no Kami. After that failed, he obtained the Electro Gnosis from Nahida by deleting his other Segments, and the Dendro Gnosis in an exchange of knowledge. His teams hunted Aranara and studied the Withering, and a desert expedition under Professor Fronkonsteen, betrayed by the Tanit matriarch Babel, was finally wiped out when its captive Jeht broke free. Viktor helped Vsevolod open a Northland Bank branch in Sumeru City. After Nod-Krai, Pantalone, disguised as one of Dottore's men, led Fatui to Gurabad and Sumeru City to support Dottore's takeover of Irminsul. Nahida burned the tree with the Pyro Gnosis, and Pulcinella wrote to apologise for Dottore's "unsanctioned" actions and promised relief supplies.

## entry: Fatui in Fontaine
@keys: Fatui in Fontaine, 34th Independent Investigative Squad, Hydro Gnosis gift
### LARGE
Arlecchino's House of the Hearth worked in Fontaine, officially to prevent the prophecy that the people would dissolve into the Primordial Sea, and investigated the Hydro Archon. Tartaglia, sent to help the local Northland Bank branch, was wrongly convicted and sent to the Fortress of Meropide, where Arlecchino's agents also tried to infiltrate. After the prophecy passed, Neuvillette gave Arlecchino the Hydro Gnosis as a "diplomatic gift". She later agreed with him that House members who wanted to leave could have their memories of it erased and live normal lives in Fontaine, and she withdrew most of her forces. Smaller affairs include Henri being tricked into stealing water-monitor cores, and a 34th Squad that only pretended to work.

## entry: Fatui in Natlan
@keys: Fatui in Natlan, Capitano's soldiers
### LARGE
Capitano came to Natlan for the Pyro Gnosis and duelled Mavuika. Learning that she had spent her power fighting him, he would not exploit her weakness and asked the Tsaritsa to release him from the task, which she accepted. His men's attempt to rework Natlan's Ley Lines through the Source Mechanism instead woke the Lord of the Night. Capitano then backed Mavuika's plan, and the Fatui fought beside the Natlanese against the Abyss, taking immense casualties. He finally merged his life force with the Lord of the Night to pay Ronova's price in Mavuika's place. Other Fatui in Natlan experimented on captured Saurians, and Sandrone's artificial Fatuus Velimiru hunted a Sovereign Lord's core with Ineffa as an unwilling key.

## entry: Palestar Edict
@keys: Palestar Edict
@version: 6.0
### LARGE
Edicts are the Tsaritsa's highest form of decree. After Columbina, the Third Harbinger, gave up much of her power to fulfil a promise to the Tsaritsa, then resigned and fled to Nod-Krai, the Tsaritsa issued the Palestar Edict, ordering the Fatui to find her at all costs. Harbingers were sent to Nod-Krai, and Dottore, Sandrone and Arlecchino stayed to oversee operations, including Sandrone's construction of the Kuuvahki Experimental Design Bureau over ancient moon ruins. After Dottore's defeat and Columbina's restoration, the Tsaritsa revoked the Edict.

## entry: Fatui Internal Affairs ruling on Dottore
@keys: Okhranka, Fatui Internal Affairs, Fatui Internal Division
@version: 6.3
@spoiler: major
### LARGE
Fatui Internal Affairs, also called the Okhranka ("security"), investigates misconduct inside the Fatui and reports to the Tsaritsa. Little else is known about it. When Dottore ignored a recall order and pursued the power of the Three Moons in Nod-Krai, the Tsaritsa had it investigate him. It concluded that he had acted against her will, and she lifted the ban on Harbingers fighting him, giving Arlecchino and Sandrone authority to eliminate him. In 7.1 the Tsaritsa promised that a suspect in the theft of Seals of Life would be sent to the internal division.

## entry: Eye of the Fatui
@keys: Eye of the Fatui
@version: 7.1
@spoiler: major
### LARGE
The Eye of the Fatui is the improved Delusion Pierro built for the fight with Ronova. Arlecchino explained that a Delusion's drain on its user falls under the authority of Death. The authorities of Life, Death, Time and Space once belonged to the moons, with the Iridescent Moon holding the greatest share of Death; after the moons fell the Heavenly Principles gave them to the Four Shades, but the broken Crimson Moon merged with the Abyss, so Death's authority survives in the Crimson Moon's bloodline. Arlecchino, a descendant of the Crimson Moon Dynasty, agreed to serve as the base, on condition that the House of the Hearth leave Fatui affairs and that no more children be trained as spies. During a full-power test the Abyssal influence surged out of control, and only the Traveler's quick purification kept it from corroding her. The decisive knowledge came from Hroptatyr's unsealed notebook. At Rankova Zorya, after Celestia had already reclaimed Ronova's authority, Pierro awakened the Eye against her. It poured out Abyssal energy, dealt her what Pierro judged fatal and irreversible damage, and left him badly depleted. Dainsleif remarked: "To wield the immense power that he did, one always has to pay an irrecoverable price."

## entry: Harbingers' unanimous vote
@keys: Hroptatyr's notebook, unanimous vote of the Harbingers, national-level risk vote
@version: 7.1
@spoiler: major
### ULTRA
After joining the Fatui, Pierro found that the notebook Hroptatyr had left him held forbidden knowledge. Fearing it could make Snezhnaya a "second Khaenri'ah", he had the Tsaritsa seal it in the depths of the Armory Palace archives, under a rule that any decision carrying national-level risk must pass by a unanimous, in-person vote of all active Harbingers, chaired by the Director. In 7.1 he summoned them. Pulcinella argued that they were already a thorn in the Ruler of Death's side. Arlecchino did not want to leave a valuable card unplayed. Pantalone said that in desperate times the greatest risk is not daring to gamble. Sandrone hesitated and then agreed, and Tartaglia voted in favour too. As the proposer, Pierro did not vote. Capitano, incapacitated, was not required. Inside the notebook was a prism holding a younger Hroptatyr, which gave Pierro what he needed for the new Delusion.

## entry: Capitano's will
@keys: Capitano's will, Capitano's subordinates
@keys2: Tartaglia, Childe, Fatui, Veche, Pierro
### ULTRA
Before leaving Snezhnaya for the last time, Capitano left Pierro a detailed letter that effectively served as his will. He expected that ambitious Harbingers, particularly Pantalone and Pulcinella, would otherwise divide his army between them and upset the balance of power. Under the letter, Tartaglia took custody of most of Capitano's subordinates and all his key personnel, and received a seat in the Snezhnograd Veche as the voice of the Fatui armed forces. The choice surprised Tartaglia, who had thought Capitano looked down on him. He and Sandrone privately opposed Project Stuzha but supported it for their subordinates' sake, while raising its harms in the Veche.

## entry: Armory Palace and its guards
@keys: Special Assignments Battalion, Royal Grenadier Guards, Sixth Company
### ULTRA
The Royal Armory Palace, deep inside Glupov and managed by Sandrone, develops Snezhnaya's weapons and has a reputation for complicated administration. It houses Project Mistilteinn's underground research site and the sealed archive where Hroptatyr's notebook lay. The Special Assignments Battalion of its Royal Grenadier Guards, headed by Major Valeriy, protects key people such as the scientist Mitya and keeps tabs on them. Two rival Armory Palace researchers, Preobrazhensky and Anton Zarkovich Karnatsky, were sent to study kuuvahki in Nod-Krai's Nothing Passage. Their rivalry ended in a disaster that killed them and the whole Sixth Company except Private Smirnova, who escaped to send a distress call.

## entry: Persikov's memory machine
@keys: Persikov
@availability: limited
@version: 2.8
### ULTRA
During the limited-time event Summertime Odyssey, a Fatuus named Persikov took a small group of Fatui to the Golden Apple Archipelago to test a machine that used a god's power to manipulate memories. His superiors had not approved the test, so he had his men sign waivers. The machine broke down, the Fatui made it worse and their minds began to break. The Traveler and Kaedehara Kazuha repaired it, restoring them, and the group packed up and left.
