# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.3 Elementen opvragen en snijden
#
# Alles wat je in hoofdstuk 8 over strings leerde, geldt hier ook.

leden = ["Anke", "Bram", "Cato", "Dirk", "Els"]

print(leden[0])       # Anke
print(leden[-1])      # Els
print(leden[1:3])     # ['Bram', 'Cato']
print(leden[:2])      # ['Anke', 'Bram']
print(leden[-2:])     # ['Dirk', 'Els']
print(leden[::-1])    # omgekeerd


# Verwachte uitvoer:
# Anke
# Els
# ['Bram', 'Cato']
# ['Anke', 'Bram']
# ['Dirk', 'Els']
# ['Els', 'Dirk', 'Cato', 'Bram', 'Anke']
