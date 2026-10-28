# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.3 Het omgekeerde, het tegengestelde en de contrapositie

from itertools import product


def gelijkwaardig(links, rechts):
    """Vergelijkt twee formules over twee variabelen, op alle vier de rijen."""
    return all(links(p, q) == rechts(p, q)
               for p, q in product([True, False], repeat=2))


origineel = lambda p, q: (not p) or q            # noqa: E731
omgekeerde = lambda p, q: (not q) or p           # noqa: E731
tegengestelde = lambda p, q: p or (not q)        # noqa: E731
contrapositie = lambda p, q: q or (not p)        # noqa: E731

print("omgekeerde    == origineel:", gelijkwaardig(origineel, omgekeerde))
print("tegengestelde == origineel:", gelijkwaardig(origineel, tegengestelde))
print("contrapositie == origineel:", gelijkwaardig(origineel, contrapositie))
print("omgekeerde    == tegengestelde:",
      gelijkwaardig(omgekeerde, tegengestelde))


# Verwachte uitvoer:
# omgekeerde    == origineel: False
# tegengestelde == origineel: False
# contrapositie == origineel: True
# omgekeerde    == tegengestelde: True
