# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.4 De lusinvariant
#
# Neem het optellen van bladzijden:

# Een if kun je nagaan met een waarheidstabel. Een lus niet: die kan duizend keer
# draaien. Daarvoor dient de LUSINVARIANT: een bewering die waar is vóór de lus
# begint en na ELKE ronde opnieuw waar is.
# Het bewijs heeft altijd drie delen:
#   BEGINWAARDE -> de invariant is waar vóór de eerste ronde
#   BEHOUD      -> was ze waar aan het begin van een ronde, dan ook aan het einde
#   EINDE       -> invariant plus stopvoorwaarde geven samen wat je wilde
# De redeneervorm is MODUS PONENS (24.2), steeds opnieuw toegepast: waar aan het
# begin, dus waar na ronde 1, dus waar na ronde 2, enzovoort.
def totaal_bladzijden(boeken):
    """Het totale aantal bladzijden.

    Invariant: `totaal` is de som van de eerste `i` boeken.
    """
    # BEGINWAARDE: nog geen enkel boek opgeteld, en de som van nul boeken is 0.
    # De invariant klopt dus al vóór de lus.
    totaal = 0
    # enumerate (10.5) geeft bij elk element ook een teller. Met start=1 telt
    # die vanaf 1 in plaats van 0: i is dan "hoeveel boeken je al hebt gezien".
    # Ronde 1: i=1, aantal=320. Ronde 2: i=2, aantal=180. Ronde 3: i=3, aantal=250.
    for i, aantal in enumerate(boeken, start=1):
        # BEHOUD: was totaal de som van de eerste i-1 boeken, dan is het na
        # deze optelling de som van de eerste i boeken.
        totaal += aantal
        # De invariant laten nakijken door Python.
        # boeken[:i] is een SNEDE (12.3): de eerste i elementen. sum() telt ze
        # op. Klopt totaal niet met die som, dan stopt het programma hier.
        # LET OP: deze controle rekent elke ronde de hele som opnieuw uit. Dat is
        # traag bij lange lijsten; ze staat er om te LEREN, niet voor productie.
        assert totaal == sum(boeken[:i]), "invariant geschonden"
    # EINDE: de lus is gestopt na het laatste boek, dus i is len(boeken).
    # Invariant + stopvoorwaarde: totaal is de som van ALLE boeken.
    return totaal


# 320 + 180 + 250 = 750
print(totaal_bladzijden([320, 180, 250]))
# Het LEGE GEVAL komt er gratis uit: de lus draait nul keer, en totaal blijft op
# zijn beginwaarde 0 staan. Precies wat de invariant voorspelt: de som van nul
# boeken is nul. Je hoeft er geen aparte if voor te schrijven.
print(totaal_bladzijden([]))


# Verwachte uitvoer:
# 750
# 0
