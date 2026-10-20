# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.7 Twee objecten vergelijken

class Boek:
    def __init__(self, titel: str, jaar: int):
        self.titel = titel
        self.jaar = jaar


a = Boek("Het diner", 2009)
b = Boek("Het diner", 2009)

print(a == b)
print(a is b)


# Verwachte uitvoer:
# False
# False
