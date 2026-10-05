# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.2 — De gedeelde leeslijst, uitwerking
#
# De functie is nu correct, en toch gaat het mis. De aanroeper gaf twee keer dezelfde
# lijst mee. Dat kun je in de functie oplossen:

def maak_lid(naam: str, gelezen: list = None) -> dict:
    """Maakt een lid met een eigen leeslijst, ook bij een meegegeven lijst."""
    return {"naam": naam, "gelezen": list(gelezen or [])}


start = ["Max Havelaar"]
anke = maak_lid("Anke", start)
bram = maak_lid("Bram", start)
anke["gelezen"].append("Het diner")

print(anke)
print(bram)
print(start)


# Verwachte uitvoer:
# {'naam': 'Anke', 'gelezen': ['Max Havelaar', 'Het diner']}
# {'naam': 'Bram', 'gelezen': ['Max Havelaar']}
# ['Max Havelaar']
