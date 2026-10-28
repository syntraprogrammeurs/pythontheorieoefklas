<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 29.2 — De kern bouwen en testen

Uit *Python basis — theoriebundel*, hoofdstuk 29 (Eindopdracht: alles samen), paragraaf 29.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-de-tests-bij-die-kern.py` | uitwerking |  |

## Opgave

**De situatie.** De vragen zijn beantwoord. Nu bouw je stap 4 en 5 van het
werkplan: de klassen en de rekenregel, met hun tests, en nog geen menu.

**Wat je doet.**

1. Schrijf de klasse `Lid` met de velden uit 29.8.
2. Schrijf de functie `lidgeld_centen` volgens het contract.
3. Schrijf de tests met equivalentieklassen en grenswaarden.
4. Toon dat de kern volledig werkt zonder dat er één keer iets ingetypt wordt.

## Uitwerking

```python
# Turnclub De Sprong — de kern van de eindopdracht
# Cursus Python basis, hoofdstuk 29, oefening 2

HUIDIG_JAAR = 2026

BASISTARIEF_CENTEN = 12_000
JEUGDTARIEF_CENTEN = 9_000
JEUGD_TOT_EN_MET = 17
GEZINSKORTING_CENTEN = 1_500


class Lid:
    """Eén lid van de turnclub."""

    def __init__(self, nummer, naam, geboortejaar, groep_id,
                 gezin_id=None, rang_in_gezin=1):
        assert naam.strip(), "een lid moet een naam hebben"
        self.nummer = nummer
        self.naam = naam.strip()
        self.geboortejaar = geboortejaar
        self.groep_id = groep_id
        self.gezin_id = gezin_id
        self.rang_in_gezin = rang_in_gezin
        self.betaald_centen = 0

    def leeftijd(self, in_jaar=HUIDIG_JAAR):
        """De leeftijd die het lid dit jaar bereikt."""
        return in_jaar - self.geboortejaar

    def openstaand_centen(self):
        """Wat er nog betaald moet worden; nooit negatief."""
        return max(0, lidgeld_centen(self.geboortejaar,
                                     self.rang_in_gezin) - self.betaald_centen)

    def __repr__(self):
        return f"Lid({self.nummer}, {self.naam!r}, {self.geboortejaar})"


def lidgeld_centen(geboortejaar, rang_in_gezin=1, in_jaar=HUIDIG_JAAR):
    """Het lidgeld in hele centen.

    Preconditie : 1900 <= geboortejaar <= in_jaar, rang_in_gezin >= 1.
    Postconditie: 0 <= resultaat <= BASISTARIEF_CENTEN.
    """
    if not isinstance(geboortejaar, int) or isinstance(geboortejaar, bool):
        raise TypeError("geboortejaar moet een geheel getal zijn")
    if not 1900 <= geboortejaar <= in_jaar:
        raise ValueError(f"geboortejaar {geboortejaar} is onmogelijk")
    if rang_in_gezin < 1:
        raise ValueError("de rang in het gezin begint bij 1")

    leeftijd = in_jaar - geboortejaar
    bedrag = (JEUGDTARIEF_CENTEN if leeftijd <= JEUGD_TOT_EN_MET
              else BASISTARIEF_CENTEN)

    if rang_in_gezin >= 2:
        bedrag -= GEZINSKORTING_CENTEN

    bedrag = max(0, bedrag)
    assert 0 <= bedrag <= BASISTARIEF_CENTEN
    return bedrag


def in_euro(centen):
    """Centen als leesbaar bedrag."""
    return f"{centen // 100},{centen % 100:02d} euro"


LEDEN = [
    Lid(1, "Anke Peeters", 1990, groep_id=2),
    Lid(2, "Bram Janssens", 2012, groep_id=1, gezin_id=7, rang_in_gezin=1),
    Lid(3, "Cato Janssens", 2015, groep_id=1, gezin_id=7, rang_in_gezin=2),
    Lid(4, "Dirk Willems", 1978, groep_id=3),
]
LEDEN[0].betaald_centen = 12_000
LEDEN[1].betaald_centen = 5_000

print(f"{'Lid':<16}{'Leeftijd':>9}{'Lidgeld':>12}{'Openstaand':>13}")
print("-" * 50)
for lid in LEDEN:
    print(f"{lid.naam:<16}{lid.leeftijd():>9}"
          f"{in_euro(lidgeld_centen(lid.geboortejaar, lid.rang_in_gezin)):>12}"
          f"{in_euro(lid.openstaand_centen()):>13}")

wanbetalers = [lid for lid in LEDEN if lid.openstaand_centen() > 0]
print()
print("Nog te betalen door:", ", ".join(lid.naam for lid in wanbetalers))
print("Totaal openstaand  :",
      in_euro(sum(lid.openstaand_centen() for lid in LEDEN)))
```

```text
Lid              Leeftijd     Lidgeld   Openstaand
--------------------------------------------------
Anke Peeters           36 120,00 euro    0,00 euro
Bram Janssens          14  90,00 euro   40,00 euro
Cato Janssens          11  75,00 euro   75,00 euro
Dirk Willems           48 120,00 euro  120,00 euro

