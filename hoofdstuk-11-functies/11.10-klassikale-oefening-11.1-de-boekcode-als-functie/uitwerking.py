# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Klassikale oefening 11.1 — De boekcode als functie, uitwerking

# De Leeslamp — de boekcode, in functies
# Cursus Python basis, hoofdstuk 11, oefening 1

LIDWOORDEN = ("de", "het", "een", "van")


def beginletters(titel: str) -> str:
    """De beginletters van elk woord in de titel, zonder de lidwoorden."""
    letters = ""
    for woord in titel.split():
        if woord.lower() not in LIDWOORDEN:
            letters += woord[0].upper()
    return letters


def achternaam_van(schrijver: str) -> str:
    """Alles na de eerste spatie, dus ook een samengestelde achternaam."""
    delen = schrijver.split(" ", 1)
    return delen[1] if len(delen) > 1 else delen[0]


def boekcode(schrijver: str, titel: str, jaar: int, lengte: int = 3) -> str:
    """De code van een boek, bijvoorbeeld MUL-OH-1992.

    `lengte` bepaalt hoeveel letters van de achternaam worden gebruikt.
    """
    deel_schrijver = achternaam_van(schrijver)[:lengte].upper()
    return f"{deel_schrijver}-{beginletters(titel)}-{jaar}"


gevallen = [
    ("Harry Mulisch", "De ontdekking van de hemel", 1992, "MUL-OH-1992"),
    ("Herman Koch", "Het diner", 2009, "KOC-D-2009"),
    ("Jan Wolkers", "Turks fruit", 1969, "WOL-TF-1969"),
    ("Anna Bo", "Het licht van de zee", 2015, "BO-LZ-2015"),
]

for schrijver, titel, jaar, verwacht in gevallen:
    gekregen = boekcode(schrijver, titel, jaar)
    teken = "ok" if gekregen == verwacht else "FOUT"
    print(f"{gekregen:<14}{verwacht:<14}{teken}")

print()
print("Met vier letters:", boekcode("Harry Mulisch", "Het stenen bruidsbed", 1959, lengte=4))
print("Met twee letters:", boekcode("Harry Mulisch", "Het stenen bruidsbed", 1959, lengte=2))


# Verwachte uitvoer:
# MUL-OH-1992   MUL-OH-1992   ok
# KOC-D-2009    KOC-D-2009    ok
# WOL-TF-1969   WOL-TF-1969   ok
# BO-LZ-2015    BO-LZ-2015    ok
#
# Met vier letters: MULI-SB-1959
# Met twee letters: MU-SB-1959
