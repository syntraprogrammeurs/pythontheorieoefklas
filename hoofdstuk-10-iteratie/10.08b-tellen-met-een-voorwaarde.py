# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.8 De patronen die je constant nodig hebt — Tellen met een voorwaarde

bladzijden = [320, 180, 250, 410]
dikke = 0

for aantal in bladzijden:
    if aantal > 300:
        dikke += 1

print(f"{dikke} dikke boeken")


# Verwachte uitvoer:
# 2 dikke boeken
