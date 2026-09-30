# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.5 Elementen toevoegen en verwijderen

leden = ["Anke", "Bram"]

leden.append("Cato")            # achteraan erbij
leden.insert(0, "Aaron")        # op positie 0
leden.extend(["Dirk", "Els"])   # meerdere achteraan
print(leden)

leden.remove("Bram")            # op waarde
print(leden)

laatste = leden.pop()           # laatste eruit, en geef hem terug
print(laatste, leden)

eerste = leden.pop(0)           # op positie
print(eerste, leden)

del leden[0]
print(leden)

leden.clear()
print(leden)


# Verwachte uitvoer:
# ['Aaron', 'Anke', 'Bram', 'Cato', 'Dirk', 'Els']
# ['Aaron', 'Anke', 'Cato', 'Dirk', 'Els']
# Els ['Aaron', 'Anke', 'Cato', 'Dirk']
# Aaron ['Anke', 'Cato', 'Dirk']
# ['Cato', 'Dirk']
# []
