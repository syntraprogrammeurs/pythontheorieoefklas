# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.9 Het programma opgedeeld

# De Leeslamp — lidgeld en boetes
# Cursus Python basis, hoofdstuk 11

LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3
KORTING = 5

TARIEF_WEEK_1 = 0.50
TARIEF_DAARNA = 1.00
DAGEN_PER_WEEK = 7
PRIJS_VERLOREN = 25.00


def bereken_lidgeld(leeftijd: int, is_student: bool, jaren_lid: int) -> int:
    """Het lidgeld in hele euro's, korting inbegrepen."""
    if leeftijd < LEEFTIJD_GRATIS:
        bedrag = 0
    elif is_student:
        bedrag = LIDGELD_STUDENT
    else:
        bedrag = LIDGELD_VOLWASSENE

    if jaren_lid >= JAREN_VOOR_KORTING:
        bedrag -= KORTING

    return max(bedrag, 0)


def bereken_boete(dagen_te_laat: int) -> float:
    """De boete in euro voor een boek dat te laat is."""
    if dagen_te_laat >= 4 * DAGEN_PER_WEEK:
        return PRIJS_VERLOREN

    if dagen_te_laat <= DAGEN_PER_WEEK:
        bedrag = dagen_te_laat * TARIEF_WEEK_1
    else:
        bedrag = DAGEN_PER_WEEK * TARIEF_WEEK_1
        bedrag += (dagen_te_laat - DAGEN_PER_WEEK) * TARIEF_DAARNA

    return min(bedrag, PRIJS_VERLOREN)


def totaal_te_betalen(leeftijd: int, is_student: bool,
                      jaren_lid: int, dagen_te_laat: int) -> float:
    """Lidgeld plus boete."""
    return bereken_lidgeld(leeftijd, is_student, jaren_lid) + bereken_boete(dagen_te_laat)


def toon_rekening(naam: str, bedrag: float) -> None:
    """Zet één regel van de rekening op het scherm."""
    print(f"{naam:<16}{bedrag:>8.2f}")


leden = [
    ("Anke Peeters", 34, False, 3, 0),
    ("Bram Coppens", 20, True, 1, 10),
    ("Cato Dhondt", 11, False, 4, 30),
]

print(f"{'Lid':<16}{'Bedrag':>8}")
print("-" * 24)
for naam, leeftijd, student, jaren, te_laat in leden:
    toon_rekening(naam, totaal_te_betalen(leeftijd, student, jaren, te_laat))


# Verwachte uitvoer:
# Lid               Bedrag
# ------------------------
# Anke Peeters       25.00
# Bram Coppens       21.50
# Cato Dhondt        25.00
