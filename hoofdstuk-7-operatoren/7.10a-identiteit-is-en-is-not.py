# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.10 Identiteit: is en is not

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)      # True   — dezelfde inhoud
print(a is b)      # False  — niet hetzelfde object
print(a is c)      # True   — c verwijst naar hetzelfde object als a
