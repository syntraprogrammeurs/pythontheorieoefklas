# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.7 Sorteren
#
# Er zijn twee manieren, en het verschil is belangrijk.

bladzijden = [320, 180, 250, 410]

gesorteerd = sorted(bladzijden)
print(bladzijden)
print(gesorteerd)

bladzijden.sort()
print(bladzijden)


# Verwachte uitvoer:
# [320, 180, 250, 410]
# [180, 250, 320, 410]
# [180, 250, 320, 410]
