# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.8 Het lidgeldprogramma, nu echt
#
# Dit is het probleem dat je in hoofdstuk 3 uitschreef in pseudocode.

# De Leeslamp — het lidgeld berekenen
# Cursus Python basis, hoofdstuk 9

LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12          # jonger dan 12 is gratis
JAREN_VOOR_KORTING = 3        # 3 jaar of meer geeft korting
KORTING = 5

leeftijd = 45
is_student = False
jaren_lid = 3

# 1 — het basisbedrag, van streng naar soepel
if leeftijd < LEEFTIJD_GRATIS:
    bedrag = 0
elif is_student:
    bedrag = LIDGELD_STUDENT
else:
    bedrag = LIDGELD_VOLWASSENE

# 2 — de trouwkorting
if jaren_lid >= JAREN_VOOR_KORTING:
    bedrag -= KORTING

# 3 — nooit onder nul
if bedrag < 0:
    bedrag = 0

print(f"Leeftijd   : {leeftijd}")
print(f"Student    : {is_student}")
print(f"Jaren lid  : {jaren_lid}")
print(f"Te betalen : {bedrag} euro")


# Verwachte uitvoer:
# Leeftijd   : 45
# Student    : False
# Jaren lid  : 3
# Te betalen : 25 euro
