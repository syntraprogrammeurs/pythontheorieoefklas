# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.2 De vier vormen met "als … dan" — Met de toets uit hoofdstuk 23 nagerekend

# Dit programma rekent de vier vormen met "als ... dan" uit 24.2 MECHANISCH na,
# met de GELDIGHEIDSTOETS uit 23.8:
#   Een argument is ONGELDIG zodra er één rij in de waarheidstabel bestaat waarin
#   alle premissen waar zijn en de conclusie onwaar. Zo'n rij heet een
#   TEGENVOORBEELD. Bestaat er geen enkele zo'n rij, dan is het argument GELDIG.
# Je hoeft dus niet op je gevoel te vertrouwen: de computer probeert alle rijen.

# De vier vormen, mechanisch getoetst
# itertools is een module uit de standaardbibliotheek (hoofdstuk 17).
# product maakt alle combinaties van waarden: precies de rijen van een
# waarheidstabel (zie 23.7).
from itertools import product


# geldig() krijgt drie dingen mee:
#   aantal    -> hoeveel variabelen er zijn (hier 2: p en q)
#   premissen -> een LIJST van functies; elke functie is één premisse
#   conclusie -> één functie: de conclusie
# Elke premisse en de conclusie is een functie die True of False teruggeeft
# zodra je ze waarden voor p en q geeft.
# geldig() geeft een TUPLE van twee waarden terug (hoofdstuk 13):
#   (True, None)          -> geldig, er is geen tegenvoorbeeld
#   (False, (p, q))       -> ongeldig, en dit is de rij die het bewijst
def geldig(aantal, premissen, conclusie):
    """(geldig?, tegenvoorbeeld). Ongeldig zodra één rij het breekt."""
    # product([True, False], repeat=2) geeft de vier rijen van de tabel:
    #   (True, True), (True, False), (False, True), (False, False)
    # w is telkens één rij, een tuple zoals (True, False).
    for w in product([True, False], repeat=aantal):
        # pr(*w): de ster PAKT DE TUPLE UIT. pr(*(True, False)) is hetzelfde
        # als pr(True, False). Zo werkt geldig() voor elk aantal variabelen.
        #
        # all(...) geeft True als ELK element waar is (en ook bij een lege reeks).
        # Hier: "zijn alle premissen waar op deze rij?". Wat tussen de haakjes
        # staat, is een GENERATOR-EXPRESSIE: een comprehension (hoofdstuk 14)
        # zonder vierkante haken. all() stopt zodra het eerste False opduikt.
        #
        # Samen: alle premissen waar EN de conclusie onwaar = een tegenvoorbeeld.
        if all(pr(*w) for pr in premissen) and not conclusie(*w):
            # Eén tegenvoorbeeld volstaat: meteen stoppen met return.
            return False, w
    # De lus is helemaal doorlopen zonder tegenvoorbeeld: het argument is geldig.
    return True, None


# De implicatie p -> q, als functie geschreven.
# LAMBDA (hoofdstuk 11) maakt een kleine functie zonder naam:
#   lambda p, q: (not p) or q   is hetzelfde als
#   def f(p, q): return (not p) or q
# Waarom (not p) or q? Zo schrijf je de implicatie met de operatoren van Python
# (23.3): p -> q is alleen onwaar als p waar is en q onwaar. Dat klopt hier ook:
# (not True) or False is False, en elke andere combinatie geeft True.
# "# noqa: E731" is een opmerking voor de stijlcontrole (Ruff/flake8). Regel
# E731 zegt "geef een lambda geen naam, schrijf dan een def". noqa = "negeer
# dat hier", omdat de korte vorm hier leesbaarder is.
ALS_P_DAN_Q = lambda p, q: (not p) or q          # noqa: E731

# De vier vormen uit de tabel van 24.2, elk als tuple van drie delen:
#   (naam, lijst van premissen, conclusie)
# De spaties achter de naam zijn er alleen om de uitvoer netjes onder elkaar te
# krijgen: elke naam is even lang.
# Alle vier hebben dezelfde eerste premisse, p -> q. Het verschil zit in de
# tweede premisse en in de conclusie.
vormen = [
    # MODUS PONENS: p -> q, p, dus q. "Je regel vuurt."
    ("modus ponens          ", [ALS_P_DAN_Q, lambda p, q: p],
     lambda p, q: q),
    # MODUS TOLLENS: p -> q, niet q, dus niet p. "Je regel vuurt achterwaarts."
    ("modus tollens         ", [ALS_P_DAN_Q, lambda p, q: not q],
     lambda p, q: not p),
    # BEVESTIGEN VAN HET CONSEQUENS: p -> q, q, dus p. Een drogreden.
    ("consequens bevestigen ", [ALS_P_DAN_Q, lambda p, q: q],
     lambda p, q: p),
    # ONTKENNEN VAN HET ANTECEDENS: p -> q, niet p, dus niet q. Ook een drogreden.
    ("antecedens ontkennen  ", [ALS_P_DAN_Q, lambda p, q: not p],
     lambda p, q: not q),
]

# Elke tuple in vormen wordt meteen UITGEPAKT in drie variabelen (hoofdstuk 13).
for naam, premissen, conclusie in vormen:
    # Ook de terugkeerwaarde van geldig() is een tuple: die pak je uit in twee.
    klopt, tegenvoorbeeld = geldig(2, premissen, conclusie)
    if klopt:
        print(f"{naam}geldig")
    else:
        # tegenvoorbeeld is een tuple zoals (False, True): uitpakken in p en q.
        p, q = tegenvoorbeeld
        print(f"{naam}ONGELDIG — tegenvoorbeeld: p={p}, q={q}")

# Wat je in de uitvoer ziet: beide drogredenen breken op DEZELFDE rij, p onwaar en
# q waar. Met het voorbeeld uit 24.2 ("als de code fout is, falen de tests"): de
# code klopt (p onwaar) en de tests falen toch (q waar). Dat kan, en daarom mag
# je uit "de tests falen" niet besluiten dat de code fout is.


# Verwachte uitvoer:
# modus ponens          geldig
# modus tollens         geldig
# consequens bevestigen ONGELDIG — tegenvoorbeeld: p=False, q=True
# antecedens ontkennen  ONGELDIG — tegenvoorbeeld: p=False, q=True
