# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.2 — De gedeelde leeslijst, uitwerking
#
# 4 — Dezelfde fout, anders veroorzaakt.

def maak_lid(naam: str, gelezen: list = None) -> dict:
    """Maakt een lid met een eigen, lege leeslijst."""
    if gelezen is None:
        gelezen = []
    return {"naam": naam, "gelezen": gelezen}


start = ["Max Havelaar"]
anke = maak_lid("Anke", start)
bram = maak_lid("Bram", start)

anke["gelezen"].append("Het diner")

print(anke)
print(bram)
print(start)


# Verwachte uitvoer:
# {'naam': 'Anke', 'gelezen': ['Max Havelaar', 'Het diner']}
# {'naam': 'Bram', 'gelezen': ['Max Havelaar', 'Het diner']}
# ['Max Havelaar', 'Het diner']
