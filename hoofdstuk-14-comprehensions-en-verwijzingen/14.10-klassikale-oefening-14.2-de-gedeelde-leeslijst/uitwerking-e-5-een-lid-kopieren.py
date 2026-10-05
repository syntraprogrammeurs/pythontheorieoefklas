# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.2 — De gedeelde leeslijst, uitwerking
#
# 5 — Een lid kopiëren.

def kopieer_lid(lid: dict) -> dict:
    """Een kopie van een lid, met een eigen leeslijst."""
    nieuw = lid.copy()
    nieuw["gelezen"] = lid["gelezen"].copy()
    return nieuw


anke = {"naam": "Anke", "gelezen": ["Het diner"]}
zus = kopieer_lid(anke)
zus["naam"] = "Zus van Anke"
zus["gelezen"].append("Turks fruit")

print(anke)
print(zus)


# Verwachte uitvoer:
# {'naam': 'Anke', 'gelezen': ['Het diner']}
# {'naam': 'Zus van Anke', 'gelezen': ['Het diner', 'Turks fruit']}
