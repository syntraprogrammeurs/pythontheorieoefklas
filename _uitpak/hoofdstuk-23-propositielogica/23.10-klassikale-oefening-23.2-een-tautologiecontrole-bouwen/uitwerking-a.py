# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# Klassikale oefening 23.2 — Een tautologiecontrole bouwen, uitwerking

# Tautologie, contradictie of contingentie
from itertools import product


def beoordeel(aantal, formule):
    """Zegt wat de laatste kolom van de waarheidstabel doet."""
    uitkomsten = [formule(*w)
                  for w in product([True, False], repeat=aantal)]
    if all(uitkomsten):
        return "tautologie"
    if not any(uitkomsten):
        return "contradictie"
    return "contingentie"


formules = [
    ("p OF NIET p", 1, lambda p: p or not p),
    ("p EN NIET p", 1, lambda p: p and not p),
    ("p -> q", 2, lambda p, q: (not p) or q),
    ("(p -> q) OF (q -> p)", 2,
     lambda p, q: ((not p) or q) or ((not q) or p)),
    ("(p EN q) -> (p OF q)", 2,
     lambda p, q: (not (p and q)) or (p or q)),
]

for naam, aantal, formule in formules:
    print(f"{naam:<24}{beoordeel(aantal, formule)}")


# Verwachte uitvoer:
# p OF NIET p             tautologie
# p EN NIET p             contradictie
# p -> q                  contingentie
# (p -> q) OF (q -> p)    tautologie
# (p EN q) -> (p OF q)    tautologie
