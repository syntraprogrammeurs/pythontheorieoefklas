# Python basis — theoriebundel
# Hoofdstuk 20 — Trends in programmeren
# 20.4 Zes trends van dit moment — 2. Types in dynamische talen
#
# Python is dynamisch getypeerd, zoals je in hoofdstuk 5 leerde. Sinds 2015 kun je er
# type hints bij schrijven, en dat wordt in professionele projecten de norm.

# DYNAMISCH GETYPEERD betekent: een variabele heeft zelf geen vast type, de waarde
# erin wel. Python controleert pas tijdens het draaien of iets past.
# Een TYPE HINT (hoofdstuk 11.7) is een notitie bij je code over welk type je
# verwacht:
#   leeftijd: int          -> deze parameter hoort een geheel getal te zijn
#   is_student: bool       -> deze hoort True of False te zijn
#   = False                -> een standaardwaarde: laat je hem weg, dan is hij False
#   -> int                 -> de functie geeft een geheel getal terug
# LET OP: Python zelf controleert type hints NIET. bereken_lidgeld("34") wordt
# gewoon uitgevoerd (en loopt dan pas vast bij de vergelijking <). Pylance en je
# linter lezen de hints wel en waarschuwen je al in de editor, nog voor je draait.
# Dat is precies de trend: de fout vroeger vinden, waar ze het minst kost.
def bereken_lidgeld(leeftijd: int, is_student: bool = False) -> int:
    """Het lidgeld in hele euro's."""
    # Jonger dan 12: gratis. return stopt de functie meteen (hoofdstuk 11).
    if leeftijd < 12:
        return 0
    # De verkorte keuze uit hoofdstuk 9: "15 als is_student waar is, anders 30".
    return 15 if is_student else 30


# Een volwassene die geen student is: is_student krijgt de standaardwaarde False.
print(bereken_lidgeld(34))
# is_student=True is een TREFWOORDARGUMENT: je noemt de parameter bij naam. Dat
# leest duidelijker dan bereken_lidgeld(20, True), waar je moet raden wat True is.
print(bereken_lidgeld(20, is_student=True))


# Verwachte uitvoer:
# 30
# 15
