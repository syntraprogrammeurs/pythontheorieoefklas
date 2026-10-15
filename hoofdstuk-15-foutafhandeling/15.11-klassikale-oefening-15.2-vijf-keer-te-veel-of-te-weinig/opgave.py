# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, opgave
#
# De situatie. Je krijgt vijf stukjes code. Elk vangt fouten op, en elk doet dat
# verkeerd. Zeg wat er fout is en herstel het.
#
# Let op: deze code draait met opzet niet: opgave van oefening 15.2: vijf fragmenten
# met opzet verkeerde foutafhandeling.

# A
try:
    getal = int("abc")
    resultaat = 100 / getal
    print(resultaat)
except:
    print("er ging iets mis")

# B
def lees_leeftijd(tekst):
    try:
        return int(tekst)
    except ValueError:
        return 0

# C
leden = ["Anke", "Bram"]
try:
    print(leden[5])
except ValueError:
    print("die staat er niet in")

# D
def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass

# E
lid = {"naam": "Anke"}
try:
    naam = lid["naam"]
    leeftijd = lid["leeftijd"]
    print(f"{naam} is {leeftijd}")
except KeyError:
    print("gegevens onvolledig")
