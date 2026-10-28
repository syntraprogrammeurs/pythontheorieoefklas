# Python basis — theoriebundel
# Hoofdstuk 22 — Logica en kritisch denken: de basisbegrippen
# 22.7 Wanneer je code geldig is en toch fout
#
# Het onderscheid uit 22.5 is geen woordenspel. Hier is het in Python.

# De Leeslamp — de redenering klopt, de premisse niet
KORTING_VANAF = 3          # aanname: korting vanaf 3 boeken per maand


def prijs(boeken):
    """De maandprijs: 2 euro per boek, met korting vanaf de drempel."""
    if boeken >= KORTING_VANAF:
        return boeken * 2 - 1
    return boeken * 2


for aantal in (1, 2, 3, 4):
    print(f"{aantal} boeken: {prijs(aantal)} euro")


# Verwachte uitvoer:
# 1 boeken: 2 euro
# 2 boeken: 4 euro
# 3 boeken: 5 euro
# 4 boeken: 7 euro
