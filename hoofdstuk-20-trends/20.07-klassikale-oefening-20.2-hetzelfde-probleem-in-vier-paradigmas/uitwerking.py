# Python basis — theoriebundel
# Hoofdstuk 20 — Trends in programmeren
# Klassikale oefening 20.2 — Hetzelfde probleem in vier paradigma's, uitwerking

# De Leeslamp — één probleem, vier stijlen
# Cursus Python basis, hoofdstuk 20, oefening 2

# Het probleem: geef de titels van alle boeken van meer dan 250 bladzijden, in
# hoofdletters en alfabetisch gesorteerd. Je lost het vier keer op, telkens in een
# ander PARADIGMA (20.3). Alle vier moeten exact hetzelfde antwoord geven.

# De gegevens: een lijst van TUPLES (hoofdstuk 13). Elke tuple is één boek:
#   b[0] -> de titel (str)
#   b[1] -> het aantal bladzijden (int)
# Een tuple past hier: titel en bladzijden horen samen en veranderen niet.
# HOOFDLETTERS in de naam: een "constante" (hoofdstuk 5), die je niet aanpast.
BOEKEN = [
    ("Turks fruit", 175),
    ("De ontdekking van de hemel", 928),
    ("Het diner", 288),
    ("De aanslag", 246),
    ("Max Havelaar", 340),
    ("Bint", 96),
]
# Een boek is "dik" als het MEER dan GRENS bladzijden heeft (dus > en niet >=).
GRENS = 250


# 1 — procedureel
# PROCEDUREEL: stap voor stap, met een lus en een lege lijst die je opvult
# (het opbouwpatroon uit hoofdstuk 10).
def dikke_titels_procedureel(boeken, grens):
    """Met lussen, stap voor stap."""
    uit = []
    # Tuple uitpakken in de for-kop: elke tuple ("Turks fruit", 175) wordt
    # meteen gesplitst in titel = "Turks fruit" en bladzijden = 175.
    for titel, bladzijden in boeken:
        if bladzijden > grens:
            # upper() geeft een nieuwe string terug, volledig in hoofdletters.
            uit.append(titel.upper())
    # sort() sorteert de lijst ZELF (ter plaatse) en geeft None terug.
    # LET OP: schrijf dus niet return uit.sort(), want dan geef je None terug.
    uit.sort()
    return uit


# 2 — functioneel
# FUNCTIONEEL: je bouwt het antwoord uit functies die je aan elkaar doorgeeft.
# Er is geen lijst die je stap voor stap aanpast.
def dikke_titels_functioneel(boeken, grens):
    """Met filter, map en sorted."""
    # filter(functie, reeks) houdt alleen de elementen over waarvoor de functie
    # True teruggeeft. De functie is hier een LAMBDA (hoofdstuk 11.8): een functie
    # van één uitdrukking, zonder naam. lambda b: b[1] > grens betekent
    # "neem een boek b en geef terug of zijn bladzijden boven de grens liggen".
    # filter geeft geen lijst terug maar een filter-object dat pas rekent als
    # iemand de waarden opvraagt.
    dik = filter(lambda b: b[1] > grens, boeken)
    # map(functie, reeks) past de functie toe op ELK element en geeft de
    # uitkomsten één voor één door. Hier: van elk dik boek de titel in hoofdletters.
    # Ook map geeft een map-object terug, nog geen lijst.
    titels = map(lambda b: b[0].upper(), dik)
    # sorted(reeks) neemt eender welke reeks, haalt alle waarden op en geeft een
    # NIEUWE, gesorteerde lijst terug. Pas hier wordt er echt gerekend.
    return sorted(titels)


# 3 — met een comprehension
# De Python-manier: één uitdrukking die zegt wat je wilt.
# Tussen de haakjes van sorted() staat een comprehension ZONDER vierkante haken:
# een GENERATOR (hoofdstuk 14.3). Die geeft de waarden één voor één door aan
# sorted, zonder eerst een tussenlijst te maken. Lees ze als: "titel.upper(),
# voor elke titel en blz in boeken, als blz groter is dan grens".
def dikke_titels_comprehension(boeken, grens):
    """De Python-manier."""
    return sorted(titel.upper() for titel, blz in boeken if blz > grens)


