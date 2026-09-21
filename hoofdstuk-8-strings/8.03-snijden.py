# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.3 Snijden

zin = "Boekenclub De Leeslamp"

print(zin[0:6])        # Boeken
print(zin[6:10])       # club
print(zin[:6])         # Boeken       — vanaf het begin
print(zin[14:])        # Leeslamp     — tot het einde
print(zin[-8:])        # Leeslamp     — de laatste acht
print(zin[:])          # alles
print(zin[::2])        # elk tweede teken
print(zin[::-1])       # achterstevoren


# Verwachte uitvoer:
# Boeken
# club
# Boeken
# Leeslamp
# Leeslamp
# Boekenclub De Leeslamp
# Beecu eLelm
# pmalseeL eD bulcnekeoB
