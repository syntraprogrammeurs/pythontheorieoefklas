# Python basis — theoriebundel
# Hoofdstuk 29 — Eindopdracht: alles samen
# Klassikale oefening 29.2 — De kern bouwen en testen, uitwerking
#
# De tests bij die kern.

# Dit is stap 5 van het werkplan (29.5): de tests bij de kern, gekozen met
# equivalentieklassen en grenswaarden (hoofdstuk 28). Eis 9 vraagt minstens
# vijftien controles; hier zijn het er precies vijftien, plus een lus die de
# postconditie nagaat.
# De constanten en de functie zijn hier overgenomen uit uitwerking-a, zodat dit
# bestand op zichzelf draait. In je eigen project importeer je ze uit je
# kernmodule (hoofdstuk 17) in plaats van ze te kopiëren.
HUIDIG_JAAR = 2026
BASISTARIEF_CENTEN = 12_000
JEUGDTARIEF_CENTEN = 9_000
JEUGD_TOT_EN_MET = 17
GEZINSKORTING_CENTEN = 1_500


# Dezelfde rekenregel als in uitwerking-a, zonder de assert op het einde.
# De postconditie wordt hier niet in de functie zelf gecontroleerd, maar van
# buitenaf, door de test onderaan in draai().
def lidgeld_centen(geboortejaar, rang_in_gezin=1, in_jaar=HUIDIG_JAAR):
    """Zie oefening 29.2."""
    if not isinstance(geboortejaar, int) or isinstance(geboortejaar, bool):
        raise TypeError("geboortejaar moet een geheel getal zijn")
    if not 1900 <= geboortejaar <= in_jaar:
        raise ValueError(f"geboortejaar {geboortejaar} is onmogelijk")
    if rang_in_gezin < 1:
        raise ValueError("de rang in het gezin begint bij 1")
    leeftijd = in_jaar - geboortejaar
    bedrag = (JEUGDTARIEF_CENTEN if leeftijd <= JEUGD_TOT_EN_MET
              else BASISTARIEF_CENTEN)
    if rang_in_gezin >= 2:
        bedrag -= GEZINSKORTING_CENTEN
    return max(0, bedrag)


# POSITIEVE tests: geldige invoer met het bedrag dat je verwacht.
# De leeftijd is HUIDIG_JAAR (2026) min het geboortejaar.
# GRENSWAARDENANALYSE (28.4) rond de grens "tot en met 17":
#   2010 (16 jaar), 2009 (17 jaar) en 2008 (18 jaar) = eronder, erop, erboven.
#   Schreef iemand "< 17" in plaats van "<= 17", dan faalt het geval 2009.
# De randen van het geldige bereik: 2026 (net geboren) en 1900 (oudste jaar).
# EQUIVALENTIEKLASSEN (28.3): 1990 staat voor "gewoon volwassen".
# De korting wordt getest in beide klassen (jeugd en volwassen), en met rang 5.
# equivalentieklassen en grenswaarden rond de leeftijdsgrens van 17
GELDIG = [
    # (geboortejaar, rang, verwacht in centen)
    (2026, 1, 9_000),      # pasgeboren: onderste grens
    (2010, 1, 9_000),      # 16 jaar: binnen de jeugdklasse
    (2009, 1, 9_000),      # 17 jaar: precies op de grens
    (2008, 1, 12_000),     # 18 jaar: net erboven
    (1990, 1, 12_000),     # volwassen: midden in de klasse
    (1900, 1, 12_000),     # oudste toegelaten jaar
    (2009, 2, 7_500),      # jeugd met gezinskorting
    (1990, 2, 10_500),     # volwassen met gezinskorting
    # Het interessantste geval. De regel zegt "vanaf het tweede lid". Wie
    # rang * korting schrijft, geeft lid 5 vijf keer korting. Dit ene geval
    # legt dat verschil bloot.
    (1990, 5, 10_500),     # korting geldt vanaf de tweede, niet per rang
]

