<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 16.2 — Een tekstbestand analyseren

Uit *Python basis — theoriebundel*, hoofdstuk 16 (Bestanden lezen en schrijven), paragraaf 16.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** De club heeft de leesverslagen van het voorbije jaar in één
tekstbestand. Je maakt er een woordstatistiek van.

**Wat je maakt.**

1. Schrijf eerst een tekstbestand met vijf regels tekst.
2. Lees het regel per regel.
3. Toon het aantal regels, woorden en tekens.
4. Toon de tien meest voorkomende woorden, zonder de stopwoorden `de`, `het`,
   `een`, `en`, `van`, `is`, `in`, `dat`, `die`, `te`.
5. Toon per regel het nummer en het aantal woorden.
6. Schrijf het resultaat weg naar een tweede bestand.

## Uitwerking

```python
# De Leeslamp — een tekstbestand analyseren
# Cursus Python basis, hoofdstuk 16, oefening 2

from pathlib import Path

BRON = Path("verslagen.txt")
DOEL = Path("statistiek.txt")
STOPWOORDEN = {"de", "het", "een", "en", "van", "is", "in", "dat", "die", "te"}
LEESTEKENS = ".,;:!?\"'()"

TEKST = """Het boek gaat over twee families en een diner in een restaurant.
De schrijfstijl is vlot en het verhaal loopt goed door.
Het einde stelt teleur, want het verhaal valt in de laatste bladzijden stil.
Toch is het een boek dat je in een avond uitleest.
De discussie in de club ging vooral over het einde van het boek."""

BRON.write_text(TEKST + "\n", encoding="utf-8")


def tel_woorden(pad: Path) -> dict:
    """Per woord het aantal keer dat het voorkomt, zonder de stopwoorden."""
    telling = {}
    with open(pad, encoding="utf-8") as bestand:
        for regel in bestand:
            for ruw in regel.split():
                woord = ruw.strip(LEESTEKENS).lower()
                if not woord or woord in STOPWOORDEN:
                    continue
                telling[woord] = telling.get(woord, 0) + 1
    return telling


def kengetallen(pad: Path) -> dict:
    """Het aantal regels, woorden en tekens van een tekstbestand."""
    regels = woorden = tekens = 0
    with open(pad, encoding="utf-8") as bestand:
        for regel in bestand:
            regels += 1
            woorden += len(regel.split())
            tekens += len(regel.rstrip("\n"))
    return {"regels": regels, "woorden": woorden, "tekens": tekens}


cijfers = kengetallen(BRON)
telling = tel_woorden(BRON)
top = sorted(telling.items(), key=lambda p: (-p[1], p[0]))[:10]

regels_uit = [
    "STATISTIEK VAN DE LEESVERSLAGEN",
    "=" * 34,
    f"Regels : {cijfers['regels']}",
    f"Woorden: {cijfers['woorden']}",
    f"Tekens : {cijfers['tekens']}",
    f"Verschillende woorden (zonder stopwoorden): {len(telling)}",
    "",
    "De tien meest gebruikte woorden",
    "-" * 34,
]
for woord, aantal in top:
    regels_uit.append(f"{woord:<20}{aantal:>4}  {'*' * aantal}")

regels_uit.append("")
regels_uit.append("Woorden per regel")
regels_uit.append("-" * 34)
with open(BRON, encoding="utf-8") as bestand:
    for nummer, regel in enumerate(bestand, start=1):
        regels_uit.append(f"  regel {nummer}: {len(regel.split()):>3} woorden")

DOEL.write_text("\n".join(regels_uit) + "\n", encoding="utf-8")
print(DOEL.read_text(encoding="utf-8"))

BRON.unlink()
DOEL.unlink()
```

```text
STATISTIEK VAN DE LEESVERSLAGEN
==================================
Regels : 5
Woorden: 59
Tekens : 309
Verschillende woorden (zonder stopwoorden): 29

De tien meest gebruikte woorden
----------------------------------
boek                   3  ***
einde                  2  **
over                   2  **
verhaal                2  **
avond                  1  *
bladzijden             1  *
club                   1  *
diner                  1  *
discussie              1  *
door                   1  *

Woorden per regel
----------------------------------
  regel 1:  12 woorden
  regel 2:  10 woorden
  regel 3:  13 woorden
  regel 4:  11 woorden
  regel 5:  13 woorden
```

**De vijf technieken.**

**Sorteren op twee sleutels tegelijk.** `key=lambda p: (-p[1], p[0])` sorteert
eerst aflopend op aantal en dan oplopend op woord. Python vergelijkt tuples
element per element. Zonder die tweede sleutel is de volgorde van woorden met
hetzelfde aantal willekeurig, en dan ziet je uitvoer er bij elke uitvoering
anders uit.

**Leestekens strippen met een reeks.** `ruw.strip(LEESTEKENS)` haalt links en
rechts elk teken uit die reeks weg. `"restaurant."` wordt `"restaurant"` en
`'"Het'` wordt `"Het"`.

**Twee keer door het bestand lopen.** `kengetallen` en `tel_woorden` openen het
bestand elk apart. Dat is bewust: elke functie doet één ding, en een geopend
bestand kun je maar één keer doorlopen. Wil je dat vermijden, lees dan één keer
in een lijst.

**De uitvoer opbouwen als lijst.** Alle regels komen eerst in `regels_uit`, en
pas op het einde gaat alles in één keer naar het bestand. Daardoor kun je
hetzelfde resultaat ook afdrukken, of testen, zonder de code te wijzigen.

**`.rstrip("\\n")` bij het tellen van tekens.** Anders telt elk regeleinde mee
als teken. Of dat de bedoeling is, hangt van je definitie af. Kies bewust en
schrijf het op.

**De opruiming.** De laatste twee regels verwijderen de bestanden weer. In een
oefening is dat netjes; in een echt programma verwijder je nooit iets zonder dat
de gebruiker het vroeg.