# 4 — objectgeoriënteerd
# OBJECTGERICHT (hoofdstuk 18): de gegevens en de bewerkingen erop zitten samen
# in één klasse. Je stelt de vraag aan het object zelf.
class Catalogus:
    """Een verzameling boeken met bevragingen erop."""

    # list(boeken) maakt altijd een nieuwe, eigen lijst. Dat werkt voor een lijst,
    # maar ook voor een generator (zie dikker_dan hieronder). Het object deelt zo
    # ook geen lijst met de buitenwereld (kopie versus verwijzing, hoofdstuk 14).
    def __init__(self, boeken):
        self.boeken = list(boeken)

    # Geeft geen lijst terug maar een NIEUW Catalogus-object. Daardoor kun je
    # na dikker_dan() meteen een volgende methode oproepen (zie onderaan).
    # Het argument is een generator; __init__ maakt er met list() een lijst van.
    def dikker_dan(self, grens):
        """Een nieuwe catalogus met alleen de dikke boeken."""
        return Catalogus(b for b in self.boeken if b[1] > grens)

    # De underscore _ is een gewone variabelenaam die zegt: "deze waarde (de
    # bladzijden) heb ik niet nodig". Een afspraak tussen programmeurs.
    def titels(self):
        """De titels, in hoofdletters en gesorteerd."""
        return sorted(titel.upper() for titel, _ in self.boeken)

    # __len__ is een speciale methode (hoofdstuk 18): door ze te schrijven werkt
    # len(catalogus) op je eigen klasse. Ze wordt in dit programma niet gebruikt.
    def __len__(self):
        return len(self.boeken)


# Een dictionary (hoofdstuk 13): de naam van de stijl is de sleutel, de lijst met
# titels die die stijl teruggeeft is de waarde. Elke regel roept één versie op.
# De laatste regel leest van links naar rechts als een zin:
#   Catalogus(BOEKEN)      -> een catalogus met alle zes boeken
#   .dikker_dan(GRENS)     -> een nieuwe catalogus met alleen de dikke boeken
#   .titels()              -> hun titels, in hoofdletters en gesorteerd
resultaten = {
    "procedureel": dikke_titels_procedureel(BOEKEN, GRENS),
    "functioneel": dikke_titels_functioneel(BOEKEN, GRENS),
    "comprehension": dikke_titels_comprehension(BOEKEN, GRENS),
    "objectgericht": Catalogus(BOEKEN).dikker_dan(GRENS).titels(),
}

# items() geeft paren (sleutel, waarde), die je in de for-kop uitpakt.
# {stijl:<16} uit hoofdstuk 6: de naam links uitlijnen in een vak van 16 tekens,
# zodat de lijsten mooi onder elkaar beginnen.
for stijl, uitkomst in resultaten.items():
    print(f"{stijl:<16}{uitkomst}")

# Een lege regel.
print()
# De controle dat alle vier hetzelfde antwoord geven, van binnen naar buiten:
#   resultaten.values()  -> de vier lijsten
#   map(tuple, ...)      -> zet elke lijst om naar een tuple. Dat moet, want een
#                           set mag alleen onveranderlijke waarden bevatten
#                           (hoofdstuk 13): een lijst mag er niet in, een tuple wel.
#   set(...)             -> een set laat dubbels vallen: vier gelijke tuples
#                           worden één element
#   len(...) == 1        -> is er precies één verschillend antwoord? Dan True.
print("Alle vier gelijk:", len(set(map(tuple, resultaten.values()))) == 1)


# Verwachte uitvoer:
# procedureel     ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
# functioneel     ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
# comprehension   ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
# objectgericht   ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
#
# Alle vier gelijk: True
