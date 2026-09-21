# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.7 Kortsluiting
#
# Dat is niet alleen sneller, het is ook een veiligheidsklep:

deler = 0

# dit crasht niet
if deler != 0 and 10 / deler > 2:
    print("groter")

print("we zijn nog in leven")


# Verwachte uitvoer:
# we zijn nog in leven
