# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.2 — De gedeelde leeslijst, opgave
#
# De situatie. Dit programma zou elk lid een eigen leeslijst moeten geven. Het doet
# iets anders, en je gaat uitzoeken wat.

def maak_lid(naam, gelezen=[]):
    return {"naam": naam, "gelezen": gelezen}


anke = maak_lid("Anke")
bram = maak_lid("Bram")

anke["gelezen"].append("Het diner")

print(anke)
print(bram)
