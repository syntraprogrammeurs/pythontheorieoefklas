# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.3 self uitgelegd
#
# Dit is het enige echt verwarrende stuk van dit hoofdstuk.

class Boek:
    """Eén boek."""

    def __init__(self, titel: str):
        self.titel = titel


een = Boek("Het diner")
twee = Boek("Turks fruit")

print(een.titel)
print(twee.titel)
print(een is twee)


# Verwachte uitvoer:
# Het diner
# Turks fruit
# False
