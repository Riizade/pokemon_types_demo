from enum import Enum

class PokemonType(Enum):
    NORMAL = 0
    FIGHTING = 1
    FLYING = 2
    POISON = 3
    GROUND = 4
    ROCK = 5
    BUG = 6
    GHOST = 7
    FIRE = 8
    WATER = 9
    GRASS = 10
    ELECTRIC = 11
    PSYCHIC = 12
    ICE = 13
    DRAGON = 14


# alias these types to shorter names for more concise syntax
NORMAL = PokemonType.NORMAL
FIGHTING = PokemonType.FIGHTING
FLYING = PokemonType.FLYING
POISON = PokemonType.POISON
GROUND = PokemonType.GROUND
ROCK = PokemonType.ROCK
BUG = PokemonType.BUG
GHOST = PokemonType.GHOST
FIRE = PokemonType.FIRE
WATER = PokemonType.WATER
GRASS = PokemonType.GRASS
ELECTRIC = PokemonType.ELECTRIC
PSYCHIC = PokemonType.PSYCHIC
ICE = PokemonType.ICE
DRAGON = PokemonType.DRAGON
