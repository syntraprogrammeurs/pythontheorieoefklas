# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.8 Positief en negatief testen
#
# Negatief testen doe je met try en except uit hoofdstuk 15:

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


def verwacht_fout(soort, functie, *argumenten):
    """True als de aanroep precies deze foutsoort opgooit."""
    try:
        functie(*argumenten)
    except soort:
        return True
    except Exception:
        return False
    return False


print("negatieve leeftijd :", verwacht_fout(ValueError, lidgeld, -1))
print("te hoge leeftijd   :", verwacht_fout(ValueError, lidgeld, 200))
print("tekst als invoer   :", verwacht_fout(TypeError, lidgeld, "veertig"))
print("geldige leeftijd   :", verwacht_fout(ValueError, lidgeld, 40))


# Verwachte uitvoer:
# negatieve leeftijd : True
# te hoge leeftijd   : True
# tekst als invoer   : True
# geldige leeftijd   : False
