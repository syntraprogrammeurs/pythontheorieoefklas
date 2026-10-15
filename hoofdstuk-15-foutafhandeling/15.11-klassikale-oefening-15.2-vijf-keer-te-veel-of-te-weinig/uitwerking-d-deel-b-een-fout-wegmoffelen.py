# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# Twee juiste vormen:

def lees_leeftijd(tekst: str) -> int | None:
    """Het getal, of None wanneer de tekst geen getal is."""
    try:
        return int(tekst)
    except ValueError:
        return None


print(lees_leeftijd("abc"))
print(lees_leeftijd("0"))


# Verwachte uitvoer:
# None
# 0
