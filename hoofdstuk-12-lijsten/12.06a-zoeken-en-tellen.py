# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.6 Zoeken en tellen

leden = ["Anke", "Bram", "Cato", "Bram"]

print("Cato" in leden)          # True
print(leden.index("Bram"))      # 1  — de eerste
print(leden.count("Bram"))      # 2
print(len(leden))               # 4


# Verwachte uitvoer:
# True
# 1
# 2
# 4
