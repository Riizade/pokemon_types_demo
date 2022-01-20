Pokemon Types Demo
=====

This repository contains various demos for instantiating Pokemon type advantages/disadvantages.

This repository only contains Generation 1 Pokemon types, but can be easily extended.

Similar Projects
=====
- https://github.com/Spimtav/Pokemon-Type-Calculator
- https://github.com/awcrotwell/pokemon-type-calculator
- https://gist.github.com/kkjdroid/efbf978a48eddb82978089f0a2fed8db
- https://github.com/DerekParry/pkmn_type_calc/blob/master/pkmn_type_calc.py
- https://github.com/PokeAPI/pokeapi (https://github.com/PokeAPI/pokeapi/blob/master/data/v2/csv/type_efficacy.csv)

Setup
=====
- `pipenv install`

Run
=====
- `pipenv run python main.py`

Project Layout
=====
- `pkmn_type_enum.py` contains a simple enum definition containing each of the Pokemon types, as well as shorthand names for each to avoid verbosity when using a lot of type names during defining damage multipliers.
- each `pkmn_types_<name>.py` file contains a definition for all Pokemon damage multipliers in a particular format, as well as a function with the signature `def damage_effectiveness(attacking_type: PokemonType, defending_type: PokemonType) -> float`
    - `pkmn_types_matrix.py` defines the damage multipliers in a format of `Dict[(attacking_type, defending_type), float]`
    - `pkmn_types_structs.py` defines the damage multipliers in a dataclass for each type which contains a map of `Dict[defending_type, float]`
- `main.py` simply iterates over all type combinations and prints out the information about multipliers from each `pkmn_types_<name>.py` definition; if the multipliers don't match between the definitions, the program will crash after printing