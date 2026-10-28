# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# Klassikale oefening 23.1 — De uitleenregel formaliseren, uitwerking
#
# 5. In Python, met het bewijs erbij.

# De Leeslamp — de uitleenregel, twee schrijfwijzen
# product geeft alle combinaties van True en False (zie 23.07a).
from itertools import product

# De drie atomaire proposities uit de oefening, met hun letter:
#   b = betaald   -> het lid heeft zijn lidgeld betaald
#   s = geschorst -> het lid is geschorst
#   v = te_veel   -> het lid heeft meer dan drie boeken thuis


# De regel letterlijk zoals het bestuur hem zei: b EN NIET s EN NIET v.
# LET OP de voorrang uit hoofdstuk 7: not gaat voor and. Python leest dit als
# betaald and (not geschorst) and (not te_veel).
def mag_lenen_lang(betaald, geschorst, te_veel):
    """De regel zoals het bestuur hem uitsprak."""
    return betaald and not geschorst and not te_veel


# Dezelfde regel, korter: De Morgan zegt dat (NIET s) EN (NIET v) hetzelfde is
# als NIET (s OF v). "Betaald, en geen van beide bezwaren." Eén not in plaats
# van twee. Hier zijn de haakjes WEL nodig: zonder haakjes zou not alleen op
# geschorst slaan.
def mag_lenen_kort(betaald, geschorst, te_veel):
    """Dezelfde regel, met De Morgan samengenomen."""
    return betaald and not (geschorst or te_veel)


# list() maakt van alle combinaties een echte lijst van 8 tuples. Dat is nodig,
# want je loopt er TWEE keer over: in de for-lus en in all() onderaan.
# LET OP: zonder list() zou product na de eerste keer "op" zijn, en zou de
# tweede ronde niets meer zien.
rijen = list(product([True, False], repeat=3))
# De kop en een lijn van 40 streepjes.
print("b       s       v       lang    kort")
print("-" * 40)
# Elke tuple wordt in de for-kop uitgepakt in b, s en v.
for b, s, v in rijen:
    lang = mag_lenen_lang(b, s, v)
    kort = mag_lenen_kort(b, s, v)
    # !s:<8 -> de boolean als tekst, links uitgelijnd in 8 tekens (hoofdstuk 7).
    print(f"{b!s:<8}{s!s:<8}{v!s:<8}{lang!s:<8}{kort}")

# Een lege regel.
print()
# Het BEWIJS: geven beide functies op ALLE acht rijen hetzelfde? all() geeft dan
# True. *r pakt elke tuple uit tot drie argumenten (zie 23.07a).
# Dit is deductie, geen inductie (hoofdstuk 22): je probeert niet een paar
# gevallen uit, je controleert ze allemaal. Bij drie booleans kost dat niets.
print("Gelijkwaardig:",
      all(mag_lenen_lang(*r) == mag_lenen_kort(*r) for r in rijen))


# Verwachte uitvoer:
# b       s       v       lang    kort
# ----------------------------------------
# True    True    True    False   False
# True    True    False   False   False
# True    False   True    False   False
# True    False   False   True    True
# False   True    True    False   False
# False   True    False   False   False
# False   False   True    False   False
# False   False   False   False   False
#
# Gelijkwaardig: True
