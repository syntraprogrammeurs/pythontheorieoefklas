# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.8 Positief en negatief testen
#
# Negatief testen doe je met try en except uit hoofdstuk 15:

# POSITIEF TESTEN: werkt het bij geldige invoer?
# NEGATIEF TESTEN: weigert het netjes bij ongeldige invoer?
# Bij een negatieve test is een fout dus GOED nieuws: de functie hoort te
# weigeren. De test slaagt als precies de juiste foutsoort opgegooid wordt.

# Dezelfde lidgeldfunctie als in 28.6. Ze gooit twee soorten fouten op:
#   TypeError  -> de invoer is geen geheel getal
#   ValueError -> wel een geheel getal, maar buiten 0 tot en met 120
def lidgeld(leeftijd):
    """Het lidgeld in hele euro's."""
    if not isinstance(leeftijd, int):
        raise TypeError("leeftijd moet een geheel getal zijn")
    if not 0 <= leeftijd <= 120:
        raise ValueError(f"leeftijd {leeftijd} ligt buiten het bereik")
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    return 20


# Een hulpfunctie voor negatieve tests.
#   soort       -> de foutklasse die je verwacht, bv. ValueError (zonder haakjes:
#                  je geeft de klasse zelf door, niet een fout)
#   functie     -> de functie die je test, ook zonder haakjes
#   *argumenten -> alle overige argumenten worden samen een tuple. Met het
#                  sterretje kun je er zoveel meegeven als je wilt.
#   geeft True terug als PRECIES die foutsoort optrad, anders False.
def verwacht_fout(soort, functie, *argumenten):
    """True als de aanroep precies deze foutsoort opgooit."""
    try:
        # functie(*argumenten): het sterretje pakt de tuple weer uit, zodat
        # verwacht_fout(ValueError, lidgeld, -1) neerkomt op lidgeld(-1).
        functie(*argumenten)
    # De verwachte fout: de functie weigerde zoals het hoort.
    except soort:
        return True
    # Een ANDERE fout, bv. TypeError terwijl je ValueError verwachtte: dan
    # weigert de functie wel, maar om de verkeerde reden. Dat telt als fout.
    except Exception:
        return False
    # Hier kom je alleen als er GEEN fout was: de functie aanvaardde de invoer.
    # Bij een negatieve test is dat net verkeerd.
    return False


# Elke regel test één klasse ONGELDIGE invoer (de equivalentieklassen uit 28.3):
#   -1        -> ongeldig: negatief. Ook een grenswaarde: net onder 0.
#   200       -> ongeldig: onmogelijk hoog (boven 120)
#   "veertig" -> ongeldig: geen getal, dus een TypeError en geen ValueError
print("negatieve leeftijd :", verwacht_fout(ValueError, lidgeld, -1))
print("te hoge leeftijd   :", verwacht_fout(ValueError, lidgeld, 200))
print("tekst als invoer   :", verwacht_fout(TypeError, lidgeld, "veertig"))
# De laatste regel staat er MET OPZET: 40 is geldig, dus er komt geen fout en
# verwacht_fout moet False geven. Zo zie je dat de controle ook "nee" kan
# zeggen. Een controle die altijd True zegt, controleert niets: dat is de
# tautologie uit hoofdstuk 23 in testvorm.
print("geldige leeftijd   :", verwacht_fout(ValueError, lidgeld, 40))


# Verwachte uitvoer:
# negatieve leeftijd : True
# te hoge leeftijd   : True
# tekst als invoer   : True
# geldige leeftijd   : False
