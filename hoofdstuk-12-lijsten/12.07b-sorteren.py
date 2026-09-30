# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.7 Sorteren
#
# Achterstevoren en met een sleutel:

namen = ["cato", "Anke", "bo", "dominique"]

print(sorted(namen))
print(sorted(namen, reverse=True))
print(sorted(namen, key=str.lower))
print(sorted(namen, key=len))


# Verwachte uitvoer:
# ['Anke', 'bo', 'cato', 'dominique']
# ['dominique', 'cato', 'bo', 'Anke']
# ['Anke', 'bo', 'cato', 'dominique']
# ['bo', 'cato', 'Anke', 'dominique']
