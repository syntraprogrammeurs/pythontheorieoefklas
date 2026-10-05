# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.6 De ledenlijst, nu met dictionaries

# De Leeslamp — de ledenlijst met dictionaries
# Cursus Python basis, hoofdstuk 13

LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3
KORTING = 5


def lidgeld(lid: dict) -> int:
    """Het lidgeld voor één lid, op basis van zijn gegevens."""
    if lid["leeftijd"] < LEEFTIJD_GRATIS:
        bedrag = 0
    elif lid.get("is_student", False):
        bedrag = LIDGELD_STUDENT
    else:
        bedrag = LIDGELD_VOLWASSENE

    if lid.get("jaren", 0) >= JAREN_VOOR_KORTING:
        bedrag -= KORTING
    return max(bedrag, 0)


leden = [
    {"naam": "Anke Peeters", "leeftijd": 34, "jaren": 3,
     "gelezen": {"Het diner", "Turks fruit"}},
    {"naam": "Bram Coppens", "leeftijd": 20, "jaren": 1, "is_student": True,
     "gelezen": {"Turks fruit", "De aanslag"}},
    {"naam": "Cato Dhondt", "leeftijd": 11, "jaren": 4,
     "gelezen": set()},
]

print(f"{'Lid':<16}{'Leeftijd':>9}{'Gelezen':>9}{'Lidgeld':>9}")
print("-" * 43)
for lid in leden:
    print(f"{lid['naam']:<16}{lid['leeftijd']:>9}"
          f"{len(lid['gelezen']):>9}{lidgeld(lid):>9}")

print("-" * 43)
print(f"{'Totaal':<16}{'':>9}{'':>9}{sum(lidgeld(lid) for lid in leden):>9}")

alles = set()
for lid in leden:
    alles |= lid["gelezen"]

    

print()
print("Alle gelezen titels:", sorted(alles))
print("Door iedereen gelezen:", sorted(
    leden[0]["gelezen"] & leden[1]["gelezen"] & leden[2]["gelezen"]))


# Verwachte uitvoer:
# Lid              Leeftijd  Gelezen  Lidgeld
# -------------------------------------------
# Anke Peeters           34        2       25
# Bram Coppens           20        2       15
# Cato Dhondt            11        0        0
# -------------------------------------------
# Totaal                                   40
#
# Alle gelezen titels: ['De aanslag', 'Het diner', 'Turks fruit']
# Door iedereen gelezen: []
