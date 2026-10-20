# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.12 Veelgemaakte fouten
#
# De op één na laatste rij verdient aandacht. Dit werkt gewoon:

class Boek:
    def __init__(self, titel):
        self.titel = titel


boek = Boek("Het diner")
boek.jaartal = 2009
print(boek.jaartal)


# Verwachte uitvoer:
# 2009
