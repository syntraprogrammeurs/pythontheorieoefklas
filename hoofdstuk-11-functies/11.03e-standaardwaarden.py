# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.3 Parameters en argumenten — Standaardwaarden
#
# De oplossing is altijd dezelfde: gebruik None en maak de lijst binnenin.

def voeg_toe(boek, lijst=None):
    if lijst is None:
        lijst = []
    lijst.append(boek)
    return lijst


print(voeg_toe("Het diner"))
print(voeg_toe("Turks fruit"))


# Verwachte uitvoer:
# ['Het diner']
# ['Turks fruit']
