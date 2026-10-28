# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.2 — De beslissingstabel van de uitleenregel, uitwerking
#
# 3. De herstelde functie, met de tabel als test.

# De Leeslamp — de uitleenregel, met de volledige beslissingstabel als test
# Cursus Python basis, hoofdstuk 28, oefening 2
# itertools is een ingebouwde module met hulpmiddelen voor lussen.
# product() maakt alle combinaties van waarden (zie de lus onderaan).
from itertools import product


# De herstelde functie. De derde parameter heet nu te_veel_thuis: een bool,
# True als het lid meer dan drie boeken thuis heeft.
# Elke reden om te weigeren krijgt een eigen if. Pas als geen enkele if een
# reden vond, mag het lid lenen.
def mag_lenen(betaald, geschorst, te_veel_thuis):
    """Lenen mag als er geen enkele reden is om te weigeren."""
    if not betaald:
        return False
    if geschorst:
        return False
    # Dit is het geval dat in de opgave ontbrak.
    if te_veel_thuis:
        return False
    return True


# Het ORAKEL: de regel nog eens, maar nu rechtstreeks als logische uitdrukking
# (propositielogica, hoofdstuk 23): betaald EN NIET geschorst EN NIET te veel.
# Waarom twee keer dezelfde regel? Je vergelijkt de code met een tweede,
# onafhankelijke schrijfwijze. Komen ze in elke rij overeen, dan klopt de code.
def verwacht(betaald, geschorst, te_veel_thuis):
    """De regel zoals het bestuur hem uitsprak, los van de code."""
    return betaald and not geschorst and not te_veel_thuis


# De kop van de tabel en een lijn van 47 streepjes ("-" * 47 herhaalt de tekst).
print("betaald  gesch.   te veel  hoort  geeft  klopt")
print("-" * 47)
# Teller voor het aantal rijen waarin code en regel van elkaar verschillen.
gefaald = 0
# product([True, False], repeat=3) geeft alle 2 x 2 x 2 = 8 combinaties van
# drie booleans, telkens als tuple: (True, True, True), (True, True, False),
# ... tot (False, False, False). Dat zijn precies de acht rijen van de
# BESLISSINGSTABEL (28.5). Zo vergeet je geen enkele rij.
# b, g en t pakken elk tuple uit: betaald, geschorst, te veel thuis.
for b, g, t in product([True, False], repeat=3):
    hoort = verwacht(b, g, t)      # wat de regel zegt
    geeft = mag_lenen(b, g, t)     # wat de code zegt
    klopt = hoort == geeft         # True als ze overeenkomen
    # Een bool optellen bij een int: True telt als 1, False als 0.
    # not klopt is True bij een verschil, dus de teller stijgt dan met 1.
    gefaald += not klopt
    # {b!s:<9}: !s maakt er tekst van ("True"/"False"), :<9 lijnt links uit
    # over 9 tekens. Zo staan de kolommen netjes onder de kop.
    print(f"{b!s:<9}{g!s:<9}{t!s:<9}{hoort!s:<7}{geeft!s:<7}{klopt}")

print()
# 8 rijen in totaal. Een beslissingstabel is pas af met 2 tot de macht n rijen;
# bij een vierde voorwaarde worden het er 16.
print(f"{8 - gefaald} van de 8 rijen kloppen")


# Verwachte uitvoer:
# betaald  gesch.   te veel  hoort  geeft  klopt
# -----------------------------------------------
# True     True     True     False  False  True
# True     True     False    False  False  True
# True     False    True     False  False  True
# True     False    False    True   True   True
# False    True     True     False  False  True
# False    True     False    False  False  True
# False    False    True     False  False  True
# False    False    False    False  False  True
#
# 8 van de 8 rijen kloppen
