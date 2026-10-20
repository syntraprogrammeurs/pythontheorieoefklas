# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# Klassikale oefening 17.2 — De boekentombola, uitwerking

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


# Verwachte uitvoer:
# Trekking met seed 2026:
#   Bram    wint Het diner
#   Cato    wint Turks fruit
#   Els     wint De aanslag
#
# Dezelfde seed, opnieuw:
#   ['Bram', 'Cato', 'Els']
# Een andere seed:
#   ['Bram', 'Dirk', 'Anke']
#
# Geweigerd: 20 prijzen voor 8 leden: dat kan niet zonder dubbels
#
# Honderd trekkingen van drie winnaars:
#   Anke      35  ***********************************
#   Bram      32  ********************************
#   Cato      42  ******************************************
#   Dirk      39  ***************************************
#   Els       41  *****************************************
#   Femke     37  *************************************
#   Gert      34  **********************************
#   Hilde     40  ****************************************
#
#   totaal    300  (100 trekkingen x 3 winnaars)
#   verwacht   38 per lid
