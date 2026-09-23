# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.5 De methodes die je constant gebruikt — Hoofdletters en kleine letters

tekst = "  anke PEETERS  "

print(tekst.upper())          # ALLES IN HOOFDLETTERS
print(tekst.lower())          # alles in kleine letters
print(tekst.strip())          # spaties links en rechts weg
print(tekst.strip().title())  # Elk Woord Een Hoofdletter
print("gent".capitalize())    # Alleen de eerste letter


# Verwachte uitvoer:
#   ANKE PEETERS
#   anke peeters
# anke PEETERS
# Anke Peeters
# Gent
