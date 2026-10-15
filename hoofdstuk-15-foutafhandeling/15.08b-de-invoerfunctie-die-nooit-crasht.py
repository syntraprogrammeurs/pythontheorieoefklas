# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.8 De invoerfunctie die nooit crasht
#
# Een versie die je kunt testen zonder te typen:

def controleer_getal(antwoord: str, minimum=None, maximum=None):
    """Geeft het getal terug, of een foutboodschap als tekst."""
    antwoord = antwoord.strip().replace(",", ".")
    try:
        getal = int(float(antwoord))
    except ValueError:
        return "geen getal"

    if minimum is not None and getal < minimum:
        return f"minstens {minimum}"
    if maximum is not None and getal > maximum:
        return f"hoogstens {maximum}"
    return getal


gevallen = ["24", " 24 ", "2,5", "abc", "", "-5", "200", "24.0"]
for tekst in gevallen:
    print(f"{tekst!r:<10}{controleer_getal(tekst, minimum=0, maximum=130)}")


# Verwachte uitvoer:
# '24'      24
# ' 24 '    24
# '2,5'     2
# 'abc'     geen getal
# ''        geen getal
# '-5'      minstens 0
# '200'     hoogstens 130
# '24.0'    24
