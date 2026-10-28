# Python basis — theoriebundel
# Hoofdstuk 20 — Trends in programmeren
# Klassikale oefening 20.2 — Hetzelfde probleem in vier paradigma's, uitwerking

# De Leeslamp — één probleem, vier stijlen
# Cursus Python basis, hoofdstuk 20, oefening 2

BOEKEN = [
    ("Turks fruit", 175),
    ("De ontdekking van de hemel", 928),
    ("Het diner", 288),
    ("De aanslag", 246),
    ("Max Havelaar", 340),
    ("Bint", 96),
]
GRENS = 250


# 1 — procedureel
def dikke_titels_procedureel(boeken, grens):
    """Met lussen, stap voor stap."""
    uit = []
    for titel, bladzijden in boeken:
        if bladzijden > grens:
            uit.append(titel.upper())
    uit.sort()
    return uit


# 2 — functioneel
def dikke_titels_functioneel(boeken, grens):
    """Met filter, map en sorted."""
    dik = filter(lambda b: b[1] > grens, boeken)
    titels = map(lambda b: b[0].upper(), dik)
    return sorted(titels)


# 3 — met een comprehension
def dikke_titels_comprehension(boeken, grens):
    """De Python-manier."""
    return sorted(titel.upper() for titel, blz in boeken if blz > grens)


# 4 — objectgeoriënteerd
class Catalogus:
    """Een verzameling boeken met bevragingen erop."""

    def __init__(self, boeken):
        self.boeken = list(boeken)

    def dikker_dan(self, grens):
        """Een nieuwe catalogus met alleen de dikke boeken."""
        return Catalogus(b for b in self.boeken if b[1] > grens)

    def titels(self):
        """De titels, in hoofdletters en gesorteerd."""
        return sorted(titel.upper() for titel, _ in self.boeken)

    def __len__(self):
        return len(self.boeken)


resultaten = {
    "procedureel": dikke_titels_procedureel(BOEKEN, GRENS),
    "functioneel": dikke_titels_functioneel(BOEKEN, GRENS),
    "comprehension": dikke_titels_comprehension(BOEKEN, GRENS),
    "objectgericht": Catalogus(BOEKEN).dikker_dan(GRENS).titels(),
}

for stijl, uitkomst in resultaten.items():
    print(f"{stijl:<16}{uitkomst}")

print()
print("Alle vier gelijk:", len(set(map(tuple, resultaten.values()))) == 1)


# Verwachte uitvoer:
# procedureel     ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
# functioneel     ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
# comprehension   ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
# objectgericht   ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
#
# Alle vier gelijk: True
