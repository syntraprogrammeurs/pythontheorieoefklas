# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# Klassikale oefening 24.2 — De toegangsregels afleiden, uitwerking
#
# 2 en 3. Het programma.

# De Leeslamp — toegangsregels met een uitleg erbij
# Cursus Python basis, hoofdstuk 24, oefening 2

# Dit programma bouwt verder op leid_af() uit 24.7. Het verschil: het onthoudt bij
# elke conclusie WELKE regel haar opleverde en WAAROM. Zo kan het een lid dat
# geweigerd wordt, ook vertellen wat de reden is.
#
# De vijf regels van het bestuur, als implicaties (deel 1 van de uitwerking):
#   R1  g -> niet l            geschorst, dus niet lenen
#   R2  niet b -> niet l       lidgeld niet betaald, dus niet lenen
#   R3  t -> g                 boek langer dan zes weken thuis, dus geschorst
#   R4  v -> niet l            meer dan drie boeken thuis, dus niet lenen
#   R5  (niet l EN p) -> u     mag niet lenen en probeert het toch, dus uitleg

# REGELS is een lijst van tuples met nu VIER delen:
#   (code, {voorwaarden}, gevolg, uitleg in gewone taal)
# De voorwaarden staan weer in een set (hoofdstuk 13): ze moeten allemaal gelden.
# De uitleg staat bij de regel zelf. Zo hoef je de tekst nergens een tweede keer
# te typen, en kan hij nooit uit de pas lopen met de voorwaarde.
REGELS = [
    ("R1", {"geschorst"}, "mag_niet_lenen",
     "je bent geschorst"),
    ("R2", {"onbetaald"}, "mag_niet_lenen",
     "je lidgeld is niet betaald"),
    # R3 maakt een keten met R1: boek_zes_weken -> geschorst -> mag_niet_lenen.
    # Dat is het HYPOTHETISCH SYLLOGISME uit 24.4: t -> g en g -> niet l geven
    # samen t -> niet l. Het programma legt die keten vanzelf.
    ("R3", {"boek_zes_weken"}, "geschorst",
     "je hebt een boek langer dan zes weken thuis"),
    ("R4", {"meer_dan_drie"}, "mag_niet_lenen",
     "je hebt meer dan drie boeken thuis"),
    # R5 heeft twee voorwaarden: ze moeten ALLEBEI gelden (een EN, een conjunctie).
    ("R5", {"mag_niet_lenen", "probeert_te_lenen"}, "toon_uitleg",
     "je probeert te lenen terwijl dat niet mag"),
]


# leid_af() geeft twee dingen terug:
#   bekend -> een DICTIONARY (hoofdstuk 13): sleutel = een feit of conclusie,
#             waarde = waar het vandaan komt ("gegeven" of de code van de regel)
#   spoor  -> een lijst van (code, voorwaarden, gevolg, uitleg), in de volgorde
#             waarin de regels vuurden
def leid_af(feiten, regels):
    """Herhaalde modus ponens, met per conclusie de regel die haar gaf."""
    # dict.fromkeys(reeks, waarde) maakt een nieuwe dictionary met elk element
    # van de reeks als sleutel en telkens dezelfde waarde.
    # dict.fromkeys({"a", "b"}, "gegeven") geeft {"a": "gegeven", "b": "gegeven"}.
    bekend = dict.fromkeys(feiten, "gegeven")
    spoor = []
    # Dezelfde lus als in 24.7: blijf rondes draaien zolang er iets bijkomt.
    nieuw = True
    while nieuw:
        nieuw = False
        # Elke regel uitpakken in zijn vier delen.
        for code, voorwaarden, gevolg, uitleg in regels:
            # bekend.keys() geeft de sleutels van de dictionary. Die gedragen zich
            # als een set, dus <= werkt: "staan alle voorwaarden bij de sleutels?"
            # LET OP: "gevolg not in bekend" zoekt bij een dictionary in de
            # SLEUTELS, niet in de waarden. Dat is precies wat je hier wilt.
            if voorwaarden <= bekend.keys() and gevolg not in bekend:
                # Modus ponens: alle voorwaarden gelden, dus het gevolg ook.
                # Bewaar erbij welke regel het opleverde.
                bekend[gevolg] = code
                # sorted() maakt van de set een gesorteerde lijst, voor een vaste
                # volgorde in de uitvoer.
                spoor.append((code, sorted(voorwaarden), gevolg, uitleg))
                nieuw = True
    return bekend, spoor