# NEGATIEVE tests (28.8): ongeldige invoer en de fout die je verwacht.
#   1899      -> grenswaarde net onder het oudste toegelaten jaar
#   2027      -> grenswaarde net na het huidige jaar: geboren in de toekomst
#   rang 0    -> grenswaarde net onder de laagste rang (1)
#   "1990"    -> tekst in plaats van een getal (wat input() je zou geven!)
#   True      -> de bool-valkuil: True is ook een int
#   1990.5    -> een kommagetal
ONGELDIG = [
    (1899, 1, ValueError),
    (2027, 1, ValueError),
    (1990, 0, ValueError),
    ("1990", 1, TypeError),
    (True, 1, TypeError),
    (1990.5, 1, TypeError),
]


# De TESTLOPER (28.7), met hetzelfde patroon als draai_alles in oefening 28.1.
# Hij geeft True terug als alles slaagt: klaar om met sys.exit() een
# afsluitcode voor de pijplijn te maken (28.7, eis 17).
def draai():
    """Draait alle gevallen en meldt elk verschil."""
    gefaald = []

    # Deel 1: de positieve tests. Werkelijk en verwacht vergelijken.
    # LET OP: hier staat geen try. Gooit lidgeld_centen bij geldige invoer
    # toch een fout op, dan crasht de testloper zelf in plaats van die fout
    # netjes te melden. In oefening 28.1 vangt draai_alles dat wel op.
    for jaar, rang, verwacht in GELDIG:
        werkelijk = lidgeld_centen(jaar, rang)
        if werkelijk != verwacht:
            gefaald.append(f"{jaar} rang {rang}: {werkelijk} in plaats van {verwacht}")

    # Deel 2: de negatieve tests, met drie mogelijke uitkomsten:
    #   de verwachte fout       -> goed, continue naar het volgende geval
    #   een andere foutsoort    -> noteren
    #   helemaal geen fout      -> noteren (de laatste append in de lus)
    for jaar, rang, soort in ONGELDIG:
        try:
            lidgeld_centen(jaar, rang)
        except soort:
            continue
        except Exception as fout:
            gefaald.append(f"{jaar!r}: {type(fout).__name__} "
                           f"in plaats van {soort.__name__}")
            continue
        gefaald.append(f"{jaar!r}: geen fout, wel {soort.__name__} verwacht")

    # Deel 3: de POSTCONDITIE (hoofdstuk 25) nagaan over het HELE bereik.
    # range(1900, HUIDIG_JAAR + 1) geeft 1900 tot en met 2026; de + 1 is nodig
    # omdat range de bovengrens zelf niet meer meetelt.
    # Twee geneste lussen: elk jaar met rang 1 en met rang 2. Meer rangen
    # zijn niet nodig: vanaf rang 2 is de korting altijd dezelfde.
    # Dit is uitputtend testen (28.2) op een klein bereik: 127 jaren x 2
    # rangen = 254 combinaties. Dat kan hier, omdat er maar weinig zijn.
    for jaar in range(1900, HUIDIG_JAAR + 1):
        for rang in (1, 2):
            bedrag = lidgeld_centen(jaar, rang)
            if not 0 <= bedrag <= BASISTARIEF_CENTEN:
                gefaald.append(f"{jaar} rang {rang}: {bedrag} buiten bereik")

    # Het verslag. 9 geldige + 6 ongeldige gevallen = 15.
    # LET OP: de 254 controles uit deel 3 tellen niet mee in totaal. Mislukt
    # er daar een, dan komt ze wel in gefaald en in de FOUT-regels, maar de
    # telling "x van de 15" klopt dan niet meer helemaal.
    totaal = len(GELDIG) + len(ONGELDIG)
    print(f"{totaal - len(gefaald)} van de {totaal} gevallen geslaagd")
    # Het aantal combinaties wordt berekend, niet vast ingetypt: (2026 - 1900
    # + 1) * 2 = 254. Verandert HUIDIG_JAAR, dan klopt het getal nog.
    print(f"postconditie nagegaan voor {(HUIDIG_JAAR - 1900 + 1) * 2} combinaties")
    for regel in gefaald:
        print(f"  FOUT {regel}")
    # True als gefaald leeg is: "groen".
    return not gefaald


# draai() wordt eerst uitgevoerd (en drukt zijn verslag af); daarna toont
# print het teruggegeven True of False.
print("Groen:", draai())


# Verwachte uitvoer:
# 15 van de 15 gevallen geslaagd
# postconditie nagegaan voor 254 combinaties
# Groen: True
