# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.3 Het omgekeerde, het tegengestelde en de contrapositie

# Uit één implicatie p -> q kun je drie andere maken (24.3). Neem als voorbeeld:
#   "Als een lid geschorst is (p), mag het niet lenen (q)."
#
#   Naam            Vorm         Gelijkwaardig aan het origineel?
#   origineel       p -> q       -
#   OMGEKEERDE      q -> p       nee
#   TEGENGESTELDE   niet p -> niet q   nee
#   CONTRAPOSITIE   niet q -> niet p   ja
#
# Twee formules zijn GELIJKWAARDIG (23.6) als ze op ELKE rij van de waarheidstabel
# dezelfde waarde geven. Dit programma controleert dat voor alle vier de rijen.

# product maakt alle combinaties van True en False: de rijen van de tabel (23.7).
from itertools import product


# gelijkwaardig() krijgt twee functies mee (links en rechts). Elke functie neemt
# p en q en geeft True of False terug. De functie geeft zelf True terug als beide
# formules op alle vier de rijen hetzelfde zeggen, anders False.
def gelijkwaardig(links, rechts):
    """Vergelijkt twee formules over twee variabelen, op alle vier de rijen."""
    # product([True, False], repeat=2) levert (True, True), (True, False),
    # (False, True) en (False, False). Elke rij wordt meteen uitgepakt in p en q.
    # all(...) geeft True als de vergelijking op ELKE rij True is; zodra één rij
    # verschilt, stopt all() en geeft False. Tussen de haakjes staat een
    # generator-expressie: een comprehension (hoofdstuk 14) zonder vierkante haken.
    # De regel loopt door op de volgende regel: binnen haakjes mag dat in Python.
    return all(links(p, q) == rechts(p, q)
               for p, q in product([True, False], repeat=2))


# De vier formules, elk als LAMBDA (hoofdstuk 11): een korte functie zonder def.
# Elke implicatie a -> b schrijf je in Python als (not a) or b (zie 23.3).
# "# noqa: E731" vraagt de stijlcontrole om hier geen opmerking te geven over een
# lambda met een naam.

# origineel: p -> q
origineel = lambda p, q: (not p) or q            # noqa: E731
# omgekeerde: q -> p, dus (not q) or p. Voor- en achterkant zijn verwisseld.
omgekeerde = lambda p, q: (not q) or p           # noqa: E731
# tegengestelde: (niet p) -> (niet q), dus (not (not p)) or (not q).
# not (not p) is gewoon p, dus: p or (not q).
tegengestelde = lambda p, q: p or (not q)        # noqa: E731
# contrapositie: (niet q) -> (niet p), dus (not (not q)) or (not p).
# not (not q) is gewoon q, dus: q or (not p).
# Kijk goed: dat is (not p) or q met de twee delen in een andere volgorde.
# "or" is COMMUTATIEF (a or b is hetzelfde als b or a), dus dit MOET wel
# gelijkwaardig zijn aan het origineel.
contrapositie = lambda p, q: q or (not p)        # noqa: E731

# Drie vergelijkingen met het origineel. Verwacht: alleen de contrapositie klopt.
print("omgekeerde    == origineel:", gelijkwaardig(origineel, omgekeerde))
print("tegengestelde == origineel:", gelijkwaardig(origineel, tegengestelde))
print("contrapositie == origineel:", gelijkwaardig(origineel, contrapositie))
# De "aardigheid" uit 24.3: het omgekeerde en het tegengestelde zijn wel
# gelijkwaardig aan ELKAAR. Ze zijn elkaars contrapositie.
print("omgekeerde    == tegengestelde:",
      gelijkwaardig(omgekeerde, tegengestelde))

# Waarom dit belangrijk is (het patroon uit 24.3):
#   - het omgekeerde aannemen IS het bevestigen van het consequens;
#   - het tegengestelde aannemen IS het ontkennen van het antecedens.
# Twee manieren om naar dezelfde twee fouten uit 24.2 te kijken. Wil je een regel
# toch "omdraaien", doe het dan altijd met omkeren EN ontkennen: de contrapositie.


# Verwachte uitvoer:
# omgekeerde    == origineel: False
# tegengestelde == origineel: False
# contrapositie == origineel: True
# omgekeerde    == tegengestelde: True
