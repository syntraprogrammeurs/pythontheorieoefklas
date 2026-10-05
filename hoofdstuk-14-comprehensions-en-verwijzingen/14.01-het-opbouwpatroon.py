# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.1 Het opbouwpatroon
#
# Dit schreef je in hoofdstuk 10:

namen = ["anke", "bram", "cato"]
netjes = []

for naam in namen:
    netjes.append(naam.capitalize())

print(netjes)


# Verwachte uitvoer:
# ['Anke', 'Bram', 'Cato']
