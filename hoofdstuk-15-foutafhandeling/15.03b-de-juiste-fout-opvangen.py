# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.3 De juiste fout opvangen
#
# Meerdere soorten in één except:

try:
    getal = int("abc")
except (ValueError, TypeError) as fout:
    print(f"Er ging iets mis: {fout}")
    print(f"De soort was: {type(fout).__name__}")


# Verwachte uitvoer:
# Er ging iets mis: invalid literal for int() with base 10: 'abc'
# De soort was: ValueError
