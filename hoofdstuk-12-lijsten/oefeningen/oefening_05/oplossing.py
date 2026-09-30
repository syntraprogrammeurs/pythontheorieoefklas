# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 5 — Hoe vaak werd een boek uitgeleend?

uitleningen = ["Het diner", "Turks fruit", "Het diner",
               "De aanslag", "Het diner", "Turks fruit"]
zoeken = ["Het diner", "De aanslag", "Max Havelaar"]

for titel in zoeken:
    if titel in uitleningen:
        aantal = uitleningen.count(titel)
        positie = uitleningen.index(titel)
        print(f"{titel}: {aantal} keer, eerst op positie {positie}")
    else:
        print(f"{titel}: nooit uitgeleend")

# index() geeft een ValueError als de titel niet in de lijst staat.
