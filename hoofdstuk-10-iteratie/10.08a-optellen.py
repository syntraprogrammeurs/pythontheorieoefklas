# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.8 De patronen die je constant nodig hebt — Optellen

bladzijden = [320, 180, 250, 410]
totaal = 0

for aantal in bladzijden:
    totaal += aantal

print(totaal)
print(sum(bladzijden))


# Verwachte uitvoer:
# 1160
# 1160
