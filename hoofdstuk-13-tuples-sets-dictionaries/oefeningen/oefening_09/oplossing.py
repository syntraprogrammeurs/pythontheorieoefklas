# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 9 — De voorraad overlopen

voorraad = {"Het diner": 3, "Turks fruit": 0, "De aanslag": 5, "Max Havelaar": 1}

for titel, aantal in voorraad.items():
    print(f"{titel:<14}{aantal:>3}")

print(f"Totaal in voorraad: {sum(voorraad.values())}")

uitverkocht = []
for titel, aantal in voorraad.items():
    if aantal == 0:
        uitverkocht.append(titel)
print(f"Uitverkocht: {uitverkocht}")
