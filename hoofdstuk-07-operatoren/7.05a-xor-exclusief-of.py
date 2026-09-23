# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.5 De drie poorten die Python niet heeft: NAND, NOR en XOR — XOR — exclusief of
#
# Drie manieren om het in Python te schrijven:

a = True
b = False

print(a != b)                          # de eenvoudigste, voor booleans
print((a or b) and not (a and b))      # letterlijk de definitie
print(bool(a) ^ bool(b))               # met de bitsgewijze operator


# Verwachte uitvoer:
# True
# True
# True
