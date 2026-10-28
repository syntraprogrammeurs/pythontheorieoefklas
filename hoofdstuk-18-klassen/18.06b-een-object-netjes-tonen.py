# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.6 Een object netjes tonen
#
# Dat toont iets als <__main__.Boek object at 0x000001A2B3C4D5E6>. Niet erg
# behulpzaam.

class Boek:
    """Eén boek."""

    def __init__(self, titel: str, jaar: int):
        self.titel = titel
        self.jaar = jaar

    def __str__(self) -> str:
        """Wat print() toont."""
        return f"{self.titel} ({self.jaar})"

    def __repr__(self) -> str:
        """Wat je ziet in een lijst en tijdens het debuggen."""
        return f"Boek({self.titel!r}, {self.jaar})"
    


boek = Boek("Het diner", 2009)

print(boek, boek)
print([boek, boek, boek])

# Verwachte uitvoer:
# Het diner (2009)
# [Boek('Het diner', 2009), Boek('Het diner', 2009)]
