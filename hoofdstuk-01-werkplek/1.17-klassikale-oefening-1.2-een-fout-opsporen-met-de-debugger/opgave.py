# Python basis — theoriebundel
# Hoofdstuk 1 — Je Python-werkplek professioneel opzetten
# Klassikale oefening 1.2 — Een fout opsporen met de debugger, opgave
#
# De situatie. Een medecursist stuurt je dit programma. Het zou de langste naam uit de
# lijst moeten tonen, maar het toont Bram.

namen = ["Anke", "Bram", "Cato", "Dominique", "Els"]
langste = ""

for naam in namen:
    if len(naam) > len(langste):
        langste = naam
        break

print(f"De langste naam is {langste}")
