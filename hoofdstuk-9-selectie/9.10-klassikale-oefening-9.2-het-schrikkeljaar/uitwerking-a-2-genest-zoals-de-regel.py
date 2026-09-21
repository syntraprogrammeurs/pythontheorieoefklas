# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Klassikale oefening 9.2 — Het schrikkeljaar, uitwerking
#
# 2 — Genest, zoals de regel is opgeschreven.

for jaar in (1900, 2000, 2024, 2025):
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            if jaar % 400 == 0:
                schrikkeljaar = True
            else:
                schrikkeljaar = False
        else:
            schrikkeljaar = True
    else:
        schrikkeljaar = False

    print(f"{jaar}: {schrikkeljaar}")


# Verwachte uitvoer:
# 1900: False
# 2000: True
# 2024: True
# 2025: False
