# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.9 Het raadspel
#
# Dit is het stroomdiagram uit oefening 3.2, nu in code.

# De Leeslamp — het raadspel
# Cursus Python basis, hoofdstuk 10


        # normaal met random, zie hoofdstuk 17


MAX_POGINGEN = int(input("Hoeveel pogingen wens je uit te voeren:"))
GEHEIM = int(input("Geef een geheim nummer in:"))



# Verwachte uitvoer:
# Poging 1: 50 is te hoog
# Poging 2: 25 is te laag
# Poging 3: 37 is te laag
# Poging 4: 43 is te hoog
# Poging 5: 40 is te laag
# Juist! In 6 pogingen.
