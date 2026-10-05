# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.3 Comprehensions voor sets en dictionaries
#
# Die laatste is bijzonder:

bladzijden = [320, 180, 250]

print(sum(b for b in bladzijden if b > 200))
print(any(b > 300 for b in bladzijden))
print(max(b for b in bladzijden))


# Verwachte uitvoer:
# 570
# True
# 320
