# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# Klassikale oefening 17.1 — De uitleentermijn met echte datums, uitwerking

# De Leeslamp — uitleentermijnen met echte datums
# Cursus Python basis, hoofdstuk 17, oefening 1

from datetime import date, timedelta

TERMIJNEN = {"gewoon": 4, "nieuw": 2}
TARIEF_WEEK_1 = 0.50
TARIEF_DAARNA = 1.00
DAGEN_PER_WEEK = 7
PRIJS_VERLOREN = 25.00


def vervaldatum(uitgeleend: date, soort: str) -> date | None:
    """De datum waarop dit boek terug moet, of None bij een naslagwerk."""
    if soort not in TERMIJNEN:
        return None
    return uitgeleend + timedelta(weeks=TERMIJNEN[soort])


def dagen_te_laat(vervalt: date | None, vandaag: date) -> int:
    """Hoeveel dagen te laat, of nul als het nog op tijd is."""
    if vervalt is None:
        return 0
    verschil = (vandaag - vervalt).days
    return max(verschil, 0)


def boete(dagen: int) -> float:
    """De boete in euro voor een boek dat `dagen` dagen te laat is."""
    if dagen >= 4 * DAGEN_PER_WEEK:
        return PRIJS_VERLOREN
    if dagen <= DAGEN_PER_WEEK:
        bedrag = dagen * TARIEF_WEEK_1
    else:
        bedrag = DAGEN_PER_WEEK * TARIEF_WEEK_1
        bedrag += (dagen - DAGEN_PER_WEEK) * TARIEF_DAARNA
    return min(bedrag, PRIJS_VERLOREN)


def be_datum(d: date | None) -> str:
    """Een datum in de Belgische schrijfwijze, of een streepje."""
    return "-" if d is None else d.strftime("%d/%m/%Y")


VANDAAG = date(2026, 9, 10)

uitleningen = [
    ("Anke Peeters", "Het diner", date(2026, 9, 1), "gewoon"),
    ("Bram Coppens", "Turks fruit", date(2026, 8, 1), "gewoon"),
    ("Cato Dhondt", "De aanslag", date(2026, 8, 20), "nieuw"),
    ("Dirk Vermeulen", "Van Dale", date(2026, 7, 1), "naslagwerk"),
    ("Els Janssens", "Max Havelaar", date(2026, 6, 1), "gewoon"),
]

print(f"Vandaag: {be_datum(VANDAAG)}")
print()
print(f"{'Lid':<16}{'Titel':<15}{'Uitgeleend':<12}{'Vervalt':<12}"
      f"{'Te laat':>8}{'Boete':>8}")
print("-" * 71)

totaal = 0.0
for lid, titel, uitgeleend, soort in uitleningen:
    vervalt = vervaldatum(uitgeleend, soort)
    te_laat = dagen_te_laat(vervalt, VANDAAG)
    bedrag = boete(te_laat)
    totaal += bedrag
    print(f"{lid:<16}{titel:<15}{be_datum(uitgeleend):<12}"
          f"{be_datum(vervalt):<12}{te_laat:>8}{bedrag:>8.2f}")

print("-" * 71)
print(f"{'Totaal':<63}{totaal:>8.2f}")


# Verwachte uitvoer:
# Vandaag: 10/09/2026
#
# Lid             Titel          Uitgeleend  Vervalt      Te laat   Boete
# -----------------------------------------------------------------------
# Anke Peeters    Het diner      01/09/2026  29/09/2026         0    0.00
# Bram Coppens    Turks fruit    01/08/2026  29/08/2026        12    8.50
# Cato Dhondt     De aanslag     20/08/2026  03/09/2026         7    3.50
# Dirk Vermeulen  Van Dale       01/07/2026  -                  0    0.00
# Els Janssens    Max Havelaar   01/06/2026  29/06/2026        73   25.00
# -----------------------------------------------------------------------
# Totaal                                                            37.00
