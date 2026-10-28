# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.2 — De beslissingstabel van de uitleenregel, uitwerking
#
# 3. De herstelde functie, met de tabel als test.

# De Leeslamp — de uitleenregel, met de volledige beslissingstabel als test
# Cursus Python basis, hoofdstuk 28, oefening 2
from itertools import product


def mag_lenen(betaald, geschorst, te_veel_thuis):
    """Lenen mag als er geen enkele reden is om te weigeren."""
    if not betaald:
        return False
    if geschorst:
        return False
    if te_veel_thuis:
        return False
    return True


def verwacht(betaald, geschorst, te_veel_thuis):
    """De regel zoals het bestuur hem uitsprak, los van de code."""
    return betaald and not geschorst and not te_veel_thuis


print("betaald  gesch.   te veel  hoort  geeft  klopt")
print("-" * 47)
gefaald = 0
for b, g, t in product([True, False], repeat=3):
    hoort = verwacht(b, g, t)
    geeft = mag_lenen(b, g, t)
    klopt = hoort == geeft
    gefaald += not klopt
    print(f"{b!s:<9}{g!s:<9}{t!s:<9}{hoort!s:<7}{geeft!s:<7}{klopt}")

print()
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
