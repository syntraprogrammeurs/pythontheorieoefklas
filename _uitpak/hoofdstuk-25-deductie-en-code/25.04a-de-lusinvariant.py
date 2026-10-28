# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.4 De lusinvariant
#
# Neem het optellen van bladzijden:

def totaal_bladzijden(boeken):
    """Het totale aantal bladzijden.

    Invariant: `totaal` is de som van de eerste `i` boeken.
    """
    totaal = 0
    for i, aantal in enumerate(boeken, start=1):
        totaal += aantal
        assert totaal == sum(boeken[:i]), "invariant geschonden"
    return totaal


print(totaal_bladzijden([320, 180, 250]))
print(totaal_bladzijden([]))


# Verwachte uitvoer:
# 750
# 0
