<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 26.2 — Drie syllogismen toetsen

Uit *Python basis — theoriebundel*, hoofdstuk 26 (Categorische logica en venndiagrammen), paragraaf 26.8.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-3-het-programma.py` | uitwerking |  |

## Opgave

**De situatie.** Drie redeneringen uit een gesprek over de nieuwe website.

| Nr. | Redenering |
|---|---|
| 1 | Alle beheerders mogen leden verwijderen. Geen enkel gewoon lid is beheerder. Dus geen enkel gewoon lid mag leden verwijderen |
| 2 | Alle geschorste leden krijgen een waarschuwing. Sommige leden krijgen een waarschuwing. Dus sommige leden zijn geschorst |
| 3 | Geen enkel geschorst lid mag lenen. Alle leden met een boete zijn geschorst. Dus geen enkel lid met een boete mag lenen |

**Wat je doet.**

1. Benoem per redenering S, P en de middenterm.
2. Voorspel welke geldig zijn, met de vijf regels uit 26.5.
3. Toets ze met het programma uit 26.6, en bekijk de tegenwerelden.
4. Leg uit waarom nummer 1 de meeste mensen misleidt.

## Uitwerking

**1. De termen.**

| Nr. | S (onderwerp conclusie) | P (predicaat conclusie) | Middenterm |
|---|---|---|---|
| 1 | gewone leden | mogen verwijderen | beheerders |
| 2 | leden | geschorst | krijgen een waarschuwing |
| 3 | leden met een boete | mogen lenen | geschorste leden |

**2. De voorspelling met de regels.**

*Nummer 1.* De middenterm "beheerders" staat in premisse 1 als onderwerp van een
A-uitspraak, dus volledig genomen. Regel 1 is voldaan. Maar kijk naar regel 2:
de conclusie is een E-uitspraak, dus "mogen verwijderen" is er volledig genomen.
In premisse 1 staat die term als predicaat van een A-uitspraak, en daar is hij
**niet** volledig genomen. Regel 2 is geschonden, dus ongeldig.

*Nummer 2.* De middenterm "krijgen een waarschuwing" staat in premisse 1 als
predicaat van een A-uitspraak (niet volledig) en in premisse 2 als deel van een
I-uitspraak (niet volledig). Regel 1 geschonden, dus ongeldig. Dit is bovendien
het bevestigen van het consequens uit hoofdstuk 24, in categorische vorm.

*Nummer 3.* Middenterm "geschorst": volledig genomen in de E-uitspraak. In de
conclusie is "mogen lenen" volledig genomen, en in premisse 1 ook, want E maakt
beide termen volledig. Alle regels voldaan, dus geldig.

**3. Het programma.**

```python
# De Leeslamp — drie syllogismen mechanisch getoetst
# Cursus Python basis, hoofdstuk 26, oefening 2
from itertools import product

TERMEN = ("S", "P", "M")
GEBIEDEN = list(product([False, True], repeat=3))


def hoort_bij(gebied, term):
    return gebied[TERMEN.index(term)]


def alle(wereld, a, b):
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


def geen(wereld, a, b):
    return not any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def sommige(wereld, a, b):
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def werelden():
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


def beschrijf(gebied):
    binnen = [t for t in TERMEN if hoort_bij(gebied, t)]
    return "+".join(binnen) if binnen else "niets"


def toets(nummer, premissen, conclusie):
    """Zoekt een wereld waarin de premissen kloppen en de conclusie niet."""
    for wereld in werelden():
        if all(p(wereld) for p in premissen) and not conclusie(wereld):
            bewoond = ", ".join(beschrijf(g) for g in wereld) or "lege wereld"
            print(f"{nummer}  ONGELDIG")
            print(f"   tegenwereld: bewoond zijn {bewoond}")
            return
    print(f"{nummer}  geldig")


toets("1.",
      [lambda w: alle(w, "M", "P"), lambda w: geen(w, "S", "M")],
      lambda w: geen(w, "S", "P"))

toets("2.",
      [lambda w: alle(w, "P", "M"), lambda w: sommige(w, "S", "M")],
      lambda w: sommige(w, "S", "P"))

toets("3.",
      [lambda w: geen(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: geen(w, "S", "P"))
```

```text
1.  ONGELDIG
   tegenwereld: bewoond zijn S+P
2.  ONGELDIG
   tegenwereld: bewoond zijn S+M
3.  geldig
```

**De tegenwerelden gelezen.**

*Nummer 1.* Bewoond is alleen het gebied S en P, buiten M: er bestaat een gewoon
lid dat geen beheerder is en tóch leden mag verwijderen. Beide premissen
kloppen — alle beheerders mogen verwijderen, en dit lid is geen beheerder — en de
conclusie is onwaar.

Concreet: de voorzitter mag ook leden verwijderen, zonder beheerder te zijn. Dat
is precies de situatie die premisse 1 nooit uitsloot.

*Nummer 2.* Bewoond is alleen het gebied S en M, buiten P: er is een lid dat een
waarschuwing kreeg en niet geschorst is. Verder is de wereld leeg, en dus is er
geen enkel geschorst lid.

Reken de premissen na. "Alle geschorste leden krijgen een waarschuwing" is waar,
want er zijn geen geschorste leden en dus geen tegenvoorbeeld. Dat is opnieuw de
lege implicatie uit hoofdstuk 23. "Sommige leden krijgen een waarschuwing" is
waar, want dat ene lid zit er. En de conclusie "sommige leden zijn geschorst" is
onwaar.

Concreet: iemand kreeg een waarschuwing omdat zijn boek te laat was, niet omdat
hij geschorst is. De waarschuwing heeft meer oorzaken dan schorsing, en dat is
precies wat premisse 1 niet uitsluit.

> **Let op**
>
> De tegenwereld toont alleen de gebieden die bewoond zijn. Wat er níet staat, is
> even belangrijk: alle andere gebieden zijn leeg, en juist die leegte maakt de
> eerste premisse waar.
>
> Wanneer een tegenwereld je verrast, reken hem dan met de hand na in plaats van
> het programma op zijn woord te geloven. En bedenk dat er meestal meer dan één
> tegenwereld is; `toets` stopt bij de eerste die hij vindt.

*Nummer 3.* Geen tegenwereld gevonden, in geen van de 256. Geldig.

**4. Waarom nummer 1 zo goed misleidt.**

De conclusie klínkt niet alleen aannemelijk, ze is in de praktijk waarschijnlijk
ook waar. In de meeste systemen mogen gewone leden inderdaad niemand
verwijderen.

Maar dat is toevallig zo, en het volgt niet uit deze twee premissen. Als er ooit
een tweede rol bijkomt — moderator, voorzitter, secretaris — die ook mag
verwijderen, dan valt de conclusie om, terwijl beide premissen ongewijzigd waar
blijven.

Dat is een concreet beveiligingsrisico, en het is de reden waarom rechten in
software geregeld worden met een expliciete lijst van wie wat mag, en niet met
een redenering over wie iets níet is.
