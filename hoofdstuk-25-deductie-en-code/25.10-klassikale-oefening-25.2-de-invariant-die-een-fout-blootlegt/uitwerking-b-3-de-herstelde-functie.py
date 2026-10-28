# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.2 — De invariant die een fout blootlegt, uitwerking
#
# 3. De herstelde functie.

# Het herstel in één zin: neem als beginwaarde een getal UIT de lijst zelf.
# Dan is de invariant al waar vóór de lus begint: na één bekeken getal is dat
# ene getal vanzelf het grootste.

def hoogste(getallen):
    """Het grootste getal uit de reeks.

    Preconditie : getallen bevat minstens één getal.
    Invariant   : `grootste` is het grootste van de reeds bekeken getallen.
    Postconditie: het resultaat zit in getallen, en niets erin is groter.
    """
    # De preconditie uitgesproken. Dit is ook het antwoord op vraag 4: wat
    # gebeurt er met een lege lijst? Hier kiezen we: dat mag niet, en de functie
    # stopt met een duidelijke melding. Je had ook None kunnen teruggeven. Welke
    # keuze juist is, hangt af van wat het programma met het antwoord doet, en
    # dat is een beslissing, geen technische vraag.
    assert len(getallen) > 0, "hoogste() verwacht minstens één getal"

    grootste = getallen[0]                 # beginwaarde uit de reeks zelf
    # getallen[1:] is de lijst zonder het eerste getal: dat hebben we al.
    # enumerate() geeft bij elk getal ook een teller. Met start=2 telt die mee
    # HOEVEEL getallen er na deze ronde bekeken zijn: het eerste plus dit = 2.
    for i, getal in enumerate(getallen[1:], start=2):
        if getal > grootste:
            grootste = getal
        # De invariant gecontroleerd na elke ronde. getallen[:i] zijn de eerste
        # i getallen, precies de bekeken getallen, en max() geeft daar het
        # grootste van. Breekt de invariant ooit, dan stopt het programma hier.
        # (Dit is een controle voor tijdens het ontwikkelen: max() in elke ronde
        # opnieuw uitrekenen is traag bij een lange lijst.)
        assert grootste == max(getallen[:i]), "invariant geschonden"

    # De postconditie, in twee delen:
    #   1. het resultaat komt in de lijst voor (dit deel vangt de oude fout);
    #   2. geen enkel getal in de lijst is groter.
    # all(...) geeft True als de voorwaarde voor ELK getal in de lijst waar is.
    # Wat tussen de haakjes staat, lijkt op een comprehension (hoofdstuk 14) zonder
    # vierkante haken.
    assert grootste in getallen
    assert all(getal <= grootste for getal in getallen)
    return grootste


# Dezelfde gewone en negatieve lijst als in uitwerking 2, en nu ook de kleinste
# lijst die de preconditie toelaat: één element. Die draait de lus nul keer,
# en toch klopt het antwoord, want de beginwaarde is al het juiste getal.
# De lege lijst staat er bewust niet meer bij: die zou de assert bovenaan
# laten afgaan. Probeer het gerust: print(hoogste([])).
print("gewone lijst   :", hoogste([320, 180, 250]))
print("negatieve lijst:", hoogste([-5, -12, -3]))
print("één element    :", hoogste([7]))


# Verwachte uitvoer:
# gewone lijst   : 320
# negatieve lijst: -3
# één element    : 7
