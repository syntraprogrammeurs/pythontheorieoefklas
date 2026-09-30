# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 2 — De week in stukken snijden

dagen = ["ma", "di", "wo", "do", "vr", "za", "zo"]

werkdagen = dagen[:5]
weekend = dagen[-2:]
om_de_andere = dagen[::2]
omgekeerd = dagen[::-1]

print(f"Werkdagen: {werkdagen}")
print(f"Weekend: {weekend}")
print(f"Om de andere: {om_de_andere}")
print(f"Omgekeerd: {omgekeerd}")
