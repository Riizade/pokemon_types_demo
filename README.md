Pokemon Types Demo
=====

This repository contains two demos for instantiating Pokemon type advantages/disadvantages.

This repository only contains Generation 1 Pokemon types, but can be easily extended.

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