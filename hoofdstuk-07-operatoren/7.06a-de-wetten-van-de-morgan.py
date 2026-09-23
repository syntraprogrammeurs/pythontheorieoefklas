# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.6 De wetten van De Morgan
#
# Waarom dat nuttig is:

leeftijd = 30
is_lid = True

# moeilijk te lezen
if not (leeftijd >= 18 and is_lid):
    print("Mag niet lenen")

# na De Morgan: even waar, veel duidelijker
if leeftijd < 18 or not is_lid:
    print("Mag niet lenen")
