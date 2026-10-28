# Python basis — theoriebundel
# Hoofdstuk 27 — Inductie, Mill's methods en kritisch denken
# 27.6 Foutzoeken als inductief onderzoek — git bisect is binair zoeken over je
# geschiedenis
#
# Lineair zoeken kost zestig keer uitproberen. Binair zoeken, uit hoofdstuk 25, kost
# er zes.

# Binair zoeken naar de eerste stukke commit
COMMITS = [f"c{n:02d}" for n in range(1, 61)]
EERSTE_STUKKE = 43          # in het echt weet je dit niet


def werkt(index):
    """Doet alsof we die versie uitchecken en testen."""
    return index < EERSTE_STUKKE - 1


def zoek_eerste_stukke(commits):
    """De invariant: links werkt nog, rechts is al stuk."""
    links, rechts = 0, len(commits) - 1
    pogingen = 0
    while links < rechts:
        midden = (links + rechts) // 2
        pogingen += 1
        if werkt(midden):
            links = midden + 1
        else:
            rechts = midden
    return commits[links], pogingen


commit, pogingen = zoek_eerste_stukke(COMMITS)
print(f"Eerste stukke commit : {commit}")
print(f"Aantal pogingen      : {pogingen}")
print(f"Lineair zou kosten   : {EERSTE_STUKKE}")


# Verwachte uitvoer:
# Eerste stukke commit : c43
# Aantal pogingen      : 6
# Lineair zou kosten   : 43
