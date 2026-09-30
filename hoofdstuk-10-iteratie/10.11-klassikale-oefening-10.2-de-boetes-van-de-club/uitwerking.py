# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Klassikale oefening 10.2 — De boetes van de club, uitwerking

# De Leeslamp — de boete berekenen
# Cursus Python basis, hoofdstuk 10, oefening 2

TARIEF_WEEK_1 = 0.50
TARIEF_DAARNA = 1.00
DAGEN_PER_WEEK = 7
WEKEN_TOT_VERLOREN = 4
PRIJS_VERLOREN = 25.00


def boete(dagen):
    """De boete voor een boek dat `dagen` dagen te laat is."""
    if dagen >= WEKEN_TOT_VERLOREN * DAGEN_PER_WEEK:
        return PRIJS_VERLOREN

    if dagen <= DAGEN_PER_WEEK:
        bedrag = dagen * TARIEF_WEEK_1
    else:
        bedrag = DAGEN_PER_WEEK * TARIEF_WEEK_1
        bedrag += (dagen - DAGEN_PER_WEEK) * TARIEF_DAARNA

    return min(bedrag, PRIJS_VERLOREN)


print("Dag  Boete   Verandering")
print("-" * 26)

vorige = None
for dagen in range(0, 31):
    bedrag = boete(dagen)
    verandert = vorige is None or bedrag != vorige
    mijlpaal = dagen in (0, 7, 14, 21, 28)

    if verandert or mijlpaal:
        merk = ""
        if vorige is not None and bedrag != vorige:
            merk = f"+{bedrag - vorige:.2f}"
        print(f"{dagen:>3}  {bedrag:>6.2f}   {merk}")

    vorige = bedrag

print()
eerste = None
for dagen in range(0, 60):
    if boete(dagen) >= PRIJS_VERLOREN:
        eerste = dagen
        break

print(f"Vanaf dag {eerste} betaal je de volle {PRIJS_VERLOREN:.2f} euro.")


# Verwachte uitvoer:
# Dag  Boete   Verandering
# --------------------------
#   0    0.00
#   1    0.50   +0.50
#   2    1.00   +0.50
#   3    1.50   +0.50
#   4    2.00   +0.50
#   5    2.50   +0.50
#   6    3.00   +0.50
#   7    3.50   +0.50
#   8    4.50   +1.00
#   9    5.50   +1.00
#  10    6.50   +1.00
#  11    7.50   +1.00
#  12    8.50   +1.00
#  13    9.50   +1.00
#  14   10.50   +1.00
#  15   11.50   +1.00
#  16   12.50   +1.00
#  17   13.50   +1.00
#  18   14.50   +1.00
#  19   15.50   +1.00
#  20   16.50   +1.00
#  21   17.50   +1.00
#  22   18.50   +1.00
#  23   19.50   +1.00
#  24   20.50   +1.00
#  25   21.50   +1.00
#  26   22.50   +1.00
#  27   23.50   +1.00
#  28   25.00   +1.50
#
# Vanaf dag 28 betaal je de volle 25.00 euro.
