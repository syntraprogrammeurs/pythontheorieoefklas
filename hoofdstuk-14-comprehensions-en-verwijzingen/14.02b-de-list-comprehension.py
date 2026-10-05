# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.2 De list comprehension
#
# Met een voorwaarde erbij:

bladzijden = [320, 180, 250, 410, 96]

dik = [b for b in bladzijden if b > 250]
verdubbeld = [b * 2 for b in bladzijden]
labels = [f"{b} blz" for b in bladzijden if b < 200]

print(dik)
print(verdubbeld)
print(labels)


# Verwachte uitvoer:
# [320, 410]
# [640, 360, 500, 820, 192]
# ['180 blz', '96 blz']
