# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 7 — Titels op verschillende manieren sorteren

titels = ["Max Havelaar", "het diner", "Grand Hotel Europa", "Turks fruit"]

print(sorted(titels))
print(sorted(titels, key=lambda titel: titel.lower()))
print(sorted(titels, key=len))

# Hoofdletters komen voor kleine letters, dus "h" komt na "T".
