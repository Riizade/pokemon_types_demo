module Pokemon (PokemonType) where
    -- We are not making this an enumeration (deriving (Enum) ), aka assigning integers
    -- as there is no reasonable reason to impose an ordering on this type
    data PokemonType =
        NORMAL | 
        FIGHTING |
        FLYING |
        POISON |
        GROUND |
        ROCK |
        BUG |
        GHOST |
        FIRE |
        WATER |
        GRASS |
        ELECTRIC |
        PSYCHIC |
        ICE |
        DRAGON deriving (Eq, Show) 
    