# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.4 De lusinvariant — De invariant van binair zoeken
#
# Binair zoeken is het raadspel uit hoofdstuk 10, als functie: je zoekt in een
# gesorteerde lijst door telkens het midden te nemen. Hier doet de invariant echt
# werk.

# BINAIR ZOEKEN: je kijkt naar het element in het midden van een gesorteerde lijst.
#   - Is het je doel, dan ben je klaar.
#   - Is het te klein, dan zit het doel (als het er is) RECHTS van het midden.
#   - Is het te groot, dan zit het LINKS ervan.
# Elke ronde valt zo de helft weg, net als bij "hoger" of "lager" in het raadspel.
# Het stuk lijst waarin je nog zoekt, heet hier het VENSTER: van index links tot
# en met index rechts.
def binair_zoek(gesorteerd, doel):
    """Geeft de index van `doel`, of -1.

    Preconditie : `gesorteerd` is oplopend gesorteerd.
    Invariant   : als `doel` erin zit, ligt het tussen links en rechts.
    Postconditie: de teruggegeven index bevat `doel`, of het antwoord is -1.
    """
    # PRECONDITIE: binair zoeken werkt alleen op een gesorteerde lijst.
    # sorted() maakt een NIEUWE, gesorteerde kopie (12.7). Is die gelijk aan het
    # origineel, dan was het origineel al gesorteerd.
    assert gesorteerd == sorted(gesorteerd), "de lijst moet gesorteerd zijn"

    # Twee variabelen tegelijk toewijzen (5.2). Het venster begint als de hele
    # lijst: van de eerste index (0) tot de laatste (len - 1).
    links, rechts = 0, len(gesorteerd) - 1
    # Zolang links <= rechts bevat het venster minstens één element.
    # Is links groter dan rechts, dan is het venster leeg.
    while links <= rechts:
        # De INVARIANT, als assert. Lees ze als een implicatie (23.3):
        #   "als doel in de lijst zit, dan zit het in het venster"
        # geschreven als (not p) or q:
        #   doel not in gesorteerd  OF  doel in het venster.
        # gesorteerd[links:rechts + 1] is de snede (12.3) van links tot en met
        # rechts: bij een snede telt de bovengrens niet mee, vandaar de + 1.
        # LET OP: "in" doorzoekt de hele lijst, element per element. Deze assert
        # is dus trager dan het binair zoeken zelf. Ze staat er om de redenering
        # zichtbaar te maken, niet om in een echt programma te laten staan.
        assert doel not in gesorteerd or doel in gesorteerd[links:rechts + 1]

        # // is de GEHELE DELING (6.1): (0 + 5) // 2 is 2, niet 2.5.
        # Een index moet een geheel getal zijn.
        midden = (links + rechts) // 2
        # Gevonden: POSTCONDITIE "de teruggegeven index bevat doel" is waar.
        if gesorteerd[midden] == doel:
            return midden
        # Het middelste is te klein. Omdat de lijst gesorteerd is, zijn alle
        # getallen links van het midden nog kleiner: het doel kan daar niet
        # zitten. Het venster schuift naar rechts. De invariant blijft dus staan.
        if gesorteerd[midden] < doel:
            links = midden + 1
        # Het middelste is te groot: het doel kan alleen nog links zitten.
        else:
            rechts = midden - 1
        # Elke ronde wordt het venster minstens één kleiner. Zo weet je dat de lus
        # STOPT: iets dat elke ronde kleiner wordt en niet onder nul kan.
        # LET OP: schrijf je links = midden in plaats van links = midden + 1, dan
        # kan het venster blijven steken en draait de lus eeuwig. De invariant
        # blijft dan waar; het is het verkleinen dat je vergat.
    # De lus stopte met een leeg venster. Invariant: "als het doel erin zat, zat
    # het in het venster". Het venster is leeg, dus het doel zat er niet in. Dat
    # is MODUS TOLLENS (24.2): als p dan q; niet q; dus niet p.
    return -1


# Zes boeken, gesorteerd op hun aantal bladzijden.
BLADZIJDEN = [96, 175, 246, 288, 340, 928]

# Vier zoekopdrachten: midden in de lijst, het laatste element, het eerste
# element, en een getal dat er niet in zit. Juist de randen zijn interessant:
# daar gaan grensfouten het eerst mis.
# {doel:>4} lijnt het getal rechts uit over vier tekens (6.7).
for doel in (246, 928, 96, 300):
    print(f"{doel:>4} -> index {binair_zoek(BLADZIJDEN, doel)}")


# Verwachte uitvoer:
#  246 -> index 2
#  928 -> index 5
#   96 -> index 0
#  300 -> index -1
