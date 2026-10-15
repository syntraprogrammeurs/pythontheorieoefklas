# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.9 Het lidgeldprogramma, nu bestand tegen alles

# De Leeslamp — lidgeld, met invoer die niet crasht
# Cursus Python basis, hoofdstuk 15

LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3
KORTING = 5


def bereken_lidgeld(leeftijd: int, is_student: bool, jaren_lid: int) -> int:
    """Het lidgeld in hele euro's. Weigert onmogelijke waarden."""
    if leeftijd < 0 or leeftijd > 130:
        raise ValueError(f"onmogelijke leeftijd: {leeftijd}")
    if jaren_lid < 0:
        raise ValueError(f"onmogelijk aantal jaren: {jaren_lid}")
    if jaren_lid > leeftijd:
        raise ValueError(f"{jaren_lid} jaar lid op {leeftijd}-jarige leeftijd?")

    if leeftijd < LEEFTIJD_GRATIS:
        bedrag = 0
    elif is_student:
        bedrag = LIDGELD_STUDENT
    else:
        bedrag = LIDGELD_VOLWASSENE

    if jaren_lid >= JAREN_VOOR_KORTING:
        bedrag -= KORTING
    return max(bedrag, 0)


gevallen = [
    (34, False, 3),
    (11, False, 4),
    (20, True, 1),
    (-5, False, 0),
    (200, False, 0),
    (20, False, 25),
]

for leeftijd, student, jaren in gevallen:
    try:
        bedrag = bereken_lidgeld(leeftijd, student, jaren)
    except ValueError as fout:
        print(f"{leeftijd:>5} {student!s:<6}{jaren:>3}   geweigerd: {fout}")
    else:
        print(f"{leeftijd:>5} {student!s:<6}{jaren:>3}   {bedrag:>3} euro")


# Verwachte uitvoer:
#    34 False   3    25 euro
#    11 False   4     0 euro
#    20 True    1    15 euro
#    -5 False   0   geweigerd: onmogelijke leeftijd: -5
#   200 False   0   geweigerd: onmogelijke leeftijd: 200
#    20 False  25   geweigerd: 25 jaar lid op 20-jarige leeftijd?
