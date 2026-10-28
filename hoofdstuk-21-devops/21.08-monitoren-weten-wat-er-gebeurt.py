# Python basis — theoriebundel
# Hoofdstuk 21 — DevOps, en waar Git daarin past
# 21.8 Monitoren: weten wat er gebeurt
#
# Voor het logboek gebruik je niet print() maar de module logging uit de
# standaardbibliotheek. Het verschil: bij logging heeft elk bericht een niveau, een
# tijdstip en een herkomst, en kun je achteraf beslissen wat je wilt zien zonder je
# code aan te passen.

# De Leeslamp — een logboek in plaats van print
# logging en sys komen allebei uit de standaardbibliotheek (hoofdstuk 17):
# je hoeft niets te installeren.
import logging
import sys

# logging.basicConfig() stelt één keer, bovenaan, in HOE en WAAR het logboek
# schrijft. Elke optie apart:
#   stream=sys.stdout   -> schrijf naar het gewone uitvoerkanaal, zoals print.
#                          Zonder deze optie schrijft logging naar sys.stderr,
#                          het kanaal voor foutmeldingen.
#   level=logging.INFO  -> het LOGNIVEAU: toon alleen berichten van INFO of
#                          ernstiger. De niveaus, van licht naar zwaar:
#                          DEBUG, INFO, WARNING, ERROR, CRITICAL.
#   format=...          -> hoe elke regel eruitziet. {levelname:<8} is het
#                          niveau, links uitgelijnd in 8 tekens (zoals in de
#                          f-string uit hoofdstuk 6); {message} is je bericht.
#                          Hier staat geen tijdstip in, zodat de uitvoer elke
#                          keer gelijk is. Met {asctime} krijg je het erbij.
#   style="{"           -> zegt dat format de schrijfwijze met { } gebruikt.
#                          LET OP: zonder deze optie verwacht logging de oudere
#                          vorm %(levelname)s, en kwam {levelname} letterlijk
#                          op het scherm.
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="{levelname:<8} {message}",
    style="{",
)

# logging.getLogger(naam) geeft een LOGGER terug: het object waarmee je berichten
# schrijft. De naam "leeslamp" is de HERKOMST: in een groot programma zie je zo
# uit welk deel een bericht komt. Vraag je dezelfde naam twee keer op, dan krijg
# je hetzelfde object terug.
log = logging.getLogger("leeslamp")


# Elke methode van log schrijft een bericht op een ander niveau:
# log.debug(), log.info(), log.warning(), log.error(), log.critical().
# In het bericht zijn %s (een tekst) en %d (een geheel getal) PLAATSHOUDERS.
# De waarden geef je als APARTE argumenten mee, niet in een f-string. Zo vult
# logging ze pas in als het bericht echt getoond wordt: werk dat je bespaart
# voor berichten die toch wegvallen.
def leen_uit(titel, exemplaren):
    """Leent een boek uit en houdt het logboek bij."""
    # DEBUG ligt onder INFO, dus dit bericht verschijnt NIET. Zet je bovenaan
    # level=logging.DEBUG, dan zie je het wel, zonder iets anders te veranderen.
    # Dat is het grote voordeel tegenover print().
    log.debug("uitleenpoging voor %s", titel)
    if exemplaren == 0:
        # WARNING: iets loopt niet zoals verwacht, maar het programma gaat door.
        # De voorraad blijft 0: je kunt niet onder nul uitlenen.
        log.warning("geen exemplaar meer van %s", titel)
        return exemplaren
    # INFO: het programma doet zijn gewone werk. %s krijgt titel, %d krijgt
    # exemplaren - 1, in die volgorde.
    log.info("%s uitgeleend, nog %d over", titel, exemplaren - 1)
    return exemplaren - 1


# Drie uitleningen na elkaar. Elke oproep krijgt de voorraad die de vorige
# teruggaf: 2 -> 1, dan 1 -> 0, en de derde keer is er niets meer (een WARNING).
voorraad = leen_uit("Max Havelaar", 2)
voorraad = leen_uit("Max Havelaar", voorraad)
voorraad = leen_uit("Max Havelaar", voorraad)


# Verwachte uitvoer:
# INFO     Max Havelaar uitgeleend, nog 1 over
# INFO     Max Havelaar uitgeleend, nog 0 over
# WARNING  geen exemplaar meer van Max Havelaar
