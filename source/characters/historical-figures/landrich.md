---
{
  "id": "historical.landrich",
  "entity_type": "historical_figure",
  "name": "Landrich",
  "aliases": ["Master Landrich"],
  "summary_line": "A Mondstadt aristocrat of the Aristocratic period, about a thousand years ago, known only through the Ancient Investigation Journals as the master behind the doomed Dragonspine expedition.",
  "nation": "location.mondstadt",
  "tags": ["Mondstadt", "Aristocratic period", "historical", "Dragonspine expedition"],
  "introduced_in": "1.2",
  "spoiler_level": "minor",
  "availability": "permanent",
  "related": [
    "historical.eberhart", "historical.parsifal", "historical.ingbert", "historical.luther",
    "faction.mondstadt-aristocracy", "historical.vennessa", "location.dragonspine", "quest.a-land-entombed",
    "historical.priscilla"
  ],
  "relationships": [
    {"target": "historical.eberhart", "type": "father (illegitimate son)", "summary": "Luther writes that Landrich judged Eberhart well and meant to bestow the clan name on him after the expedition; Eberhart's resentment and secret plan for the clan and for his brothers went unnoticed by Landrich, as far as the journals show.", "classification": "strongly_supported", "since": "1.2"},
    {"target": "historical.ingbert", "type": "father (legitimate son)", "summary": "Ingbert, a keen explorer, travelled on the expedition Landrich sent out and was struck down by Eberhart's polearm.", "classification": "strongly_supported", "since": "1.2"},
    {"target": "historical.parsifal", "type": "father (legitimate son)", "summary": "Parsifal's disobedience, love of chivalric play-acting and eventual departure are described by Luther as things Eberhart encouraged. The journals do not record how Landrich reacted.", "classification": "strongly_supported", "since": "1.2"},
    {"target": "historical.luther", "type": "master and servant", "summary": "Luther, who wrote the journals, calls Landrich 'Master' and fears Landrich's displeasure if the expedition fails; his last words ask whoever finds the journal to warn Landrich.", "classification": "confirmed", "since": "1.2"}
  ],
  "knowledge": {
    "knows": [
      {"fact": "He wanted the Dragonspine expedition to bring back great achievements that would quell the arrogance of those who conspired to rebel (as Luther reports his purpose).", "learned": "Ancient Investigation Journal: Part I", "version": "1.2", "visibility": "restricted"}
    ],
    "does_not_know": [
      {"fact": "That Eberhart planned to kill the expedition and clear his path to the clan", "note": "Luther's last entry begs for a warning to be carried to him; there is no sign one arrived."},
      {"fact": "Anything after the expedition, including Vennessa's revolution", "note": "His fate is not recorded."}
    ],
    "believes": [
      {"belief": "Eberhart is a capable, loyal heir worth legitimising.", "reality": "Luther's journal reveals Eberhart arranged the deaths of the party.", "classification": "strongly_supported"}
    ]
  },
  "facts": {
    "full_name": null,
    "title": null,
    "pronouns": "he/him",
    "species": "Human",
    "origin": "location.mondstadt",
    "residence": "location.mondstadt",
    "occupation": "Aristocrat; head of his family, which clan is not stated",
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
    "identity_notes": "Never appears in person; known only as 'Master Landrich' in the Ancient Investigation Journals. A Hydro Abyss Mage called Landrich appears in Diluc's Story Quest; the wiki treats the two as probably unrelated."
  },
  "uncertainties": [
    {"topic": "Which clan Landrich led", "classification": "unknown", "note": "The journals call him 'Master' and speak of Luther's 'family's name'; no clan is named. The wiki says he headed his clan, an inference from his authority over the heirs."},
    {"topic": "His fate", "classification": "unknown", "note": "Nothing records whether Eberhart returned or whether Landrich was warned. The wiki guesses he was among the aristocrats exiled after Vennessa's rebellion; canon does not say."},
    {"topic": "Landrich as the parent of all three brothers", "classification": "strongly_supported", "note": "Luther's third journal speaks of Eberhart as an illegitimate child whom Landrich meant to name heir, and of Ingbert as 'Master'. The wiki lists Parsifal and Ingbert as his legitimate sons and Eberhart as the illegitimate one; Parsifal's parentage was not traced to an exact line here."},
    {"topic": "The Abyss Mage named Landrich", "classification": "disputed", "note": "A Hydro Abyss Mage in Darknight Hero's Alibi has a near-identical name. Do not treat it as the aristocrat."},
    {"topic": "Who organised the expedition", "classification": "inferred", "note": "The wiki says Landrich organised it though he did not travel. The journals show the party acting for him but do not state outright that he sent it."}
  ],
  "sources": [
    {"title": "Landrich", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Landrich", "accessed": "2026-10-12", "confidence": "medium", "section": "Story, Trivia", "version": "1.2"},
    {"title": "Ancient Investigation Journal: Part I", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ancient_Investigation_Journal:_Part_I", "accessed": "2026-10-12", "confidence": "high", "version": "1.2"},
    {"title": "Ancient Investigation Journal: Part II", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ancient_Investigation_Journal:_Part_II", "accessed": "2026-10-12", "confidence": "high", "version": "1.2"},
    {"title": "Ancient Investigation Journal: Part III", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/Ancient_Investigation_Journal:_Part_III", "accessed": "2026-10-12", "confidence": "high", "version": "1.2"},
    {"title": "Eberhart", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Eberhart", "accessed": "2026-10-12", "confidence": "medium", "section": "Story"}
  ],
  "wi": {"keys": ["Landrich", "Master Landrich"]},
  "status": "drafted",
  "last_verified": null,
  "notes": "Canon is thin: Landrich never appears and is known only from three Dragonspine journals (A Land Entombed, 1.2). This is a short entry by design. No post-1.2 canon about him was found."
}
---

## summary
### LITE
Landrich was a Mondstadt aristocrat of the Aristocratic period, about a thousand years ago. He is never seen; the Ancient Investigation Journals show him as a trusted master whose approval his household feared losing, and as the man who stood to lose most from the Dragonspine expedition.
### STANDARD +
Luther's journals say the expedition was meant to bring back a great achievement to quiet the arrogance of those plotting rebellion, and that Landrich planned to name his illegitimate son Eberhart heir to the clan name once the party returned.

## background
### LITE
Landrich lived when the old noble clans ruled Mondstadt, before Vennessa's revolution. He had at least three sons: Parsifal and Ingbert, his legitimate heirs, and Eberhart, an illegitimate son.
### STANDARD +
He stayed in Mondstadt while a party of young aristocrats and servants, including his sons Ingbert and Eberhart and the servant Luther, went to explore ancient ruins on Dragonspine. Luther's accounts suggest Landrich valued Eberhart's competence despite the boy's birth, and intended to give him the clan name on his return.
### LARGE +
The expedition's stated aim, per Luther, was to win great achievements for the family that would put down the arrogance of those conspiring to rebel. Landrich therefore saw the venture as a show of strength as well as exploration. The party searched the Dragonspine ruins for frescoes and Starsilver weapons, losing companions to a snowstorm and a cave-in.

## status
### LITE
Dead long ago. His fate is not recorded; he never learns the truth about Eberhart in any surviving text.
### STANDARD +
Luther's last journal asks whoever finds it to warn Landrich that Eberhart, wounded but possibly alive, would have only one obstacle left on his road to revolt. Nothing says the warning arrived, and no later source mentions Landrich.

## relationships
### STANDARD
Father of three sons by differing status: Parsifal and Ingbert (legitimate) and Eberhart (illegitimate, trusted most on the expedition). Luther serves the household and addresses him as Master.
### LARGE +
Ingbert's death and Eberhart's treachery both flow from the succession Landrich meant to settle. Parsifal left the family before the expedition, which Luther attributes in part to Eberhart's influence.

## knowledge
### STANDARD
He does not know of Eberhart's scheme. As a figure known only from others' writing, he should never be portrayed as possessing knowledge from after the expedition.
### ULTRA +
What the journals reveal about his household's fear of him: Luther writes that failing Master Landrich could end with him facing monsters in the gladiatorial arena, and that Eberhart's own gladiator was cut down by the red-haired Lawrence Clan fighter (Vennessa). That says more about the regime Landrich belonged to than about Landrich himself, whose own words survive nowhere. Any dialogue for him is invention and should be labelled as such.

## mistakes
### STANDARD
- Do not give him a clan name, voice lines or personality traits canon does not supply.
- He is not the Hydro Abyss Mage named Landrich from Diluc's Story Quest.
- He did not travel to Dragonspine himself.
- Do not state that he was exiled or killed; canon is silent.

## entry: Dragonspine expedition
@keys: Dragonspine expedition, Ancient Investigation Journal, Ancient Investigation Journals, Dragonspine aristocrats
@keys2: Landrich, Eberhart, Luther
@version: 1.2
### STANDARD
Landrich's expedition to the ruins on Dragonspine, known from three journals found during A Land Entombed. The party, young aristocrats and servants, set out from South Base Camp. Companions vanished in a snowstorm; a cave-in before a round door killed another and cost the party its food and fuel. Eberhart then led Ingbert and Luther into the cellar of the southwestern ruins and attacked them with a polearm. Luther survived long enough to write the third journal. See the entries for Luther and Eberhart.