# beoordeel() rekent één lid door en drukt het resultaat af. Ze geeft niets terug
# (dus None): ze doet alleen iets op het scherm, een NEVENEFFECT (hoofdstuk 11).
def beoordeel(naam, feiten):
    """Drukt de afleiding voor één lid af."""
    # feiten | {"probeert_te_lenen"}: | is de VERENIGING van twee sets
    # (hoofdstuk 13). Het resultaat is een NIEUWE set met alles uit beide.
    # De set feiten van de aanroeper blijft dus onveranderd.
    # Elk lid probeert hier iets te lenen: zo kan R5 vuren.
    bekend, spoor = leid_af(feiten | {"probeert_te_lenen"}, REGELS)
    print(f"{naam}")
    # Alleen de echte feiten van het lid tonen, zonder "probeert_te_lenen".
    print(f"  gegeven : {sorted(feiten)}")
    # Het spoor: elke regel die vuurde, met zijn voorwaarden en zijn gevolg.
    # uitleg wordt hier uitgepakt maar niet gebruikt.
    for code, voorwaarden, gevolg, uitleg in spoor:
        print(f"  {code}      : {voorwaarden} -> {gevolg}")
    # Het besluit. Volgt "mag_niet_lenen" nergens uit, dan mag het lid lenen.
    mag = "mag_niet_lenen" not in bekend
    # De verkorte if (9.5): 'mag lenen' als mag waar is, anders 'mag NIET lenen'.
    # Binnen de f-string staan enkele aanhalingstekens, want de f-string zelf
    # gebruikt al dubbele.
    print(f"  besluit : {'mag lenen' if mag else 'mag NIET lenen'}")
    if not mag:
        # Een list comprehension (hoofdstuk 14): verzamel de uitleg u van elke
        # stap waarvan het gevolg g "mag_niet_lenen" is.
        # _ is de afspraak voor "dit deel heb ik niet nodig" (code en voorwaarden).
        redenen = [u for _, _, g, u in spoor if g == "mag_niet_lenen"]
        # redenen[0]: alleen de EERSTE reden wordt getoond. Zie de opmerking bij
        # Cato onderaan.
        print(f"  reden   : {redenen[0]}")
    print()


# Anke: niets aan de hand. Geen enkele regel vuurt, dus ze mag lenen.
# set() is een lege set. LET OP: {} is GEEN lege set maar een lege dictionary.
beoordeel("Anke", set())
# Bram: een boek van acht weken, dus langer dan zes weken thuis.
# Kijk naar de volgorde in zijn spoor: eerst R3, dan pas R1, hoewel R1 hoger in de
# lijst staat. In de eerste ronde kan R1 nog niet vuren (geschorst is nog niet
# bekend); R3 vuurt wel. Pas in de tweede ronde vuurt R1. Daarom heeft leid_af()
# die while-lus met meerdere rondes nodig.
beoordeel("Bram", {"boek_zes_weken"})
# Cato: twee redenen om geweigerd te worden (R2 en R4). Toch toont het spoor alleen
# R2. Zodra R2 "mag_niet_lenen" afleidt, staat dat gevolg al in bekend, en dan
# voegt R4 niets nieuws meer toe ("gevolg not in bekend" is onwaar).
# Logisch is dat correct: één reden volstaat om te weigeren. Voor Cato is het wel
# vervelend: ze betaalt haar lidgeld en hoort dan pas van haar te veel boeken.
# Een geldige redenering is dus niet automatisch een goede oplossing.
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
