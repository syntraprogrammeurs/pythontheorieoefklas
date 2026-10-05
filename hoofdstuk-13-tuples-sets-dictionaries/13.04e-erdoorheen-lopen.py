# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.4 Dictionaries — Erdoorheen lopen

lid = {"naam": "Anke", "leeftijd": 34, "stad": "Gent"}

for sleutel in lid:
    print(sleutel)

print()
for waarde in lid.values():
    print(waarde)

print()
for sleutel, waarde in lid.items():
    print(f"{sleutel:<10}{waarde}")


# Verwachte uitvoer:
# naam
# leeftijd
# stad
#
# Anke
# 34
# Gent
#
# naam      Anke
# leeftijd  34
# stad      Gent
