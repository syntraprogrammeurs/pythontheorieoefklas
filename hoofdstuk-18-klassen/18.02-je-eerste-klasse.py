# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.2 Je eerste klasse

class Boek:
    """Eén boek uit de catalogus van De Leeslamp."""

    def __init__(self, titel: str, schrijver: str, jaar: int):
        self.titel = titel
        self.schrijver = schrijver
        self.jaar = jaar



boek = Boek("Het diner", "Herman Koch", 2009)

boek2 = Boek("De leeslamp","MM", 2010);





print(boek.titel)
print(boek.jaar)
print(type(boek).__name__)
print(boek2.titel)



# Verwachte uitvoer:
# Het diner
# 2009
# Boek
