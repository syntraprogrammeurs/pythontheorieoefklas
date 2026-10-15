# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.5 Zelf een fout veroorzaken met raise

def bereken_lidgeld(leeftijd: int) -> int:
    # """Het lidgeld. Weigert een onmogelijke leeftijd."""
    if leeftijd < 0:
        raise ValueError(f"leeftijd kan niet negatief zijn: {leeftijd}")
    if leeftijd > 130:
        raise ValueError(f"leeftijd lijkt onmogelijk: {leeftijd}")
    return 0 if leeftijd < 12 else 30


print(bereken_lidgeld(34))

try:
    bereken_lidgeld(-5)
except ValueError as fout:
    print("Geweigerd:", fout)


# Verwachte uitvoer:
# 30
# Geweigerd: leeftijd kan niet negatief zijn: -5
