# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 3 — Boekgegevens tonen

def toon_boek(titel, auteur, jaar):
    print(f"{titel} van {auteur} ({jaar})")


toon_boek("Het diner", "Herman Koch", 2009)
toon_boek(jaar=1969, auteur="Jan Wolkers", titel="Turks fruit")
