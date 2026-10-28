# Python basis — theoriebundel
# Hoofdstuk 26 — Categorische logica en venndiagrammen
# 26.6 De acht gebieden in Python
#
# De diagrammethode laat zich programmeren, en het resultaat is de tegenhanger van de
# waarheidstabel uit hoofdstuk 23. In plaats van alle combinaties van waarheidswaarden
# ga je alle mogelijke werelden af: welke van de acht gebieden zijn bewoond en welke
# niet.

# Syllogismen toetsen door alle werelden af te gaan
#
# Het idee in één zin: een venndiagram met drie cirkels (S, P en M) heeft acht
# GEBIEDEN. Een WERELD is een keuze welke van die acht gebieden BEWOOND zijn (er zit
# minstens iemand) en welke LEEG zijn. Dit bestand bouwt die gebieden en werelden op,
# en schrijft de vier categorische uitspraken (A, E, I, O uit 26.2) als functies.
# In 26.06b gebruik je dat alles om een syllogisme te toetsen.

# itertools.product kent je uit hoofdstuk 23 (de waarheidstabel). product(x, repeat=n)
# geeft ALLE combinaties van n waarden uit x, als tupels. Met [False, True] en repeat=3
# krijg je 2 x 2 x 2 = 8 tupels: (False, False, False), (False, False, True), ...
from itertools import product

# De drie groepen (TERMEN) van een syllogisme, uit 26.4:
#   S = het onderwerp van de conclusie
#   P = het predicaat van de conclusie
#   M = de MIDDENTERM: staat in beide premissen, maar niet in de conclusie
# Een tupel en geen lijst: deze volgorde mag nooit veranderen, want ze bepaalt welke
# plaats in een gebied bij welke groep hoort (zie hoort_bij hieronder).
TERMEN = ("S", "P", "M")

# Elk GEBIED is een tupel van drie waarheidswaarden: (in S?, in P?, in M?).
#   (False, False, False) -> buiten alles          (gebied 1 in de tabel van 26.4)
#   (False, False, True)  -> alleen M              (gebied 2)
#   (True, True, True)    -> in alle drie          (gebied 8)
# Omdat product met False begint, staan de acht gebieden in precies dezelfde volgorde
# als in de tabel van 26.4. list() maakt er een echte lijst van: product geeft
# anders een "eenmalige" reeks die je maar één keer kunt doorlopen.
GEBIEDEN = list(product([False, True], repeat=3))


# Hulpfunctie: ligt dit gebied binnen de groep 'term'?
#   gebied -> een tupel zoals (True, False, True)
#   term   -> "S", "P" of "M"
# TERMEN.index(term) zoekt de plaats van de term in TERMEN: "S" -> 0, "P" -> 1,
# "M" -> 2. Met die plaats haal je de juiste True/False uit het gebied.
# Voorbeeld: hoort_bij((True, False, True), "M") -> index 2 -> True.
def hoort_bij(gebied, term):
    """Zit dit gebied binnen de gegeven groep?"""
    return gebied[TERMEN.index(term)]


# De vier categorische vormen uit 26.2, elk als functie.
# Elke functie krijgt:
#   wereld -> een tupel met de BEWOONDE gebieden (wat er niet in staat, is leeg)
#   a, b   -> twee termen, bv. "M" en "P" voor "alle M zijn P"
# en geeft True of False terug: klopt deze uitspraak in deze wereld?
#
# Je gebruikt telkens any() (hoofdstuk 12): any(...) geeft True zodra minstens één
# element waar is, en False als er geen enkel is (ook bij een lege reeks).
# Tussen de haakjes staat een GENERATOR-uitdrukking: "... for g in wereld" rekent voor
# elk bewoond gebied g één True/False uit, zonder eerst een lijst te maken.


# A-uitspraak (algemeen bevestigend): "Alle A zijn B".
# Venndiagram: het gebied "in A en buiten B" is LEEG (gearceerd).
# In code: er is GEEN bewoond gebied dat in a ligt en niet in b.
# Dus: not any(...). Is er zo'n gebied, dan is dat een tegenvoorbeeld.
# LET OP: in een lege wereld geeft any() False, dus alle() geeft True.
# "Alle A zijn B" is dus waar als er geen enkele A bestaat. Dat is de bewuste keuze
# uit 26.3: "alle" garandeert niet dat de groep bestaat (net als all([]) == True).
def alle(wereld, a, b):
    """Alle A zijn B: geen bewoond gebied ligt in A en buiten B."""
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


# E-uitspraak (algemeen ontkennend): "Geen enkele A is B".
# Venndiagram: de overlap van A en B is LEEG.
# In code: er is geen bewoond gebied dat in a EN in b ligt.
def geen(wereld, a, b):
    """Geen enkele A is B: geen bewoond gebied ligt in allebei."""
    return not any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


# I-uitspraak (particulier bevestigend): "Sommige A zijn B".
# Venndiagram: een X in de overlap van A en B.
# In code: minstens één bewoond gebied ligt in a en in b.
# Vergelijk met geen(): precies dezelfde any(), maar zonder "not" ervoor.
# Dat is de TEGENSPRAAK tussen E en I uit 26.3: precies één van de twee is waar.
def sommige(wereld, a, b):
    """Sommige A zijn B: minstens één bewoond gebied ligt in allebei."""
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


# O-uitspraak (particulier ontkennend): "Sommige A zijn geen B".
# Venndiagram: een X in het gebied "in A, buiten B".
# Vergelijk met alle(): dezelfde any(), zonder "not". A en O spreken elkaar tegen.
# Daarom is de ontkenning van "alle" niet "geen enkele", maar "sommige niet".
def sommige_niet(wereld, a, b):
    """Sommige A zijn geen B: minstens één bewoond gebied ligt in A, buiten B."""
    return any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


# werelden() maakt alle mogelijke werelden aan, één voor één.
# Elk van de acht gebieden is bewoond of leeg: 2 tot de achtste macht = 256 werelden.
#
# Hoe het werkt:
#   - product([False, True], repeat=8) geeft 256 tupels van acht True/False-waarden.
#     Elke 'keuze' zegt per gebied: bewoond (True) of leeg (False).
#   - zip(GEBIEDEN, keuze) legt elk gebied naast zijn True/False:
#     (gebied1, False), (gebied2, True), ...
#   - "... if bewoond" houdt alleen de bewoonde gebieden over.
#   - tuple(...) maakt daar één tupel van: dat is de wereld.
#
# yield in plaats van return: dit is een GENERATOR. De functie geeft telkens één
# wereld af en loopt pas verder als iemand om de volgende vraagt. Zo hoeft Python
# niet alle 256 werelden tegelijk in het geheugen te houden.
# De eerste wereld is de LEGE wereld (keuze bestaat volledig uit False): ().
def werelden():
    """Alle 256 manieren waarop de acht gebieden bewoond kunnen zijn."""
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


# Controle: klopt het aantal gebieden en werelden?
# len(GEBIEDEN) werkt, want GEBIEDEN is een lijst.
# LET OP: len(werelden()) werkt NIET: een generator heeft geen lengte. Daarom eerst
# list(werelden()), dat alle werelden ophaalt in een lijst, en daarvan de lengte.
# De functies alle, geen, sommige en sommige_niet worden hier nog niet gebruikt: ze
# staan klaar voor de toets in 26.06b.
print("Aantal gebieden :", len(GEBIEDEN))
print("Aantal werelden :", len(list(werelden())))


# Verwachte uitvoer:
# Aantal gebieden : 8
# Aantal werelden : 256
