<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 16.1 — Het uitleenregister

Uit *Python basis — theoriebundel*, hoofdstuk 16 (Bestanden lezen en schrijven), paragraaf 16.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** De club wil bijhouden wie welk boek wanneer geleend heeft. Elke
uitlening komt als één regel in een bestand.

**Wat je maakt.**

1. `noteer_uitlening(pad, lid, titel, datum)` die één regel **toevoegt**, zonder
   het bestaande te wissen.
2. `lees_uitleningen(pad)` die alle uitleningen als lijst van dictionaries
   geeft, met foute regels overgeslagen en gemeld.
3. `per_lid(uitleningen)` die per lid telt hoeveel boeken het geleend heeft.
4. `boeken_van(uitleningen, lid)` die de titels van één lid geeft.
5. Een overzicht.

Test met zes uitleningen, waaronder één kapotte regel.

## Uitwerking

```python
# De Leeslamp — het uitleenregister
# Cursus Python basis, hoofdstuk 16, oefening 1

from pathlib import Path

REGISTER = Path("uitleningen.csv")
SCHEIDING = ";"


def noteer_uitlening(pad: Path, lid: str, titel: str, datum: str) -> None:
    """Voegt één uitlening toe aan het register."""
    if SCHEIDING in lid or SCHEIDING in titel:
        raise ValueError(f"een veld mag geen {SCHEIDING!r} bevatten")
    with open(pad, "a", encoding="utf-8") as bestand:
        bestand.write(f"{datum}{SCHEIDING}{lid}{SCHEIDING}{titel}\n")


def lees_uitleningen(pad: Path) -> list:
    """Alle uitleningen. Foute regels worden gemeld en overgeslagen."""
    if not pad.exists():
        return []

    uit = []
    with open(pad, encoding="utf-8") as bestand:
        for nummer, regel in enumerate(bestand, start=1):
            regel = regel.strip()
            if not regel:
                continue
            delen = regel.split(SCHEIDING)
            if len(delen) != 3:
                print(f"  regel {nummer} overgeslagen: {regel!r}")
                continue
            uit.append({"datum": delen[0], "lid": delen[1], "titel": delen[2]})
    return uit


def per_lid(uitleningen: list) -> dict:
    """Per lid het aantal uitleningen."""
    telling = {}
    for u in uitleningen:
        telling[u["lid"]] = telling.get(u["lid"], 0) + 1
    return telling


def boeken_van(uitleningen: list, lid: str) -> list:
    """De titels die dit lid geleend heeft, in volgorde van uitlening."""
    return [u["titel"] for u in uitleningen if u["lid"].lower() == lid.lower()]


if REGISTER.exists():
    REGISTER.unlink()

noteer_uitlening(REGISTER, "Anke Peeters", "Het diner", "2026-09-01")
noteer_uitlening(REGISTER, "Bram Coppens", "Turks fruit", "2026-09-02")
noteer_uitlening(REGISTER, "Anke Peeters", "De aanslag", "2026-09-05")
noteer_uitlening(REGISTER, "Cato Dhondt", "Max Havelaar", "2026-09-05")
noteer_uitlening(REGISTER, "Anke Peeters", "De ontdekking", "2026-09-11")

with open(REGISTER, "a", encoding="utf-8") as bestand:
    bestand.write("dit is geen geldige regel\n")

try:
    noteer_uitlening(REGISTER, "Els;Janssens", "Iets", "2026-09-12")
except ValueError as fout:
    print("Geweigerd bij het schrijven:", fout)

print()
uitleningen = lees_uitleningen(REGISTER)

print()
print(f"{'Datum':<12}{'Lid':<16}Titel")
print("-" * 48)
for u in uitleningen:
    print(f"{u['datum']:<12}{u['lid']:<16}{u['titel']}")

print()
print("Aantal per lid:")
for lid, aantal in sorted(per_lid(uitleningen).items(), key=lambda p: -p[1]):
    print(f"  {lid:<16}{aantal}")

print()
print("Anke leende:", boeken_van(uitleningen, "anke peeters"))
print("Totaal      :", len(uitleningen), "uitleningen")

REGISTER.unlink()
```

```text
Geweigerd bij het schrijven: een veld mag geen ';' bevatten

  regel 6 overgeslagen: 'dit is geen geldige regel'

Datum       Lid             Titel
------------------------------------------------
2026-09-01  Anke Peeters    Het diner
2026-09-02  Bram Coppens    Turks fruit
2026-09-05  Anke Peeters    De aanslag
2026-09-05  Cato Dhondt     Max Havelaar
2026-09-11  Anke Peeters    De ontdekking

Aantal per lid:
  Anke Peeters    3
  Bram Coppens    1
  Cato Dhondt     1

Anke leende: ['Het diner', 'De aanslag', 'De ontdekking']
Totaal      : 5 uitleningen
```

**De zes beslissingen.**

**`"a"` en niet `"w"`.** Een register groeit; je overschrijft het nooit. Zou je
`"w"` gebruiken, dan bevat het bestand na elke uitlening precies één regel, en
was alles daarvoor weg. Onherroepelijk.

**Weigeren bij het schrijven, niet bij het lezen.** `noteer_uitlening` werpt een
fout wanneer een veld een puntkomma bevat. Dat is het juiste moment: schrijf je
zo'n regel weg, dan is het bestand kapot en kun je het achteraf niet meer
betrouwbaar herstellen. Bewaak de ingang.

**De datum als `2026-09-01`.** In die schrijfwijze sorteert een datum als tekst
vanzelf chronologisch. `01/09/2026` doet dat niet. Deze vorm heet ISO 8601 en je
gebruikt hem overal waar je datums als tekst bewaart.

**De datum vooraan.** Daardoor staat het register vanzelf in de goede volgorde
zodra je het sorteert. De volgorde van je velden is een ontwerpkeuze.

**`sorted(..., key=lambda p: -p[1])`.** Het minteken sorteert aflopend zonder
`reverse=True`. Beide werken; `reverse=True` leest beter. Het minteken werkt
alleen bij getallen.

**Hoofdletterongevoelig zoeken.** `u["lid"].lower() == lid.lower()`, zodat
`"anke peeters"` de uitleningen van `"Anke Peeters"` vindt. Bij invoer van
mensen doe je dit altijd.

**Wat er nog aan schort.** Het register wordt bij elke opvraging volledig
ingelezen. Bij vijf regels is dat prima; bij vijf miljoen niet. Dan gebruik je
een databank. Weet waar de grens van deze aanpak ligt.
