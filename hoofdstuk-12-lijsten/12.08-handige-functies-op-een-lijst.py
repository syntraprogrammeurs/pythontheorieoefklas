# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.8 Handige functies op een lijst

bladzijden = [320, 180, 250, 410]

print(sum(bladzijden))
print(min(bladzijden))
print(max(bladzijden))
print(len(bladzijden))
print(sum(bladzijden) / len(bladzijden))
print(any(b > 400 for b in bladzijden))
print(all(b > 100 for b in bladzijden))


# Verwachte uitvoer:
# 1160
# 180
# 410
# 4
# 290.0
# True
# True
