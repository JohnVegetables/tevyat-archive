---
{
  "id": "system.roleplay-physics",
  "entity_type": "system",
  "subdir": "physics",
  "name": "Physical laws and roleplay physics",
  "aliases": ["roleplay physics", "Teyvat physics", "physical laws of Teyvat"],
  "summary_line": "Guidance on how bodies, hazards, travel, healing, death and magic behave in Teyvat roleplay: grounded in canon examples, with canon and recommended interpretation kept apart.",
  "nation": null,
  "introduced_in": "1.0",
  "spoiler_level": "major",
  "availability": "mixed",
  "related": [
    "core.canon-rules", "system.vision", "system.elements", "system.stamina", "system.immortality", "system.teleport-waypoint",
    "cosmology.ley-lines", "cosmology.ley-line-disorder", "cosmology.irminsul", "cosmology.primordial-sea",
    "cosmology.ode-of-resurrection", "cosmology.four-shades", "cosmology.gnosis",
    "culture.medicine-in-teyvat", "creature.adepti", "creature.oceanid",
    "lore.curse-of-the-khaenriahns", "lore.prophecy-of-fontaine", "lore.eleazar",
    "npc.ronova", "npc.dainsleif", "character.qiqi", "item.wind-glider",
    "location.dragonspine", "location.fontaine", "location.natlan", "location.night-kingdom"
  ],
  "facts": {"system_type": "physics", "lore_status": "mixed", "element": null},
  "uncertainties": [
    {"topic": "Ordinary biology, ageing and lifespans", "classification": "unknown", "note": "Canon never states a human lifespan or sets out biological rules. This entry assumes ordinary human biology for ordinary people as a roleplay default, not as a canon statement."},
    {"topic": "How Teleport Waypoints work", "classification": "unknown", "note": "The wiki notes that canon is inconsistent: items and the map treat waypoints as teleportation devices, while some characters treat them as unexplained ancient devices. Teleportation by Ley Lines is hinted at but not explained."},
    {"topic": "Whether Statues of The Seven revive the dead", "classification": "noncanon", "note": "Reviving fallen characters at a Statue of The Seven is a game mechanic (alongside Teleport Waypoints and dishes). No story source was found treating it as literal in-world resurrection; this entry treats it as a gameplay abstraction."},
    {"topic": "Full effect of Fontaine's Primordial Sea after the 4.x story", "classification": "disputed", "note": "The wiki states the Primordial Sea is no longer a threat to Fontainians after Neuvillette's act of forgiveness, but this entry did not trace that to a specific in-game line; treat it as medium confidence."},
    {"topic": "Heat, pressure and other hazards without a Vision", "classification": "unknown", "note": "Canon shows a few hazards (Dragonspine cold, adeptal energy, Fontaine's water pressure) but gives no general system for them."}
  ],
  "sources": [
    {"title": "Fallen Character", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Fallen_Character", "accessed": "2026-10-12", "confidence": "high", "section": "Death, drowning and revival (gameplay mechanics)"},
    {"title": "Diving", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Diving", "accessed": "2026-10-12", "confidence": "high", "section": "Lore: Transoceanic Sourcewater, diving gear, water pressure", "version": "4.0"},
    {"title": "Sheer Cold", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Sheer_Cold", "accessed": "2026-10-12", "confidence": "high", "section": "Overview (Dragonspine and Snezhnaya)"},
    {"title": "Dragonspine", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Dragonspine", "accessed": "2026-10-12", "confidence": "high", "section": "Subzero Climate; Lore (Skyfrost Nail, Durin)", "version": "1.2"},
    {"title": "Ode of Resurrection", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Ode_of_Resurrection", "accessed": "2026-10-12", "confidence": "high", "section": "Ceremony; The Failed Ceremony; The Night Wars", "version": "5.0"},
    {"title": "Incandescent Ode of Resurrection", "type": "in_game_quest", "url": "https://genshin-impact.fandom.com/wiki/Incandescent_Ode_of_Resurrection", "accessed": "2026-10-12", "confidence": "medium", "section": "Natlan Archon Quest (cited via the Ode of Resurrection page)", "version": "5.0"},
    {"title": "Primordial Sea", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Primordial_Sea", "accessed": "2026-10-12", "confidence": "high", "section": "Overview: dissolution of Fontainians, Ichor, Sinthe", "version": "4.0"},
    {"title": "Prophecy of Fontaine", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Prophecy_of_Fontaine", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; History", "version": "4.0"},
    {"title": "Adeptus", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Adeptus", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Rite of Parting; adeptal energy and mortals; resurrection of Qiqi; esoteric techniques"},
    {"title": "Qiqi/Profile", "type": "in_game_profile", "url": "https://genshin-impact.fandom.com/wiki/Qiqi/Profile", "accessed": "2026-10-12", "confidence": "high", "section": "Personality; Appearance (zombie traits)", "version": "1.0"},
    {"title": "Ronova", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Ronova", "accessed": "2026-10-12", "confidence": "high", "section": "Intro; Profile (Ruler of Death, curse of immortality)", "version": "5.0"},
    {"title": "Khaenri'ah/History", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Khaenri%27ah/History", "accessed": "2026-10-12", "confidence": "high", "section": "Cataclysm: curse of immortality, Dainsleif's ring"},
    {"title": "Dainsleif", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Dainsleif", "accessed": "2026-10-12", "confidence": "high", "section": "Intro"},
    {"title": "The Seven", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/The_Seven", "accessed": "2026-10-12", "confidence": "high", "section": "Archon deaths; divine thrones; mortal Pyro Archons"},
    {"title": "Medicine in Teyvat", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Medicine_in_Teyvat", "accessed": "2026-10-12", "confidence": "high", "section": "Elemental powers; herbs; non-herbal treatments"},
    {"title": "Teleport Waypoint", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Teleport_Waypoint", "accessed": "2026-10-12", "confidence": "high", "section": "Lore (canonicity of waypoints, Ley Line travel, Katheryne)"},
    {"title": "Ley Lines", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Ley_Lines", "accessed": "2026-10-12", "confidence": "high", "section": "Overview"},
    {"title": "Ley Line Disorder", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Ley_Line_Disorder", "accessed": "2026-10-12", "confidence": "medium", "section": "Environmental hazards (gameplay-only effects)"},
    {"title": "Irminsul", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Irminsul", "accessed": "2026-10-12", "confidence": "high", "section": "Repository of memories; Descenders", "version": "3.0"},
    {"title": "Wind Glider", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Wind_Glider", "accessed": "2026-10-12", "confidence": "high", "section": "Story: invention by Leonard 2,600 years ago", "version": "1.0"},
    {"title": "Food", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Food", "accessed": "2026-10-12", "confidence": "high", "section": "Overview (food heals; gameplay)"},
    {"title": "Healing", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Healing", "accessed": "2026-10-12", "confidence": "medium", "section": "Overview (gameplay)"},
    {"title": "Night Kingdom", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Night_Kingdom", "accessed": "2026-10-12", "confidence": "high", "section": "Overview (creation by Yohualtecuhtin; Ode and Ancient Names)", "version": "5.0"},
    {"title": "Belyi Tsar", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Belyi_Tsar", "accessed": "2026-10-12", "confidence": "high", "section": "Infobox (killed during the cataclysm 500 years ago)"},
    {"title": "Dvalin", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Dvalin", "accessed": "2026-10-12", "confidence": "high", "section": "History (ingesting Durin's poisonous blood)", "version": "1.0"},
    {"title": "Barbatos", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Barbatos", "accessed": "2026-10-12", "confidence": "high", "section": "Weakest Archon (Abyss Mage quest); holding back against Signora (For a Reunion Without Tears)"},
    {"title": "For a Reunion Without Tears", "type": "in_game_event", "url": "https://genshin-impact.fandom.com/wiki/For_a_Reunion_Without_Tears", "accessed": "2026-10-12", "confidence": "medium", "section": "Homeward, He Who Caught the Wind event, part II (Version Luna V / 6.4)", "version": "6.4"}
  ],
  "status": "verified",
  "last_verified": "2026-10-12"
}
---

## summary
### LITE
This entry tells a narrator how physical reality works in Teyvat roleplay. The default is ordinary human biology and consequences: people eat, sleep, tire, are hurt and recover slowly, and death is permanent unless a specific canon mechanism applies. Visions, Archons, adepti and ancient powers are exceptions with limits. Game mechanics (health bars, respawning at a Statue of The Seven, instant fast travel) are abstractions, not literal in-world rules. Each section below separates what canon shows from this project's recommended reading.
### STANDARD +
Rule of thumb: when canon shows a rule, follow it; when canon is silent, assume the real-world answer for a pre-industrial setting with magic added only where a source supports it; never let a character do something because "it is a game".
### LARGE +
Labels used below: "Canon" is something a source shows; "Gameplay" is a mechanic that is not literal lore; "Recommended" is this project's roleplay interpretation, not canon text. Where a thing is open in canon, it is left open.

## ordinary_biology
### LITE
Canon: ordinary people in Teyvat are shown living as humans do: they work, eat, rest and fall ill. Recommended: treat ordinary NPCs and Vision holders alike as physically human, with normal needs for food, water, sleep and shelter. A Vision grants control over one element, not toughness, immunity or freedom from need.
### STANDARD +
Canon shows food and drink at the centre of daily life across the nations, and food is used to restore strength in the game. Recommended: hunger, thirst, fatigue and cold should matter on long journeys, and the narrator should avoid hand-waving them unless the scene is brief. Do not add specifics (calorie needs, sleep hours) as canon.
### LARGE +
The wiki's treatment of food as the main healing consumable is a gameplay abstraction; in a story a good meal comforts and restores energy but does not mend a serious wound. Recommended: eating and resting should help recovery in proportion, and exhaustion should lower a character's competence before it incapacitates them.

## ageing_and_lifespans
### STANDARD
Canon: no source gives a human lifespan. Ordinary people age. Long-lived beings exist but are not ordinary: the adepti are extremely long-lived or immortal by enlightenment; pure-blooded Khaenri'ahns were cursed with immortality; Pyro Archons, unlike other Archons, are mortals who age and die like humans.
### LARGE +
Adepti may choose the appearance of their human form: Madame Ping's old-woman look is described as her own choice, not ageing. Half-blooded humans such as Ganyu can qualify as adepti, but canon leaves their lifespans unstated. Recommended: do not state ages or lifespans for characters whose entries leave them null.
### ULTRA +
Ages and "how old" a character looks are separate. Recommended: for characters with Visions or divine blood, do not assume agelessness unless their own entry says so. Do not infer an Archon's age from appearance; Archon ages are tied to stories, such as Barbatos becoming Archon about 2,600 years ago after the fall of Decarabian.
## travel_and_communication
### LARGE
Canon: travel is physical in the world's setting. Wind gliders were invented, per legend, 2,600 years ago by a retired adventurer named Leonard after he failed to climb Pilos Peak, and let a user glide; the Teleport Waypoints and instant fast travel of the game are an abstraction (see teleportation). Recommended: journeys take days, and the narrator should name terrain, weather and stops.
### ULTRA +
Canon: letters, notices and word of mouth carry news; Katheryne of the Adventurers' Guild passes on commissions. Recommended: news takes time; a character should only know what they have learned by a plausible route, matching the knowledge rules in the canon-rules entry. Gliding costs stamina in gameplay, so it has limits. Recommended: a glider reduces fall danger but does not make someone fly.
## medicine_and_healing
### STANDARD
Canon: medicine in Teyvat mixes herbal remedies with more advanced care, including surgery, bandages, setting dislocations, injected medicines and some recognition of mental illness and therapy. Elemental power can heal: Barbara is a known Hydro healer and Jean has healed with Anemo. Manipulating the elemental energy in a body has been used experimentally to control Eleazar's symptoms and is not widespread.
### LARGE +
Recommended: healing by an elemental user speeds recovery of ordinary wounds but is not a reset; a lethal wound still needs time and care, and healing powers should be scarce, tiring and tied to a named character. Herbs and nursing are the common route.
### ULTRA +
Canon shows healing powers coexisting with long illnesses that no one cures quickly, such as Eleazar and Anna's ongoing treatments. Gameplay: healing numbers, food heals and team heals are abstractions and should not be quoted in a scene. Medicine varies by region (for example Liyue's herbal blends and Sumeru's Nilotpala Lotus for Eleazar patients). Recommended: do not apply one region's remedy as universal, and keep dosage and procedure vague rather than inventing exact medical detail.
## injury_and_recovery
### STANDARD
Canon shows wounds, scars, poisoning and illness, and that recovery takes time. Recommended: injuries stay with a character until they plausibly heal; an injured character fights worse, moves slower or rests; a serious wound is not erased between scenes.
### LARGE +
Gameplay: characters have HP and are healed by dishes, Statues of The Seven and talents; that is not how bodies work in a story. Recommended: describe injuries in prose (a bleeding gash, a limp), and let rest, treatment and time resolve them.
### ULTRA +
Canon includes injuries that are not purely physical: abyssal corruption, Durin's poisonous blood that Dvalin swallowed, and long-term erosion. Recommended: treat corruption and poison as ongoing conditions with their own cures or consequences, not as quick damage.
## death
### LITE
Canon: death is real and usually permanent. Gods and Archons can die: Decarabian fell, Rukkhadevata and the Belyi Tsar died in past struggles against the Abyss, and Ronova died during the story. Recommended: a character who dies in a roleplay stays dead unless a canon mechanism below applies and the story earns it.
### STANDARD +
Gameplay (not literal lore): a "fallen" character is revived at a Statue of The Seven, by a dish or by a constellation; if the whole party falls, it is restored at the nearest waypoint at low health. This is a rule of the game, not of the world. Recommended: do not treat death as a setback that resets; the narrator may fade to a rescue or a near-death, but should say so.
### LARGE +
Canon marks the importance of dying: the Rite of Parting is a funeral custom for the passing of an adeptus (the Wangsheng Funeral Parlor, which has handled it only a handful of times in three thousand years). Recommended: show grief, rites and consequences in scenes with a death.
### ULTRA +
Ronova, the Ruler of Death, governed the laws of death and could define its form for anyone or deny it, as she did with the curse of immortality on the Khaenri'ahns. After she exceeded the limits of her authority in Snezhnaya, Celestia recalled it and she was defeated and died. Archons' divine thrones can be passed on after death; destroying a throne requires the death of its Archon.

## resurrection
@spoiler: major
### LITE
Canon shows only a few bounded forms: the Natlan Ode of Resurrection, adepti raising Qiqi as a zombie, and the cursed immortality of the Khaenri'ahns. None is a general fix for death.
### STANDARD +
Qiqi was mortally wounded, then resurrected by the adepti as a zombie, which required sealing her in amber because the adeptal energy overwhelmed her. She has trouble keeping memories, has no sense of smell and no strong emotions, prefers cold, and her flesh decays in heat. Recommended: resurrection costs something lasting.
### LARGE +
The Ode of Resurrection, in Natlan, raises warriors with Ancient Names who died fighting the Abyss in the Night Warden Wars, only if the group achieved victory. The healing applies to fatal injuries only, not to earlier wounds or illness. The Pyro Archon enters the Sacred Flame to seek the dead and their Ancient Name in the Night Kingdom. When Kachina's Ode failed, Mavuika said Abyssal unrest in the Night Kingdom prevented her from finding Kachina; the Pilgrimage was suspended. Later, Mavuika drew on the Lord of the Night's power to extend the Ode's blessing to all Natlan's warriors, and after the Night Wars the ceremony was discontinued.
### ULTRA +
Recommended: in a scene, a resurrected person should show the mechanism's conditions and cost. Do not offer the Ode as a service outside its context, and do not extend it to Sumeru, Liyue or Fontaine characters. Canon leaves unanswered how much of a person returns, and whether those who are resurrected differ in any way.

## weather_and_environment
### LARGE
Canon: the world has real climate hazards. Dragonspine has a subzero climate where grass does not burn and the cold drains health over time unless one keeps warm; the wiki notes that Goulash and sources of warmth mitigate it. Snezhnaya has cold zones with a similar mechanic. Recommended: travel in extreme cold needs shelter, fire and food.
### ULTRA +
Dragonspine's climate changed when the Skyfrost Nail fell and destroyed a silver ley line tree, turning a verdant mountain into a frozen one, per the wiki's account of the Sal Vindagnyr ruins. Gameplay: the Sheer Cold gauge is a mechanic. Recommended: describe numbness, slowed movement and frostbite-like effects without numbers. Qiqi is cold-adapted by her undead nature and decays in heat; she is an exception, not a model for ordinary people. Ley Line Disorder (storms, icicles, lightning) is a Spiral Abyss and domain mechanic, so treat it as local ley line instability, not weather that follows a character. Recommended: weather should respect geography; avoid inventing blizzards in Liyue harbours or sandstorms in Mondstadt. Where an element shapes a nation, keep its effects to the feel of the land (see the element entries) rather than controlling the weather.
## elemental_damage
### LARGE
Canon: elemental power is real and dangerous. A Vision holder channels one element and can burn, freeze, shock or knock things around, but is still mortal. Recommended: describe elements through their physical effects (heat, cold, current, pressure, root and growth) rather than numbers.
### ULTRA +
Elements interact in canon-adjacent ways the game calls reactions, such as fire boiling water to steam or wind spreading a flame. The element entries and the elemental-reactions entry describe them; this entry only adds that damage to people should leave burns, chills or injuries, not a bar going down. Adeptal energy is harmful to ordinary humans; prolonged contact with adepti can overwhelm a human soul. Recommended: ordinary people near adepti or divine power should feel strain over time, not be harmed at once. Archon-level power is of a different order. Barbatos considers himself the weakest Archon because he does not exert control over his nation. Recommended: do not have Archons casually level cities, and keep the consequences of their power visible.
## water_and_pressure
### STANDARD
Canon: in Fontaine, the power of the Transoceanic Sourcewater lets Vision holders (and others such as the Traveler and Paimon) breathe and speak underwater. People without Visions rely on diving gear and specialised training. Archenoul says adapting to water pressure is a concern for non-Vision holders, which implies it is not for Vision holders. Outside that context there is no breathing-underwater rule.
### LARGE +
Recommended: elsewhere in Teyvat, drowning is real: swimming tires a person and cold water sucks heat. Gameplay: stamina and drowning mechanics are abstractions. In a scene, someone who goes into deep water without help should struggle quickly.
### ULTRA +
Fontaine's water is also lore-bearing: its humans were made from Oceanids using water from the Primordial Sea, and contact with pure Primordial Seawater of high concentration dissolves Fontainians into water, though non-Fontainians simply become more sensitive to Hydro. The wiki states that after Neuvillette's act this is no longer a threat. Remus's attempt to dilute Ichor to grant eternal life destroyed his nation, and diluted Primordial Seawater became the euphoric drug Sinthe. Recommended: after 4.x, treat Fontaine's water as ordinary water for Fontainians in everyday scenes; refer to the dissolution only when recounting the history or the prophecy. Do not apply Fontainian dissolution to non-Fontainians.
## explosions_and_structures
### LARGE
Canon shows deliberate and accidental destruction at human scale (bombs, collapses) and at divine scale (the Cataclysm, the Skyfrost Nail). Recommended: scale damage to the source. A bomb damages a wall, a room, or people near it; it does not level a city.
### ULTRA +
Recommended: buildings in Teyvat are stone, timber and plaster by region and can burn, collapse or flood; fire spreads through wood and dry grass, though not in Dragonspine's subzero climate. Ruin Guards and ancient machines are durable and need real force. Canon also shows lasting environmental damage from large events: the Skyfrost Nail's effect on Dragonspine, the Cataclysm's effects on Khaenri'ah and the Abyss's corruption of land. Recommended: major damage has aftermath, such as refugees, rebuilding or hazard zones.
## magic_and_limits
### LARGE
Canon: a Vision binds its holder to one element. Archons draw power from divine thrones, and Barbatos says Archons draw power from their control over their nations. Power has costs and limits; canon shows exhaustion, injury and consequences when it is overused.
### ULTRA +
Recommended: no one is all-powerful. A Vision holder tires and misses; an adeptus is strong but bound by agreements and responsibilities; a god is limited by authority, memory and other gods. Keep any power to what a character's own entry supports. Canon includes special techniques with specific rules: the adepti's "gifting of dreams and visions", Dream Trawler (which separates soul from body), and Mortal Lingering (a temporary vessel). Recommended: do not generalise these into powers for other characters. Anything on the order of the Heavenly Principles, Celestia or the Abyss is not a tool for an ordinary scene. Recommended: if a user asks for a god-level effect, show its price or have it blocked by a canon limit rather than granting it.
## teleportation
### LARGE
Canon is unclear. The game's Teleport Waypoints work as fast travel, but the wiki notes sources disagree on whether people in the world understand them: some items and the map treat them as teleportation devices, while some characters treat them as ancient devices of unknown purpose. Katheryne's own statements are ambiguous.
### ULTRA +
What does exist: the Fatui and Mona use teleportation in quests, and Leifhelm says his Grand Master crossed from Nod-Krai to Mondstadt quickly along the Ley Lines. The Ley Lines are a network of elemental energy and memories, and Portable Waypoints depend on their power. The Abyss has portals that Dainsleif describes as gateways to a network. Recommended: do not let characters teleport at will. Treat teleportation as rare, costly or tied to a device, a character's established power or an Abyssal portal. Fast travel in the game should be narrated as a journey, a lift on a trusted route, or a cut forward in time. Ley Lines are key: Irminsul and the Ley Lines record the memories of Teyvat, and Descenders have no records in Irminsul. Recommended: do not use the Ley Lines as a free transport system for the user's character.
## dimensional_boundaries
### LARGE
Canon contains separate realms: the Night Kingdom of Natlan (created by Yohualtecuhtin at Ronova's instruction to repair Natlan's Ley Lines), the adepti's own domains, Enkanomiya and the Abyss. Some are hard or dangerous to enter: mortals who enter adeptal land uninvited are considered brave or desperate.
### ULTRA +
Recommended: crossing into a realm needs a way in (a ritual, a key, a portal, an invitation) and carries a risk. Realms keep their own rules; do not import a character's powers from one into another. Canon shows that people and memory can be altered by changes to Irminsul without those affected noticing, and that people from outside Teyvat, including Descenders, have no record there. Recommended: treat changes to memory and records as story events with a source, not a convenience.
## roleplay
### LARGE
Recommended practice (not canon): default to consequence. Hunger, injury, cold, fatigue and death matter; powers have limits; travel takes time. When the user asks for something game-like (reviving, instant travel, healing in a fight), narrate it as a plausible in-world event or decline gently and offer an in-world alternative. Never contradict an established canon fact to make a scene easier.
### ULTRA +
Match tone to the scene: a warm tavern stay can skim travel and meals, while a survival scene should linger on cold, water and wounds. The aim is internal consistency, not realism for its own sake. When canon is silent, say so briefly or choose the most conservative reading; mark invented details as scene colour, never as lore. Respect the knowledge rules in the canon-rules entry: a character can only describe hazards they have met.
## limits
### STANDARD
This entry does not give a statistical system and does not replace character or location entries. Where an individual entry states a power, a condition or a lifespan, that entry takes priority over the general guidance here.

## entry: Ode of Resurrection
@keys: Ode of Resurrection, Rite of Resurrection
@spoiler: major
@version: 5.0
### STANDARD
The Ode of Resurrection is a Natlan ceremony at the Stadium of the Sacred Flame that raises Ancient Name bearers who died fighting the Abyss in the Night Warden Wars, provided their group achieved victory. It heals only fatal injuries. The Pyro Archon enters the Sacred Flame to seek the deceased and their Ancient Name in the Night Kingdom. It failed for Kachina; later Mavuika extended it to all of Natlan's warriors with the Lord of the Night's power, and it ended after the Night Wars.
### LARGE +
The singing of those present is part of the rite. Treat it as a bounded Natlan rite, not a general resurrection power.

## entry: Dragonspine cold
@keys: Sheer Cold, Subzero Climate
@keys2: Dragonspine, Snezhnaya
### STANDARD
Dragonspine, formerly Vindagnyr, has an extreme cold climate that built up after the Skyfrost Nail destroyed the ley line tree on the mountain. Grass does not burn there, and the cold weakens travellers over time unless they keep warm. Snezhnaya has comparable cold zones. Recommended: describe it as dangerous exposure requiring shelter, fire and food.

## entry: Transoceanic Sourcewater
@keys: Transoceanic Sourcewater, diving gear
@keys2: Fontaine, underwater
@version: 4.0
### STANDARD
In Fontaine, the Transoceanic Sourcewater lets Vision holders, the Traveler and Paimon breathe and speak underwater. People without Visions use diving gear and specialised training, and water pressure is a concern for them. Do not carry this over to other nations.

## entry: Curse of immortality
@keys: curse of immortality
@keys2: Khaenri'ah, Khaenri'ahn, Dainsleif, Ronova
@spoiler: major
### STANDARD
During the Cataclysm, Ronova placed a curse of immortality on pure-blooded Khaenri'ahns, which the wiki describes as a punishment. Dainsleif is also immortal; his brother Vedrfolnir gave him a ring that continuously resets his body's condition, but his mind is still affected by erosion. Immortality in canon is a burden, not a reward.

## entry: Teleportation limits
@keys: Teleport Waypoint, teleportation, fast travel
@keys2: Katheryne, Ley Lines, Leifhelm
### STANDARD
Canon is unclear about how Teleport Waypoints work. Leifhelm says his Grand Master crossed from Nod-Krai to Mondstadt along the Ley Lines quickly, and the Fatui and Mona use teleportation in quests. Recommended: treat teleportation as rare and tied to a device or power.

## entry: Zombie condition
@keys: Qiqi, zombie, adeptal energy
@keys2: resurrect, resurrected, undead
### STANDARD
Qiqi was resurrected as a zombie by the adepti after being mortally wounded, and sealed in amber because the energy was too much for her. She has trouble retaining memories, lacks a sense of smell, shows little emotion, prefers cold and decays in heat. Use this as the template for how canon treats the cost of resurrection.

## entry: Archon restraint against Signora
@keys: Signora
@keys2: Venti, Barbatos, Anemo Archon, Gnosis
@version: 6.4
@availability: limited
### ULTRA
During the 6.4 limited-time event "Homeward, He Who Caught the Wind", Venti said he had deliberately held back when Signora ambushed him for the Gnosis, because fighting her at greater strength would likely have destroyed the city. Recommended: use this as the canon model for Archons limiting their power near people, not as proof of exact strength.
