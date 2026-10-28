# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.7 De tabel automatisch laten maken
#
# Met dezelfde aanpak kun je gelijkwaardigheid nagaan.

from itertools import product


def gelijkwaardig(aantal, links, rechts):
    """True als beide formules op elke rij dezelfde waarde geven."""
    return all(links(*w) == rechts(*w)
               for w in product([True, False], repeat=aantal))


# De Morgan
print("De Morgan:      ",
      gelijkwaardig(2,
                    lambda p, q: not (p and q),
                    lambda p, q: (not p) or (not q)))

# Contrapositie
print("Contrapositie:  ",
      gelijkwaardig(2,
                    lambda p, q: (not p) or q,
                    lambda p, q: (not (not q)) or (not p)))

# Alleen omkeren: NIET gelijkwaardig
print("Alleen omkeren: ",
      gelijkwaardig(2,
                    lambda p, q: (not p) or q,
                    lambda p, q: (not q) or p))


# Verwachte uitvoer:
# De Morgan:       True
# Contrapositie:   True
# Alleen omkeren:  False
