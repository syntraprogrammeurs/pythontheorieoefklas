# Python basis — theoriebundel
# Hoofdstuk 29 — Eindopdracht: alles samen
# Klassikale oefening 29.2 — De kern bouwen en testen, uitwerking

# Turnclub De Sprong — de kern van de eindopdracht
# Cursus Python basis, hoofdstuk 29, oefening 2

# Dit bestand is de KERN: de klasse en de rekenregel, stap 4 van het werkplan
# uit 29.5. Er staat nergens een input() in. Daardoor kun je alles testen
# zonder één keer iets te typen (zie uitwerking-b). Het menu komt pas later.

# CONSTANTEN (hoofdstuk 5): vaste waarden in HOOFDLETTERS, bovenaan het bestand.
# Verandert het tarief, dan pas je één regel aan in plaats van overal in de code.
HUIDIG_JAAR = 2026

# Alle bedragen staan in hele CENTEN, als int. 12_000 centen is 120 euro.
# Waarom? Kommagetallen (float) zijn niet exact: 0.1 + 0.2 == 0.3 is onwaar
# (hoofdstuk 6). Met hele centen klopt elke optelling. Pas bij het tonen deel
# je door honderd (zie in_euro).
# Het liggende streepje in 12_000 is alleen voor de leesbaarheid; Python
# negeert het. 12_000 is gewoon 12000.
BASISTARIEF_CENTEN = 12_000
JEUGDTARIEF_CENTEN = 9_000
# Tot en met 17 jaar betaal je het jeugdtarief, vanaf 18 het basistarief.
JEUGD_TOT_EN_MET = 17
GEZINSKORTING_CENTEN = 1_500


# De klasse Lid (hoofdstuk 18): elk object is één lid, met zijn eigen
# ATTRIBUTEN (nummer, naam, ...) en METHODEN (leeftijd, openstaand_centen).
class Lid:
    """Eén lid van de turnclub."""

    # __init__ wordt opgeroepen bij Lid(...). Ze vult de attributen van het
    # nieuwe object.
    #   gezin_id=None    -> STANDAARDWAARDE: laat je het weg, dan hoort het lid
    #                       bij geen gezin
    #   rang_in_gezin=1  -> het hoeveelste gezinslid dit is (1 = het eerste)
    def __init__(self, nummer, naam, geboortejaar, groep_id,
                 gezin_id=None, rang_in_gezin=1):
        # strip() haalt spaties vooraan en achteraan weg. Een naam van alleen
        # spaties wordt zo "", en een lege string telt als onwaar.
        # assert (hoofdstuk 25) stopt het programma met een AssertionError en
        # deze boodschap als de naam leeg is.
        # LET OP: een assert is bedoeld om programmeerfouten te vangen, niet om
        # invoer van de gebruiker te controleren. Python kan asserts zelfs
        # uitschakelen (met python -O). Controleer namen uit het menu straks
        # dus met een gewone if en een duidelijke melding (eis 5).
        assert naam.strip(), "een lid moet een naam hebben"
        self.nummer = nummer
        # De naam bewaar je zonder overbodige spaties.
        self.naam = naam.strip()
        self.geboortejaar = geboortejaar
        self.groep_id = groep_id
        self.gezin_id = gezin_id
        self.rang_in_gezin = rang_in_gezin
        # Een nieuw lid heeft nog niets betaald. Ook dit is in centen.
        self.betaald_centen = 0

    # De leeftijd wordt BEREKEND, niet bewaard. Een bewaarde leeftijd zou
    # volgend jaar fout zijn; het geboortejaar blijft altijd juist.
    # in_jaar heeft een standaardwaarde, zodat je in een test een ander jaar
    # kunt meegeven.
    def leeftijd(self, in_jaar=HUIDIG_JAAR):
        """De leeftijd die het lid dit jaar bereikt."""
        return in_jaar - self.geboortejaar

    # Het nog te betalen bedrag: lidgeld min wat al betaald is.
    # max(a, b) geeft de grootste van de twee terug. max(0, ...) zorgt dat het
    # nooit onder nul gaat, ook als iemand te veel betaalde.
    # De methode roept de functie lidgeld_centen op, die pas verderop in het
    # bestand staat. Dat werkt: de methode loopt pas als het hele bestand
    # gelezen is, en dan bestaat lidgeld_centen al.
    def openstaand_centen(self):
        """Wat er nog betaald moet worden; nooit negatief."""
        return max(0, lidgeld_centen(self.geboortejaar,
                                     self.rang_in_gezin) - self.betaald_centen)

    # __repr__ bepaalt hoe een Lid eruitziet als je het afdrukt in een lijst of
    # in de interactieve shell. Zonder deze methode zie je iets als
    # <__main__.Lid object at 0x...>. {self.naam!r} zet de naam tussen
    # aanhalingstekens.
    def __repr__(self):
        return f"Lid({self.nummer}, {self.naam!r}, {self.geboortejaar})"


