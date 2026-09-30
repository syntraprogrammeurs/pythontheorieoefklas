# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.7 Docstrings en type hints

def bereken_lidgeld(leeftijd: int, is_student: bool, jaren_lid: int) -> int:
    """Geeft het lidgeld in hele euro's.

    Jonger dan 12 is gratis, studenten betalen 15 en de rest 30.
    Vanaf 3 jaar lidmaatschap gaat er 5 euro af, met een minimum van nul.
    """
    if leeftijd < 12:
        bedrag = 0
    elif is_student:
        bedrag = 15
    else:
        bedrag = 30

    if jaren_lid >= 3:
        bedrag -= 5

    return max(bedrag, 0)


print(bereken_lidgeld(45, False, 3))
print(bereken_lidgeld(11, False, 4))
print(bereken_lidgeld.__doc__.splitlines()[0])


# Verwachte uitvoer:
# 25
# 0
# Geeft het lidgeld in hele euro's.
