# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.4 if __name__ == "__main__"

def bereken_lidgeld(leeftijd: int) -> int:
    """Het lidgeld voor deze leeftijd."""
    return 0 if leeftijd < 12 else 30


def zelftest() -> None:
    """Een snelle controle van deze module."""
    print("zelftest van berekeningen")
    print(" 11 jaar ->", bereken_lidgeld(11))
    print(" 34 jaar ->", bereken_lidgeld(34))

# DUNDER. DOUBLE UNDER. (magic const). Door er twee underscores voor en achter te zetten (zoals __name__), voorkomt Python dat deze variabelen per 
# ongeluk botsen met variabelen die je zelf bedenkt (zoals een functie die je zomaar name zou noemen).
if __name__ == "__main__":
    zelftest()


# Verwachte uitvoer:
# zelftest van berekeningen
#  11 jaar -> 0
#  34 jaar -> 30
