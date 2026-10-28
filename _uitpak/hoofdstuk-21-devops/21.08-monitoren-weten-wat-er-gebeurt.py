# Python basis — theoriebundel
# Hoofdstuk 21 — DevOps, en waar Git daarin past
# 21.8 Monitoren: weten wat er gebeurt
#
# Voor het logboek gebruik je niet print() maar de module logging uit de
# standaardbibliotheek. Het verschil: bij logging heeft elk bericht een niveau, een
# tijdstip en een herkomst, en kun je achteraf beslissen wat je wilt zien zonder je
# code aan te passen.

# De Leeslamp — een logboek in plaats van print
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="{levelname:<8} {message}",
    style="{",
)

log = logging.getLogger("leeslamp")


def leen_uit(titel, exemplaren):
    """Leent een boek uit en houdt het logboek bij."""
    log.debug("uitleenpoging voor %s", titel)
    if exemplaren == 0:
        log.warning("geen exemplaar meer van %s", titel)
        return exemplaren
    log.info("%s uitgeleend, nog %d over", titel, exemplaren - 1)
    return exemplaren - 1


voorraad = leen_uit("Max Havelaar", 2)
voorraad = leen_uit("Max Havelaar", voorraad)
voorraad = leen_uit("Max Havelaar", voorraad)


# Verwachte uitvoer:
# INFO     Max Havelaar uitgeleend, nog 1 over
# INFO     Max Havelaar uitgeleend, nog 0 over
# WARNING  geen exemplaar meer van Max Havelaar
