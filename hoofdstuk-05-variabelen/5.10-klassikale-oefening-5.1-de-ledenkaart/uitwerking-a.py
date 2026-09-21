# Python basis — theoriebundel
# Hoofdstuk 5 — Variabelen, "constanten" en datatypes
# Klassikale oefening 5.1 — De ledenkaart, uitwerking

# De Leeslamp — de ledenkaart
# Cursus Python basis, hoofdstuk 5, oefening 1

# --- constanten: de afspraken van de club --------------------------------
LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3

# --- de gegevens van dit lid ---------------------------------------------
naam = "Anke Peeters"
leeftijd = 34
is_student = False
jaren_lid = 3
aantal_geleend = 7
huidig_boek = None

print("Naam:", naam, type(naam))
print("Leeftijd:", leeftijd, type(leeftijd))
print("Student:", is_student, type(is_student))
print("Jaren lid:", jaren_lid, type(jaren_lid))
print("Geleend:", aantal_geleend, type(aantal_geleend))
print("Huidig boek:", huidig_boek, type(huidig_boek))


# Verwachte uitvoer:
# Naam: Anke Peeters <class 'str'>
# Leeftijd: 34 <class 'int'>
# Student: False <class 'bool'>
# Jaren lid: 3 <class 'int'>
# Geleend: 7 <class 'int'>
# Huidig boek: None <class 'NoneType'>
