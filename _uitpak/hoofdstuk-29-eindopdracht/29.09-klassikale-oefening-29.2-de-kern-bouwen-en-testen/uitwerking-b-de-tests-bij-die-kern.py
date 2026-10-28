# Python basis — theoriebundel
# Hoofdstuk 29 — Eindopdracht: alles samen
# Klassikale oefening 29.2 — De kern bouwen en testen, uitwerking
#
# De tests bij die kern.

HUIDIG_JAAR = 2026
BASISTARIEF_CENTEN = 12_000
JEUGDTARIEF_CENTEN = 9_000
JEUGD_TOT_EN_MET = 17
GEZINSKORTING_CENTEN = 1_500


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
    (1990, 5, 10_500),     # korting geldt vanaf de tweede, niet per rang
]

ONGELDIG = [
    (1899, 1, ValueError),
    (2027, 1, ValueError),
    (1990, 0, ValueError),
    ("1990", 1, TypeError),
    (True, 1, TypeError),
    (1990.5, 1, TypeError),
]


def draai():
    """Draait alle gevallen en meldt elk verschil."""
    gefaald = []

    for jaar, rang, verwacht in GELDIG:
        werkelijk = lidgeld_centen(jaar, rang)
        if werkelijk != verwacht:
            gefaald.append(f"{jaar} rang {rang}: {werkelijk} in plaats van {verwacht}")

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

    # postconditie over het hele bereik
    for jaar in range(1900, HUIDIG_JAAR + 1):
        for rang in (1, 2):
            bedrag = lidgeld_centen(jaar, rang)
            if not 0 <= bedrag <= BASISTARIEF_CENTEN:
                gefaald.append(f"{jaar} rang {rang}: {bedrag} buiten bereik")

    totaal = len(GELDIG) + len(ONGELDIG)
    print(f"{totaal - len(gefaald)} van de {totaal} gevallen geslaagd")
    print(f"postconditie nagegaan voor {(HUIDIG_JAAR - 1900 + 1) * 2} combinaties")
    for regel in gefaald:
        print(f"  FOUT {regel}")
    return not gefaald


print("Groen:", draai())


# Verwachte uitvoer:
# 15 van de 15 gevallen geslaagd
# postconditie nagegaan voor 254 combinaties
# Groen: True
