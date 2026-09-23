# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.5 De methodes die je constant gebruikt — Testen wat voor tekens erin zitten

print("24".isdigit())          # True    — alleen cijfers
print("24a".isdigit())         # False
print("Anke".isalpha())        # True    — alleen letters
print("Anke Peeters".isalpha())# False   — de spatie telt niet als letter
print("   ".isspace())         # True
print("ANKE".isupper())        # True


# Verwachte uitvoer:
# True
# False
# True
# False
# True
# True
