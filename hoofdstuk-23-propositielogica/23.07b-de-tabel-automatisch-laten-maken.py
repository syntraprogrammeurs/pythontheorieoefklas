# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.7 De tabel automatisch laten maken
#
# Met dezelfde aanpak kun je gelijkwaardigheid nagaan.

# Twee uitdrukkingen zijn LOGISCH GELIJKWAARDIG (23.6) als ze op ELKE rij van de
# waarheidstabel dezelfde waarde geven. Eén rij die verschilt, en ze zijn het niet.
# product geeft alle combinaties van True en False (zie 23.07a).
from itertools import product


# aantal -> hoeveel variabelen de formules hebben
# links, rechts -> twee functies (lambda's) die je met elkaar vergelijkt
# all() uit hoofdstuk 12 geeft True als ELKE vergelijking True is, en stopt bij
# de eerste False. Tussen de haakjes staat een generator (hoofdstuk 14): voor
# elke rij w de vraag "geven links en rechts hier hetzelfde?".
# links(*w): het sterretje pakt de tuple w uit tot losse argumenten (zie 23.07a).
def gelijkwaardig(aantal, links, rechts):
    """True als beide formules op elke rij dezelfde waarde geven."""
    return all(links(*w) == rechts(*w)
               for w in product([True, False], repeat=aantal))


# De Morgan
# De wet van De Morgan uit hoofdstuk 7: NIET (p EN q) is hetzelfde als
# (NIET p) OF (NIET q). Verwacht: True.
# print() met een komma tussen de delen zet er een spatie tussen.
print("De Morgan:      ",
      gelijkwaardig(2,
                    lambda p, q: not (p and q),
                    lambda p, q: (not p) or (not q)))

# Contrapositie
# De CONTRAPOSITIE: "als p dan q" is hetzelfde als "als niet q dan niet p".
# Beide kanten zijn een implicatie, vertaald met (not A) or B (23.3):
#   links:  p -> q            wordt (not p) or q
#   rechts: (niet q) -> (niet p) wordt (not (not q)) or (not p)
# Omkeren EN ontkennen verandert niets aan de betekenis. Verwacht: True.
print("Contrapositie:  ",
      gelijkwaardig(2,
                    lambda p, q: (not p) or q,
                    lambda p, q: (not (not q)) or (not p)))

# Alleen omkeren: NIET gelijkwaardig
# Het OMGEKEERDE: "als q dan p", rechts vertaald als (not q) or p. Dat is een
# andere bewering. Bij p onwaar en q waar is links True en rechts False.
# LET OP: dit is een veelgemaakte denkfout. "Wie geschorst is, mag niet lenen"
# betekent niet "wie niet mag lenen, is geschorst". Verwacht: False.
print("Alleen omkeren: ",
      gelijkwaardig(2,
                    lambda p, q: (not p) or q,
                    lambda p, q: (not q) or p))


# Verwachte uitvoer:
# De Morgan:       True
# Contrapositie:   True
# Alleen omkeren:  False
