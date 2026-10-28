# Python basis — theoriebundel
# Hoofdstuk 29 — Eindopdracht: alles samen
# Klassikale oefening 29.2 — De kern bouwen en testen, uitwerking

# Turnclub De Sprong — de kern van de eindopdracht
# Cursus Python basis, hoofdstuk 29, oefening 2

HUIDIG_JAAR = 2026

BASISTARIEF_CENTEN = 12_000
JEUGDTARIEF_CENTEN = 9_000
JEUGD_TOT_EN_MET = 17
GEZINSKORTING_CENTEN = 1_500


class Lid:
    """Eén lid van de turnclub."""

    def __init__(self, nummer, naam, geboortejaar, groep_id,
                 gezin_id=None, rang_in_gezin=1):
        assert naam.strip(), "een lid moet een naam hebben"
        self.nummer = nummer
        self.naam = naam.strip()
        self.geboortejaar = geboortejaar
        self.groep_id = groep_id
        self.gezin_id = gezin_id
        self.rang_in_gezin = rang_in_gezin
        self.betaald_centen = 0

    def leeftijd(self, in_jaar=HUIDIG_JAAR):
        """De leeftijd die het lid dit jaar bereikt."""
        return in_jaar - self.geboortejaar

    def openstaand_centen(self):
        """Wat er nog betaald moet worden; nooit negatief."""
        return max(0, lidgeld_centen(self.geboortejaar,
                                     self.rang_in_gezin) - self.betaald_centen)

    def __repr__(self):
        return f"Lid({self.nummer}, {self.naam!r}, {self.geboortejaar})"


def lidgeld_centen(geboortejaar, rang_in_gezin=1, in_jaar=HUIDIG_JAAR):
    """Het lidgeld in hele centen.

    Preconditie : 1900 <= geboortejaar <= in_jaar, rang_in_gezin >= 1.
    Postconditie: 0 <= resultaat <= BASISTARIEF_CENTEN.
    """
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

    bedrag = max(0, bedrag)
    assert 0 <= bedrag <= BASISTARIEF_CENTEN
    return bedrag


def in_euro(centen):
    """Centen als leesbaar bedrag."""
    return f"{centen // 100},{centen % 100:02d} euro"


LEDEN = [
    Lid(1, "Anke Peeters", 1990, groep_id=2),
    Lid(2, "Bram Janssens", 2012, groep_id=1, gezin_id=7, rang_in_gezin=1),
    Lid(3, "Cato Janssens", 2015, groep_id=1, gezin_id=7, rang_in_gezin=2),
    Lid(4, "Dirk Willems", 1978, groep_id=3),
]
LEDEN[0].betaald_centen = 12_000
LEDEN[1].betaald_centen = 5_000

print(f"{'Lid':<16}{'Leeftijd':>9}{'Lidgeld':>12}{'Openstaand':>13}")
print("-" * 50)
for lid in LEDEN:
    print(f"{lid.naam:<16}{lid.leeftijd():>9}"
          f"{in_euro(lidgeld_centen(lid.geboortejaar, lid.rang_in_gezin)):>12}"
          f"{in_euro(lid.openstaand_centen()):>13}")

wanbetalers = [lid for lid in LEDEN if lid.openstaand_centen() > 0]
print()
print("Nog te betalen door:", ", ".join(lid.naam for lid in wanbetalers))
print("Totaal openstaand  :",
      in_euro(sum(lid.openstaand_centen() for lid in LEDEN)))


# Verwachte uitvoer:
# Lid              Leeftijd     Lidgeld   Openstaand
# --------------------------------------------------
# Anke Peeters           36 120,00 euro    0,00 euro
# Bram Janssens          14  90,00 euro   40,00 euro
# Cato Janssens          11  75,00 euro   75,00 euro
# Dirk Willems           48 120,00 euro  120,00 euro
#
# Nog te betalen door: Bram Janssens, Cato Janssens, Dirk Willems
# Totaal openstaand  : 235,00 euro
