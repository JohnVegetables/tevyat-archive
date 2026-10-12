---
{
  "id": "system.burning",
  "entity_type": "system",
  "subdir": "elemental-reactions",
  "name": "Burning",
  "aliases": ["Burning reaction", "Burning aura"],
  "summary_line": "Burning is the elemental reaction between Pyro and Dendro: a lingering fire that deals Pyro damage over time while it consumes the Dendro on its target.",
  "introduced_in": "1.0",
  "spoiler_level": "none",
  "availability": "permanent",
  "related": [
    "system.elemental-reaction", "system.pyro", "system.dendro", "system.bloom", "system.hyperbloom", "system.burgeon",
    "system.quicken", "system.elemental-mastery", "system.elements", "system.electro-charged", "system.crystallize"
  ],
  "facts": {"system_type": "reaction", "lore_status": "gameplay_abstraction"},
  "uncertainties": [
    {"topic": "In-universe explanation of Burning", "classification": "unknown", "note": "Burning is documented as a combat rule. The wiki page read gives no character's in-world account of it, so the entry stays at the level of what the game shows."}
  ],
  "sources": [
    {"title": "Burning", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Burning", "accessed": "2026-10-12", "confidence": "high", "section": "Overview; Damage; Immunity; Environment; Change History", "version": "1.0"},
    {"title": "Bloom", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Bloom", "accessed": "2026-10-12", "confidence": "high", "section": "Dendro Core (Burgeon)", "version": "3.0"},
    {"title": "Elemental Reaction", "type": "wiki", "url": "https://genshin-impact.fandom.com/wiki/Elemental_Reaction", "accessed": "2026-10-12", "confidence": "high", "section": "Overview table"}
  ],
  "status": "drafted",
  "last_verified": null
}
---

## summary
### LITE
Burning is what happens when Pyro and Dendro meet on a target, in either order. It sets the target alight: fire damage over time, a small burst of flame around them, and a flaming aura that lasts while the Dendro on the target lasts. Plants and grass catch fire the same way.
### STANDARD +
The fire consumes the Dendro as it burns, so it goes out when the plant energy is spent. The wiki lists Burning as a Transformative reaction.

## in_universe
### LITE
Canon offers no in-world explanation. Burning appears in tutorials and combat, not in character dialogue in the sources read. Treat it as a gameplay abstraction that a scene may borrow from.
### STANDARD +
The wiki's Environment section ties it to the open world: Wood objects such as grass, haystacks, shrubs, small trees, crates and barrels burn when Pyro touches them, and a burning creature spreads flame to combustible things it touches.

## gameplay
### LITE
Gameplay (not literal lore): applying Pyro to a Dendro-affected target, or Dendro to a Pyro-affected one, triggers Burning. It deals area Pyro damage and applies 1 gauge unit of Pyro within a 1 m radius to players and enemies, with a 2 second internal cooldown on that Pyro application. The Burning aura looks like an animated Pyro aura and coexists with the underlying Pyro and Dendro auras.
### STANDARD +
- The Dendro aura is steadily consumed during Burning. The state needs both the Burning aura and the Dendro aura, and ends when either runs out.
- Burning cannot damage off-field characters. Switching away pauses the damage ticks but not the Dendro consumption; if the character returns while still affected by Dendro, they resume taking damage.
- For effects that trigger on reactions, such as the Scroll of the Hero of Cinder City artifact set and Nahida's Seeds of Skandha, refreshing a Burning aura with more Pyro or Dendro does not count as triggering Burning again.
### LARGE +
- Immunity: some enemies are immune to Burning damage, including its Poise damage and Pyro application, even when not immune to Pyro itself. The wiki lists Pyro Slimes (and Large Pyro Slimes), Pyro Specters, the Pyro Hilichurl Shooter, Hilichurl Berserker, Hilichurl Grenadier, Pyro Whopperflower, Blazing Axe Mitachurl, Pyro Abyss Mage, Abyss Lector: Fathomless Flames, the Pyro Hypostasis and the Pyro Regisvine. Every Burning-immune enemy has Pyro in some form, but not every Pyro enemy is immune; the Fatui Skirmisher - Pyroslinger Bracer is the wiki's example.
- Environment: burning grass deals damage by the grass's own level; burning bushes deal none but still apply Pyro; other burning objects deal damage using the stats of the character who set them alight. Burned grass is charred and cannot be burned again until the area resets, while shrubs and small trees are temporarily destroyed. Pyro objects such as lit bonfires and stoves can be set to Burning by applying Dendro.
- Tri-Lakshana creatures that are not enemies are Dendro objects. They react with Hydro and Electro as Bloom and Quicken, but Pyro simply strips their Dendro status without causing Burning.
- Damage is Transformative: it comes from the triggering character's level and Elemental Mastery and is resisted by the target's Pyro RES.
### ULTRA +
Talents, constellations and artifact sets exist that raise Burning damage, reduce Pyro RES against it, or let it critically strike; the wiki holds them in category tables, which this entry does not copy.

## relation_to_bloom
### LARGE
Burning is separate from Burgeon, the Pyro-on-Dendro-Core reaction in the Bloom family. Burning needs Dendro on a target; Burgeon needs a Dendro Core, which only Dendro meeting Hydro (Bloom) creates.

## roleplay
### STANDARD
Roleplay interpretation (this project's recommendation, not canon text): show Burning as stubborn fire clinging to something green: leaves curling and blackening, sparks dropping from a smouldering target, grass flaring along the path of a burning enemy. It feeds on the plant energy and dies when that is gone.
### LARGE +
Make the stakes physical and local: spreading fire in a meadow, scorched earth, an enemy who stops burning when its leafy covering is consumed. Do not have a Pyro user ignite stone, water, or a person's body without a canon reason.

## examples
### STANDARD
An archer's Dendro arrow sticks to a hilichurl's wooden shield. A fire-slime spark touches it and flames climb the grain, spilling onto the dry grass around it.
### LARGE +
Since a burning creature spreads fire to grass it touches, a chase through a meadow plausibly leaves a trail of ash behind it.

## limits
### STANDARD
Burning requires both Pyro and Dendro; Anemo, Geo, Hydro, Electro and Cryo do not cause it. Do not describe it as an instant burst; its identity is the continuing burn. A burning character who is switched off the field stops taking Burning damage until they return.
### LARGE +
Do not claim Burning affects every Pyro creature: many Pyro enemies are immune to it. Do not mix it up with Burgeon, which is a Bloom-family explosion.

## entry: Burning aura
@keys: Burning aura, Burning reaction
### STANDARD
The Burning aura is the flaming overlay created by the Burning reaction. It coexists with ordinary Pyro and Dendro auras and ends when either the Burning aura or the Dendro aura is used up. Refreshing it with more Pyro or Dendro does not count as another Burning reaction for reaction-triggered effects.

## entry: Burning immunity
@keys: Burning immunity, immune to Burning
### LARGE
Some Pyro-related enemies are immune to Burning damage, its Poise damage and its Pyro application: Pyro Slimes, Pyro Specters, certain Pyro hilichurls and mitachurls, Pyro Whopperflowers, Pyro Abyss Mages, the Abyss Lector: Fathomless Flames, the Pyro Hypostasis and the Pyro Regisvine. Not every Pyro enemy shares it.
