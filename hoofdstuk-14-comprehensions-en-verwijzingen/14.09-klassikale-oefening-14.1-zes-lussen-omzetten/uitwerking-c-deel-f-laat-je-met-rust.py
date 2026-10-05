# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.1 — Zes lussen omzetten, uitwerking
#
# F laat je met rust.

boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]

uit = []
vorige = ""
for titel, blz in sorted(boeken):
    if titel[0] != vorige:
        uit.append(f"--- {titel[0]} ---")
        vorige = titel[0]
    uit.append(f"{titel} ({blz})")

for regel in uit:
    print(regel)


# Verwachte uitvoer:
# --- D ---
# De aanslag (246)
# --- H ---
# Het diner (288)
# --- T ---
# Turks fruit (175)
