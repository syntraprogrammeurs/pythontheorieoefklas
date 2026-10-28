# Python basis — theoriebundel
# Hoofdstuk 26 — Categorische logica en venndiagrammen
# 26.6 De acht gebieden in Python
#
# Nu is de geldigheidstoets exact dezelfde als in hoofdstuk 23: geldig betekent dat er
# geen enkele wereld bestaat waarin de premissen kloppen en de conclusie niet.

# Dit bestand herhaalt de bouwstenen uit 26.06a (zonder docstrings, en alleen de
# vormen die je hier nodig hebt) en voegt er twee functies aan toe:
#   beschrijf -> maakt van een gebied een leesbare naam, zoals "S+M"
#   toets     -> gaat alle 256 werelden af en zoekt een TEGENWERELD
# Een TEGENWERELD (of tegenvoorbeeld) is een wereld waarin alle premissen waar zijn
# en de conclusie toch onwaar. Bestaat er zo één, dan is de redenering ONGELDIG.
# Bestaat er geen enkele, dan is ze GELDIG (de definitie van geldigheid uit
# hoofdstuk 22 en 24).

# product(x, repeat=n): alle combinaties van n waarden uit x (hoofdstuk 23).
from itertools import product

# De drie termen: S en P uit de conclusie, M is de middenterm (26.4).
TERMEN = ("S", "P", "M")
# De acht gebieden, elk een tupel (in S?, in P?, in M?), in de volgorde van de
# tabel in 26.4: van (False, False, False) "buiten alles" tot (True, True, True).
GEBIEDEN = list(product([False, True], repeat=3))


# Ligt dit gebied in de groep 'term'? TERMEN.index geeft de plaats: S=0, P=1, M=2.
def hoort_bij(gebied, term):
    return gebied[TERMEN.index(term)]


# A-uitspraak "Alle a zijn b": geen enkel bewoond gebied ligt in a en buiten b.
# any() geeft True zodra één element waar is; "not any" betekent dus "geen enkel".
# Een lege wereld maakt alle() altijd True: "alle" zegt niet dat de groep bestaat.
def alle(wereld, a, b):
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


# I-uitspraak "Sommige a zijn b": minstens één bewoond gebied ligt in a en in b.
# Een lege wereld maakt sommige() altijd False: er is dan niemand.
def sommige(wereld, a, b):
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


# Alle 256 werelden, één per keer (een GENERATOR met yield, zie 26.06a).
# Per keuze van True/False voor de acht gebieden blijven de bewoonde gebieden over.
# De allereerste wereld is de lege wereld ().
def werelden():
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


# beschrijf zet een gebied om in tekst, zodat je de tegenwereld kunt lezen.
#   - De LIST COMPREHENSION (hoofdstuk 14) houdt de termen over waarin het gebied
#     ligt.
#     Voorbeeld: (True, False, True) -> ["S", "M"].
#   - "+".join(...) plakt die termen aan elkaar met een plusteken: "S+M".
#   - "... if binnen else ..." is een VOORWAARDELIJKE UITDRUKKING: een korte if/else
#     op één regel (hoofdstuk 9). Een lege lijst telt als False, dus het gebied
#     (False, False, False) krijgt de naam "buiten alles".
def beschrijf(gebied):
    """Een leesbare naam voor één gebied."""
    binnen = [t for t in TERMEN if hoort_bij(gebied, t)]
    return "+".join(binnen) if binnen else "buiten alles"


# toets is de eigenlijke geldigheidstoets, net zoals bij de waarheidstabel (h. 23).
#   naam      -> een tekst om af te drukken
#   premissen -> een LIJST van functies; elke functie krijgt een wereld en zegt of
#                die premisse daar waar is
#   conclusie -> één zo'n functie voor de conclusie
#
# all() is de tegenhanger van any() (beide uit hoofdstuk 12): all(...) geeft True
# als ELK element waar is.
# "all(p(wereld) for p in premissen)" vraagt dus: zijn alle premissen waar?
# Is dat zo, en is de conclusie NIET waar, dan heb je een tegenwereld gevonden.
#
# Zodra er één tegenwereld is, druk je die af en stopt return de functie meteen.
# Eén tegenvoorbeeld volstaat om een algemene bewering onderuit te halen (26.3).
# Pas als de lus alle 256 werelden heeft afgelopen zonder tegenwereld, kom je bij
# de laatste print: dan is de redenering geldig.
#
# LET OP: toets toont alleen de EERSTE tegenwereld die hij vindt. Er kunnen er meer
# zijn. Welke de eerste is, hangt af van de volgorde in werelden().
def toets(naam, premissen, conclusie):
    """Drukt af of het syllogisme geldig is, met tegenvoorbeeld."""
    for wereld in werelden():
        if all(p(wereld) for p in premissen) and not conclusie(wereld):
            # De bewoonde gebieden als tekst, gescheiden door komma's.
            # Is de wereld leeg, dan geeft join een lege string "". Een lege string
            # telt als False, dus "or" kiest dan het woord "leeg".
            bewoond = ", ".join(beschrijf(g) for g in wereld) or "leeg"
            # {naam:<34} vult de naam aan met spaties tot 34 tekens, links uitgelijnd
            # (f-strings uit hoofdstuk 6), zodat de uitkomsten onder elkaar staan.
            print(f"{naam:<34}ONGELDIG — tegenwereld: {bewoond}")
            return
    print(f"{naam:<34}geldig")


# De premissen en de conclusie geef je door als LAMBDA-functies: kleine naamloze
# functies op één regel (hoofdstuk 11). "lambda w: alle(w, "M", "P")" betekent:
# een functie die een wereld w krijgt en alle(w, "M", "P") teruggeeft. Zo kan toets
# elke premisse zelf oproepen voor elke wereld die hij afgaat.
# LET OP: je roept alle() hier nog niet op. Je geeft het RECEPT door; toets voert het
# pas uit, voor elke wereld opnieuw.

# Barbara: alle M zijn P, alle S zijn M, dus alle S zijn P
# Twee A-premissen en een A-conclusie: de bekendste geldige vorm. Er bestaat geen
# wereld waarin beide premissen kloppen en er toch een S buiten P zit.
toets("alle M-P, alle S-M => alle S-P",
      [lambda w: alle(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: alle(w, "S", "P"))

# Dezelfde premissen, maar met een particuliere conclusie
# Een I-conclusie: "sommige S zijn P". Dit is de valkuil uit 26.3: uit "alle" volgt
# geen "sommige". In de LEGE wereld (niemand bestaat) zijn beide A-premissen waar,
# want er is geen tegenvoorbeeld. Maar "sommige S zijn P" is daar onwaar, want er is
# niemand. Die lege wereld is ook de eerste die werelden() aflevert.
toets("alle M-P, alle S-M => sommige S-P",
      [lambda w: alle(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: sommige(w, "S", "P"))


# Verwachte uitvoer:
# alle M-P, alle S-M => alle S-P    geldig
# alle M-P, alle S-M => sommige S-P ONGELDIG — tegenwereld: leeg
