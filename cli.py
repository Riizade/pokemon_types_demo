import click
from pkmn_types_matrix import damage_effectiveness as matrix_fn
from pkmn_types_structs import damage_effectiveness as structs_fn
from pkmn_type_enum import PokemonType
from typing import Callable

@click.group()
def cli():
    pass

@click.group()
def effectiveness():
    pass

@click.command()
@click.option("--attack-type", "-a", type=str, required=True, help="The type of attack from the attacking pokemon")
@click.option("--defending-type", "-d", type=str, multiple=True, help="The type of the defending Pokemon; can be specified multiple times")
@click.option("--implementation", "-i", type=click.Choice(["MATRIX", "STRUCTS"], case_sensitive=False), default="STRUCTS", help="The underlying implementation to use")
def attack_type(attack_type: str, defending_type: list[str], implementation: str):
    attack_type_enum: PokemonType = PokemonType.from_str(attack_type)
    defending_type_enums: list[PokemonType] = [PokemonType.from_str(t) for t in defending_type]

    effectiveness_fn: Callable[[PokemonType, PokemonType], float] = None
    if implementation == "MATRIX":
        effectiveness_fn = matrix_fn
    elif implementation == "STRUCTS":
        effectiveness_fn = structs_fn
    else:
        raise NotImplementedError(f"Impementation method {implementation} not recognized")

    effectiveness = 1.0
    for defending_type in defending_type_enums:
        effectiveness *= effectiveness_fn(attack_type_enum, defending_type)
    print(f"the effectiveness for types {attack_type_enum} against [{', '.join([str(t) for t in defending_type_enums])}] is {effectiveness:.2f}x")


cli.add_command(effectiveness)
effectiveness.add_command(attack_type)

if __name__ == "__main__":
    cli()


