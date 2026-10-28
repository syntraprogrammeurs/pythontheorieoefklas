# Python basis — theoriebundel
# Hoofdstuk 26 — Categorische logica en venndiagrammen
# Klassikale oefening 26.2 — Drie syllogismen toetsen, uitwerking
#
# 3. Het programma.

# De Leeslamp — drie syllogismen mechanisch getoetst
# Cursus Python basis, hoofdstuk 26, oefening 2
#
# Dit is het programma uit 26.6, toegepast op de drie redeneringen van de oefening.
# "Mechanisch toetsen" betekent: je denkt niet zelf na over de redenering, je laat
# de computer ALLE 256 werelden afgaan (alle manieren waarop de acht gebieden van
# het venndiagram bewoond of leeg kunnen zijn). Vindt hij een wereld waarin de
# premissen kloppen en de conclusie niet, dan is de redenering ONGELDIG.
#
# product(x, repeat=n) uit hoofdstuk 23 geeft alle combinaties van n waarden uit x.
from itertools import product

# S = onderwerp van de conclusie, P = predicaat van de conclusie, M = middenterm.
TERMEN = ("S", "P", "M")
# De acht gebieden: tupels (in S?, in P?, in M?), van (False, False, False) tot
# (True, True, True). 2 x 2 x 2 = 8, net als de acht rijen van de tabel in 26.4.
GEBIEDEN = list(product([False, True], repeat=3))


# Ligt dit gebied in de groep 'term'? TERMEN.index("S") geeft 0, "P" 1, "M" 2,
# en op die plaats in het gebied staat True of False.
def hoort_bij(gebied, term):
    return gebied[TERMEN.index(term)]


# De drie vormen die je in deze oefening nodig hebt. Elk krijgt een wereld (het
# tupel met de bewoonde gebieden) en twee termen, en geeft True of False terug.
# any() uit hoofdstuk 12: True zodra minstens één element waar is.

# A-uitspraak "Alle a zijn b": het gebied "in a, buiten b" is leeg.
def alle(wereld, a, b):
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


# E-uitspraak "Geen enkele a is b": de overlap van a en b is leeg.
def geen(wereld, a, b):
    return not any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


# I-uitspraak "Sommige a zijn b": in de overlap van a en b zit minstens iemand (X).
def sommige(wereld, a, b):
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


# Alle 256 werelden, één voor één (een GENERATOR: yield geeft telkens één wereld af).
# product(..., repeat=8) kiest per gebied bewoond (True) of leeg (False); zip legt
# elk gebied naast zijn keuze, en alleen de bewoonde gebieden komen in de wereld.
# De eerste wereld is de lege wereld (), omdat product met False begint.
def werelden():
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


# Een leesbare naam voor een gebied: de termen waarin het ligt, met + ertussen.
# Voorbeeld: (True, True, False) -> "S+P". Het gebied buiten alles heet "niets".
# (In 26.06b heette dat nog "buiten alles"; de betekenis is dezelfde.)
def beschrijf(gebied):
    binnen = [t for t in TERMEN if hoort_bij(gebied, t)]
    return "+".join(binnen) if binnen else "niets"


# De toets zelf. Hij loopt over alle werelden en zoekt een TEGENWERELD:
#   all(p(wereld) for p in premissen)  -> zijn ALLE premissen waar? (all() uit h. 12)
#   not conclusie(wereld)              -> en is de conclusie onwaar?
# Zijn beide waar, dan is dat het bewijs dat de redenering ongeldig is. Je drukt die
# wereld af en stopt met return: één tegenvoorbeeld volstaat.
# Wordt de lus volledig doorlopen zonder treffer, dan is de redenering geldig.
# LET OP: je ziet alleen de EERSTE tegenwereld. Er kunnen er nog andere zijn.
def toets(nummer, premissen, conclusie):
    """Zoekt een wereld waarin de premissen kloppen en de conclusie niet."""
    for wereld in werelden():
        if all(p(wereld) for p in premissen) and not conclusie(wereld):
            # join op een lege wereld geeft "", en "" or "lege wereld" geeft de tekst
            # rechts van or. Zo krijgt ook een lege tegenwereld een naam.
            bewoond = ", ".join(beschrijf(g) for g in wereld) or "lege wereld"
            print(f"{nummer}  ONGELDIG")
            # LET OP bij het lezen: alleen de BEWOONDE gebieden staan in de uitvoer.
            # Alle andere gebieden zijn in die wereld leeg, en juist die leegte
            # maakt vaak een premisse waar.
            print(f"   tegenwereld: bewoond zijn {bewoond}")
            return
    print(f"{nummer}  geldig")


# Elke premisse en conclusie is een LAMBDA (hoofdstuk 11): een kleine functie die
# een wereld w krijgt en True of False teruggeeft. toets roept ze zelf op, voor elke
# wereld opnieuw.

# Redenering 1: "Alle beheerders mogen leden verwijderen. Geen enkel gewoon lid is
# beheerder. Dus geen enkel gewoon lid mag leden verwijderen."
#   S = gewone leden, P = mogen verwijderen, M = beheerders
#   premissen: A (alle M zijn P) en E (geen S is M); conclusie: E (geen S is P)
# Voorspelling met de regels uit 26.5: ongeldig, want regel 2 is geschonden. P is in
# de E-conclusie volledig genomen, maar in de A-premisse (als predicaat) niet.
# Tegenwereld S+P: een gewoon lid dat geen beheerder is en toch mag verwijderen.
toets("1.",
      [lambda w: alle(w, "M", "P"), lambda w: geen(w, "S", "M")],
      lambda w: geen(w, "S", "P"))

# Redenering 2: "Alle geschorste leden krijgen een waarschuwing. Sommige leden krijgen
# een waarschuwing. Dus sommige leden zijn geschorst."
#   S = leden, P = geschorst, M = krijgen een waarschuwing
#   premissen: A (alle P zijn M) en I (sommige S zijn M); conclusie: I (sommige S
#   zijn P)
# Voorspelling: ongeldig, regel 1. De middenterm M is in geen van beide premissen
# volledig genomen. Het is het bevestigen van het consequens uit hoofdstuk 24, maar
# dan met groepen. Tegenwereld S+M: een lid met een waarschuwing, en verder niemand.
# Er is dus geen geschorst lid, en "alle geschorste leden..." is dan vanzelf waar.
toets("2.",
      [lambda w: alle(w, "P", "M"), lambda w: sommige(w, "S", "M")],
      lambda w: sommige(w, "S", "P"))

# Redenering 3: "Geen enkel geschorst lid mag lenen. Alle leden met een boete zijn
# geschorst. Dus geen enkel lid met een boete mag lenen."
#   S = leden met een boete, P = mogen lenen, M = geschorste leden
#   premissen: E (geen M is P) en A (alle S zijn M); conclusie: E (geen S is P)
# Voorspelling: geldig, alle vijf regels zijn voldaan. In geen van de 256 werelden
# vindt toets een tegenwereld.
toets("3.",
      [lambda w: geen(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: geen(w, "S", "P"))


# Verwachte uitvoer:
# 1.  ONGELDIG
#    tegenwereld: bewoond zijn S+P
# 2.  ONGELDIG
#    tegenwereld: bewoond zijn S+M
# 3.  geldig
