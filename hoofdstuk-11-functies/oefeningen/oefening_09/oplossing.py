# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 9 — Korting berekenen met docstring en type hints

def bereken_korting(bedrag: float, is_lid: bool) -> float:
    """Geeft het bedrag na korting.

    Leden krijgen 10% korting, niet-leden betalen het volledige bedrag.
    """
    if is_lid:
        return bedrag * 0.9
    return bedrag


print(bereken_korting(40, True))
print(bereken_korting(40, False))
print(bereken_korting.__doc__.splitlines()[0])
