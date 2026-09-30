# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.3 Parameters en argumenten
#
# Meerdere parameters, gescheiden door komma's:

def toon_lid(naam, leeftijd, stad):
    print(f"{naam} ({leeftijd}) uit {stad}")


toon_lid("Anke", 34, "Gent")
toon_lid(leeftijd=41, stad="Brugge", naam="Bram")


# Verwachte uitvoer:
# Anke (34) uit Gent
# Bram (41) uit Brugge
