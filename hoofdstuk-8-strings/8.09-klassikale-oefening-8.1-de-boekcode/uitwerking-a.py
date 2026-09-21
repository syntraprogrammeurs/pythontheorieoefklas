# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# Klassikale oefening 8.1 — De boekcode, uitwerking

# De Leeslamp — de boekcode
# Cursus Python basis, hoofdstuk 8, oefening 1

LIDWOORDEN = "de het een van"

schrijver = "Harry Mulisch"
titel = "De ontdekking van de hemel"
jaar = 1992

# 1 — de eerste drie letters van de achternaam
achternaam = schrijver.split(" ", 1)[1]
deel_schrijver = achternaam[:3].upper()

# 2 — de beginletters van de titel, zonder de lidwoorden
deel_titel = ""
for woord in titel.split():
    if woord.lower() not in LIDWOORDEN.split():
        deel_titel = deel_titel + woord[0].upper()

# 3 — samenvoegen
code = f"{deel_schrijver}-{deel_titel}-{jaar}"
print(code)


# Verwachte uitvoer:
# MUL-OH-1992
