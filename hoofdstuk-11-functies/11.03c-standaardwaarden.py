# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.3 Parameters en argumenten — Standaardwaarden

def toon_lid(naam, leeftijd, stad="Gent"):
    print(f"{naam} ({leeftijd}) uit {stad}")


toon_lid("Anke", 34)
toon_lid("Bram", 41, "Brugge")


# Verwachte uitvoer:
# Anke (34) uit Gent
# Bram (41) uit Brugge
