# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.9 Het raadspel
#
# Dit is het stroomdiagram uit oefening 3.2, nu in code.

# De Leeslamp — het raadspel
# Cursus Python basis, hoofdstuk 10

MAX_POGINGEN = 7
GEHEIM = 42          # normaal met random, zie hoofdstuk 17

gokken = [50, 25, 37, 43, 40, 42]
pogingen = 0

for gok in gokken:
    pogingen += 1
    if gok == GEHEIM:
        print(f"Juist! In {pogingen} pogingen.")
        break
    if gok < GEHEIM:
        print(f"Poging {pogingen}: {gok} is te laag")
    else:
        print(f"Poging {pogingen}: {gok} is te hoog")
    if pogingen == MAX_POGINGEN:
        print(f"Op. Het was {GEHEIM}.")
        break


# Verwachte uitvoer:
# Poging 1: 50 is te hoog
# Poging 2: 25 is te laag
# Poging 3: 37 is te laag
# Poging 4: 43 is te hoog
# Poging 5: 40 is te laag
# Juist! In 6 pogingen.
