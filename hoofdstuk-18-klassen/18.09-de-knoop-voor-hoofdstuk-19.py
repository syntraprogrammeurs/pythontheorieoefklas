# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.9 De knoop, voor hoofdstuk 19

class Knoop:
    """Eén schakel in een gelinkte lijst."""

    def __init__(self, waarde):
        self.waarde = waarde
        self.volgende = None

    def __repr__(self) -> str:
        return f"Knoop({self.waarde!r})"


eerste = Knoop("Anke")
tweede = Knoop("Bram")
derde = Knoop("Cato")

eerste.volgende = tweede
tweede.volgende = derde

huidig = eerste
while huidig is not None:
    print(huidig.waarde, end=" -> ")
    huidig = huidig.volgende
print("None")


# Verwachte uitvoer:
# Anke -> Bram -> Cato -> None
