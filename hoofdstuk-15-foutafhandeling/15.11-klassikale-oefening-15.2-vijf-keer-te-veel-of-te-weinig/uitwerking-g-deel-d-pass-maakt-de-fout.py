# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# D — pass maakt de fout onzichtbaar.

def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass


print(deel(10, 2))
print(deel(10, 0))


# Verwachte uitvoer:
# 5.0
# None
