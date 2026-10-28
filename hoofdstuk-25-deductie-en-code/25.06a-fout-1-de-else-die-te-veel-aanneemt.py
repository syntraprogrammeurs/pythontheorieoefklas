# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 1 — de else die te veel aanneemt

# LET OP: deze functie is met opzet FOUT. Ze draait zonder foutmelding, maar het
# antwoord klopt niet. Herstel haar niet: kijk waarom ze fout is.
#
# Fout 1 uit 25.6: de else die te veel aanneemt.
# De drogreden erachter: ONTKENNEN VAN HET ANTECEDENS (24.2).
#   Regel:      als geschorst, dan mag het lid niet lenen.     (p -> q)
#   Gegeven:    het lid is niet geschorst.                     (niet p)
#   Conclusie:  dus het lid mag wel lenen.                     (niet q) ONGELDIG
# Er zijn andere redenen om te weigeren (lidgeld niet betaald, te veel boeken
# thuis), en die negeert de functie.
def mag_lenen_fout(geschorst, betaald, boeken_thuis):
    """Fout: de else neemt aan dat schorsing de enige reden is."""
    # De enige controle: schorsing. Tot hier klopt het (modus ponens).
    if geschorst:
        return False
    # Er staat geen woord "else", maar deze regel werkt wel als een else: je komt
    # hier alleen als geschorst onwaar was. Hier zit de fout: "niet geschorst"
    # wordt behandeld als "alles in orde".
    # Merk op: de parameters betaald en boeken_thuis worden NERGENS gebruikt. Een
    # parameter die je niet gebruikt, is vaak een teken dat er een controle
    # ontbreekt. Een editor als VS Code toont zo'n naam soms grijs.
    return True


# Een lid dat niet geschorst is, maar NIETS betaalde en vijf boeken thuis heeft.
# De functie zegt toch True: dit lid mag lenen.
# De print loopt over twee regels: binnen haakjes mag dat (4.1).
print("geschorst=False, betaald=False, 5 boeken thuis ->",
      mag_lenen_fout(False, False, 5))

# Hoe het wel moet: geef ELKE reden om te weigeren een eigen controle, en laat pas
# helemaal onderaan True terugkomen. Dat zijn de bewaakclausules uit 25.7.


# Verwachte uitvoer:
# geschorst=False, betaald=False, 5 boeken thuis -> True
