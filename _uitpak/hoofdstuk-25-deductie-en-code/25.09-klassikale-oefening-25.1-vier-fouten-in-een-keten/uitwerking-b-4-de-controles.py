# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.1 — Vier fouten in één keten, uitwerking
#
# 4. De controles.

DAGTARIEF_STUDENT = 0.25
DAGTARIEF_EERSTE_WEEK = 0.50
DAGTARIEF_DAARNA = 0.75
MAXIMUM = 50.00


def boetebedrag(dagen_te_laat, is_student=False, is_erelid=False):
    """De boete in euro's, zie oefening 25.1."""
    assert isinstance(dagen_te_laat, int)
    if dagen_te_laat <= 0:
        return 0.00
    if is_erelid:
        return 0.00
    tarief = DAGTARIEF_STUDENT if is_student else DAGTARIEF_EERSTE_WEEK
    if dagen_te_laat <= 7:
        bedrag = dagen_te_laat * tarief
    else:
        bedrag = 7 * tarief + (dagen_te_laat - 7) * DAGTARIEF_DAARNA
    return round(min(bedrag, MAXIMUM), 2)


def controleer():
    """De controles die uit de contracten volgen."""
    # de grenzen
    assert boetebedrag(-1) == 0.00
    assert boetebedrag(0) == 0.00
    assert boetebedrag(1) == 0.50
    assert boetebedrag(7) == 3.50
    assert boetebedrag(8) == 4.25

    # het erelid
    assert boetebedrag(100, is_erelid=True) == 0.00

    # de student betaalt nooit meer dan een gewoon lid
    for dagen in range(0, 400):
        assert boetebedrag(dagen, is_student=True) <= boetebedrag(dagen)

    # postconditie: het bedrag daalt nooit als de dagen stijgen
    vorige = 0.00
    for dagen in range(0, 400):
        nu = boetebedrag(dagen)
        assert nu >= vorige, f"bij {dagen} dagen daalt het bedrag"
        assert 0 <= nu <= MAXIMUM
        vorige = nu

    print("Alle controles geslaagd, voor 400 waarden.")


controleer()


# Verwachte uitvoer:
# Alle controles geslaagd, voor 400 waarden.
