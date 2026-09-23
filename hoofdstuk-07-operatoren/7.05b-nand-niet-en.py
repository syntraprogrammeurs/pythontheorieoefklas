# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.5 De drie poorten die Python niet heeft: NAND, NOR en XOR — NAND — niet en

a = True
b = True

print(not (a and b))
print((not a) or (not b))     # hetzelfde, volgens De Morgan


# Verwachte uitvoer:
# False
# False
