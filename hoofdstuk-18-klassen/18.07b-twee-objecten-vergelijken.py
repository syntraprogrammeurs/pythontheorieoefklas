# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.7 Twee objecten vergelijken
#
# Twee objecten met dezelfde inhoud zijn standaard niet gelijk. Python vergelijkt op
# identiteit, niet op inhoud. Wil je dat anders, schrijf dan __eq__:

class Boek:
    def __init__(self, titel: str, jaar: int):
        self.titel = titel
        self.jaar = jaar

    def __eq__(self, ander) -> bool:
        """Twee boeken zijn gelijk bij dezelfde titel en hetzelfde jaar."""
        if not isinstance(ander, Boek):
            return NotImplemented
        return self.titel == ander.titel and self.jaar == ander.jaar


a = Boek("Het diner", 2009)
b = Boek("Het diner", 2009)
c = Boek("Turks fruit", 1969)

print(a == b)
print(a == c)
print(a is b)


# Verwachte uitvoer:
# True
# False
# False
