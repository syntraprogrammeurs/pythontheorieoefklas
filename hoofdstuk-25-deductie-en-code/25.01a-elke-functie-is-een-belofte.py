# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.1 Elke functie is een belofte
#
# Kijk nog eens naar een functie uit hoofdstuk 11, maar dan als logische uitspraak.

# Een gewone functie uit hoofdstuk 11. Ze werkt, maar kijk naar wat er NIET staat.
# De docstring (11.7) zegt wat de functie DOET. Ze zegt niet wat de functie
# VERWACHT van wie haar aanroept. Daar zit een aanname in die niemand uitspreekt:
# de lijst mag niet leeg zijn. In 25.01b zie je wat er dan gebeurt.
def gemiddelde(getallen):
    """Het rekenkundig gemiddelde van een reeks getallen."""
    # sum() telt alle getallen op, len() telt hoeveel het er zijn (12.8).
    # De deling met / geeft altijd een float, ook als het netjes uitkomt:
    # daarom 250.0 en geen 250.
    return sum(getallen) / len(getallen)


# 320 + 180 + 250 = 750, gedeeld door 3 = 250.0
print(gemiddelde([320, 180, 250]))

# Een functie als logische uitspraak: "als je mij een niet-lege lijst getallen
# geeft, dan geef ik je hun gemiddelde terug". Dat is een IMPLICATIE (hoofdstuk 23).
# Het deel na "als" heet de PRECONDITIE, het deel na "dan" de POSTCONDITIE.
# Samen vormen ze het CONTRACT van de functie. In 25.02a schrijf je ze op.


# Verwachte uitvoer:
# 250.0
