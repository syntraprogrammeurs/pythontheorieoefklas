# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.2 — De gedeelde leeslijst, uitwerking
#
# 1 — De uitvoer.

def maak_lid(naam, gelezen=[]):
    return {"naam": naam, "gelezen": gelezen}


anke = maak_lid("Anke")
bram = maak_lid("Bram")

anke["gelezen"].append("Het diner")

print(anke)
print(bram)


# Verwachte uitvoer:
# {'naam': 'Anke', 'gelezen': ['Het diner']}
# {'naam': 'Bram', 'gelezen': ['Het diner']}
