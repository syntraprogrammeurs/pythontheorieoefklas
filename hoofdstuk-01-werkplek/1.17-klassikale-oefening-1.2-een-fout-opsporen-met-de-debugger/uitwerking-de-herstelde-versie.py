# Python basis — theoriebundel
# Hoofdstuk 1 — Je Python-werkplek professioneel opzetten
# Klassikale oefening 1.2 — Een fout opsporen met de debugger, uitwerking
#
# De herstelde versie:

namen = ["Anke", "Bram", "Cato", "Dominique", "Els"]
langste = ""

for naam in namen:
    if len(naam) > len(langste):
        langste = naam

print(f"De langste naam is {langste}")


# Verwachte uitvoer:
# De langste naam is Dominique