# De rekenregel (eis 7) als losse functie, met een CONTRACT in de docstring
# (hoofdstuk 25, eis 16):
#   PRECONDITIE  -> wat geldig is als invoer
#   POSTCONDITIE -> wat de functie belooft over het resultaat
# De functie staat los van de klasse, zodat je ze kunt testen zonder eerst een
# Lid te maken.
def lidgeld_centen(geboortejaar, rang_in_gezin=1, in_jaar=HUIDIG_JAAR):
    """Het lidgeld in hele centen.

    Preconditie : 1900 <= geboortejaar <= in_jaar, rang_in_gezin >= 1.
    Postconditie: 0 <= resultaat <= BASISTARIEF_CENTEN.
    """
    # Eerst de precondities controleren. Klopt er iets niet, dan een fout
    # opgooien (hoofdstuk 15) in plaats van een verkeerd bedrag terug te geven.
    # LET OP: bool apart uitsluiten. True is in Python ook een int (de waarde
    # 1). Zonder die extra test zou True de typecontrole passeren en pas
    # verderop een ValueError geven in plaats van een TypeError.
    # Dat is de valkuil uit hoofdstuk 28 (oefening 28.1).
    if not isinstance(geboortejaar, int) or isinstance(geboortejaar, bool):
        raise TypeError("geboortejaar moet een geheel getal zijn")
    # Geen geboortejaar in de toekomst, en niet absurd ver in het verleden.
    if not 1900 <= geboortejaar <= in_jaar:
        raise ValueError(f"geboortejaar {geboortejaar} is onmogelijk")
    if rang_in_gezin < 1:
        raise ValueError("de rang in het gezin begint bij 1")

    # Het basisbedrag. Een VOORWAARDELIJKE UITDRUKKING: "A if voorwaarde else B"
    # geeft A als de voorwaarde waar is, anders B. De haakjes laten toe om de
    # uitdrukking over twee regels te spreiden.
    # "<=" omdat de regel "tot en met 17" zegt: 17 jaar is nog jeugd.
    leeftijd = in_jaar - geboortejaar
    bedrag = (JEUGDTARIEF_CENTEN if leeftijd <= JEUGD_TOT_EN_MET
              else BASISTARIEF_CENTEN)

    # Gezinskorting vanaf het TWEEDE gezinslid. Het is een vaste korting: het
    # derde of vijfde lid krijgt dezelfde 15 euro, niet 2 of 4 keer zoveel.
    # bedrag -= X is kort voor bedrag = bedrag - X.
    if rang_in_gezin >= 2:
        bedrag -= GEZINSKORTING_CENTEN

    # Nooit onder nul. Met de huidige tarieven kan dat niet, maar verandert
    # iemand later de korting, dan blijft de postconditie toch gelden.
    bedrag = max(0, bedrag)
    # De POSTCONDITIE als assert: de functie controleert haar eigen belofte.
    # Faalt deze regel ooit, dan zit de fout in deze functie zelf.
    assert 0 <= bedrag <= BASISTARIEF_CENTEN
    return bedrag


