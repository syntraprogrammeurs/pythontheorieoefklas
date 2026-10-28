# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.9 Testdekking, en waarom honderd procent niets bewijst

# TESTDEKKING meet welk deel van je regels code tijdens de tests uitgevoerd is.
# Deze functie is MET OPZET FOUT. De regeling heeft vier tarieven (0, 15, 30 en
# 20 euro), maar de functie kent er maar twee: iedereen vanaf 12 betaalt 15.
# Je herstelt de fout niet: het bestand toont dat de tests haar niet vinden.
def tarief(leeftijd):
    """Volledig gedekt door één test, en toch fout."""
    # Regel 1 van de functie: wordt uitgevoerd door de test met 5 jaar.
    if leeftijd < 12:
        return 0
    # Regel 2: wordt uitgevoerd door de test met 20 jaar.
    return 15                       # klopt niet voor 26 en ouder


# Twee tests. Elke test vergelijkt met == en toont True (geslaagd) of False.
# Samen voeren ze elke regel van tarief uit: dekking 100 procent.
# Toch zijn de gekozen waarden slecht: 5 en 20 liggen allebei in een klasse
# waar de foute functie toevallig het juiste antwoord geeft.
print("test met 5 jaar :", tarief(5) == 0)
print("test met 20 jaar:", tarief(20) == 15)
print("beide regels uitgevoerd, dekking 100 procent")
# Wat er werkelijk gebeurt bij een volwassene: 15 in plaats van 30.
# LET OP: dekking telt REGELS, geen GEVALLEN. "return 15" is uitgevoerd, dus
# telt als gedekt, ook al is ze voor de helft van de leeftijden fout.
# Een grenswaarde uit 28.4, de waarde 26, had de fout meteen gevonden.
# Hoge dekking volgt uit goed testen, maar goed testen volgt NIET uit hoge
# dekking: dat omkeren is de fout uit hoofdstuk 26.
print("werkelijk bij 40:", tarief(40), "in plaats van 30")


# Verwachte uitvoer:
# test met 5 jaar : True
# test met 20 jaar: True
# beide regels uitgevoerd, dekking 100 procent
# werkelijk bij 40: 15 in plaats van 30
