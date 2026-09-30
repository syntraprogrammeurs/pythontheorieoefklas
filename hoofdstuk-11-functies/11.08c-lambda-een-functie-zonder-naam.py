# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.8 lambda: een functie zonder naam
#
# De echte toepassing:

boeken = [
    ("Het diner", 2009, 288),
    ("Turks fruit", 1969, 175),
    ("De ontdekking van de hemel", 1992, 928),
]

op_jaar = sorted(boeken, key=lambda boek: boek[1])
op_dikte = sorted(boeken, key=lambda boek: boek[2], reverse=True)

for titel, jaar, bladzijden in op_jaar:
    print(f"{jaar}  {titel}")

print()
for titel, jaar, bladzijden in op_dikte:
    print(f"{bladzijden:>4}  {titel}")


# Verwachte uitvoer:
# 1969  Turks fruit
# 1992  De ontdekking van de hemel
# 2009  Het diner
#
#  928  De ontdekking van de hemel
#  288  Het diner
#  175  Turks fruit
