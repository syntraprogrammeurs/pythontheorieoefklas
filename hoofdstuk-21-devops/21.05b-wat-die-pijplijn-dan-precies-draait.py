# Python basis — theoriebundel
# Hoofdstuk 21 — DevOps, en waar Git daarin past
# 21.5 Wat die pijplijn dan precies draait
#
# Nu de fout die deze controles moeten vangen. Iemand schrijft > waar >= hoort:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

# Dezelfde functie als in 21.05a, met één teken verschil. Herstel het NIET: het
# doel is net dat je ziet hoe een controle de fout vangt.
def lidgeld(leeftijd, is_student=False):
    if leeftijd < 12:
        return 0
    # DE FOUT: > betekent "strikt groter dan". 65 > 65 is False, dus iemand van
    # precies 65 valt hier NIET binnen en gaat door naar de volgende regel.
    if leeftijd > 65:                 # fout: > in plaats van >=
        return 20
    # Zo krijgt een lid van 65 het volwassenentarief van 30 in plaats van 20.
    return 15 if is_student else 30


# lidgeld(65) geeft nu 30. 30 == 20 is False, dus assert stopt het programma met
# een AssertionError en de boodschap "vanaf 65 geldt het seniorentarief".
# De afsluitcode is daardoor niet 0: de pijplijn zet een rood kruisje en
# waarschuwt het team, binnen enkele minuten na de push.
# LET OP: dit is geen SyntaxError; voor alle andere leeftijden werkt de code
# perfect. Alleen een controle op precies de grenswaarde 65 vindt deze fout.
# Het regelnummer in de traceback hieronder (line 9) is dat van het bestand
# controle.py in de bundel; in dit bestand staat de assert op een andere regel.
assert lidgeld(65) == 20, "vanaf 65 geldt het seniorentarief"


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "controle.py", line 9, in <module>
#     assert lidgeld(65) == 20, "vanaf 65 geldt het seniorentarief"
#            ^^^^^^^^^^^^^^^^^
# AssertionError: vanaf 65 geldt het seniorentarief
