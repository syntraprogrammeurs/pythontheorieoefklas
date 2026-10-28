# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# Klassikale oefening 23.2 — Een tautologiecontrole bouwen, uitwerking
#
# De dode-taktest.

# Een voorwaarde uit echte code op dode takken onderzoeken
from itertools import product


def onbereikbaar(namen, formule):
    """De combinaties waarvoor deze voorwaarde nooit waar wordt."""
    return [dict(zip(namen, w))
            for w in product([True, False], repeat=len(namen))
            if not formule(*w)]


NAMEN = ["betaald", "geschorst", "te_veel"]


def voorwaarde(betaald, geschorst, te_veel):
    """De uitleenregel uit oefening 23.1."""
    return betaald and not (geschorst or te_veel)


gevallen = onbereikbaar(NAMEN, voorwaarde)
print(f"{len(gevallen)} van de 8 combinaties geven geen toestemming.")
print()


def altijd_waar(betaald, geschorst, te_veel):
    """Een voorwaarde met een fout: hij kan niet onwaar worden."""
    return betaald or not betaald


print("Dode tak in 'altijd_waar':",
      len(onbereikbaar(NAMEN, altijd_waar)) == 0)


def nooit_waar(betaald, geschorst, te_veel):
    """En een voorwaarde die nooit uitvoert."""
    return geschorst and not geschorst


print("Dode tak in 'nooit_waar': ",
      len(onbereikbaar(NAMEN, nooit_waar)) == 8)


# Verwachte uitvoer:
# 7 van de 8 combinaties geven geen toestemming.
#
# Dode tak in 'altijd_waar': True
# Dode tak in 'nooit_waar':  True
