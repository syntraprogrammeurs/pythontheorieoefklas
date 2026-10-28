# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# Klassikale oefening 24.2 — De toegangsregels afleiden, uitwerking
#
# 2 en 3. Het programma.

# De Leeslamp — toegangsregels met een uitleg erbij
# Cursus Python basis, hoofdstuk 24, oefening 2

REGELS = [
    ("R1", {"geschorst"}, "mag_niet_lenen",
     "je bent geschorst"),
    ("R2", {"onbetaald"}, "mag_niet_lenen",
     "je lidgeld is niet betaald"),
    ("R3", {"boek_zes_weken"}, "geschorst",
     "je hebt een boek langer dan zes weken thuis"),
    ("R4", {"meer_dan_drie"}, "mag_niet_lenen",
     "je hebt meer dan drie boeken thuis"),
    ("R5", {"mag_niet_lenen", "probeert_te_lenen"}, "toon_uitleg",
     "je probeert te lenen terwijl dat niet mag"),
]


def leid_af(feiten, regels):
    """Herhaalde modus ponens, met per conclusie de regel die haar gaf."""
    bekend = dict.fromkeys(feiten, "gegeven")
    spoor = []
    nieuw = True
    while nieuw:
        nieuw = False
        for code, voorwaarden, gevolg, uitleg in regels:
            if voorwaarden <= bekend.keys() and gevolg not in bekend:
                bekend[gevolg] = code
                spoor.append((code, sorted(voorwaarden), gevolg, uitleg))
                nieuw = True
    return bekend, spoor


def beoordeel(naam, feiten):
    """Drukt de afleiding voor één lid af."""
    bekend, spoor = leid_af(feiten | {"probeert_te_lenen"}, REGELS)
    print(f"{naam}")
    print(f"  gegeven : {sorted(feiten)}")
    for code, voorwaarden, gevolg, uitleg in spoor:
        print(f"  {code}      : {voorwaarden} -> {gevolg}")
    mag = "mag_niet_lenen" not in bekend
    print(f"  besluit : {'mag lenen' if mag else 'mag NIET lenen'}")
    if not mag:
        redenen = [u for _, _, g, u in spoor if g == "mag_niet_lenen"]
        print(f"  reden   : {redenen[0]}")
    print()


beoordeel("Anke", set())
beoordeel("Bram", {"boek_zes_weken"})
beoordeel("Cato", {"meer_dan_drie", "onbetaald"})


# Verwachte uitvoer:
# Anke
#   gegeven : []
#   besluit : mag lenen
#
# Bram
#   gegeven : ['boek_zes_weken']
#   R3      : ['boek_zes_weken'] -> geschorst
#   R1      : ['geschorst'] -> mag_niet_lenen
#   R5      : ['mag_niet_lenen', 'probeert_te_lenen'] -> toon_uitleg
#   besluit : mag NIET lenen
#   reden   : je bent geschorst
#
# Cato
#   gegeven : ['meer_dan_drie', 'onbetaald']
#   R2      : ['onbetaald'] -> mag_niet_lenen
#   R5      : ['mag_niet_lenen', 'probeert_te_lenen'] -> toon_uitleg
#   besluit : mag NIET lenen
#   reden   : je lidgeld is niet betaald
