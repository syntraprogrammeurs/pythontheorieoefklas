# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.3 De implicatie, en waarom ze verwarrend is
#
# In Python zie je hetzelfde:

def implicatie(p, q):
    """p -> q, oftewel: als p dan q."""
    return (not p) or q


for p in (True, False):
    for q in (True, False):
        print(f"p={p!s:<5} q={q!s:<5} p -> q = {implicatie(p, q)}")


# Verwachte uitvoer:
# p=True  q=True  p -> q = True
# p=True  q=False p -> q = False
# p=False q=True  p -> q = True
# p=False q=False p -> q = True
