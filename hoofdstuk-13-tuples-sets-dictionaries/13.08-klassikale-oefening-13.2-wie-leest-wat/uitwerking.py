# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Klassikale oefening 13.2 — Wie leest wat?, uitwerking

# De Leeslamp — wie leest wat
# Cursus Python basis, hoofdstuk 13, oefening 2

CATALOGUS = {
    "Het diner", "Turks fruit", "De aanslag", "Max Havelaar",
    "De ontdekking", "Nooit meer slapen",
}

gelezen = {
    "Anke": {"Het diner", "Turks fruit", "De aanslag", "Max Havelaar"},
    "Bram": {"De aanslag", "De ontdekking"},
    "Cato": {"De aanslag", "Max Havelaar", "De ontdekking", "Het diner"},
}

anke = gelezen["Anke"]
bram = gelezen["Bram"]
cato = gelezen["Cato"]

# 1 — door iedereen gelezen
door_iedereen = anke & bram & cato

# 2 — door niemand gelezen
door_iemand = anke | bram | cato
door_niemand = CATALOGUS - door_iemand

# 3 — door precies één gelezen
telling = {}
for titels in gelezen.values():
    for titel in titels:
        telling[titel] = telling.get(titel, 0) + 1
door_een = {titel for titel, aantal in telling.items() if aantal == 1}

# 4 — Anke wel, Bram niet
alleen_anke = anke - bram

print("Door iedereen gelezen :", sorted(door_iedereen))
print("Door niemand gelezen  :", sorted(door_niemand))
print("Door precies één      :", sorted(door_een))
print("Anke wel, Bram niet   :", sorted(alleen_anke))
print("Samen verschillend    :", len(door_iemand))

print()
print(f"{'Titel':<20}{'Gelezen door':>13}")
print("-" * 33)
for titel in sorted(CATALOGUS):
    print(f"{titel:<20}{telling.get(titel, 0):>13}")


# Verwachte uitvoer:
# Door iedereen gelezen : ['De aanslag']
# Door niemand gelezen  : ['Nooit meer slapen']
# Door precies één      : ['Turks fruit']
# Anke wel, Bram niet   : ['Het diner', 'Max Havelaar', 'Turks fruit']
# Samen verschillend    : 5
#
# Titel                Gelezen door
# ---------------------------------
# De aanslag                      3
# De ontdekking                   2
# Het diner                       2
# Max Havelaar                    2
# Nooit meer slapen               0
# Turks fruit                     1
