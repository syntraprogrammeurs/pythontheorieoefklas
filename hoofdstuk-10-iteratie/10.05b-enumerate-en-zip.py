# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.5 enumerate en zip
#
# En dit is de Python-manier:

leden = ["Anke", "Bram", "Cato"]
start = 0
for nummer, lid in enumerate(leden, start=1):
    print(f"{nummer}. {lid}")


# Verwachte uitvoer:
# 1. Anke
# 2. Bram
# 3. Cato
