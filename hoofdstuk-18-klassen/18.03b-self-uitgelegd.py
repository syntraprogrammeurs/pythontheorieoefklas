# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.3 self uitgelegd
#
# self is de eerste parameter van elke methode, en je geeft hem nooit mee bij het
# aanroepen. Python vult hem zelf in.

class Boek:
    def __init__(self, titel):
        self.titel = titel

    def toon(self):
        print(self.titel)


boek = Boek("Het diner")
boek.toon()
Boek.toon(boek)


# Verwachte uitvoer:
# Het diner
# Het diner
