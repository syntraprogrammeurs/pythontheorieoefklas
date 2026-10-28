# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.8 Geldigheid toetsen met een waarheidstabel

# De TOETS OP GELDIGHEID: een argument is ONGELDIG zodra er één rij bestaat waarin
# alle premissen waar zijn en de conclusie onwaar. Zo'n rij heet een
# TEGENVOORBEELD. Bestaat er geen enkele zo'n rij, dan is het argument geldig.
# Dit programma zoekt die rij voor je, over alle combinaties (zie 23.07a).
from itertools import product


# aantal    -> hoeveel variabelen er zijn (hier telkens 2: p en q)
# premissen -> een LIJST van functies, één per premisse
# conclusie -> één functie
# De functie geeft altijd een tuple van twee waarden terug (hoofdstuk 11 en 13):
#   (False, w)    -> ongeldig, en w is het tegenvoorbeeld
#   (True, None)  -> geldig, er is geen tegenvoorbeeld
def geldig(aantal, premissen, conclusie):
    """(geldig?, tegenvoorbeeld) — het tegenvoorbeeld is None als het klopt."""
    for w in product([True, False], repeat=aantal):
        # all(...) met een generator: is ELKE premisse waar op deze rij w?
        # Elke premisse is een functie, die je oproept met de waarden uit w.
        # and not conclusie(*w): en is de conclusie hier onwaar?
        # Allebei waar: dit is een tegenvoorbeeld. return stopt de lus meteen,
        # want één tegenvoorbeeld volstaat.
        if all(premisse(*w) for premisse in premissen) and not conclusie(*w):
            return False, w
    # Deze regel bereik je alleen als de lus ALLE rijen afliep zonder
    # tegenvoorbeeld te vinden.
    return True, None


# Bij elk argument: de eerste premisse is telkens de implicatie p -> q,
# vertaald als (not p) or q (23.3). De tweede premisse en de conclusie wisselen.
# De lambda's krijgen allemaal p en q als parameters, ook als ze er maar één
# gebruiken: geldig() roept elke functie op met beide waarden.

# Modus ponens:  p -> q,  p,  dus q
# Geldig: als p waar is en p -> q ook, dan moet q waar zijn.
print("modus ponens         ",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: p],
             lambda p, q: q))

# Modus tollens: p -> q,  niet q,  dus niet p
# Geldig: dit is de contrapositie uit 23.07b in actie.
print("modus tollens        ",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: not q],
             lambda p, q: not p))

# Bevestigen van het consequens:  p -> q,  q,  dus p
# Ongeldig. Tegenvoorbeeld (False, True): p onwaar, q waar. Beide premissen zijn
# dan waar, de conclusie p niet. In je werk: "de test faalt, dus de code is
# fout" klopt niet, want de test zelf kan fout zijn.
print("consequens bevestigen",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: q],
             lambda p, q: p))

# Ontkennen van het antecedens:  p -> q,  niet p,  dus niet q
# Ook ongeldig, met hetzelfde tegenvoorbeeld: p onwaar, q toch waar.
# print() toont de tuple met haakjes, zoals in de uitvoer hieronder.
print("antecedens ontkennen ",
      geldig(2, [lambda p, q: (not p) or q, lambda p, q: not p],
             lambda p, q: not q))


# Verwachte uitvoer:
# modus ponens          (True, None)
# modus tollens         (True, None)
# consequens bevestigen (False, (False, True))
# antecedens ontkennen  (False, (False, True))
