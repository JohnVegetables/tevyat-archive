---
{
  "id": "historical.aberaku",
  "entity_type": "historical_figure",
  "name": "Aberaku",
  "aliases": ["Aberaku no Mikoto", "Abrax", "Helios-Forger", "Aberaku the sage"],
  "summary_line": "The sage of ancient Byakuyakoku who organised the building of the Dainichi Mikoshi, the artificial sun of Enkanomiya, and died imprisoned by the child-ruler his creation helped to make possible.",
  "nation": "location.inazuma",
  "tags": ["Inazuma", "Enkanomiya", "Byakuyakoku", "Dainichi Mikoshi", "Helios", "Shade of Tokoyo", "sage"],
  "introduced_in": "2.4",
  "spoiler_level": "major",
  "availability": "permanent",
  "related": [
    "location.enkanomiya", "location.dainichi-mikoshi", "lore.byakuyakoku", "npc.istaroth", "historical.orobashi",
    "creature.bathysmal-vishap", "lore.unified-civilization", "lore.war-of-funerary-flame", "cosmology.four-shades",
    "item.the-byakuyakoku-collection", "quest.hyperions-dirge", "quest.orobashis-legacy", "location.temple-of-space"
  ],
  "relationships": [
    {"target": "npc.istaroth", "type": "teacher in the art of the sun (as the lore tells it)", "summary": "The Byakuyakoku chronicle says only Istaroth, the Ruler of Time, among the shining Shades still answered the people's prayers; the wiki's reading of the Dainichi Mikoshi lore is that she taught Aberaku enough to build Helios. The chronicle itself credits an awakening of his wisdom in the Year of Blindness and names Tokoyo Ookami as the source of his enlightenment.", "classification": "strongly_supported", "since": "2.4"},
    {"target": "lore.byakuyakoku", "type": "people he led and saved", "summary": "He organised the building of Helios against the Dragonheirs of the Depths and was hailed for it, then was betrayed by nobles who turned the people to worship the sun-chariot and enthroned a child as ruler.", "classification": "confirmed", "since": "2.4"},
    {"target": "creature.bathysmal-vishap", "type": "the threat Helios was built against", "summary": "The Dragonheirs of the Depths, now called Bathysmal Vishaps, hunted the people in the dark; Helios's light drove them back.", "classification": "confirmed", "since": "2.4"},
    {"target": "historical.orobashi", "type": "later god of the land", "summary": "Orobashi came long after Aberaku's death, overthrew the Sunchildren at a child's request and strengthened the Dainichi Mikoshi.", "classification": "confirmed", "since": "2.4"}
  ],
  "knowledge": {
    "knows": [
      {"fact": "He built Helios (the Dainichi Mikoshi) to save his people from the Dragonheirs, and was imprisoned above it on a charge of high treason brought in the name of the Sunchild.", "learned": "lived it; restored once his soul was made whole", "version": "2.4", "visibility": "public"},
      {"fact": "A Divine Bridle he hid at the top of the Dainichi Mikoshi is the proof that a child is a 'child of the sun'; he says no Sunchild ever reached maturity, and implies this was tied to the birth-rite in the inner sanctum.", "learned": "recalled when his soul was reunited", "version": "2.4", "visibility": "secret"}
    ],
    "does_not_know": [
      {"fact": "Anything after his death except what he senses as a Shade: Orobashi's rule, the later fall of Byakuyakoku's culture to Watatsumi, the Traveler's wider journey.", "note": "he speaks only of his own time"},
      {"fact": "That his old teacher Istoria is in the Temple of Space and could not find his name in any record.", "note": "6.x Counterfeit Classics; Aberaku never refers to it"}
    ],
    "believes": [
      {"belief": "That the true all-devouring night was the greed in human hearts, not the dark of Enkanomiya.", "reality": "His own late realisation, stated to the Traveler; it is his reading, not an objective fact.", "classification": "confirmed"}
    ]
  },
  "facts": {
    "full_name": "Aberaku no Mikoto (birth name Abrax)",
    "title": "Helios-Forger",
    "pronouns": "he/him",
    "species": "Human",
    "origin": "lore.unified-civilization",
    "residence": "location.enkanomiya",
    "occupation": "Sage; builder of the Dainichi Mikoshi",
    "affiliations": ["location.enkanomiya"],
    "vision": null,
    "element": null,
    "weapon": null,
    "birthday": null,
    "age": null,
    "height": null,
    "body_type": null,
    "card": false,
    "status_flag": "dead",
    "era": "about 6,000 years ago, shortly before and after the War of Funerary Flame (the wiki's date, not stated in a single in-game line)",
    "identity_notes": "'Aberaku' is the Inazuman-style rendering of his name used in Enkanomiya; the older chronicle text and Istoria call him Abrax. He is known today only as a spectral Shade of Tokoyo, not as a living person."
  },
  "uncertainties": [
    {"topic": "His death date and year numbering", "classification": "inferred", "note": "The Byakuyakoku chronicle's last entry says only that by the tenth year of Sun and Moon he was 'long gone'; the Dainichi Mikoshi wiki page and the quest series place his death in prison. 'About 6,000 years ago' is the wiki infobox figure."},
    {"topic": "How he came to be wise", "classification": "disputed", "note": "The chronicle says Tokoyo Ookami opened him to wisdom and the Year of Blindness entry says his wisdom was awakened; a separate account in the Dainichi Mikoshi lore credits Istaroth. They need not conflict (she is Time, the Shade he prayed to) but canon does not reconcile them."},
    {"topic": "Whether Abrax and Aberaku are the same man", "classification": "strongly_supported", "note": "Counterfeit Classics (6.x) has Istoria speak of a student named Abrax who went to Delphi Pytho, and the chronicle's Abrax is the leader who built Helios. The in-game names for the spirit in Enkanomiya are Aberaku and Helios-Forger. The identification is the standard reading, not a single plain line."},
    {"topic": "Why no historical record of him survives", "classification": "unknown", "note": "Istoria says no one has ever found Abrax's name in historical records; canon gives no explanation."},
    {"topic": "Appearance in 6.x and 7.0-7.1", "classification": "unknown", "note": "Only a mention by Istoria in the Luna VI quest Counterfeit Classics. Nothing in Snezhnaya content up to 7.1."}
  ],
  "sources": [
    {"title": "Aberaku", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Aberaku", "accessed": "2026-10-11", "confidence": "medium", "section": "Profile, Quests", "version": "2.4"},
    {"title": "Hyperion's Dirge (World Quest)", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Hyperion%27s_Dirge_(Quest)", "accessed": "2026-10-11", "confidence": "high", "version": "2.4", "section": "Dialogue"},
    {"title": "Narrow Inquiry", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Narrow_Inquiry", "accessed": "2026-10-11", "confidence": "high", "version": "2.4", "section": "Dialogue"},
    {"title": "Temple Inquiry", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Temple_Inquiry", "accessed": "2026-10-11", "confidence": "high", "version": "2.4", "section": "Dialogue"},
    {"title": "Serpent's Heart Inquiry", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Serpent%27s_Heart_Inquiry", "accessed": "2026-10-11", "confidence": "high", "version": "2.4", "section": "Dialogue"},
    {"title": "The Byakuyakoku Collection (Vol. 1 and 2)", "type": "in_game_text", "url": "https://genshin-impact.fandom.com/wiki/The_Byakuyakoku_Collection", "accessed": "2026-10-11", "confidence": "high", "version": "2.4", "section": "The Serpent and Drakes of Tokoyokoku; Before Sun and Moon"},
    {"title": "Dainichi Mikoshi", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Dainichi_Mikoshi", "accessed": "2026-10-11", "confidence": "medium", "section": "Lore", "version": "2.4"},
    {"title": "Rikoru", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Rikoru", "accessed": "2026-10-11", "confidence": "medium", "section": "Profile", "version": "2.4", "notes": "Sunchildren Hide and Seek is cited by the wiki for the nobles' deception of Rikoru."},
    {"title": "Counterfeit Classics", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Counterfeit_Classics", "accessed": "2026-10-11", "confidence": "high", "version": "6.0", "section": "Dialogue (Istoria on his student Abrax)", "notes": "Wiki change history lists this as a Luna VI quest."}
  ],
  "wi": {"keys": ["Aberaku", "Abrax", "Helios-Forger", "Aberaku no Mikoto"]},
  "status": "drafted",
  "last_verified": null,
  "notes": "Thin canon but a real figure: a quest NPC shade plus book text. Not a card character (a fragmented memory spirit). The wiki's '6,000 years ago' and the Istaroth tutelage are wiki framing, flagged in uncertainties."
}
---

## summary
### LITE
Aberaku no Mikoto, born Abrax, was a sage of ancient Byakuyakoku in Enkanomiya. He organised the building of the Helios, now the Dainichi Mikoshi, the artificial sun that drove back the Dragonheirs of the Depths. He died in prison; only his scattered memory survives, as a Shade of Tokoyo.
### STANDARD +
He calls himself the Helios-Forger. His story is the sad part of Byakuyakoku's golden age: the light he made brought peace, and the peace let scheming nobles rule through a child.
### LARGE +
Players meet him in the Hyperion's Dirge world quest chain (2.4), where the Traveler gathers the offerings that hold the pieces of his soul. A later mention in the 6.x quest Counterfeit Classics shows that a teacher of his, Istoria, remembers him but cannot find his name in any record.

## background
### LITE
A pupil of Istoria from the unified civilisation, he was trapped in Enkanomiya when it sank underground. In the lightless land he was recognised as a sage, built Helios, and was imprisoned in its tower, where he died.
### STANDARD +
Per the wiki he lived about 6,000 years ago and went to Delphi Pytho (later Enkanomiya) shortly before the War of Funerary Flame, where the kingdom collapsed underground and trapped him. The Byakuyakoku chronicle places the story in the Year of Blindness, when Abrax's wisdom was awakened and the people began to build the Helios under him. When it was done, the Whitenight came and Evernight was banished. In the second year of Sun and Moon the first Sunchild had him imprisoned, and by the tenth year he was long gone.
### LARGE +
His own account in Hyperion's Dirge: the people worshipped the sun-chariot, nobles proclaimed a young Sunchild the ruler, and when he opposed this the child, controlled by those nobles, accused him of high treason. He was held above his own creation. After he died, his clothes, crown and bones were enshrined at three places in Enkanomiya out of honour, and that very act is what split his soul into fragments.
### ULTRA +
Another telling in the chronicle's first volume has him say to the first Sunchild that dragons and snakes are kin before troops in ambush seized him; it notes that the Sunchildren owed their very existence to his artificial star. The wiki's Rikoru page adds that Rikoru once admired him and built a small model of the Dainichi Mikoshi until nobles convinced him that Aberaku meant to kill him.

## status
### LITE
Dead. His remembered self survives only as a Shade of Tokoyo, a translucent spirit that appears in Enkanomiya's Evernight.
### STANDARD +
Once the Traveler reunites his soul, he regains full memory and gives them the Divine Bridle, then sits at the highest point of the Dainichi Mikoshi. His last words are bitter: all that talent and ability, and what use was it.
### LARGE +
Nothing about him changes in 6.x or 7.0-7.1. His only later trace is Istoria's remark in Counterfeit Classics.

## relationships
### STANDARD
Istaroth/Time (the source of his light-making knowledge), his people, the Sunchild who imprisoned him, and Orobashi, the later god who made use of his sun.
### LARGE +
He bears no hatred for the child Sunchild, only pity, and blames the nobles who pulled the strings. He did not live to see Orobashi.
### ULTRA +
Istoria remembers him as a student and does not know whether he survived the war; Aberaku, as a Shade, never learns that his teacher still lives.

## knowledge
### LITE
He knows only his own era: building Helios, his betrayal, and where his soul is divided. He is a spirit and does not know what has become of Enkanomiya.
### STANDARD +
He believes that the real eternal night was human greed, and he recalls that the Divine Bridle hidden at the top of the tower is proof of a Sunchild's birthright. He does not know the Traveler's journey beyond what they tell him.

## mistakes
### STANDARD
- He is not Orobashi and did not make Enkanomiya's day-night switch; Orobashi later strengthened the Dainichi Mikoshi so it could be toggled.
- He did not found the Sunchildren; the nobles made one of them king after he finished Helios.
- Do not give him a death year or a birthplace; canon is vague and the 6,000-year figure is the wiki's.
- Aberaku and Abrax are one man, but only the first name is used in Enkanomiya's quest text.
- He is not a living character and cannot hold ordinary conversation; the spirit repeats his name and fragments.

## chronology
### LARGE
- About 6,000 years ago (wiki): a pupil of Istoria; goes to Delphi Pytho shortly before the War of Funerary Flame.
- Year of Blindness: his wisdom awakens; Helios is built under his lead.
- First Year of Sun and Moon: Helios completed; Whitenight begins.
- Second Year: imprisoned at the order of the first Sunchild.
- Tenth Year: long gone; remains enshrined in three places.
- 2.4: Hyperion's Dirge.
- 6.x (Luna VI): Istoria mentions his student Abrax in Counterfeit Classics.

## entry: The Dainichi Mikoshi (Helios)
@keys: Dainichi Mikoshi, Helios, Hyperion, Byakuya no Hikari
@keys2: Aberaku, Abrax, Enkanomiya
@version: 2.4
@spoiler: minor
### STANDARD
The Dainichi Mikoshi is the artificial sun of Enkanomiya, which Aberaku called Helios in private. Its light turned Evernight into a cycle of Whitenight and Evernight and kept the Dragonheirs of the Depths at bay. Under Orobashi's rule it was powered up so that it could be toggled at will.
### LARGE +
Byakuyakoku's chronicle says that, as long as the people stayed ignorant, the nobles worshipped the machine as a god and made the Sunchild its voice. Aberaku saw that as vain and dead worship of a tool.

## entry: The Divine Bridle
@keys: Divine Bridle
@keys2: Aberaku, Sunchild
@version: 2.4
@spoiler: major
### STANDARD
At the top of the Dainichi Mikoshi, Aberaku hid a bridle as proof that a child was a true child of the sun. He meant to reveal it to alert the people but no longer sees the point in doing so, and hands it to the Traveler. It is needed later in the quest The Phaethons' Syrtos.
### LARGE +
He explains that no Sunchild ever came of age, and, when Paimon asks, he recites a verse about the Sunchild riding Pegasus to the feast of the sun at their birth-rite, in the inner sanctum of the mikoshi; he implies the children were put to death there but never says so outright.

## entry: The Sunchild and Rikoru
@keys: Sunchild, Sunchildren, Rikoru
@keys2: Aberaku, Enkanomiya
@version: 2.4
@spoiler: minor
### STANDARD
The Sunchild was a young puppet ruler chosen by nobles after Helios was completed. The first, Rikoru, had Aberaku imprisoned. Aberaku pities the child and blames the adults behind him.

## entry: Hyperion's Dirge
@keys: Hyperion's Dirge, Helios-Forger
@keys2: Aberaku, Paimon, Traveler
@version: 2.4
@spoiler: minor
### STANDARD
A World Quest chain in Enkanomiya. The Traveler completes three trials (Narrow Inquiry, Temple Inquiry, Serpent's Heart Inquiry) to collect offerings that hold his remnant thoughts, offers them, and then reaches the top of the Dainichi Mikoshi, where he recalls everything and gives them the Divine Bridle.

## entry: Shade of Tokoyo
@keys: Shade of Tokoyo, Sinshade, afterimage
@keys2: Aberaku, Enkanomiya
@version: 2.4
### STANDARD
Aberaku is the example given by the wiki of a Shade of Tokoyo: a translucent humanoid figure without features whose memory and emotion linger in the leylines after death, and who appears during Evernight.
