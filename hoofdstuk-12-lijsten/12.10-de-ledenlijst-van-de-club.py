# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.10 De ledenlijst van de club

# De Leeslamp — de ledenlijst
# Cursus Python basis, hoofdstuk 12


def voeg_lid_toe(leden: list, naam: str) -> list:
    """Voegt een lid toe, tenzij het er al in staat. Geeft de lijst terug."""
    if naam in leden:
        print(f"{naam} staat er al in")
    else:
        leden.append(naam)
    return leden


def verwijder_lid(leden: list, naam: str) -> list:
    """Haalt een lid uit de lijst, als het erin staat."""
    if naam in leden:
        leden.remove(naam)
    else:
        print(f"{naam} staat er niet in")
    return leden


def zoek_lid(leden: list, deel: str) -> list:
    """Alle namen waarin `deel` voorkomt, ongeacht hoofdletters."""
    gevonden = []
    for naam in leden:
        if deel.lower() in naam.lower():
            gevonden.append(naam)
    return gevonden


leden = ["Anke Peeters", "Bram Coppens", "Cato Dhondt"]

voeg_lid_toe(leden, "Dirk Vermeulen")
voeg_lid_toe(leden, "Anke Peeters")
verwijder_lid(leden, "Bram Coppens")
verwijder_lid(leden, "Zoe Janssens")

print()
print("De lijst, alfabetisch:")
for nummer, naam in enumerate(sorted(leden, key=str.lower), start=1):
    print(f"{nummer}. {naam}")

print()
print("Gezocht op 'an':", zoek_lid(leden, "an"))
print("Aantal leden   :", len(leden))


# Verwachte uitvoer:
# Anke Peeters staat er al in
# Zoe Janssens staat er niet in
#
# De lijst, alfabetisch:
# 1. Anke Peeters
# 2. Cato Dhondt
# 3. Dirk Vermeulen
#
# Gezocht op 'an': ['Anke Peeters']
# Aantal leden   : 3
