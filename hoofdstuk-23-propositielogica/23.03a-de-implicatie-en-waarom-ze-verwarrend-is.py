# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.3 De implicatie, en waarom ze verwarrend is
#
# In Python zie je hetzelfde:

# De IMPLICATIE p -> q ("als p dan q") is een belofte over één situatie: als p
# waar is, dan moet q ook waar zijn. Ze is alleen geschonden als p waar is en q
# onwaar. Is p onwaar, dan is de implicatie altijd waar: LEEG WAAR.
# Python heeft geen operator voor de implicatie. De juiste vertaling is
# (not p) or q: "p is niet waar, of q is waar". Die is alleen False als
# not p False is (p waar) EN q False is: precies de ene rij waarin de belofte
# gebroken wordt.
# LET OP: p and q is GEEN implicatie. Dat geeft False zodra p onwaar is, terwijl
# de implicatie dan juist True is.
def implicatie(p, q):
    """p -> q, oftewel: als p dan q."""
    # De haakjes rond not p zijn niet nodig (not gaat voor or, hoofdstuk 7),
    # maar ze maken duidelijk wat bij elkaar hoort.
    return (not p) or q


# Twee geneste for-lussen (hoofdstuk 10) over de tuple (True, False) geven
# alle 2 x 2 = 4 combinaties van p en q: de vier rijen van de waarheidstabel.
# {p!s:<5} uit hoofdstuk 7: !s zet de boolean eerst om naar tekst ("True"), en
# :<5 lijnt die links uit in 5 tekens. Zonder !s weigert Python die uitlijning
# toe te passen op een boolean.
# Kijk in de uitvoer naar de twee onderste rijen: p is False, en p -> q is True,
# wat q ook is. Dat is het "leeg waar" van hierboven.
for p in (True, False):
    for q in (True, False):
        print(f"p={p!s:<5} q={q!s:<5} p -> q = {implicatie(p, q)}")


# Verwachte uitvoer:
# p=True  q=True  p -> q = True
# p=True  q=False p -> q = False
# p=False q=True  p -> q = True
# p=False q=False p -> q = True
