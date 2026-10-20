# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.5 Klasseattributen
#
# LIDWOORDEN staat in de klasse maar niet in __init__. Dat is een klasseattribuut: het
# hoort bij de klasse, niet bij één object.

class Boek:
    LIDWOORDEN = ("de", "het", "een")
    aantal = 0

    def __init__(self, titel: str):
        self.titel = titel
        Boek.aantal += 1


a = Boek("Het diner")
b = Boek("Turks fruit")


print(Boek.aantal)
print(a.LIDWOORDEN is b.LIDWOORDEN)


# Verwachte uitvoer:
# 2
# True
