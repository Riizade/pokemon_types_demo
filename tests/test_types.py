import unittest
from typing import Tuple
from pkmn_type_enum import PokemonType
from pkmn_types_matrix import damage_effectiveness as dmg_eff_matrix
from pkmn_types_structs import damage_effectiveness as dmg_eff_structs


class TestTypeEffectiveness(unittest.TestCase):
    def test_equivalence(self):
        for atk_type in PokemonType:
            for def_type in PokemonType:
                matrix_result = dmg_eff_matrix(atk_type, def_type)
                structs_result = dmg_eff_structs(atk_type, def_type)
                self.assertEqual(matrix_result, structs_result, f"Damage values did not match for {atk_type} -> {def_type} (matrix: {matrix_result}, structs: {structs_result})")

    def test_various(self):
        # tuples of (attack type, defending type, expected damage effectiveness)
        tests: Tuple[PokemonType, PokemonType, float] = [
            (PokemonType.FIRE, PokemonType.WATER, 0.5),
            (PokemonType.NORMAL, PokemonType.GHOST, 0.0),
            (PokemonType.GRASS, PokemonType.GROUND, 2.0),
        ]

        for t in tests:
            # test parameters
            atk_type = t[0]
            def_type = t[1]
            expected_result = t[2]

            # test struct implementation
            structs_result = dmg_eff_structs(atk_type, def_type)
            self.assertEqual(structs_result, expected_result, f"Structs effectiveness mismatch for {atk_type} -> {def_type}, expected {expected_result}, received {structs_result}")

            # test matrix implementation
            matrix_result = dmg_eff_matrix(atk_type, def_type)
            self.assertEqual(matrix_result, expected_result, f"Matrix effectiveness mismatch for {atk_type} -> {def_type}, expected {expected_result}, received {matrix_result}")