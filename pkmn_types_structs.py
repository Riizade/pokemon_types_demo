from typing import Dict
from dataclasses import dataclass

from pkmn_type_enum import *


@dataclass(frozen=True)
class PKMNTypeMultipliers:
    multipliers: Dict[PokemonType, float]

# https://bulbapedia.bulbagarden.net/wiki/Type/Type_chart#Generation_I
NORMAL_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 1.0,
        POISON: 1.0,
        GROUND: 1.0,
        ROCK: 0.5,
        BUG: 1.0,
        GHOST: 0.0,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 1.0,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

FIGHTING_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 2.0,
        FIGHTING: 1.0,
        FLYING: 0.5,
        POISON: 0.5,
        GROUND: 1.0,
        ROCK: 2.0,
        BUG: 0.5,
        GHOST: 0.0,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 1.0,
        ELECTRIC: 1.0,
        PSYCHIC: 0.5,
        ICE: 2.0,
        DRAGON: 1.0,
    }
)

FLYING_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 2.0,
        FLYING: 1.0,
        POISON: 1.0,
        GROUND: 1.0,
        ROCK: 0.5,
        BUG: 2.0,
        GHOST: 1.0,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 2.0,
        ELECTRIC: 0.5,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

POISON_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 1.0,
        POISON: 0.5,
        GROUND: 0.5,
        ROCK: 0.5,
        BUG: 2.0,
        GHOST: 0.5,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 2.0,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

GROUND_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 0.0,
        POISON: 2.0,
        GROUND: 1.0,
        ROCK: 2.0,
        BUG: 0.5,
        GHOST: 1.0,
        FIRE: 2.0,
        WATER: 1.0,
        GRASS: 0.5,
        ELECTRIC: 2.0,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

ROCK_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 0.5,
        FLYING: 2.0,
        POISON: 1.0,
        GROUND: 0.5,
        ROCK: 1.0,
        BUG: 2.0,
        GHOST: 1.0,
        FIRE: 2.0,
        WATER: 1.0,
        GRASS: 1.0,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 2.0,
        DRAGON: 1.0,
    }
)

BUG_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 0.5,
        FLYING: 0.5,
        POISON: 2.0,
        GROUND: 1.0,
        ROCK: 1.0,
        BUG: 1.0,
        GHOST: 0.5,
        FIRE: 0.5,
        WATER: 1.0,
        GRASS: 2.0,
        ELECTRIC: 1.0,
        PSYCHIC: 2.0,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

GHOST_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 0.0,
        FIGHTING: 1.0,
        FLYING: 1.0,
        POISON: 1.0,
        GROUND: 1.0,
        ROCK: 1.0,
        BUG: 1.0,
        GHOST: 2.0,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 1.0,
        ELECTRIC: 1.0,
        PSYCHIC: 0.0,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

FIRE_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 1.0,
        POISON: 1.0,
        GROUND: 1.0,
        ROCK: 0.5,
        BUG: 2.0,
        GHOST: 1.0,
        FIRE: 0.5,
        WATER: 0.5,
        GRASS: 2.0,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 2.0,
        DRAGON: 0.5,
    }
)

WATER_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 1.0,
        POISON: 1.0,
        GROUND: 2.0,
        ROCK: 2.0,
        BUG: 1.0,
        GHOST: 1.0,
        FIRE: 2.0,
        WATER: 0.5,
        GRASS: 0.5,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 0.5,
    }
)

GRASS_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 0.5,
        POISON: 0.5,
        GROUND: 2.0,
        ROCK: 2.0,
        BUG: 0.5,
        GHOST: 1.0,
        FIRE: 0.5,
        WATER: 2.0,
        GRASS: 0.5,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 0.5,
    }
)

ELECTRIC_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 2.0,
        POISON: 1.0,
        GROUND: 0.0,
        ROCK: 1.0,
        BUG: 1.0,
        GHOST: 1.0,
        FIRE: 1.0,
        WATER: 2.0,
        GRASS: 0.5,
        ELECTRIC: 0.5,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 0.5,
    }
)

PSYCHIC_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 2.0,
        FLYING: 1.0,
        POISON: 2.0,
        GROUND: 1.0,
        ROCK: 1.0,
        BUG: 1.0,
        GHOST: 1.0,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 1.0,
        ELECTRIC: 1.0,
        PSYCHIC: 0.5,
        ICE: 1.0,
        DRAGON: 1.0,
    }
)

ICE_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 2.0,
        POISON: 1.0,
        GROUND: 2.0,
        ROCK: 1.0,
        BUG: 1.0,
        GHOST: 1.0,
        FIRE: 1.0,
        WATER: 0.5,
        GRASS: 2.0,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 0.5,
        DRAGON: 2.0,
    }
)

DRAGON_MULTIPLIERS = PKMNTypeMultipliers(
    {
        NORMAL: 1.0,
        FIGHTING: 1.0,
        FLYING: 1.0,
        POISON: 1.0,
        GROUND: 1.0,
        ROCK: 1.0,
        BUG: 1.0,
        GHOST: 1.0,
        FIRE: 1.0,
        WATER: 1.0,
        GRASS: 1.0,
        ELECTRIC: 1.0,
        PSYCHIC: 1.0,
        ICE: 1.0,
        DRAGON: 2.0,
    }
)

def damage_effectiveness(attacking_type: PokemonType, defending_type: PokemonType) -> float:
    multipliers: Dict[PokemonType, PKMNTypeMultipliers] = {
        NORMAL: NORMAL_MULTIPLIERS,
        FIGHTING: FIGHTING_MULTIPLIERS,
        FLYING: FLYING_MULTIPLIERS,
        POISON: POISON_MULTIPLIERS,
        GROUND: GROUND_MULTIPLIERS,
        ROCK: ROCK_MULTIPLIERS,
        BUG: BUG_MULTIPLIERS,
        GHOST: GHOST_MULTIPLIERS,
        FIRE: FIRE_MULTIPLIERS,
        WATER: WATER_MULTIPLIERS,
        GRASS: GRASS_MULTIPLIERS,
        ELECTRIC: ELECTRIC_MULTIPLIERS,
        PSYCHIC: PSYCHIC_MULTIPLIERS,
        ICE: ICE_MULTIPLIERS,
        DRAGON: DRAGON_MULTIPLIERS,
    }

    return multipliers[attacking_type].multipliers[defending_type]
