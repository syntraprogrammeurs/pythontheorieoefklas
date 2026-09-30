# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.6 break en continue

leden = ["Anke", "Bram", "", "Cato", "Dirk"]

for lid in leden:
    if lid == "":
        continue
    if lid == "Cato":
        print("Cato gevonden, we stoppen")
        break
    print(f"Bekeken: {lid}")


# Verwachte uitvoer:
# Bekeken: Anke
# Bekeken: Bram
# Cato gevonden, we stoppen
