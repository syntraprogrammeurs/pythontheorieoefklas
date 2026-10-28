# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.4 De lusinvariant — De invariant van binair zoeken
#
# Binair zoeken is het raadspel uit hoofdstuk 10, als functie: je zoekt in een
# gesorteerde lijst door telkens het midden te nemen. Hier doet de invariant echt
# werk.

def binair_zoek(gesorteerd, doel):
    """Geeft de index van `doel`, of -1.

    Preconditie : `gesorteerd` is oplopend gesorteerd.
    Invariant   : als `doel` erin zit, ligt het tussen links en rechts.
    Postconditie: de teruggegeven index bevat `doel`, of het antwoord is -1.
    """
    assert gesorteerd == sorted(gesorteerd), "de lijst moet gesorteerd zijn"

    links, rechts = 0, len(gesorteerd) - 1
    while links <= rechts:
        assert doel not in gesorteerd or doel in gesorteerd[links:rechts + 1]

        midden = (links + rechts) // 2
        if gesorteerd[midden] == doel:
            return midden
        if gesorteerd[midden] < doel:
            links = midden + 1
        else:
            rechts = midden - 1
    return -1


BLADZIJDEN = [96, 175, 246, 288, 340, 928]

for doel in (246, 928, 96, 300):
    print(f"{doel:>4} -> index {binair_zoek(BLADZIJDEN, doel)}")


# Verwachte uitvoer:
#  246 -> index 2
#  928 -> index 5
#   96 -> index 0
#  300 -> index -1
