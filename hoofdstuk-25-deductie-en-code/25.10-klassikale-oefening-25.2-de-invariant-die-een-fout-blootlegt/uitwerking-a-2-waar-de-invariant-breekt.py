# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.2 — De invariant die een fout blootlegt, uitwerking
#
# Concreet gaat het mis zodra alle getallen negatief zijn.

# Waar de invariant breekt. De invariant zegt: "grootste is het grootste van
# de getallen die al bekeken zijn". Vóór de eerste ronde is er nog NIETS
# bekeken, en toch staat grootste al op 0. Er bestaat geen grootste van nul
# getallen: de beginwaarde verzint een getal dat niet in de lijst staat.
#
# Zolang er een getal groter dan 0 in de lijst zit, wordt die verzonnen 0 snel
# overschreven en merk je niets. Daarom "werkt" de functie op gewone voorbeelden.

def hoogste_fout(getallen):
    """De versie met de foute beginwaarde."""
    grootste = 0                 # hier zit de fout: 0 komt niet uit de lijst
    for getal in getallen:
        if getal > grootste:
            grootste = getal
    return grootste


# Drie lijsten, gekozen om de fout bloot te leggen:
#   - een gewone lijst: hier klopt het antwoord (daarom viel niets op);
#   - een lijst met alleen negatieve getallen: geen enkel getal is groter dan
#     0, dus grootste blijft 0. Maar 0 staat niet in de lijst!
#   - een lege lijst: de lus draait geen enkele keer, dus komt de verzonnen 0
#     terug, als antwoord op een vraag die geen antwoord heeft.
print("gewone lijst  :", hoogste_fout([320, 180, 250]))
print("negatieve lijst:", hoogste_fout([-5, -12, -3]))
print("lege lijst    :", hoogste_fout([]))

# Welke postconditie vangt dit? "Het resultaat is het grootste" niet: 0 is
# groter dan alles in [-5, -12, -3], dus die bewering blijft overeind. Pas met
# "het resultaat komt IN de reeks voor" erbij vang je de fout. Een goede
# postconditie zegt niet alleen hoe groot iets is, maar ook waar het vandaan komt.


# Verwachte uitvoer:
# gewone lijst  : 320
# negatieve lijst: 0
# lege lijst    : 0
