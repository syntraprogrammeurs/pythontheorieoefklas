# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.3 Parameters en argumenten — Standaardwaarden
#
# Gebruik nooit een lijst of een dictionary als standaardwaarde:

def voeg_toe(boek, lijst=[]):
    lijst.append(boek)
    return lijst


print(voeg_toe("Het diner"))
print(voeg_toe("Turks fruit"))


# Verwachte uitvoer:
# ['Het diner']
# ['Het diner', 'Turks fruit']
