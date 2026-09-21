# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.3 elif: meer dan twee gevallen

leeftijd = 20
is_student = True

if leeftijd < 12:
    bedrag = 0
elif is_student:
    bedrag = 15
else:
    bedrag = 30

print(f"Te betalen: {bedrag} euro")


# Verwachte uitvoer:
# Te betalen: 15 euro
