# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# Klassikale oefening 23.1 — De uitleenregel formaliseren, uitwerking
#
# 5. In Python, met het bewijs erbij.

# De Leeslamp — de uitleenregel, twee schrijfwijzen
from itertools import product


def mag_lenen_lang(betaald, geschorst, te_veel):
    """De regel zoals het bestuur hem uitsprak."""
    return betaald and not geschorst and not te_veel


def mag_lenen_kort(betaald, geschorst, te_veel):
    """Dezelfde regel, met De Morgan samengenomen."""
    return betaald and not (geschorst or te_veel)


rijen = list(product([True, False], repeat=3))
print("b       s       v       lang    kort")
print("-" * 40)
for b, s, v in rijen:
    lang = mag_lenen_lang(b, s, v)
    kort = mag_lenen_kort(b, s, v)
    print(f"{b!s:<8}{s!s:<8}{v!s:<8}{lang!s:<8}{kort}")

print()
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
