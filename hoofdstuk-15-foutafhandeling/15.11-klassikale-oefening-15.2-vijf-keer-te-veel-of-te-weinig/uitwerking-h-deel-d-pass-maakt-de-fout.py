# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# pass in een except is bijna altijd fout. Kies er één van:

def deel(a: float, b: float) -> float | None:
    """Deelt a door b. Geeft None wanneer b nul is."""
    if b == 0:
        return None
    return a / b


print(deel(10, 0))


# Verwachte uitvoer:
# None
