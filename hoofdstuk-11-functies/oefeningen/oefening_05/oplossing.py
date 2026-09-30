# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 5 — Kwadraten optellen

def kwadraat(getal):
    return getal * getal


getallen = [2, 3, 5, 7]
totaal = 0

for getal in getallen:
    totaal += kwadraat(getal)

print(f"Totaal: {totaal}")
