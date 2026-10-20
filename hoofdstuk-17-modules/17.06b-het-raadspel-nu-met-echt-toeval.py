# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.6 Het raadspel, nu met echt toeval
#
# De versie die je in de les speelt, met echte invoer:
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# Dit voorbeeld wacht op invoer; voer het uit in je eigen terminal.
import random

geheim = random.randint(1, 100)

for poging in range(1, 8):
    gok = int(input(f"Poging {poging}/7: "))
    if gok == geheim:
        print("Juist!")
        break
    print("Te laag" if gok < geheim else "Te hoog")
else:
    print(f"Op. Het was {geheim}.")
