# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.9 Het raadspel
#
# De versie met echte invoer, die je in de les uitvoert:
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# Dit voorbeeld wacht op invoer; voer het uit in je eigen terminal.
MAX_POGINGEN = 7
GEHEIM = 42

for poging in range(1, MAX_POGINGEN + 1):
    gok = int(input(f"Poging {poging}/{MAX_POGINGEN}, jouw gok: "))
    if gok == GEHEIM:
        print(f"Juist! In {poging} pogingen.")
        break
    print("Te laag" if gok < GEHEIM else "Te hoog")
else:
    print(f"Op. Het was {GEHEIM}.")
