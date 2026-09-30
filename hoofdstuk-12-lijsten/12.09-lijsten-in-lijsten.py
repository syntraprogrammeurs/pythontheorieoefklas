# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.9 Lijsten in lijsten

ledenlijst = [
    ["Anke Peeters", 34, 3],
    ["Bram Coppens", 20, 1],
    ["Cato Dhondt", 11, 4],
]

print(ledenlijst[0])
print(ledenlijst[0][0])
print(ledenlijst[2][1])

for naam, leeftijd, jaren in ledenlijst:
    print(f"{naam:<16}{leeftijd:>4}{jaren:>4}")


# Verwachte uitvoer:
# ['Anke Peeters', 34, 3]
# Anke Peeters
# 11
# Anke Peeters      34   3
# Bram Coppens      20   1
# Cato Dhondt       11   4
