# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.1 — Zes lussen omzetten, opgave
#
# De situatie. Je krijgt zes stukjes code die elk met een lus een lijst opbouwen. Je
# schrijft ze om naar comprehensions, en bij één ervan beslis je dat je dat beter niet
# doet.

# A — alle titels in hoofdletters
titels = ["het diner", "turks fruit"]
uit = []
for t in titels:
    uit.append(t.upper())

# B — alleen de boeken van meer dan 200 bladzijden
boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]
uit = []
for titel, blz in boeken:
    if blz > 200:
        uit.append(titel)

# C — de lengte van elke titel, als dictionary
uit = {}
for titel, blz in boeken:
    uit[titel] = len(titel)

# D — alle verschillende beginletters
uit = set()
for titel, blz in boeken:
    uit.add(titel[0])

# E — de bladzijden, maar nooit meer dan 250 tellen
uit = []
for titel, blz in boeken:
    if blz > 250:
        uit.append(250)
    else:
        uit.append(blz)

# F — per boek een regel, met een tussenkop per beginletter
uit = []
vorige = ""
for titel, blz in sorted(boeken):
    if titel[0] != vorige:
        uit.append(f"--- {titel[0]} ---")
        vorige = titel[0]
    uit.append(f"{titel} ({blz})")
