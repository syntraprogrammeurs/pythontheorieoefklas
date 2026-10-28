# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.2 De vier vormen met "als … dan" — Met de toets uit hoofdstuk 23 nagerekend

# De vier vormen, mechanisch getoetst
from itertools import product


def geldig(aantal, premissen, conclusie):
    """(geldig?, tegenvoorbeeld). Ongeldig zodra één rij het breekt."""
    for w in product([True, False], repeat=aantal):
        if all(pr(*w) for pr in premissen) and not conclusie(*w):
            return False, w
    return True, None


ALS_P_DAN_Q = lambda p, q: (not p) or q          # noqa: E731

vormen = [
    ("modus ponens          ", [ALS_P_DAN_Q, lambda p, q: p],
     lambda p, q: q),
    ("modus tollens         ", [ALS_P_DAN_Q, lambda p, q: not q],
     lambda p, q: not p),
    ("consequens bevestigen ", [ALS_P_DAN_Q, lambda p, q: q],
     lambda p, q: p),
    ("antecedens ontkennen  ", [ALS_P_DAN_Q, lambda p, q: not p],
     lambda p, q: not q),
]

for naam, premissen, conclusie in vormen:
    klopt, tegenvoorbeeld = geldig(2, premissen, conclusie)
    if klopt:
        print(f"{naam}geldig")
    else:
        p, q = tegenvoorbeeld
        print(f"{naam}ONGELDIG — tegenvoorbeeld: p={p}, q={q}")


# Verwachte uitvoer:
# modus ponens          geldig
# modus tollens         geldig
# consequens bevestigen ONGELDIG — tegenvoorbeeld: p=False, q=True
# antecedens ontkennen  ONGELDIG — tegenvoorbeeld: p=False, q=True
