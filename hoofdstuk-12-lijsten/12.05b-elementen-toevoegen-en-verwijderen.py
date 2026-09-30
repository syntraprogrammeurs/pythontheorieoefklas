# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.5 Elementen toevoegen en verwijderen
#
# .append() geeft None terug, niet de nieuwe lijst. Dit is de meest gemaakte fout met
# lijsten:

leden = ["Anke"]
leden = leden.append("Bram")
print(leden)


# Verwachte uitvoer:
# None
