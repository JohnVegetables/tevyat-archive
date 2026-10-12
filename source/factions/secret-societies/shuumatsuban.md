---
{
  "id": "faction.shuumatsuban",
  "entity_type": "faction",
  "subdir": "secret-societies",
  "name": "Shuumatsuban",
  "aliases": ["Shiyuumatsu-Ban", "Shuumatsu-ban", "the Shuumatsuban"],
  "summary_line": "A secret ninja unit of Inazuma that answers only to the head of the Kamisato Clan and Yashiro Commissioner, now Kamisato Ayato; Sayu is its best-known member.",
  "nation": "location.inazuma",
  "introduced_in": "2.0",
  "spoiler_level": "minor",
  "availability": "permanent",
  "related": [
    "location.inazuma", "location.inazuma-city", "location.yashiro-commission-headquarters", "location.kamisato-estate",
    "faction.yashiro-commission", "faction.kamisato-clan", "faction.tenryou-commission",
    "character.kamisato-ayato", "character.kamisato-ayaka", "character.thoma", "character.sayu", "character.yae-miko",
    "quest.hangout-event-sayu", "quest.hangout-event-thoma"
  ],
  "facts": {
    "faction_type": "secret_society",
    "leaders": ["character.kamisato-ayato"],
    "leader_note": "Reports directly to the head of the Kamisato Clan, who is also the Yashiro Commissioner. Ayato inherited command after his father's death. Thoma says that under most circumstances nobody else has authority to inquire into the unit's business, though Ayato agreed to let Thoma bend that rule in one case.",
    "headquarters": null,
    "parent_org": "faction.yashiro-commission",
    "founded": null,
    "current_status": "Active and secret as of 7.1. No later story has changed its status in the sources checked.",
    "operating_areas": ["location.inazuma"]
  },
  "uncertainties": [
    {"topic": "Headquarters", "classification": "inferred", "note": "The wiki says the headquarters is a ninja village, citing an NPC (Nakanishi). No location is named or mapped, so no location id is given."},
    {"topic": "Duties such as espionage and assassination", "classification": "inferred", "note": "Canon states the unit handles matters 'inconvenient' to superiors, which includes ambushes, and that its ninja die on top-secret missions. The wiki's wider summary (espionage, intelligence gathering, assassination) is an interpretation."},
    {"topic": "Founding and size", "classification": "unknown", "note": "Canon gives no founding date, total headcount or internal ranks. Ayato's father led it before him."},
    {"topic": "Authority of Ayaka and Thoma", "classification": "inferred", "note": "The wiki says both have some authority over the unit. The sources only show Ayaka arranging for Kano Nana to watch over Sayu and Thoma being allowed to make inquiries with Ayato's consent."},
    {"topic": "Positions of Kazuaki and Kano Nana", "classification": "unknown", "note": "The wiki lists both as staff with unknown positions. Kazuaki is shown keeping the unit's stored belongings and informing Thoma; Kano Nana is possibly an instructor."},
    {"topic": "Sayu's age", "classification": "unknown", "note": "Official text calls her pint-sized and raised in the unit since childhood, but never states an age."}
  ],
  "sources": [
    {"title": "Shuumatsuban", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Shuumatsuban", "accessed": "2026-10-11", "confidence": "high", "section": "Activities, Membership, Members, Trivia", "version": "7.1"},
    {"title": "Sayu/Profile", "type": "in_game_profile", "url": "https://genshin-impact.fandom.com/wiki/Sayu/Profile", "accessed": "2026-10-11", "confidence": "high", "section": "Character Details, Character Stories 3 and 5, official introduction", "version": "2.0"},
    {"title": "Kamisato Ayato/Voice-Overs", "type": "in_game_voiceover", "url": "https://genshin-impact.fandom.com/wiki/Kamisato_Ayato/Voice-Overs", "accessed": "2026-10-11", "confidence": "high", "section": "More About Kamisato Ayato: IV and V", "version": "2.6"},
    {"title": "Ninken by the Shore", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Ninken_by_the_Shore", "accessed": "2026-10-11", "confidence": "high", "section": "Thoma's Hangout Event dialogue (Thoma, Kazuaki)", "version": "2.2"},
    {"title": "Inu Shoushou", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Inu_Shoushou", "accessed": "2026-10-11", "confidence": "high", "section": "Profile", "version": "2.2"},
    {"title": "A Mysterious Order", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/A_Mysterious_Order", "accessed": "2026-10-11", "confidence": "high", "section": "Sayu's Hangout Event: Sayu explains the unit's work", "version": "2.2"},
    {"title": "Shuumatsuban Suspicions", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Shuumatsuban_Suspicions", "accessed": "2026-10-11", "confidence": "high", "section": "Sayu's Hangout Event: forged order, Ayaka's account of Sayu's sensei", "version": "2.2"},
    {"title": "Shuumatsuban Operations", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Shuumatsuban_Operations", "accessed": "2026-10-11", "confidence": "medium", "section": "Elemental powder detail as summarised on the Shuumatsuban page; quest not read in full", "version": "2.2"},
    {"title": "The Replacement's Secret", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/The_Replacement%27s_Secret", "accessed": "2026-10-11", "confidence": "medium", "section": "Artificial cadaver technique as summarised on the Shuumatsuban page; quest not read in full", "version": "2.2"}
  ],
  "status": "drafted",
  "last_verified": null,
  "notes": "Thin entity: canon on the organisation is spread across Sayu's and Thoma's hangout quests, Ayato's voice-overs and Sayu's profile. No 6.x or 7.0-7.1 Shuumatsuban story content was found; the wiki search returned only Inazuma-era pages. Hangout quest versions (2.2) come from the wiki change-history tags."
}
---

## summary
### LITE
The Shuumatsuban is a secret unit of ninja in Inazuma, part of the Yashiro Commission's hidden side and answerable to the head of the Kamisato Clan, currently Kamisato Ayato. Most Inazumans do not know it exists. It takes on matters that are awkward for the higher-ups to handle openly. Its best-known member is Sayu, a sleepy young ninja who is far better at hiding from work than doing it.
### STANDARD +
The name is written 終末番 and glossed by the wiki as "End Squad". The wiki reports its informal slogan, taken from a fortune-slip series, as a promise to send in the Shuumatsu against traitors and criminals alike. Inazuma's safety is its stated concern, but it is neither public nor peaceful.

## structure
### LITE
There is no public structure. The unit reports to the Kamisato Clan head, who is also the Yashiro Commissioner. Beneath him are ninja and support staff, with most identities classified.
### STANDARD +
Ayato says the unit reports directly to the head of the Kamisato Clan, and it passed to him when his father died. Orders are carried by staff such as Ogawa, who delivers orders and receives reports on ambush missions. Kazuaki appears in Thoma's hangout looking after the unit's stored belongings, and Kano Nana is assigned to keep an eye on Sayu. Koharu, a Kamisato household servant, is a ninja in training. Members receive a monthly salary; Sayu's is 200,000 Mora.
### LARGE +
Authority beyond Ayato is informal. Thoma says nobody else may normally inquire into the unit's business, but Ayato agreed to let him do so once. The unit may also answer to others in exceptional circumstances. Ayaka is shown giving direction regarding Sayu. Retired figures such as Nakanishi and the ninken Taroumaru are named by the wiki as former members. Sayu's own sensei left the unit after she grew capable, and their present status is not stated.

## members
### LITE
Sayu is the best-known ninja. Other named ninja include Hisashi, Gaumaru and the ninken Inu Shoushou. Most members are orphans raised from a young age by the unit.
### STANDARD +
Ayato says the unit takes in orphans and raises them, which he considers the surest way of securing loyalty. Sayu was raised there since childhood and is very loyal despite her laziness. Dogs also serve: Inu Shoushou is a ninken in ninja attire, paired with a human partner. Identities are classified so thoroughly that members who die on top-secret missions are not publicly commemorated.
### LARGE +
Named active staff and ninja, per the wiki: Hisashi, Gaumaru, Kazuaki, Kano Nana, Ogawa, Koharu and an inspector named Sumire. Named former members: Furuta (Koharu's teacher), Nakanishi, the ninken Taroumaru and Ayato's late father. Ayaka and Thoma are not members but have some say. Treat the roster as incomplete.

## methods
### STANDARD
Ninjutsu and stealth, escape and concealment, and combat when needed. Sayu explains in her hangout that the unit deals with matters that are "inconvenient" to the higher-ups, and that this sometimes includes ambushing people. Ayato describes the unit as his means of resolving situations he cannot involve himself in directly. Ninken serve as partners.
### LARGE +
The wiki also records some trade skills. Members can make an elemental powder that is slightly toxic and can permanently blind if it gets in eyes. They can also build artificial corpses to fake a death, using raw meat, white-iron composite bones and Sea Ganoderma, dressed in the subject's clothing and burned so that only the clothes identify the body. One body takes about a day. A text attributed to the unit holds that a competent ninja never overlooks a mechanism in play. Ayato also uses the unit to deliver oddly chosen food to Thoma.

## goals
### STANDARD
Keep Inazuma safe and deal with threats, traitors and criminals without publicity, in service of the Kamisato Clan and the Yashiro Commission. Ayato describes his own work as being for all of Inazuma.

## relations
### STANDARD
Its closest tie is to the Kamisato Clan and Ayato, who commands it. Ayaka cares about Sayu's wellbeing and has arranged for Kano Nana to watch over her. Thoma deals with the unit with Ayato's consent. In Sayu's hangout, Ogawa is aghast when a client asks the unit to move against the Tenryou Commission.
### LARGE +
In Sayu's hangout, a forged Yashiro Commission order was used to send a ninja to ambush the Traveler. Ogawa delivered it to Sayu, who normally ignores orders, and she carried it out efficiently. The scheme was then traced back to its instigators and the Traveler and Sayu captured the man behind it.

## reputation
### STANDARD
Almost no one in Inazuma knows it exists, and fewer know that Sayu belongs to it. Those who do, mostly Kamisato Clan insiders and the Traveler, see it as loyal and efficient, if grim.

## secrets
### LARGE
The unit's existence, its members' identities and the fates of ninja killed on missions are all deliberately concealed. Inu Shoushou's owner was sent on a dangerous mission at sea and did not return; Kazuaki told Thoma and the Traveler as much.

## history
### STANDARD
Before Ayato, his father led the unit. Players first met it in Version 2.0 with Sayu's release, and its inner workings were shown in Sayu's and Thoma's hangout events (both tagged 2.2 on the wiki).
### LARGE +
Sayu's profile says she was trained by a sensei who left quietly once she could defend herself; she later earned a Vision. Ayaka thinks Sayu's laziness comes from that loss. Inu Shoushou waited by the shore near Konda Village for his owner until Thoma and the Traveler brought the owner's old training kunai in Thoma's hangout.

### ULTRA +
In the hangout, Ayaka explains that Sayu would have left the unit long ago if she had forgotten what her sensei hoped for her. She says she assigned Kano Nana partly to keep a promise to watch over Sayu's progress. Sayu herself insists that the unit would be the same with or without her, while others insist some missions only she can finish.

## status
### STANDARD
Active and still secret as of 7.1. No later story has changed its status in the sources checked.

## entry: Sayu in the Shuumatsuban
@keys: Sayu, Shuumatsuban, Shiyuumatsu-Ban
@keys2: ninja, nap, sleep, Kano Nana
@version: 2.0
### STANDARD
Sayu is the unit's "resident ninja" and is famous for avoiding work. She sleeps and hides to grow taller and has mastered escape and concealment techniques accordingly. When missions appear, she vanishes, and by the time she is found a more suitable ninja has been assigned. Her colleagues know that she will not betray the unit's principles or shirk truly important jobs. Ayaka has arranged for Kano Nana to keep an eye on her. Her own entry carries her full details.

## entry: Inu Shoushou
@keys: Inu Shoushou, Shoushou
@keys2: Shuumatsuban, ninken, Thoma, Konda Village
@version: 2.2
### STANDARD
A red Shiba ninken in ninja attire, with scarring near the left eye. He and his owner went on missions together until the owner left on a top-secret mission and never returned. Shoushou waited by the shore near Konda Village. Thoma and the Traveler eventually calmed him with the owner's old training kunai, which Kazuaki found in the warehouse. The unit agreed to cover his expenses.
### LARGE +
Thoma uses the episode to explain the unit's lot: its ninja face dangerous work, and those who die on top-secret missions are not commemorated. The story is told in Thoma's hangout event.

## entry: Ayato and the Shuumatsuban
@keys: Shuumatsuban, Shiyuumatsu-Ban
@keys2: Ayato, Yashiro Commissioner, Kamisato Clan head
@version: 2.6
### STANDARD
In his voice-overs Ayato says it is a secret unit reporting directly to the Kamisato Clan head, and it came to him after his father passed. It lets him act where he cannot appear himself. He adds that most members are orphans raised in the unit from childhood, which makes their loyalty close to guaranteed. In another line he hints that the unit is not his only resource.
