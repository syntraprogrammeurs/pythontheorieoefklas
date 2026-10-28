# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# Klassikale oefening 23.2 — Een tautologiecontrole bouwen, uitwerking

# Tautologie, contradictie of contingentie
# product geeft alle combinaties van True en False (zie 23.07a).
from itertools import product


# Deze functie kijkt alleen naar de LAATSTE KOLOM van de waarheidstabel (23.5):
#   altijd True        -> TAUTOLOGIE
#   nooit True         -> CONTRADICTIE
#   soms wel, soms niet -> CONTINGENTIE
# Ze geeft een van die drie woorden terug als string.
def beoordeel(aantal, formule):
    """Zegt wat de laatste kolom van de waarheidstabel doet."""
    # Een list comprehension (hoofdstuk 14): de uitkomst van de formule voor elke
    # rij w. Dit is de laatste kolom, als lijst van True en False.
    # Een lijst (en geen generator), omdat je er twee keer naar kijkt.
    uitkomsten = [formule(*w)
                  for w in product([True, False], repeat=aantal)]
    # all() uit hoofdstuk 12: True als ELKE waarde True is.
    if all(uitkomsten):
        return "tautologie"
    # any() geeft True als MINSTENS ÉÉN waarde True is. not any(...) betekent dus:
    # geen enkele rij is waar.
    if not any(uitkomsten):
        return "contradictie"
    # Hier kom je alleen als geen van beide return's hierboven uitvoerde: er is
    # minstens één True en minstens één False.
    return "contingentie"


# Een lijst van tuples (hoofdstuk 13). Elke tuple heeft drie delen:
#   de naam om af te drukken, het aantal variabelen, en de formule als lambda.
# Elke implicatie A -> B is vertaald als (not A) or B (23.3).
# Een tuple die te lang is voor één regel, mag je over twee regels verdelen:
# binnen haakjes leest Python gewoon verder.
formules = [
    # Altijd waar: p is waar, of het is niet waar. Een derde is er niet.
    ("p OF NIET p", 1, lambda p: p or not p),
    # Nooit waar: p kan niet tegelijk waar en onwaar zijn.
    ("p EN NIET p", 1, lambda p: p and not p),
    # Soms waar, soms niet (zie de tabel in 23.03a).
    ("p -> q", 2, lambda p, q: (not p) or q),
    # Een verrassende tautologie: van twee beweringen volgt er altijd minstens
    # één uit de andere, ook als ze niets met elkaar te maken hebben. Logica
    # kijkt naar waarheidswaarden, niet naar betekenis.
    ("(p -> q) OF (q -> p)", 2,
     lambda p, q: ((not p) or q) or ((not q) or p)),
    # Als p en q allebei waar zijn, is zeker één van beide waar: altijd waar.
    ("(p EN q) -> (p OF q)", 2,
     lambda p, q: (not (p and q)) or (p or q)),
]

# Elke tuple wordt in de for-kop uitgepakt in drie variabelen.
# {naam:<24}: de naam links uitgelijnd in 24 tekens, zodat het oordeel netjes
# in een kolom staat (hoofdstuk 6).
for naam, aantal, formule in formules:
    print(f"{naam:<24}{beoordeel(aantal, formule)}")


# Verwachte uitvoer:
# p OF NIET p             tautologie
# p EN NIET p             contradictie
# p -> q                  contingentie
# (p -> q) OF (q -> p)    tautologie
# (p EN q) -> (p OF q)    tautologie
