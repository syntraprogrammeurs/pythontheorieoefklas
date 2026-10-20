# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.6 Het raadspel, nu met echt toeval

# De Leeslamp — het raadspel met random
# Cursus Python basis, hoofdstuk 17

import random

MINIMUM = 1
MAXIMUM = 100
MAX_POGINGEN = 7


def speel(geheim: int, gokken: list) -> str:
    """Speelt het spel met een vaste reeks gokken. Geeft het verslag terug."""
    regels = []
    for poging, gok in enumerate(gokken, start=1):
        if gok == geheim:
            regels.append(f"Poging {poging}: {gok} — juist!")
            return "\n".join(regels)
        if poging >= MAX_POGINGEN:
            regels.append(f"Poging {poging}: {gok} — op. Het was {geheim}.")
            return "\n".join(regels)
        richting = "te laag" if gok < geheim else "te hoog"
        regels.append(f"Poging {poging}: {gok} — {richting}")
    regels.append(f"Geen gokken meer. Het was {geheim}.")
    return "\n".join(regels)


def slimme_gokken(geheim: int) -> list:
    """De gokken van een speler die telkens het midden kiest."""
    laag, hoog = MINIMUM, MAXIMUM
    gokken = []
    for _ in range(MAX_POGINGEN):
        gok = (laag + hoog) // 2
        gokken.append(gok)
        if gok == geheim:
            break
        if gok < geheim:
            laag = gok + 1
        else:
            hoog = gok - 1
    return gokken


random.seed(2026)
geheim = random.randint(MINIMUM, MAXIMUM)

print(f"Het geheime getal is {geheim}.")
print()
print(speel(geheim, slimme_gokken(geheim)))
print()

random.seed(2026)
print("Drie willekeurige getallen met dezelfde seed:")
print([random.randint(MINIMUM, MAXIMUM) for _ in range(3)])
random.seed(2026)
print([random.randint(MINIMUM, MAXIMUM) for _ in range(3)])


# Verwachte uitvoer:
# Het geheime getal is 16.
#
# Poging 1: 50 — te hoog
# Poging 2: 25 — te hoog
# Poging 3: 12 — te laag
# Poging 4: 18 — te hoog
# Poging 5: 15 — te laag
# Poging 6: 16 — juist!
#
# Drie willekeurige getallen met dezelfde seed:
# [16, 41, 65]
# [16, 41, 65]
