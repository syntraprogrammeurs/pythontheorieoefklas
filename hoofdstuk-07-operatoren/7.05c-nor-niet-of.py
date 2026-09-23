# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.5 De drie poorten die Python niet heeft: NAND, NOR en XOR — NOR — niet of

a = False
b = False

print(not (a or b))
print((not a) and (not b))    # hetzelfde, opnieuw De Morgan


# Verwachte uitvoer:
# True
# True
