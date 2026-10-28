# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.1 — Vier fouten in één keten, uitwerking
#
# 3. De herschreven functie.

# De Leeslamp — boetebedrag, met uitgesproken aannames
# Cursus Python basis, hoofdstuk 25, oefening 1

DAGTARIEF_STUDENT = 0.25
DAGTARIEF_EERSTE_WEEK = 0.50
DAGTARIEF_DAARNA = 0.75
MAXIMUM = 50.00


def boetebedrag(dagen_te_laat, is_student=False, is_erelid=False):
    """De boete in euro's.

    Preconditie : dagen_te_laat is een geheel getal.
    Postconditie: het resultaat ligt tussen 0 en MAXIMUM,
                  en daalt nooit wanneer dagen_te_laat stijgt.
    """
    assert isinstance(dagen_te_laat, int), "dagen_te_laat hoort een int te zijn"

    # bewaakclausules: elke reden om niets te rekenen, apart
    if dagen_te_laat <= 0:
        return 0.00
    if is_erelid:
        return 0.00

    tarief = DAGTARIEF_STUDENT if is_student else DAGTARIEF_EERSTE_WEEK

    if dagen_te_laat <= 7:
        bedrag = dagen_te_laat * tarief
    else:
        bedrag = 7 * tarief + (dagen_te_laat - 7) * DAGTARIEF_DAARNA

    bedrag = min(bedrag, MAXIMUM)

    assert 0 <= bedrag <= MAXIMUM
    return round(bedrag, 2)


for dagen in (0, 1, 7, 8, 30, 365):
    print(f"{dagen:>4} dagen: gewoon {boetebedrag(dagen):>6.2f}   "
          f"student {boetebedrag(dagen, is_student=True):>6.2f}")


# Verwachte uitvoer:
#    0 dagen: gewoon   0.00   student   0.00
#    1 dagen: gewoon   0.50   student   0.25
#    7 dagen: gewoon   3.50   student   1.75
#    8 dagen: gewoon   4.25   student   2.50
#   30 dagen: gewoon  20.75   student  19.00
#  365 dagen: gewoon  50.00   student  50.00
