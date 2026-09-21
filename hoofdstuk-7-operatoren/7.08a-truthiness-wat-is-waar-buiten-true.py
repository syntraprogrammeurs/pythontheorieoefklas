# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.8 Truthiness: wat is "waar" buiten True

print(bool(0))          # False
print(bool(-1))         # True   — niet nul, dus waar
print(bool(""))         # False
print(bool(" "))        # True   — een spatie is een teken
print(bool([]))         # False
print(bool([0]))        # True   — een lijst met één element
print(bool("False"))    # True   — tekst, en niet leeg
