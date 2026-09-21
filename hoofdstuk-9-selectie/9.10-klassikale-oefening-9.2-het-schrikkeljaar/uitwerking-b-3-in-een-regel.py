# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Klassikale oefening 9.2 — Het schrikkeljaar, uitwerking
#
# 3 — In één regel.

for jaar in (1900, 2000, 2024, 2025):
    schrikkeljaar = jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)
    print(f"{jaar}: {schrikkeljaar}")


# Verwachte uitvoer:
# 1900: False
# 2000: True
# 2024: True
# 2025: False