# Centen omzetten naar tekst, pas op het moment dat je ze toont.
#   centen // 100     -> GEHELE DELING: de hele euro's (7500 // 100 = 75)
#   centen % 100      -> MODULO: de rest, de centen (7500 % 100 = 0)
#   :02d              -> als geheel getal, minstens 2 cijfers, aangevuld met
#                        een 0 vooraan: 5 wordt "05", zodat je "75,05" krijgt
# De komma als scheidingsteken is de Belgische schrijfwijze.
def in_euro(centen):
    """Centen als leesbaar bedrag."""
    return f"{centen // 100},{centen % 100:02d} euro"


# Proefgegevens: vier leden in een lijst. Zo toon je dat de kern werkt zonder
# menu (opdracht 4 van de oefening).
# Waarom deze vier? Ze dekken elk ander geval:
#   Anke  -> volwassen, alles betaald
#   Bram  -> jeugd, eerste gezinslid, deels betaald
#   Cato  -> jeugd, tweede gezinslid: krijgt de gezinskorting
#   Dirk  -> volwassen, nog niets betaald
# Bram en Cato hebben hetzelfde gezin_id (7): zo weet het programma dat ze bij
# hetzelfde gezin horen.
# groep_id=2 is een TREFWOORDARGUMENT: je noemt de parameter bij naam.
LEDEN = [
    Lid(1, "Anke Peeters", 1990, groep_id=2),
    Lid(2, "Bram Janssens", 2012, groep_id=1, gezin_id=7, rang_in_gezin=1),
    Lid(3, "Cato Janssens", 2015, groep_id=1, gezin_id=7, rang_in_gezin=2),
    Lid(4, "Dirk Willems", 1978, groep_id=3),
]
# Betalingen registreren. LEDEN[0] is het eerste lid (indexen beginnen bij 0,
# hoofdstuk 12). Je past het attribuut van dat object rechtstreeks aan.
LEDEN[0].betaald_centen = 12_000
LEDEN[1].betaald_centen = 5_000

# Het overzicht als tabel. f-strings met uitlijning (hoofdstuk 6):
#   :<16 -> links uitgelijnd over 16 tekens
#   :>9  -> rechts uitgelijnd over 9 tekens
# Getallen en bedragen lijn je rechts uit, zodat de cijfers onder elkaar staan.
print(f"{'Lid':<16}{'Leeftijd':>9}{'Lidgeld':>12}{'Openstaand':>13}")
print("-" * 50)
for lid in LEDEN:
    # Drie f-strings na elkaar tussen haakjes worden aan elkaar geplakt tot één
    # tekst. Zo blijft elke regel kort genoeg.
    # lid.leeftijd() met haakjes: het is een methode, geen attribuut.
    print(f"{lid.naam:<16}{lid.leeftijd():>9}"
          f"{in_euro(lidgeld_centen(lid.geboortejaar, lid.rang_in_gezin)):>12}"
          f"{in_euro(lid.openstaand_centen()):>13}")

# Een FILTER (eis 8) met een list comprehension (hoofdstuk 14): alleen de leden
# die nog iets moeten betalen.
wanbetalers = [lid for lid in LEDEN if lid.openstaand_centen() > 0]
print()
# ", ".join(...) plakt teksten aan elkaar met ", " ertussen. Erin staat een
# GENERATOR-uitdrukking (een comprehension zonder vierkante haken): ze levert
# de namen een voor een aan join.
print("Nog te betalen door:", ", ".join(lid.naam for lid in wanbetalers))
# sum(...) telt alle openstaande bedragen op, nog altijd in centen. Pas het
# totaal wordt omgezet naar euro: zo kan er geen afrondingsfout insluipen.
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
