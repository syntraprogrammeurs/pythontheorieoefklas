# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.5 enumerate en zip
#
# Je hebt vaak de positie én de waarde nodig. Dit is de manier waarop beginners het
# schrijven:

leden = ["Anke", "Bram", "Cato"]

for i in range(len(leden)):
    print(f"{i + 1}. {leden[i]}")


# Verwachte uitvoer:
# 1. Anke
# 2. Bram
# 3. Cato