Nog te betalen door: Bram Janssens, Cato Janssens, Dirk Willems
Totaal openstaand  : 235,00 euro
```

**De tests bij die kern.**

```python
HUIDIG_JAAR = 2026
BASISTARIEF_CENTEN = 12_000
JEUGDTARIEF_CENTEN = 9_000
JEUGD_TOT_EN_MET = 17
GEZINSKORTING_CENTEN = 1_500


def lidgeld_centen(geboortejaar, rang_in_gezin=1, in_jaar=HUIDIG_JAAR):
    """Zie oefening 29.2."""
    if not isinstance(geboortejaar, int) or isinstance(geboortejaar, bool):
        raise TypeError("geboortejaar moet een geheel getal zijn")
    if not 1900 <= geboortejaar <= in_jaar:
        raise ValueError(f"geboortejaar {geboortejaar} is onmogelijk")
    if rang_in_gezin < 1:
        raise ValueError("de rang in het gezin begint bij 1")
    leeftijd = in_jaar - geboortejaar
    bedrag = (JEUGDTARIEF_CENTEN if leeftijd <= JEUGD_TOT_EN_MET
              else BASISTARIEF_CENTEN)
    if rang_in_gezin >= 2:
        bedrag -= GEZINSKORTING_CENTEN
    return max(0, bedrag)


# equivalentieklassen en grenswaarden rond de leeftijdsgrens van 17
GELDIG = [
    # (geboortejaar, rang, verwacht in centen)
    (2026, 1, 9_000),      # pasgeboren: onderste grens
    (2010, 1, 9_000),      # 16 jaar: binnen de jeugdklasse
    (2009, 1, 9_000),      # 17 jaar: precies op de grens
    (2008, 1, 12_000),     # 18 jaar: net erboven
    (1990, 1, 12_000),     # volwassen: midden in de klasse
    (1900, 1, 12_000),     # oudste toegelaten jaar
    (2009, 2, 7_500),      # jeugd met gezinskorting
    (1990, 2, 10_500),     # volwassen met gezinskorting
    (1990, 5, 10_500),     # korting geldt vanaf de tweede, niet per rang
]

ONGELDIG = [
    (1899, 1, ValueError),
    (2027, 1, ValueError),
    (1990, 0, ValueError),
    ("1990", 1, TypeError),
    (True, 1, TypeError),
    (1990.5, 1, TypeError),
]


def draai():
    """Draait alle gevallen en meldt elk verschil."""
    gefaald = []

    for jaar, rang, verwacht in GELDIG:
        werkelijk = lidgeld_centen(jaar, rang)
        if werkelijk != verwacht:
            gefaald.append(f"{jaar} rang {rang}: {werkelijk} in plaats van {verwacht}")

    for jaar, rang, soort in ONGELDIG:
        try:
            lidgeld_centen(jaar, rang)
        except soort:
            continue
        except Exception as fout:
            gefaald.append(f"{jaar!r}: {type(fout).__name__} "
                           f"in plaats van {soort.__name__}")
            continue
        gefaald.append(f"{jaar!r}: geen fout, wel {soort.__name__} verwacht")

    # postconditie over het hele bereik
    for jaar in range(1900, HUIDIG_JAAR + 1):
        for rang in (1, 2):
            bedrag = lidgeld_centen(jaar, rang)
            if not 0 <= bedrag <= BASISTARIEF_CENTEN:
                gefaald.append(f"{jaar} rang {rang}: {bedrag} buiten bereik")

    totaal = len(GELDIG) + len(ONGELDIG)
    print(f"{totaal - len(gefaald)} van de {totaal} gevallen geslaagd")
    print(f"postconditie nagegaan voor {(HUIDIG_JAAR - 1900 + 1) * 2} combinaties")
    for regel in gefaald:
        print(f"  FOUT {regel}")
    return not gefaald


print("Groen:", draai())
```

```text
15 van de 15 gevallen geslaagd
postconditie nagegaan voor 254 combinaties
Groen: True
```

**Wat deze uitwerking laat zien.**

| Punt | Waar het vandaan komt |
|---|---|
| Geen enkele `input()` in de kern | Het werkplan uit 29.5 |
| Bedragen in centen als `int` | De drijvendekommaval uit hoofdstuk 6 |
| `isinstance(x, bool)` apart uitgesloten | De valkuil uit hoofdstuk 28 |
| Testwaarden rond 17 en 18 jaar | Grenswaardenanalyse uit 28.4 |
| Een lus over het hele bereik voor de postconditie | Contracten uit hoofdstuk 25 |
| `rang_in_gezin` van 5 geeft dezelfde korting als 2 | De regel is "vanaf het tweede", en dat wordt getest |

Die laatste rij is de interessantste. De regel zegt "vanaf het tweede lid", en de
verleiding is om `rang * korting` te schrijven. Eén testgeval met rang 5 legt dat
verschil bloot, en het is precies het geval dat niemand verzint zonder erover na
te denken.

**Wat er nu nog moet gebeuren.** Stap 6 tot en met 10 van het werkplan: opslag,
menu, foutafhandeling, opruimen, documenteren. Dat is de zelfstandige helft van
de opdracht, en de kern waarop je verderbouwt, is nu getest.
