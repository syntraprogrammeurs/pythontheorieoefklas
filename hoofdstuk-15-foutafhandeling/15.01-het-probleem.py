# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.1 Het probleem
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

# Dit voorbeeld wacht op invoer; voer het uit in je eigen terminal.
leeftijd = int(input("Hoe oud ben je? "))
print(f"Je bent {leeftijd} jaar")


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "main.py", line 1, in <module>
#     leeftijd = int(input("Hoe oud ben je? "))
#                ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'abc'
