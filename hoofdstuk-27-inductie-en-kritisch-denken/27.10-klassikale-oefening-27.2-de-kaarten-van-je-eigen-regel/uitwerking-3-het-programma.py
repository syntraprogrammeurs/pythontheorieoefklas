# Python basis — theoriebundel
# Hoofdstuk 27 — Inductie, Mill's methods en kritisch denken
# Klassikale oefening 27.2 — De kaarten van je eigen regel, uitwerking
#
# 3. Het programma.

# De vier kaarten van Wason, met de regels van De Leeslamp
# Cursus Python basis, hoofdstuk 27, oefening 2
#
# De TESTTAAK VAN WASON (27.3): je krijgt van elk record maar één helft te zien, en
# je moet kiezen welke records je omdraait om na te gaan of een regel geschonden
# wordt. De meeste mensen kiezen de kaart die de regel BEVESTIGT, terwijl je de
# kaarten nodig hebt die de regel kunnen BREKEN. Dit programma laat zien dat die
# keuze mechanisch te maken is.

# De regel: geschorst -> reden in het logboek.
# Dat is een IMPLICATIE uit hoofdstuk 23: "als p, dan q", met
#   p = het lid is geschorst
#   q = er staat een reden in het logboek
# Een implicatie is alleen onwaar als p waar is en q onwaar. Dat is de enige
# combinatie die de regel breekt: een geschorst lid ZONDER reden.
#
# Per kaart: wat je ziet, en wat er nog verborgen is.
# Elke kaart is een tuple van vier waarden (hoofdstuk 13):
#   1. de naam van de kaart: "A", "B", "C" of "D"
#   2. een omschrijving voor op het scherm
#   3. wat je ziet van het LID: "geschorst", "niet_geschorst", of None
#   4. wat je ziet van het LOGBOEK: "reden", "geen_reden", of None
# None betekent: deze helft is nog VERBORGEN. Je weet het niet.
KAARTEN = [
    ("A", "geschorst", "geschorst", None),
    ("B", "niet geschorst", "niet_geschorst", None),
    ("C", "er staat een reden", None, "reden"),
    ("D", "geen enkele regel", None, "geen_reden"),
]


# kan_breken bevat de hele redenering in twee regels.
# Je vraagt niet "is de regel hier gebroken?" (dat weet je nog niet), maar "KAN de
# regel hier nog gebroken worden?". Dat kan zolang de combinatie "geschorst én geen
# reden" nog mogelijk is.
def kan_breken(zichtbaar_lid, zichtbaar_log):
    """Kan deze kaart de regel 'geschorst -> reden' schenden?

    Alleen de combinatie geschorst plus geen reden breekt hem. Een kaart
    moet dus omgedraaid worden als die combinatie nog mogelijk is.
    """
    # Het lid KAN geschorst zijn, tenzij je al ziet dat het niet geschorst is.
    # Bij "geschorst" is dat True, en bij None (verborgen) ook: het kan nog.
    # LET OP: != betekent "is niet gelijk aan". None != "niet_geschorst" is True.
    lid_kan_geschorst_zijn = zichtbaar_lid != "niet_geschorst"
    # Het logboek KAN zonder reden zijn, tenzij je al een reden ziet.
    log_kan_leeg_zijn = zichtbaar_log != "reden"
    # Beide moeten nog mogelijk zijn (and, hoofdstuk 7). Is één van de twee al
    # uitgesloten, dan kan deze kaart de regel nooit breken.
    return lid_kan_geschorst_zijn and log_kan_leeg_zijn


print("Regel: als een lid geschorst is, staat er een reden in het logboek.")
print()
# De lus pakt elke kaart meteen uit in vier variabelen (hoofdstuk 11 en 13).
# Per kaart, en welke argumentvorm uit hoofdstuk 24 erbij hoort:
#   A  geschorst          -> omdraaien: MODUS PONENS (p is zo, dus q moet gelden)
#   B  niet geschorst     -> laten liggen: de regel zegt niets over niet-geschorsten
#                            (willen omdraaien = het ONTKENNEN VAN HET ANTECEDENS)
#   C  er staat een reden -> laten liggen: wat er ook achter zit, niets gebroken
#                            (willen omdraaien = het BEVESTIGEN VAN HET CONSEQUENS,
#                            en dat is BEVESTIGINGSDRANG)
#   D  geen enkele regel  -> omdraaien: MODUS TOLLENS (q geldt niet, dus p mag niet)
for naam, omschrijving, lid, log in KAARTEN:
    # Een VOORWAARDELIJKE UITDRUKKING (hoofdstuk 9): de tekst links van if als
    # kan_breken True geeft, anders de tekst na else.
    besluit = "OMDRAAIEN" if kan_breken(lid, log) else "laten liggen"
    # {omschrijving:<20} vult de omschrijving aan tot 20 tekens, links uitgelijnd
    # (f-strings, hoofdstuk 6), zodat de besluiten netjes in één kolom staan.
    print(f"  {naam}  {omschrijving:<20} {besluit}")


# Verwachte uitvoer:
# Regel: als een lid geschorst is, staat er een reden in het logboek.
#
#   A  geschorst            OMDRAAIEN
#   B  niet geschorst       laten liggen
#   C  er staat een reden   laten liggen
#   D  geen enkele regel    OMDRAAIEN
