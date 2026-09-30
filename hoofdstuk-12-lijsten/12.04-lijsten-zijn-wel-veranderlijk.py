# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.4 Lijsten zijn wél veranderlijk
#
# Hier verschilt een lijst wezenlijk van een string.

leden = ["Anke", "Bram", "Cato"]

leden[1] = "Bram Coppens"
print(leden)


# Verwachte uitvoer:
# ['Anke', 'Bram Coppens', 'Cato']
