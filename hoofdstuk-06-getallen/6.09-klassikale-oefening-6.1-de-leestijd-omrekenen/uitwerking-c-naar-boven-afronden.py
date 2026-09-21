# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# Klassikale oefening 6.1 — De leestijd omrekenen, uitwerking
#
# Of, zonder import, met een bekende rekenkundige truc:
#
# Dit fragment bouwt verder op uitwerking-a.py. Die code staat hieronder eerst, zodat
# dit bestand op zichzelf draait.
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# ---- eerst de code uit uitwerking-a.py ----

# De Leeslamp — de leestijd van een boek schatten
# Cursus Python basis, hoofdstuk 6, oefening 1

WOORDEN_PER_BLADZIJDE = 300
WOORDEN_PER_MINUUT = 250
MINUTEN_PER_DAG = 20

bladzijden = int(input("Hoeveel bladzijden telt het boek? "))

woorden = bladzijden * WOORDEN_PER_BLADZIJDE
minuten = woorden / WOORDEN_PER_MINUUT

uren = int(minuten) // 60
rest_minuten = int(minuten) % 60

dagen = minuten / MINUTEN_PER_DAG
hele_dagen = int(dagen)
if dagen > hele_dagen:
    hele_dagen = hele_dagen + 1

print()
print(f"Bladzijden : {bladzijden}")
print(f"Woorden    : {woorden:,}")
print(f"Leestijd   : {minuten:.1f} minuten")
print(f"Dat is     : {uren} uur en {rest_minuten} minuten")
print(f"Bij {MINUTEN_PER_DAG} min/dag: {hele_dagen} dagen")


# ---- dan het fragment ----

hele_dagen = -(-int(minuten) // MINUTEN_PER_DAG)
