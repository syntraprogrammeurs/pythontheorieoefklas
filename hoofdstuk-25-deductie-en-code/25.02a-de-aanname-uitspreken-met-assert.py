# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.2 De aanname uitspreken met assert
#
# Een aanname die in je hoofd zit, kan niemand nakijken. Een aanname die in je code
# staat, wel.

# Dezelfde functie als in 25.1, maar nu met haar CONTRACT erbij:
#   PRECONDITIE  -> wat de aanroeper moet waarmaken (minstens één getal)
#   POSTCONDITIE -> wat de functie dan belooft (het resultaat ligt tussen het
#                   kleinste en het grootste getal)
# In logische vorm: preconditie -> postconditie, een implicatie (hoofdstuk 23).
#
# Het contract staat twee keer: in de docstring, zodat een MENS het kan lezen, en
# als assert, zodat PYTHON het kan nakijken.
def gemiddelde(getallen):
    """Het rekenkundig gemiddelde van een reeks getallen.

    Preconditie : getallen bevat minstens één getal.
    Postconditie: min(getallen) <= resultaat <= max(getallen).
    """
    # ASSERT voorwaarde, "melding"
    #   - Is de voorwaarde waar, dan gebeurt er niets en gaat het programma verder.
    #   - Is ze onwaar, dan stopt Python met een AssertionError, met jouw melding
    #     erbij.
    # assert is een opdracht, geen functie: je zet de voorwaarde dus niet tussen
    # haakjes. assert (x, "tekst") zou altijd waar zijn, want een niet-lege tuple
    # is truthy (7.8).
    # Deze eerste assert controleert de PRECONDITIE, helemaal bovenaan: nog vóór er
    # iets misgaat. Zo faalt de functie op de plek waar de fout BINNENKOMT.
    assert len(getallen) > 0, "gemiddelde() verwacht minstens één getal"

    # Het eigenlijke werk. Dankzij de assert hierboven weet je dat len(getallen)
    # minstens 1 is: delen door nul kan hier niet meer. Dat is MODUS PONENS
    # (24.2): als de assert slaagde, is de lijst niet leeg; de assert slaagde;
    # dus de lijst is niet leeg.
    uitkomst = sum(getallen) / len(getallen)

    # Deze tweede assert controleert de POSTCONDITIE, vlak voor de return.
    # min() en max() geven het kleinste en het grootste element (12.8).
    # a <= b <= c is een KETTINGVERGELIJKING (7.3): hetzelfde als
    # a <= b and b <= c.
    # Hier staat geen melding achter: die is optioneel. Faalt deze assert, dan
    # zit de fout in de functie zelf, niet bij de aanroeper.
    assert min(getallen) <= uitkomst <= max(getallen)
    return uitkomst


# Twee aanroepen die de preconditie respecteren: beide asserts slagen, je merkt er
# niets van.
print(gemiddelde([320, 180, 250]))
# Ook één enkel getal voldoet aan "minstens één". Het gemiddelde van [7] is 7.0.
print(gemiddelde([7]))


# Verwachte uitvoer:
# 250.0
# 7.0
