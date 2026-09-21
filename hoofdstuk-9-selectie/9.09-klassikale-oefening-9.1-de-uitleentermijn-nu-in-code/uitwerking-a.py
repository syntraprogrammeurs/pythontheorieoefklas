# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Klassikale oefening 9.1 — De uitleentermijn, nu in code, uitwerking

# De Leeslamp — de uitleentermijn
# Cursus Python basis, hoofdstuk 9, oefening 1

WEKEN_GEWOON = 4
WEKEN_NIEUW = 2
DRUKKE_LENER = 3          # meer dan 3 boeken geeft een week minder
MINIMUM_WEKEN = 1

gevallen = [
    ("gewoon", 1, 4),
    ("nieuw", 1, 2),
    ("naslagwerk", 1, None),
    ("gewoon", 3, 4),
    ("gewoon", 4, 3),
    ("nieuw", 4, 1),
    ("naslagwerk", 9, None),
    ("nieuw", 9, 1),
]

for soort, aantal, verwacht in gevallen:
    if soort == "naslagwerk":
        weken = None
    else:
        if soort == "nieuw":
            weken = WEKEN_NIEUW
        else:
            weken = WEKEN_GEWOON

        if aantal > DRUKKE_LENER:
            weken -= 1
        if weken < MINIMUM_WEKEN:
            weken = MINIMUM_WEKEN

    teken = "ok" if weken == verwacht else "FOUT"
    tekst = "niet uitleenbaar" if weken is None else f"{weken} weken"
    print(f"{soort:<12}{aantal:>2} boeken -> {tekst:<18}{teken}")


# Verwachte uitvoer:
# gewoon       1 boeken -> 4 weken           ok
# nieuw        1 boeken -> 2 weken           ok
# naslagwerk   1 boeken -> niet uitleenbaar  ok
# gewoon       3 boeken -> 4 weken           ok
# gewoon       4 boeken -> 3 weken           ok
# nieuw        4 boeken -> 1 weken           ok
# naslagwerk   9 boeken -> niet uitleenbaar  ok
# nieuw        9 boeken -> 1 weken           ok
