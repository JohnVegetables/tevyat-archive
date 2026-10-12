---
{
  "id": "historical.luther",
  "entity_type": "historical_figure",
  "name": "Luther",
  "aliases": ["Author of the Ancient Investigation Journals", "Luther of the Dragonspine expedition"],
  "summary_line": "A member of a Mondstadt aristocrat's household about a thousand years ago who wrote the three Ancient Investigation Journals on Dragonspine and exposed Eberhart's treachery with his last strength.",
  "nation": "location.mondstadt",
  "tags": ["Mondstadt", "Aristocratic period", "historical", "Dragonspine expedition", "journal author"],
  "introduced_in": "1.2",
  "spoiler_level": "minor",
  "availability": "permanent",
  "related": [
    "historical.landrich", "historical.eberhart", "historical.ingbert", "historical.parsifal", "historical.priscilla",
    "faction.mondstadt-aristocracy", "historical.vennessa", "historical.unnamed-gladiator", "item.starsilver",
    "location.dragonspine", "quest.a-land-entombed", "faction.lawrence-clan"
  ],
  "relationships": [
    {"target": "historical.landrich", "type": "servant to his master", "summary": "He calls Landrich 'Master', wants to live up to his expectations and fears a gladiator's fate if the expedition fails; his final entry asks readers to warn Landrich.", "classification": "confirmed", "since": "1.2"},
    {"target": "historical.ingbert", "type": "childhood companion and master", "summary": "Luther writes that they all grew up together. He addresses Ingbert as 'Master', relays his hopes of finding Starsilver weapons and frescoes, and watched Eberhart strike him down.", "classification": "confirmed", "since": "1.2"},
    {"target": "historical.eberhart", "type": "childhood companion; betrayer", "summary": "Luther admired Eberhart's calm under pressure until the cellar, where Eberhart drew a polearm on him and Ingbert. His last entry reads the whole expedition as Eberhart's plan to clear his path to the clan.", "classification": "confirmed", "since": "1.2"},
    {"target": "historical.parsifal", "type": "childhood companion and master", "summary": "He recalls Parsifal's disobedience, love of chivalric play-acting and eventual departure, and suspects Eberhart encouraged all three.", "classification": "confirmed", "since": "1.2"},
    {"target": "historical.priscilla", "type": "addressee of an apology", "summary": "His last entry says he is sorry to Priscilla because he will not return to Mondstadt. Their relationship is not stated.", "classification": "unknown", "since": "1.2"}
  ],
  "knowledge": {
    "knows": [
      {"fact": "Eberhart betrayed the party: the deaths in the snow and the cave-in were part of his plan, and he attacked Ingbert and Luther in the cellar.", "learned": "the cellar attack", "version": "1.2", "visibility": "secret"},
      {"fact": "Landrich meant to give Eberhart the clan name after the expedition.", "learned": "Ancient Investigation Journal: Part III", "version": "1.2", "visibility": "restricted"}
    ],
    "does_not_know": [
      {"fact": "Whether anyone ever read his journals or whether Landrich was warned", "note": "He dies, or is dying, as he writes."},
      {"fact": "Eberhart's later fate", "note": "He says only that Eberhart is badly injured but might reach Mondstadt."}
    ],
    "believes": [
      {"belief": "Eberhart's calm leadership proved he was fit to be an aristocrat.", "reality": "Eberhart was steering the party toward its destruction.", "classification": "strongly_supported"}
    ]
  },
  "facts": {
    "full_name": null,
    "title": null,
    "pronouns": "he/him",
    "species": "Human",
    "origin": "location.mondstadt",
    "residence": "location.mondstadt",
    "occupation": "Member of an aristocratic household; expedition scribe and surveyor",
    "affiliations": ["faction.mondstadt-aristocracy"],
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
    "card": false,
    "status_flag": "dead",
    "era": "Aristocratic period, about 1,000 years ago",
    "identity_notes": "His name appears in the Ragged Records found in the Dragonspine ruins, which note that the writer of the second record did not finish Luther off. He is otherwise 'the author' of the Ancient Investigation Journals."
  },
  "uncertainties": [
    {"topic": "Luther's social rank", "classification": "inferred", "note": "He calls the heirs 'Master' and fears being sent to the gladiatorial arena, which the wiki reads as meaning he was a commoner, a slave or a hired hand. Yet he also speaks of his 'family's name' and honouring it, so a lesser noble family is equally plausible."},
    {"topic": "His death", "classification": "strongly_supported", "note": "His third journal calls itself his last entry and describes blood loss; the wiki says he died of the wound. Canon shows no scene of his death."},
    {"topic": "Priscilla", "classification": "unknown", "note": "He apologises to Priscilla. The wiki claims he knew her and that she was part of Eberhart's plan, but the journals do not say either."},
    {"topic": "Whether Luther was meant to survive", "classification": "inferred", "note": "A Ragged Record by the attacker says he could not deal with Luther 'under the circumstances' but that the wound would suffice. The speaker of the record is not named in the lines read."}
  ],
  "sources": [
    {"title": "Luther", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Luther", "accessed": "2026-10-12", "confidence": "medium", "section": "Profile", "version": "1.2"},
    {"title": "Ancient Investigation Journal: Part I", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ancient_Investigation_Journal:_Part_I", "accessed": "2026-10-12", "confidence": "high", "version": "1.2"},
    {"title": "Ancient Investigation Journal: Part II", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ancient_Investigation_Journal:_Part_II", "accessed": "2026-10-12", "confidence": "high", "version": "1.2"},
    {"title": "Ancient Investigation Journal: Part III", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ancient_Investigation_Journal:_Part_III", "accessed": "2026-10-12", "confidence": "high", "version": "1.2"},
    {"title": "Ragged Records", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ragged_Records", "accessed": "2026-10-12", "confidence": "high", "section": "Ragged Records #2", "version": "1.2"},
    {"title": "Eberhart", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Eberhart", "accessed": "2026-10-12", "confidence": "medium", "section": "Story"}
  ],
  "wi": {"keys": ["Luther", "Ancient Investigation Journal", "Ancient Investigation Journals"]},
  "status": "drafted",
  "last_verified": null,
  "notes": "Known only from three journals and a Ragged Record in the Dragonspine ruins (A Land Entombed, 1.2); short by design. His rank and the nature of his link to Priscilla are not established. No post-1.2 canon found."
}
---

## summary
### LITE
Luther was a member of a Mondstadt aristocratic household around a thousand years ago who travelled to Dragonspine on Landrich's expedition and kept the Ancient Investigation Journals. His last entry names Eberhart as the one who destroyed the party.
### STANDARD +
His voice survives only as written pages: dutiful, anxious about failing his master, and slow to see what Eberhart was doing.

## background
### LITE
Luther grew up with Ingbert, Parsifal and Eberhart, the sons of Landrich, and calls all of them 'Master'. He joined the expedition to Dragonspine, which Landrich meant to prove the clan could still do great things. He measured the ruins' safety, recorded decisions and mourned the companions lost.
### STANDARD +
The journals follow the party from South Base Camp. After days of loss in a snowstorm, they abandoned plans to explore the southwestern cellar and went to a locked chamber thought to hold frescoes and Starsilver weapons. A cave-in killed Nick before the round door and took the party's food and fuel. The doors would not open. Luther admired Eberhart's calm, and Eberhart's proposal sent them to the cellar.
### LARGE +
In the cellar Eberhart drew a polearm and struck Ingbert; Luther was wounded too but escaped and wrote the third journal. He decided that Eberhart's talk of a lost civilisation under the snow and a power from the heavens was bait for Ingbert, who loved exploration, and that Eberhart's secret polearm training matched an illegitimate son's wish for dominion over the clan.

## status
### LITE
Dead around a thousand years ago; his last journal says it is his last entry. He is not seen in any scene.
### STANDARD +
His writings were left in the ruins, where the Traveler finds them during A Land Entombed. Whether anyone read them in his time is unknown.

## relationships
### STANDARD
He serves Landrich and the three brothers he grew up with: Ingbert (struck down), Parsifal (departed) and Eberhart (the betrayer). He fears Landrich's displeasure and apologises to Priscilla at the end.
### LARGE +
Luther is the only source that links Eberhart's schemes together: Parsifal's flight, the vanished companions, the cave-in and the cellar attack. His final request is that someone warn Landrich before Eberhart returns to finish what he began.

## knowledge
### STANDARD
He understands Eberhart's plan only at the end. Earlier entries show him trusting Eberhart's reassurance that the missing companions were trained aristocratic children who could find their way back.
### ULTRA +
He admits the harshness of his thoughts: after the loss of Nick and the supplies, he wonders if bitterness is a natural toll of desperation. He expected to be sent to the gladiatorial arena if the expedition failed, and compares it to the fate of Eberhart's gladiator, who died to the red-haired Lawrence Clan fighter, Vennessa. He knows nothing of what became of Eberhart.

## mistakes
### STANDARD
- Do not give him canon speech beyond the journals; keep his voice formal, anxious and observational.
- Do not call him a commoner, a slave or a noble as fact; canon leaves his rank open.
- Do not claim a romance or marriage with Priscilla.
- He did not win a fight with Eberhart; he fled wounded.

## entry: Ancient Investigation Journals
@keys: Ancient Investigation Journal, Ancient Investigation Journals, Dragonspine journals
@version: 1.2
### STANDARD
Three journals found in the Dragonspine ruins during A Land Entombed. Part I covers the weather, the plan to open a secret chamber and the lost companions. Part II records the failed attempt to open the round doors, the cave-in that killed Nick, and Luther's admiration of Eberhart. Part III is the confession of the betrayal and the plea to warn Landrich.

## entry: Eberhart's plan
@keys: Eberhart, Eberhart's plan, Dragonspine betrayal
@keys2: Luther, Ingbert
@version: 1.2
@spoiler: minor
### STANDARD
Luther concluded that Eberhart, an illegitimate son, used the expedition to remove obstacles to the clan: lost companions, the cave-in and the cellar attack on Ingbert and Luther. He suspected Eberhart had also pushed Parsifal toward disobedience and exile. Eberhart was badly wounded himself, and his fate is unknown.
