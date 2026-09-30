# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 10 — De ledenlijst van de club

leden = [
    ["Anke Peeters", 34, 3],
    ["Bram Coppens", 20, 1],
    ["Cato Dhondt", 11, 4],
    ["Dirk Maes", 67, 12],
]

leden.append(["Emma Claes", 16, 0])
print(f"{len(leden)} leden")

for naam, leeftijd, jaren in sorted(leden, key=lambda lid: lid[2], reverse=True):
    print(f"{naam:<16}{jaren:>3} jaar lid")

minderjarig = []
for naam, leeftijd, jaren in leden:
    if leeftijd < 18:
        minderjarig.append(naam)
print(f"Minderjarig: {minderjarig}")

totaal = 0
for naam, leeftijd, jaren in leden:
    totaal += leeftijd
print(f"Gemiddelde leeftijd: {totaal / len(leden)}")
