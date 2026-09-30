# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.5 Elementen toevoegen en verwijderen
#
# .remove("Dirk") op een lijst waar Dirk niet in staat, geeft ValueError:
# list.remove(x): x not in list. Controleer eerst:

leden = ["Anke", "Bram"]
if "Dirk" in leden:
    leden.remove("Dirk")
print(leden)


# Verwachte uitvoer:
# ['Anke', 'Bram']
