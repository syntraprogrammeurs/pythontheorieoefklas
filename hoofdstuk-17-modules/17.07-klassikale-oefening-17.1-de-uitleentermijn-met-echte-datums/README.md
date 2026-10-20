<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 17.1 — De uitleentermijn met echte datums

Uit *Python basis — theoriebundel*, hoofdstuk 17 (Modules, de standaardbibliotheek en `pip`), paragraaf 17.7.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** In hoofdstuk 9 rekende je met weken. Nu reken je met echte
datums, zodat het programma kan zeggen wanneer een boek terug moet.

**Wat je maakt.**

1. `vervaldatum(uitgeleend, soort)` die de datum teruggeeft waarop het boek
   terug moet. Gewoon boek: 4 weken. Nieuw: 2 weken. Naslagwerk: `None`.
2. `dagen_te_laat(vervaldatum, vandaag)` die nul geeft als het niet te laat is.
3. `boete(dagen)` uit oefening 10.2, hergebruikt.
4. Een overzicht van vijf uitleningen op 10 september 2026, met de datum in
   Belgische schrijfwijze en de boete.

## Uitwerking

```python
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
```

```text
Vandaag: 10/09/2026

Lid             Titel          Uitgeleend  Vervalt      Te laat   Boete
-----------------------------------------------------------------------
Anke Peeters    Het diner      01/09/2026  29/09/2026         0    0.00
Bram Coppens    Turks fruit    01/08/2026  29/08/2026        12    8.50
Cato Dhondt     De aanslag     20/08/2026  03/09/2026         7    3.50
Dirk Vermeulen  Van Dale       01/07/2026  -                  0    0.00
Els Janssens    Max Havelaar   01/06/2026  29/06/2026        73   25.00
-----------------------------------------------------------------------
Totaal                                                            37.00
```

**De vijf punten.**

**`timedelta(weeks=4)` in plaats van zelf rekenen.** Vier weken bij 1 september
optellen is 29 september. Zou je `dag + 28` schrijven op het dagnummer, dan
krijg je 29 september alleen wanneer de maand lang genoeg is. Bij 20 augustus
plus twee weken geeft naïef rekenen dag 34 van augustus, en dat bestaat niet.
`timedelta` regelt maandovergangen en schrikkeljaren voor je.

**`max(verschil, 0)` in plaats van een `if`.** Een boek dat nog niet vervallen
is, geeft een negatief verschil. Nul is dan het juiste antwoord, en `max` zegt
dat in één woord.

**Het naslagwerk geeft `None`, geen datum.** Het gaat nooit mee naar huis, dus
er is geen vervaldatum. `be_datum` vertaalt die `None` naar een streepje. Zonder
die functie zou je op drie plaatsen dezelfde `if` schrijven.

**De tabelbreedte klopt.** 16 + 15 + 12 + 12 + 8 + 8 is 71, en dat is precies de
lengte van de streepjeslijn. De totaalregel gebruikt 63 + 8, ook 71. Reken dat
na in plaats van het te schatten; dat is de les uit oefening 6.2.

**`date | None` als type hint.** Dat leest als "een datum of niets". Deze
schrijfwijze bestaat sinds Python 3.10; daarvoor schreef je `Optional[date]`.
Pylance gebruikt ze om je te waarschuwen wanneer je vergeet de `None` af te
vangen.

**Wat je kunt controleren.** Els is 73 dagen te laat, meer dan vier weken, dus
haar boek geldt als verloren en kost 25 euro. Cato is precies zeven dagen te
laat: nog net het tarief van de eerste week, dus 7 maal 0,50 is 3,50. Dat zijn
de grenswaarden uit hoofdstuk 3, en ze staan er niet toevallig in.
