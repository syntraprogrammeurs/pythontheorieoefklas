# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.8 De patronen die je constant nodig hebt — Het grootste zoeken

bladzijden = [320, 180, 250, 410]
grootste = bladzijden[0]

for aantal in bladzijden:
    if aantal > grootste:
        grootste = aantal

print(grootste)


# Verwachte uitvoer:
# 410
