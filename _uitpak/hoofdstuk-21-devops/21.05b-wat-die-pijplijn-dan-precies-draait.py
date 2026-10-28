# Python basis — theoriebundel
# Hoofdstuk 21 — DevOps, en waar Git daarin past
# 21.5 Wat die pijplijn dan precies draait
#
# Nu de fout die deze controles moeten vangen. Iemand schrijft > waar >= hoort:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

def lidgeld(leeftijd, is_student=False):
    if leeftijd < 12:
        return 0
    if leeftijd > 65:                 # fout: > in plaats van >=
        return 20
    return 15 if is_student else 30


assert lidgeld(65) == 20, "vanaf 65 geldt het seniorentarief"


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "controle.py", line 9, in <module>
#     assert lidgeld(65) == 20, "vanaf 65 geldt het seniorentarief"
#            ^^^^^^^^^^^^^^^^^
# AssertionError: vanaf 65 geldt het seniorentarief
