# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.7 De tabel automatisch laten maken
#
# Acht rijen doe je met de hand. Zestien is vervelend, tweeëndertig is een bron van
# fouten. Dit is werk voor een computer.

# Een waarheidstabel automatisch opstellen
# itertools is een module uit de standaardbibliotheek met hulpmiddelen voor
# lussen. Je haalt er alleen de functie product uit.
# itertools.product(reeks, repeat=n) geeft ALLE combinaties van n waarden uit die
# reeks, één voor één, als tuples. Voorbeeld:
#   product([True, False], repeat=2) geeft
#   (True, True), (True, False), (False, True), (False, False)
# Met n variabelen zijn dat 2 tot de macht n rijen, precies zoals in 23.4.
# Het voordeel tegenover geneste lussen (zoals in 23.03a): voor vier variabelen
# verander je één getal, in plaats van een extra lus bij te schrijven.
from itertools import product


# De functie krijgt drie dingen mee:
#   namen   -> een lijst met de namen van de variabelen, bv. ["p", "q", "r"]
#   formule -> een FUNCTIE (hier een lambda) die voor één rij True of False
#              teruggeeft. Je geeft een functie door als waarde, zonder haakjes.
#   label   -> de tekst boven de laatste kolom
# Ze geeft niets terug (None): ze drukt alleen af.
def waarheidstabel(namen, formule, label):
    """Drukt de waarheidstabel van `formule` af over de variabelen `namen`."""
    # De kopregel. "".join(...) uit hoofdstuk 8 plakt alle stukjes tekst aan
    # elkaar, met niets ("") ertussen. De stukjes komen uit een generator: elke
    # naam links uitgelijnd in 8 tekens. Daarachter komt het label.
    kop = "".join(f"{naam:<8}" for naam in namen) + label
    print(kop)
    # "-" * getal herhaalt het streepje: een lijn die precies zo lang is als de kop.
    print("-" * len(kop))
    # Elke ronde is waarden één tuple, bv. (True, False, True): één rij.
    # repeat=len(namen) zorgt dat het aantal waarden past bij het aantal namen.
    for waarden in product([True, False], repeat=len(namen)):
        # Elke waarde als tekst (!s), links uitgelijnd in 8 tekens.
        cellen = "".join(f"{w!s:<8}" for w in waarden)
        # formule(*waarden): het STERRETJE pakt de tuple uit tot losse
        # argumenten. formule(*(True, False, True)) is hetzelfde als
        # formule(True, False, True). Zo werkt de functie voor elk aantal
        # variabelen. str() maakt van de uitkomst tekst, zodat je ze met + aan
        # cellen kunt plakken (str + bool geeft een TypeError).
        print(cellen + str(formule(*waarden)))


# De oproep, verdeeld over drie regels omdat ze lang is. Python ziet dat de
# haakjes nog niet gesloten zijn en leest gewoon verder.
# De formule is een LAMBDA (hoofdstuk 11.8) met drie parameters, één per naam.
# Ze vertaalt (p EN NIET q) -> r met de regel uit 23.3: "als A dan r" wordt
# (not A) or r. Hier is A = (p and not q). Het extra paar haakjes rond
# p and not q is overbodig, maar onschuldig.
# De uitkomst is één keer False: p waar, q onwaar, r onwaar (rij vier). Dat is
# de enige rij waarin de belofte gebroken wordt.
waarheidstabel(["p", "q", "r"],
               lambda p, q, r: (not ((p and not q))) or r,
               "(p AND NIET q) -> r")


# Verwachte uitvoer:
# p       q       r       (p AND NIET q) -> r
# -------------------------------------------
# True    True    True    True
# True    True    False   True
# True    False   True    True
# True    False   False   False
# False   True    True    True
# False   True    False   True
# False   False   True    True
# False   False   False   True
