# Python basis — theoriebundel
# Hoofdstuk 5 — Variabelen, "constanten" en datatypes
# 5.9 De gegevens van een lid
#
# Zet dit in main.py:

# De Leeslamp — gegevens van één lid
# Cursus Python basis, hoofdstuk 5

# Constanten: de afspraken van de club
LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
MAX_LEDEN = 50

# De gegevens van dit lid
naam = "Anke Peeters"
leeftijd = 34
is_student = False
jaren_lid = 3
laatst_geleend = None

print("Naam:", naam)
print("Leeftijd:", leeftijd)
print("Student:", is_student)
print("Jaren lid:", jaren_lid)
print("Laatst geleend:", laatst_geleend)

print("Types:", type(naam), type(leeftijd), type(is_student))


# Verwachte uitvoer:
# Naam: Anke Peeters
# Leeftijd: 34
# Student: False
# Jaren lid: 3
# Laatst geleend: None
# Types: <class 'str'> <class 'int'> <class 'bool'>
