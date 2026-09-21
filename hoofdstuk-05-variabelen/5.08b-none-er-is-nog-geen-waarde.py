# Python basis — theoriebundel
# Hoofdstuk 5 — Variabelen, "constanten" en datatypes
# 5.8 None: er is nog geen waarde
#
# Vergelijk None altijd met is, nooit met ==:
#
# Dit fragment bouwt verder op 5.08a-none-er-is-nog-geen-waarde.py. Die code staat
# hieronder eerst, zodat dit bestand op zichzelf draait.

# ---- eerst de code uit 5.08a-none-er-is-nog-geen-waarde.py ----

gekozen_boek = None

print(gekozen_boek)          # None
print(type(gekozen_boek))    # <class 'NoneType'>


# ---- dan het fragment ----

if gekozen_boek is None:
    print("Nog geen boek gekozen")
