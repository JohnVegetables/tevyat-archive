---
{
  "id": "faction.snezhnograd-veche",
  "entity_type": "faction",
  "subdir": "nations-and-governments",
  "name": "Snezhnograd Veche",
  "aliases": ["the Veche", "Veche", "Snezhnogradskoye Veche"],
  "summary_line": "Snezhnaya's legislative assembly in Snezhnograd: founded by the Tsaritsa to replace the fae princes' rule, it votes by majority under a Speaker, currently Harbinger Pulcinella, with the Fatui dominant.",
  "nation": "location.snezhnaya",
  "introduced_in": "6.1",
  "spoiler_level": "major",
  "availability": "permanent",
  "related": [
    "location.snezhnaya", "location.snezhnograd", "location.snezhnograd-veche-state-hall", "location.zapolyarny-palace",
    "location.glupov", "location.armory-palace", "location.nod-krai",
    "npc.tsaritsa", "npc.pulcinella", "historical.i-ivanovna-n", "npc.pantalone", "character.tartaglia", "character.sandrone",
    "npc.pierro", "npc.chugunov", "character.vesna", "character.vodyanitsa", "character.odette", "character.alyosha",
    "character.arlecchino", "npc.ronova",
    "faction.fatui", "faction.eleven-fatui-harbingers", "faction.rokot", "faction.druzhna", "faction.royal-energy-commission",
    "faction.northland-bank", "faction.house-of-the-hearth", "faction.hexenzirkel", "faction.korolevskiy-troupe",
    "creature.snowland-fae", "creature.domovoy", "creature.vila", "historical.belyi-tsar",
    "lore.project-stuzha", "lore.project-mistilteinn", "lore.cataclysm", "item.a-brief-history-of-the-pale-starborn",
    "quest.everwinter-without-mercy", "quest.wraiths-nocturne", "quest.a-rekviem-for-the-underworld", "system.kresnik-kristall"
  ],
  "facts": {
    "faction_type": "government",
    "leaders": ["npc.pulcinella"],
    "leader_note": "Pulcinella (the Rooster, Fifth Harbinger) is Speaker, also called Presiding Member. The first chairperson was the human Ioanna Ivanovna N., his teacher and predecessor.",
    "headquarters": "location.snezhnograd-veche-state-hall",
    "parent_org": null,
    "founded": "In the sixth year of the 799th Cycle, shortly after the Tsaritsa took the throne following the Cataclysm about 500 years ago",
    "current_status": "Active as of 7.1. Its Project Stuzha energy-rationing policy was voted to continue in 7.0, then suspended while Ronova's Curse of Death blocked Fatui research. The wiki says it resumes after Ronova lost her Authority in 7.1, but no new vote has been shown.",
    "operating_areas": ["location.snezhnaya", "location.snezhnograd"]
  },
  "uncertainties": [
    {"topic": "Size, seat counts and electoral basis", "classification": "unknown", "note": "Canon never states how many seats the Veche has, how councillors are chosen, or how long a Veche period lasts. Known pieces: some seats are reserved by family or class (Vesna's profile says only a few are reserved for House Strivozha, fewer than those allotted to the merchant class), and members speak for interest groups such as finance, the Fatui soldiery, and the Armory Palace's engineers."},
    {"topic": "Whether Project Stuzha resumes after 7.1", "classification": "inferred", "note": "Pierro says the project was a step toward Mistilteinn and would resume once Ronova's Authority was revoked, and the Project Stuzha wiki page repeats this. No 7.0-7.1 content found shows a Veche vote after the suspension."},
    {"topic": "How far Veche law reaches Nod-Krai", "classification": "unknown", "note": "Nod-Krai was granted autonomy in the Tsaritsa's reign. Councillor Euphrosiniya recounts how her ancestor, the Trubetskoy governor, gave up his claim to it. No 6.x content found shows the Veche acting there."},
    {"topic": "Real power versus formal power", "classification": "disputed", "note": "The wiki calls the Veche nominally deliberative, with the Fatui implementing their preferred policy with little meaningful resistance. Characters inside it describe it as the place where policy is actually steered: Sandrone says a voice in the Veche is the only way to steer policy in one's favour."},
    {"topic": "Exact date of founding", "classification": "strongly_supported", "note": "A Brief History of the Pale Starborn dates it to the sixth year of the 799th Cycle. The book's own trivia notes a cycle is seven years, but how that maps to calendar years is not given in the pages checked."},
    {"topic": "Earliest in-game appearance", "classification": "unknown", "note": "The wiki lists the Veche as introduced in Luna II (6.1). The first text I could read that shows it in action is the 7.0 Archon Quest chapter, and the founding history is in a Luna IV (6.3) book."}
  ],
  "sources": [
    {"title": "Snezhnograd Veche", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Snezhnograd_Veche", "accessed": "2026-10-11", "confidence": "high", "section": "Overview, Known Members", "version": "7.1"},
    {"title": "A Brief History of the Pale Starborn", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/A_Brief_History_of_the_Pale_Starborn", "accessed": "2026-10-11", "confidence": "high", "section": "Founding of the Veche and Glupov, 799th Cycle", "version": "6.3"},
    {"title": "Silence Alone is Disfavored", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Silence_Alone_is_Disfavored", "accessed": "2026-10-11", "confidence": "high", "section": "Veche session on Project Stuzha", "version": "7.0"},
    {"title": "Gunfire in the Silent Lands", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Gunfire_in_the_Silent_Lands", "accessed": "2026-10-11", "confidence": "high", "section": "Alyosha explains Project Stuzha and the Veche", "version": "7.0"},
    {"title": "Great Deeds on the Tundra", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Great_Deeds_on_the_Tundra", "accessed": "2026-10-11", "confidence": "high", "section": "Sandrone on interest groups in the Veche", "version": "7.0"},
    {"title": "Mistilteinn", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Mistilteinn", "accessed": "2026-10-11", "confidence": "high", "section": "Stuzha suspended, Lelek withdrawn", "version": "7.0"},
    {"title": "Project Stuzha", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Project_Stuzha", "accessed": "2026-10-11", "confidence": "medium", "section": "Overview, resumption after Ronova's Authority is revoked", "version": "7.1"},
    {"title": "Rokot", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Rokot", "accessed": "2026-10-11", "confidence": "medium", "section": "Overview, Members", "version": "7.0"},
    {"title": "I. Ivanovna N.", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/I._Ivanovna_N.", "accessed": "2026-10-11", "confidence": "high", "section": "Story", "version": "3.5"},
    {"title": "Glory to Your Legacy", "type": "in_game_item", "url": "https://genshin-impact.fandom.com/wiki/Glory_to_Your_Legacy", "accessed": "2026-10-11", "confidence": "high", "section": "Pulcinella's apprenticeship under the Mayor and Speaker", "version": "6.1"},
    {"title": "Pulcinella", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Pulcinella", "accessed": "2026-10-11", "confidence": "high", "section": "Story: Present Day", "version": "7.1"},
    {"title": "Anastasya", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Anastasya", "accessed": "2026-10-11", "confidence": "medium", "section": "History: replacement of the fae aristocracy", "version": "7.1"},
    {"title": "Snezhnograd Veche State Hall", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Snezhnograd_Veche_State_Hall", "accessed": "2026-10-11", "confidence": "high", "section": "Map description, NPCs", "version": "7.0"},
    {"title": "Euphrosiniya", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Euphrosiniya", "accessed": "2026-10-11", "confidence": "high", "section": "NPC dialogue", "version": "7.0"},
    {"title": "Golitsyn", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Golitsyn", "accessed": "2026-10-11", "confidence": "high", "section": "NPC dialogue", "version": "7.0"},
    {"title": "Eteri", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Eteri", "accessed": "2026-10-11", "confidence": "high", "section": "NPC dialogue", "version": "7.0"},
    {"title": "Vesna/Profile", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Vesna/Profile", "accessed": "2026-10-11", "confidence": "high", "section": "Character Stories (reserved Veche seats, House Strivozha)", "version": "7.1"},
    {"title": "Version/7.1", "type": "official_announcement", "url": "https://genshin-impact.fandom.com/wiki/Version/7.1", "accessed": "2026-10-11", "confidence": "high", "section": "New content (Vesna, Vodyanitsa; no new Veche story)", "version": "7.1"}
  ],
  "status": "verified",
  "last_verified": "2026-10-12"
}
---

## summary
### LITE
The Snezhnograd Veche (Snezhnogradskoye Veche, "the Veche") is Snezhnaya's legislative assembly. It sits in the Veche State Hall in Snezhnograd and decides matters by majority vote in sessions chaired by a Speaker. The Tsaritsa founded it to take over the administration once the fae princes' rule ended. The Speaker is the Fatui Harbinger Pulcinella, and the Fatui steer most of its decisions.
### STANDARD +
The word "veche" belongs to medieval Russian tradition, where it names a public assembly that debated and decided key matters. In Snezhnaya the body has kept the name and the procedure, but its members are mostly the powerful: Harbingers, nobles, merchants and officials, each speaking for an interest group.

## structure
### STANDARD
Sessions are chaired by a Speaker, who opens the floor, manages motions and calls the final vote. Business follows a pattern: officials present reports, representatives speak in turn, a proposal is drafted or amended, then the members vote and the Speaker announces the result by percentage. Policies are set for a Veche "period" and stay in force until the next one. A new proposal follows "the usual procedure" and is raised as a motion at a later session. Visitors may attend from the audience seats if arranged in advance, but they cannot speak.
### LARGE +
Seats are tied to groups rather than to a single electorate. Sandrone describes a room where each person represents an interest: Pantalone the financial sector, Tartaglia the Fatui soldiers, Sandrone her engineers and researchers, and Pulcinella "politics" itself. Some seats are reserved by family or class: Vesna's profile says only a few are reserved for House Strivozha, fewer even than those allotted to the merchant class. Councillors can hold titles such as Privy Councillor, and the State Hall also has a Privy Advisor. Specialist bodies report into it, as when the Energy Commission supplies regional consumption statistics.
### ULTRA +
The Veche's procedure leans on documentation. At the 7.0 session, reports were handed out as printed industry reports, and the Speaker pointed members to them for detail. A financial report on disaster relief was attached by Pantalone. Public discussion is part of the culture: a street-stall newspaper, "Bring Out the Kvass!", covers sessions in a sensational tone, and its reporter Mironova says she sits in to meet interview quotas. The Speaker closes sessions with a standing line: "We debate only for the greater glory and solidarity of our nation. May the aurora shine ever on and the tundra always stand firm."

## leadership
### LITE
The Speaker is Pulcinella, the Fifth Fatui Harbinger, "the Rooster", who is also Mayor of Snezhnograd and of Glupov. Members call him "Lord Rooster" at sessions.
### STANDARD +
The first Speaker, also the first Mayor of Snezhnograd, was the human Ioanna Ivanovna N., a former Hexenzirkel witch who was appointed by the Tsaritsa and later became Pulcinella's teacher. Sandrone calls Pulcinella the linchpin of the Veche, because everything involves him and he knows how to mediate any issue, which she says is what the Tsaritsa values most in him. Councillor Euphrosiniya complains that he finds excuses to dismiss her heating proposals, while Councillor Golitsyn says his house stands with the Rooster.
### ULTRA +
Pulcinella's own account of his rise ties the posts together: he was told to "report to the Mayor" when he applied to the Fatui, and the Mayor was also Speaker. A fae apprenticed to a human was read publicly as the Tsaritsa warning the old order. Ivanovna's high opinion of him made him her likely successor, and after her death centuries ago he came to hold both offices. Vesna's profile has him telling her that she might one day take a seat as the youngest councillor, one of the paths he described to her before the Tsaritsa gave her a Druzhna badge instead.

## members
### STANDARD
Known members and speakers in the 7.0 and 7.1 story:
- **Pulcinella**: Speaker.
- **Pantalone** ("the Regrator"): finance and the Northland Bank.
- **Tartaglia**: speaks for the Fatui soldiers. He privately sympathises with Stuzha's critics and keeps raising concerns, but says he has held back from casting a dissenting vote because the Tsaritsa would never let him get away with it.
- **Sandrone** ("the Marionette"): speaks for engineers and researchers.
- **Euphrosiniya Ignatyevna Trubetskaya** ("Euphie"): Privy Councillor and head of House Trubetskoy. She has put forward at least five proposals for heating in the town of Zolnyy.
- **Eteri Vsevolodovna Strivozha**: Vila councillor, descendant of Saint Strivozha, and nostalgic for the Belyi Tsar's age.
- **Andrei Dmitrievich Golitsyn**: second-rank noble, Active Privy Councillor.
### LARGE +
Other voices at the 7.0 session include the industrialist Chugunov, owner of the Iskra plant, the finance scholar Arapov, the Energy Commission's Sharova, and Akvilina, who spoke on behalf of the Druzhna commander Vesna. The wiki says Harbingers are commonly entitled to take part in sessions.

## goals
### STANDARD
Officially the Veche exists to handle the administrative issues that arose when the fae princes lost their power. In practice its work under Pulcinella is steering national policy, above all the long Project Stuzha energy-rationing program. In the story, members argue over the fairness of distribution, the interests of factories and soldiers' families, and whether the Fatui's central planning is sustainable.

## methods
### LARGE
Debate and pressure. Alyosha says opposition has been growing, but detractors end up caving to political pressure from the Rooster. The Fatui hold the advantage of already running Kristall shipments, and at the 7.0 session Tartaglia proposed that the Fatui collect regional data on that basis, with the Druzhna supervising. The Speaker backed drafting a proposal but questioned whether basing quotas on local data was safe in the long term. Opponents win only by flipping votes: the Rokot's Lelek did so through threats, coercion and bribery.
### ULTRA +
Sessions stay orderly even when tempers rise: when Tartaglia slammed the table over Kristall allocation, Pantalone answered coolly and the Speaker steered the floor on to the next point. The press and civilian groups sit at the edge of the process. Vodyanitsa notes that the public sees no tangible benefit from the reports on the table, and Alyosha gets the Traveler in as a guest through arrangement rather than right.

## history
### LARGE
**Founding.** About 500 years ago the Belyi Tsar died in the Cataclysm and Anastasya succeeded as the Cryo Archon. A Brief History of the Pale Starborn records that in the sixth year of the 799th Cycle she set up the Snezhnograd Veche to handle the administrative issues caused by the princes' absence, with the human Ioanna Ivanovna as its first chairperson. The next year she issued the Imperial Order Reformation Edict, after which many princely fae gave up their titles and left.

**Project Stuzha.** The Veche is the body that passes Project Stuzha, the energy reforms that limit public consumption so power can be redirected to the Armory Palace. The project was meant to last about six months but has been extended repeatedly, each time by majority vote.
### ULTRA +
**The 7.0 session.** The Traveler sat in as a visitor in Silence Alone is Disfavored. The Speaker reported that energy commitments had been met, blamed recent blizzards on a remote monster, and opened debate. Tartaglia said Fatui families in remote areas receive 15% less Kristall than a typical Snezhnograd family, while Pantalone replied that fairness is relative and asked about broken equipment and an outdated census. The final vote to continue Stuzha passed with 61%, narrower than before, after the industrialist Chugunov voted against.

**After the vote.** When Lelek's actions came to light in Mistilteinn, the Rokot withdrew the codename. Project Stuzha was suspended while Ronova's Curse of Death blocked the Fatui's technology breakthroughs. In that suspension Euphrosiniya says the councillors still quarrel over small sums for the poor of Zolnyy. In 7.1 Ronova lost her Authority, and the wiki states the project resumes.

## relations
### LARGE
- **The Tsaritsa**: founder and ultimate authority. Members speak of acting in her name.
- **The Fatui**: dominant. Harbingers sit in the Veche, and Tartaglia presses the case of Fatui soldiers and their families.
- **Rokot**: an anonymous civilian society that opposed Project Stuzha through evidence, leaks and, in Lelek's case, pressure on voters.
- **Druzhna**: the Tsaritsa's guard is represented in debates, as when Akvilina spoke for Commander Vesna.
### ULTRA +
- **The old houses**: Vila and human houses (Strivozha, Trubetskoy, Golitsyn) hold seats. They differ widely: Eteri longs for the Belyi Tsar's age, Euphrosiniya criticises Pulcinella, and Golitsyn defends order and Project Stuzha.
- **Business and industry**: factory owners such as Chugunov have seats and an interest in energy supply. Vodyanitsa had planned to turn Chugunov against Stuzha by showing him the penalties his Iskra plant would face, but someone forced his vote first.

## reputation
### ULTRA
Paimon remarks that the Veche argues about Project Stuzha every day, and Sandrone says it is basically all anyone there cares about. Vodyanitsa calls the sessions repetitive and notes a general lack of trust. Mironova's paper treats Lelek as a hero. Euphrosiniya and the Rokot see the body as unresponsive, while Golitsyn and Pantalone defend it as an orderly framework. Sandrone says the factional strife, whether open or unspoken, plays out for all to see in that one small room.

## status
@version: 7.0
### LITE
As of 7.1 the Veche continues to meet under Speaker Pulcinella. Project Stuzha was kept going in 7.0, then paused.
### STANDARD +
After Ronova lost her Authority in 7.1 the wiki says Project Stuzha resumes, though no vote has been shown. No new Veche story was found in the 6.x Nod-Krai content or in 7.1 beyond this context, and no change of Speaker is known.

## entry: The Speaker and the Rooster
@keys: Speaker of the Veche, Presiding Member, Lord Rooster, the Rooster
@keys2: Veche, Snezhnograd, Pulcinella
### STANDARD
At Veche sessions the Fatui Harbinger Pulcinella is addressed as "The Rooster" or "Lord Rooster". As Speaker he reports statistics, calls "Order", opens and closes the floor, supports the drafting of proposals, and announces votes. He ends sessions with a standard line about debating "only for the greater glory and solidarity of our nation".

## entry: Ioanna Ivanovna N.
@keys: Ioanna Ivanovna, Ivanovna, Tricksy-Witch
@keys2: Veche, Mayor of Snezhnograd, Pulcinella, Hexenzirkel
### STANDARD
The Veche's first chairperson was a human named Ioanna Ivanovna N., codename "J". She was a member of the Hexenzirkel with no magic or combat training, left the witches after marrying, and was appointed by the Tsaritsa as the first Mayor of Snezhnograd and Speaker. She mentored Pulcinella, and Golitsyn credits her grace for his house's standing. She died centuries ago, and in the Hexenzirkel story her line of followers continues.

## entry: Project Stuzha and the Veche vote
@keys: Project Stuzha, Stuzha
@keys2: Veche, Pulcinella, Pantalone, Tartaglia, Kristall
@version: 7.0
@spoiler: major
### STANDARD
Project Stuzha is a set of energy reforms passed by the Veche that cut household and factory use of Kresnik Kristall so that energy can be sent to the Armory Palace. It was intended to last about six months but was extended repeatedly by majority vote, and the 7.0 vote kept it with 61%. Pierro later reveals it served Project Mistilteinn, the Tsaritsa's weapon against the Heavenly Principles using Stellar Linchpins.
### LARGE +
Supporters call it a resource-distribution framework, not the cause of shortages. Critics point to cold towns, shortfalls for soldiers' families and the lack of visible benefit. The project was suspended when Ronova's Curse of Death stopped the research and, per the wiki, resumes after 7.1's revocation of her Authority.

## entry: Rokot and Lelek in the Veche
@keys: Rokot, Lelek
@keys2: Veche, Stuzha, Odette, Alyosha, Vodyanitsa
@version: 7.0
@spoiler: major
### LARGE
The Rokot is an anonymous society that works for ordinary people and opposed Project Stuzha. Its codenamed members use mostly peaceful methods, such as publishing evidence of corruption. The codename Lelek, held by Odette, used threats, coercion and bribery to flip Veche votes, turning Chugunov and narrowing the margin to 61%. In Mistilteinn the Rokot withdrew the codename and suspended its holder.

## entry: Snezhnograd Veche State Hall
@keys: Veche State Hall, State Hall, Snezhnograd Veche State Hall
@keys2: Veche, Snezhnograd
@version: 7.0
### STANDARD
The Snezhnograd Veche State Hall is where the Veche holds its regular meetings. Its map description says citizen representatives from various groups deliberate on newly issued laws, in a tradition kept from Snezhnaya's early days, and that it is presided over by "The Rooster". In the hall are the councillors Eteri and Euphrosiniya and the Privy Advisor Golitsyn.
