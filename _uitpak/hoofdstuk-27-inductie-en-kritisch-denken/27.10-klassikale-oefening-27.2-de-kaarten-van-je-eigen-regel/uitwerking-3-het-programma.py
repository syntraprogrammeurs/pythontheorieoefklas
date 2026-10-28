# Python basis — theoriebundel
# Hoofdstuk 27 — Inductie, Mill's methods en kritisch denken
# Klassikale oefening 27.2 — De kaarten van je eigen regel, uitwerking
#
# 3. Het programma.

# De vier kaarten van Wason, met de regels van De Leeslamp
# Cursus Python basis, hoofdstuk 27, oefening 2

# De regel: geschorst -> reden in het logboek.
# Per kaart: wat je ziet, en wat er nog verborgen is.
KAARTEN = [
    ("A", "geschorst", "geschorst", None),
    ("B", "niet geschorst", "niet_geschorst", None),
    ("C", "er staat een reden", None, "reden"),
    ("D", "geen enkele regel", None, "geen_reden"),
]


def kan_breken(zichtbaar_lid, zichtbaar_log):
    """Kan deze kaart de regel 'geschorst -> reden' schenden?

    Alleen de combinatie geschorst plus geen reden breekt hem. Een kaart
    moet dus omgedraaid worden als die combinatie nog mogelijk is.
    """
    lid_kan_geschorst_zijn = zichtbaar_lid != "niet_geschorst"
    log_kan_leeg_zijn = zichtbaar_log != "reden"
    return lid_kan_geschorst_zijn and log_kan_leeg_zijn


print("Regel: als een lid geschorst is, staat er een reden in het logboek.")
print()
for naam, omschrijving, lid, log in KAARTEN:
    besluit = "OMDRAAIEN" if kan_breken(lid, log) else "laten liggen"
    print(f"  {naam}  {omschrijving:<20} {besluit}")


# Verwachte uitvoer:
# Regel: als een lid geschorst is, staat er een reden in het logboek.
#
#   A  geschorst            OMDRAAIEN
#   B  niet geschorst       laten liggen
#   C  er staat een reden   laten liggen
#   D  geen enkele regel    OMDRAAIEN
