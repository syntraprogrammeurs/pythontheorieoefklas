# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.8 Geldigheid toetsen met een waarheidstabel

from itertools import product


def geldig(aantal, premissen, conclusie):
    """(geldig?, tegenvoorbeeld) — het tegenvoorbeeld is None als het klopt."""
    for w in product([True, False], repeat=aantal):
        if all(premisse(*w) for premisse in premissen) and not conclusie(*w):
            return False, w
    return True, None


# Modus ponens:  p -> q,  p,  dus q
print("modus ponens         ",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: p],
             lambda p, q: q))

# Modus tollens: p -> q,  niet q,  dus niet p
print("modus tollens        ",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: not q],
             lambda p, q: not p))

# Bevestigen van het consequens:  p -> q,  q,  dus p
print("consequens bevestigen",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: q],
             lambda p, q: p))

# Ontkennen van het antecedens:  p -> q,  niet p,  dus niet q
print("antecedens ontkennen ",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: not p],
             lambda p, q: not q))


# Verwachte uitvoer:
# modus ponens          (True, None)
# modus tollens         (True, None)
# consequens bevestigen (False, (False, True))
# antecedens ontkennen  (False, (False, True))
