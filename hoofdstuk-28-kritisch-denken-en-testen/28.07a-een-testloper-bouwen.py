# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.7 Een testloper bouwen
#
# Een reeks losse assert-regels heeft één nadeel: bij de eerste die faalt, stopt
# alles, en de rest zie je niet. Met tien regels code los je dat op.

# Een TESTLOPER is een functie die een hele reeks tests na elkaar uitvoert,
# elke mislukking noteert en pas op het einde een overzicht geeft.
#   tests -> een lijst van tuples (naam, test). De naam is een string, de test
#            is een functie zonder parameters die je kunt oproepen.
#   geeft True terug als alles slaagde, anders False.
# Een minimale testloper
def loop_tests(tests):
    """Draait elke test en meldt alles wat faalt, niet alleen het eerste."""
    # Twee variabelen in één keer: een teller (0) en een lege lijst ([]).
    geslaagd, gefaald = 0, []
    # Elk element van tests is een tuple; "naam, test" pakt het uit (hoofdstuk 13).
    for naam, test in tests:
        # try/except uit hoofdstuk 15: een fout in één test mag de loper niet
        # doen stoppen. Daarom vang je ze hier op en ga je door.
        try:
            # test() voert de test uit. De haakjes zijn nodig: test is een functie.
            test()
            # Geen fout opgetreden? Dan is de test geslaagd.
            geslaagd += 1
        # Soort 1: een AssertionError. De test controleerde iets en dat klopte
        # niet. str(fout) is de boodschap; is die leeg (""), dan geeft "or" de
        # tekst "geen boodschap" (een lege string telt als onwaar).
        except AssertionError as fout:
            gefaald.append((naam, str(fout) or "geen boodschap"))
        # Soort 2: elke ANDERE fout, bv. een ZeroDivisionError. Een test die
        # crasht, is ook een test die niet slaagt.
        # type(fout).__name__ geeft de naam van de foutsoort als tekst.
        # LET OP: deze except moet ONDER de vorige staan. Exception vangt alles,
        # ook een AssertionError; stond ze eerst, dan kwam je nooit bij soort 1.
        except Exception as fout:
            gefaald.append((naam, f"{type(fout).__name__}: {fout}"))

    # Het overzicht: eerst de tellingen, dan elke mislukte test met de reden.
    # len(gefaald) is het aantal mislukte tests.
    print(f"{geslaagd} geslaagd, {len(gefaald)} gefaald")
    for naam, reden in gefaald:
        print(f"  FOUT  {naam}: {reden}")
    # Een lege lijst telt als onwaar, dus "not gefaald" is True als er niets
    # mislukte, en False zodra er minstens één mislukking in de lijst staat.
    return not gefaald


# De functie die getest wordt. Met opzet eenvoudig: het gaat om de testloper.
def deel(a, b):
    """Deelt a door b."""
    return a / b


# De testverzameling: een lijst van (naam, test).
# Elke test is een LAMBDA (11.8): een naamloze mini-functie van één uitdrukking.
# "lambda: ..." voert die uitdrukking pas uit als je de lambda oproept.
# De truc met "or": deel(10, 2) == 5 is True of False.
#   True  -> "or" kijkt niet verder; de test is geslaagd.
#   False -> "or" moet het rechterdeel uitrekenen en roept _fout(...) op,
#            die een AssertionError met een leesbare boodschap opgooit.
# "deling door nul" controleert niets: deel(1, 0) crasht met een
# ZeroDivisionError. Die test staat er om te tonen dat de loper ook een
# onverwachte fout meldt in plaats van te stoppen.
TESTS = [
    ("gewone deling", lambda: deel(10, 2) == 5 or _fout("10/2 hoort 5 te zijn")),
    ("deling door nul", lambda: deel(1, 0)),
    ("negatieve deling", lambda: deel(-6, 3) == -2 or _fout("-6/3 hoort -2")),
]


# Het hulpje staat pas NA de lijst TESTS. Toch werkt dat: een lambda zoekt de
# naam _fout pas op op het moment dat ze uitgevoerd wordt, en dat gebeurt pas
# in loop_tests. Dan bestaat _fout al.
# Het liggende streepje vooraan de naam betekent: "intern hulpje, niet bedoeld
# om van buitenaf te gebruiken".
def _fout(boodschap):
    """Hulpje: laat een lambda falen met een leesbare boodschap."""
    # raise in een lambda kan niet (een lambda bevat geen opdrachten), daarom
    # zit het in deze aparte functie.
    raise AssertionError(boodschap)


# De loper draaien en zijn antwoord (True of False) bewaren.
# "Pijplijn groen" verwijst naar de pijplijn uit hoofdstuk 21: groen betekent
# dat alle tests slaagden.
alles_goed = loop_tests(TESTS)
print("Pijplijn groen:", alles_goed)


# Verwachte uitvoer:
# 2 geslaagd, 1 gefaald
#   FOUT  deling door nul: ZeroDivisionError: division by zero
# Pijplijn groen: False
