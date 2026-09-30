<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 12.1 — De wachtlijst

Uit *Python basis — theoriebundel*, hoofdstuk 12 (Lijsten — en waarom Python geen arrays heeft), paragraaf 12.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** De club is vol: er is plaats voor tien leden. Wie zich daarna
aanmeldt, komt op een wachtlijst. Wanneer iemand vertrekt, schuift de eerste van
de wachtlijst door.

**Wat je maakt.** Functies voor:

1. `meld_aan(leden, wachtlijst, naam)`: naar de ledenlijst als er plaats is,
   anders naar de wachtlijst. Een dubbele aanmelding wordt geweigerd.
2. `vertrek(leden, wachtlijst, naam)`: haalt iemand weg en schuift de eerste van
   de wachtlijst door.
3. `toon(leden, wachtlijst)`: toont beide lijsten genummerd.

Test met een club die volloopt, drie mensen op de wachtlijst, en twee
vertrekkers.

## Uitwerking

```python
# De Leeslamp — leden en wachtlijst
# Cursus Python basis, hoofdstuk 12, oefening 1

MAX_LEDEN = 10


def meld_aan(leden: list, wachtlijst: list, naam: str) -> str:
    """Meldt iemand aan. Geeft terug wat er gebeurd is."""
    if naam in leden:
        return f"{naam} is al lid"
    if naam in wachtlijst:
        return f"{naam} staat al op de wachtlijst"

    if len(leden) < MAX_LEDEN:
        leden.append(naam)
        return f"{naam} is lid geworden"

    wachtlijst.append(naam)
    return f"{naam} staat op de wachtlijst, plaats {len(wachtlijst)}"


def vertrek(leden: list, wachtlijst: list, naam: str) -> str:
    """Laat iemand vertrekken en schuift de wachtlijst door."""
    if naam not in leden:
        return f"{naam} is geen lid"

    leden.remove(naam)
    if wachtlijst:
        volgende = wachtlijst.pop(0)
        leden.append(volgende)
        return f"{naam} vertrekt; {volgende} schuift door"
    return f"{naam} vertrekt; de wachtlijst is leeg"


def toon(leden: list, wachtlijst: list) -> str:
    """Beide lijsten als tekst."""
    regels = [f"Leden ({len(leden)}/{MAX_LEDEN})"]
    for nummer, naam in enumerate(leden, start=1):
        regels.append(f"  {nummer:>2}. {naam}")

    regels.append(f"Wachtlijst ({len(wachtlijst)})")
    if not wachtlijst:
        regels.append("   (leeg)")
    for nummer, naam in enumerate(wachtlijst, start=1):
        regels.append(f"  {nummer:>2}. {naam}")
    return "\n".join(regels)


leden = []
wachtlijst = []

kandidaten = [
    "Anke", "Bram", "Cato", "Dirk", "Els", "Femke", "Gert", "Hilde",
    "Ilse", "Jan", "Karel", "Lien", "Mo", "Anke",
]

for naam in kandidaten:
    print(meld_aan(leden, wachtlijst, naam))

print()
print(vertrek(leden, wachtlijst, "Cato"))
print(vertrek(leden, wachtlijst, "Anke"))
print(vertrek(leden, wachtlijst, "Zoe"))
print()
print(toon(leden, wachtlijst))
```

```text
Anke is lid geworden
Bram is lid geworden
Cato is lid geworden
Dirk is lid geworden
Els is lid geworden
Femke is lid geworden
Gert is lid geworden
Hilde is lid geworden
Ilse is lid geworden
Jan is lid geworden
Karel staat op de wachtlijst, plaats 1
Lien staat op de wachtlijst, plaats 2
Mo staat op de wachtlijst, plaats 3
Anke is al lid

Cato vertrekt; Karel schuift door
Anke vertrekt; Lien schuift door
Zoe is geen lid

Leden (10/10)
   1. Bram
   2. Dirk
   3. Els
   4. Femke
   5. Gert
   6. Hilde
   7. Ilse
   8. Jan
   9. Karel
  10. Lien
Wachtlijst (1)
   1. Mo
```

**De vijf beslissingen.**

**`pop(0)` voor de wachtlijst.** Wie het eerst komt, schuift het eerst door. Dat
is een **queue** of wachtrij, en je ziet ze in hoofdstuk 19 terug als
datastructuur. Daar leer je ook dat `pop(0)` op een grote lijst traag is, en wat
je in de plaats gebruikt.

**Twee controles bij het aanmelden.** Iemand kan al lid zijn óf al op de
wachtlijst staan. Vergeet je de tweede, dan kan Mo drie keer op de wachtlijst
komen. Bijzondere gevallen zijn zelden alleen.

**Een tekst teruggeven in plaats van afdrukken.** Elke functie geeft een zin
terug; het hoofdprogramma drukt af. Dat is de regel uit hoofdstuk 11, en je
merkt hier waarom: je kunt de teruggegeven zin testen met `==`. Zou de functie
zelf afdrukken, dan kon je alleen kijken.

**De volgorde in `vertrek`.** Eerst weghalen, dan doorschuiven. Zou je het
omdraaien, dan zit de club één ogenblik met elf leden. Bij deze code merk je dat
niet, maar bij een programma dat tussendoor iets anders doet, wel.

**Waarom `if wachtlijst:` en niet `if len(wachtlijst) > 0:`.** De truthiness uit
hoofdstuk 7. Een lege lijst is onwaar.

**Wat opvalt aan de uitvoer.** De ledenlijst is niet meer alfabetisch nadat er
mensen doorschoven. Dat is juist: `append` zet ze achteraan. Wil je een
alfabetisch overzicht, sorteer dan bij het **tonen** en niet bij het bewaren.
De volgorde van aankomst is namelijk zelf informatie.
