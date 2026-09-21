# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# Klassikale oefening 8.1 — De boekcode, uitwerking
#
# Voor alle drie de boeken, met een lus die je in hoofdstuk 10 echt leert maar hier al
# leesbaar is:

LIDWOORDEN = ["de", "het", "een", "van"]

boeken = [
    ("Harry Mulisch", "De ontdekking van de hemel", 1992),
    ("Herman Koch", "Het diner", 2009),
    ("Jan Wolkers", "Turks fruit", 1969),
]

for schrijver, titel, jaar in boeken:
    achternaam = schrijver.split(" ", 1)[1]
    deel_schrijver = achternaam[:3].upper()

    deel_titel = ""
    for woord in titel.split():
        if woord.lower() not in LIDWOORDEN:
            deel_titel += woord[0].upper()

    print(f"{titel:<30}{deel_schrijver}-{deel_titel}-{jaar}")


# Verwachte uitvoer:
# De ontdekking van de hemel    MUL-OH-1992
# Het diner                     KOC-D-2009
# Turks fruit                   WOL-TF-1969
