# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.8 De patronen die je constant nodig hebt — Bouwen tijdens het lopen

namen = ["anke", "bram", "cato"]
netjes = []

for naam in namen:
    netjes.append(naam.capitalize())

print(netjes)


# Verwachte uitvoer:
# ['Anke', 'Bram', 'Cato']
