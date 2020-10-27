from tabulate import tabulate

from pkmn_type_enum import PokemonType
from pkmn_types_matrix import damage_effectiveness as matrix_damage_effectiveness
from pkmn_types_structs import damage_effectiveness as struct_damage_effectiveness

def main():
    # define rows
    rows = []
    for attack_type in PokemonType:
        for defend_type in PokemonType:
            matrix_mult = matrix_damage_effectiveness(attack_type, defend_type)
            struct_mult = struct_damage_effectiveness(attack_type, defend_type)
            rows.append({
                "attacking type": str(attack_type),
                "defending type": str(defend_type),
                "eff. matrix": matrix_mult,
                "eff. struct": struct_mult,
                "match": matrix_mult == struct_mult
            })

    # display rows
    print(tabulate(rows, headers="keys"))

    # check if any didn't match
    for row in rows:
        assert(row["match"])

if __name__ == "__main__":
    main()