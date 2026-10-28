# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# Klassikale oefening 23.2 — Een tautologiecontrole bouwen, uitwerking
#
# De dode-taktest.

# Een voorwaarde uit echte code op dode takken onderzoeken
# Het idee: een if-voorwaarde is een formule. Is ze een TAUTOLOGIE, dan wordt de
# else nooit bereikt. Is ze een CONTRADICTIE, dan wordt het if-blok nooit bereikt.
# Allebei heet dat een DODE TAK (23.5).
from itertools import product


# Geeft een lijst terug met alle combinaties waarvoor de formule ONWAAR is, dus
# de rijen waarin het if-blok NIET uitvoert.
# Van binnen naar buiten gelezen, deze list comprehension (hoofdstuk 14):
#   for w in product(...)  -> loop over alle rijen, bv. (True, False, False)
#   if not formule(*w)     -> hou alleen de rijen over waar de formule False is
#   dict(zip(namen, w))    -> maak van die rij een dictionary.
#                             zip (hoofdstuk 10) koppelt elke naam aan zijn
#                             waarde: ("betaald", True), ("geschorst", False), ...
#                             dict() maakt daar {"betaald": True, ...} van
#                             (dezelfde truc als bij de CSV in hoofdstuk 16).
# Zo zie je bij elke combinatie meteen welke variabele welke waarde had.
def onbereikbaar(namen, formule):
    """De combinaties waarvoor deze voorwaarde nooit waar wordt."""
    return [dict(zip(namen, w))
            for w in product([True, False], repeat=len(namen))
            if not formule(*w)]


# De namen van de drie variabelen, in dezelfde volgorde als de parameters.
NAMEN = ["betaald", "geschorst", "te_veel"]


# Een gezonde voorwaarde: de uitleenregel uit oefening 23.1.
def voorwaarde(betaald, geschorst, te_veel):
    """De uitleenregel uit oefening 23.1."""
    return betaald and not (geschorst or te_veel)


# Je geeft de functie voorwaarde door ZONDER haakjes: onbereikbaar() roept haar
# zelf op, voor elke rij. Van de 8 combinaties geeft er maar één toestemming
# (betaald, niet geschorst, niet te veel), dus 7 zijn er onwaar.
# Dat is een CONTINGENTIE: zowel het if-blok als de else kunnen uitvoeren.
gevallen = onbereikbaar(NAMEN, voorwaarde)
print(f"{len(gevallen)} van de 8 combinaties geven geen toestemming.")
print()


# Een foute voorwaarde: betaald or not betaald is altijd True, een tautologie.
# geschorst en te_veel worden zelfs niet gebruikt. De parameters moeten er toch
# staan, want onbereikbaar() geeft altijd drie waarden mee.
def altijd_waar(betaald, geschorst, te_veel):
    """Een voorwaarde met een fout: hij kan niet onwaar worden."""
    return betaald or not betaald


# Geen enkele combinatie is onwaar, dus de lijst is leeg en len() geeft 0.
# 0 == 0 is True: ja, er is een dode tak, namelijk de else.
print("Dode tak in 'altijd_waar':",
      len(onbereikbaar(NAMEN, altijd_waar)) == 0)


# Een tweede foute voorwaarde: niemand is tegelijk geschorst en niet geschorst.
# Dit is een contradictie: altijd False.
def nooit_waar(betaald, geschorst, te_veel):
    """En een voorwaarde die nooit uitvoert."""
    return geschorst and not geschorst


# Alle 8 combinaties zijn onwaar, dus 8 == 8 is True: het if-blok is dood.
# LET OP: de vergelijking met 8 klopt alleen bij drie variabelen (2 x 2 x 2).
# Bij vier variabelen zou je met 16 moeten vergelijken.
print("Dode tak in 'nooit_waar': ",
      len(onbereikbaar(NAMEN, nooit_waar)) == 8)


# Verwachte uitvoer:
# 7 van de 8 combinaties geven geen toestemming.
#
# Dode tak in 'altijd_waar': True
# Dode tak in 'nooit_waar':  True
