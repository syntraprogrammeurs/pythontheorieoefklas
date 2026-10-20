<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 17.2 — De boekentombola

Uit *Python basis — theoriebundel*, hoofdstuk 17 (Modules, de standaardbibliotheek en `pip`), paragraaf 17.8.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** De club verloot elk jaar boeken onder haar leden. Je schrijft
het trekkingsprogramma. Het moet eerlijk zijn, herhaalbaar voor de controle, en
niemand mag twee keer winnen.

**Wat je maakt.**

1. `trek_winnaars(leden, aantal, seed)` die `aantal` verschillende winnaars
   trekt, met een vaste seed zodat de trekking te controleren is.
2. `koppel_prijzen(winnaars, prijzen)` die elk een prijs geeft.
3. Toon dat dezelfde seed dezelfde uitslag geeft en een andere seed niet.
4. Vang af wat er gebeurt wanneer er meer prijzen dan leden zijn.
5. Toon per lid hoe vaak het over honderd trekkingen wint, en zeg of dat
   eerlijk lijkt.

## Uitwerking

```python
# De Leeslamp — de boekentombola
# Cursus Python basis, hoofdstuk 17, oefening 2

import random
from collections import Counter

LEDEN = ["Anke", "Bram", "Cato", "Dirk", "Els", "Femke", "Gert", "Hilde"]
PRIJZEN = ["Het diner", "Turks fruit", "De aanslag"]


def trek_winnaars(leden: list, aantal: int, seed: int) -> list:
    """`aantal` verschillende winnaars. Dezelfde seed geeft dezelfde uitslag."""
    if aantal > len(leden):
        raise ValueError(
            f"{aantal} prijzen voor {len(leden)} leden: dat kan niet zonder dubbels"
        )
    generator = random.Random(seed)
    return generator.sample(leden, aantal)


def koppel_prijzen(winnaars: list, prijzen: list) -> list:
    """Paren van winnaar en prijs."""
    return list(zip(winnaars, prijzen, strict=True))


print("Trekking met seed 2026:")
for winnaar, prijs in koppel_prijzen(trek_winnaars(LEDEN, 3, 2026), PRIJZEN):
    print(f"  {winnaar:<8}wint {prijs}")

print()
print("Dezelfde seed, opnieuw:")
print(" ", trek_winnaars(LEDEN, 3, 2026))
print("Een andere seed:")
print(" ", trek_winnaars(LEDEN, 3, 2027))

print()
try:
    trek_winnaars(LEDEN, 20, 2026)
except ValueError as fout:
    print("Geweigerd:", fout)

print()
print("Honderd trekkingen van drie winnaars:")
telling = Counter()
for seed in range(100):
    telling.update(trek_winnaars(LEDEN, 3, seed))

for lid in LEDEN:
    aantal = telling[lid]
    print(f"  {lid:<8}{aantal:>4}  {'*' * aantal}")

print()
print(f"  totaal   {sum(telling.values()):>4}  (100 trekkingen x 3 winnaars)")
print(f"  verwacht {100 * 3 / len(LEDEN):>4.0f} per lid")
```

```text
Trekking met seed 2026:
  Bram    wint Het diner
  Cato    wint Turks fruit
  Els     wint De aanslag

Dezelfde seed, opnieuw:
  ['Bram', 'Cato', 'Els']
Een andere seed:
  ['Bram', 'Dirk', 'Anke']

Geweigerd: 20 prijzen voor 8 leden: dat kan niet zonder dubbels

Honderd trekkingen van drie winnaars:
  Anke      35  ***********************************
  Bram      32  ********************************
  Cato      42  ******************************************
  Dirk      39  ***************************************
  Els       41  *****************************************
  Femke     37  *************************************
  Gert      34  **********************************
  Hilde     40  ****************************************

  totaal    300  (100 trekkingen x 3 winnaars)
  verwacht   38 per lid
```

**De zes punten.**

**`random.Random(seed)` en niet `random.seed(seed)`.** De tweede vorm zet de
**globale** toevalsgenerator om. Roept iemand anders in je programma daarna
`random.randint()` aan, dan zit die vast aan jouw seed. Met `random.Random(seed)`
maak je een eigen generator die alleen deze functie gebruikt. Dat is de
netheidsregel uit hoofdstuk 11 over globale toestand, toegepast op toeval.

**`sample` en niet `choice` in een lus.** `sample` trekt zonder teruglegging:
niemand kan twee keer winnen. Met `choice` in een lus zou dat wel kunnen, en dan
had je een controle en een herhaling nodig.

**De controle vóór de trekking.** `sample` geeft zelf ook een `ValueError` bij
te veel prijzen, maar met de melding *Sample larger than population*. Jouw
melding zegt wat er in dit programma aan de hand is. Een goede foutmelding
spreekt de taal van het probleem, niet die van de bibliotheek.

**`zip(..., strict=True)`.** Zonder `strict` zou een lijst met vier winnaars en
drie prijzen stilzwijgend één winnaar laten vallen. Met `strict=True` krijg je
een fout. Dat is de waarschuwing uit hoofdstuk 10, hier toegepast.

**`Counter.update()` in plaats van zelf tellen.** `telling.update(lijst)` telt
alle elementen van die lijst bij de bestaande telling op. Dat spaart de lus met
`.get(x, 0) + 1` uit hoofdstuk 13.

**Is de trekking eerlijk?** Elk lid zou gemiddeld 37,5 keer moeten winnen. De
werkelijke aantallen liggen tussen 33 en 41. Dat is normale spreiding bij
honderd trekkingen: bij toeval is een perfect gelijke verdeling juist verdacht.
Wil je zekerder zijn, doe dan tienduizend trekkingen en kijk of de afwijking
verhoudingsgewijs kleiner wordt.

Dat laatste is precies het soort redenering uit hoofdstuk 28 over inductie: je
trekt een besluit uit waarnemingen, en je moet weten hoe sterk je besluit is.
