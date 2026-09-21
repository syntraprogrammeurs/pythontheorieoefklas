# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.5 De drie poorten die Python niet heeft: NAND, NOR en XOR — De zes poorten samen

for a in (False, True):
    for b in (False, True):
        print(f"{a!s:<6}{b!s:<6}"
              f"{not a!s:<7}"
              f"{a and b!s:<7}"
              f"{a or b!s:<7}"
              f"{a != b!s:<7}"
              f"{not (a and b)!s:<7}"
              f"{not (a or b)!s:<7}")


# Verwachte uitvoer:
# False False True   False  False  False  True   True
# False True  True   False  True   True   True   False
# True  False False  False  True   True   True   False
# True  True  False  True   True   False  False  False
