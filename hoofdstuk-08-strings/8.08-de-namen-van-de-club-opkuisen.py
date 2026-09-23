# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.8 De namen van de club opkuisen

# De Leeslamp — namen opkuisen
# Cursus Python basis, hoofdstuk 8

ruwe_invoer = "  anke peeters ;BRAM coppens;  Cato   Dhondt  "

print("Ruw:", repr(ruwe_invoer))
print()

stukken = ruwe_invoer.split(";") #["anke peeters ", "BRAM coppens", "  Cato   Dhondt  "]

for stuk in stukken:
    naam = stuk.strip()
    naam = " ".join(naam.split())
    voornaam, achternaam = naam.split(" ", 1)
    net = f"{voornaam.capitalize()} {achternaam.capitalize()}"
    initialen = voornaam[0].upper() + achternaam[0].upper()
    print(f"{net:<20}{initialen:<6}{len(net):>3} tekens")


# Verwachte uitvoer:
# Ruw: '  anke peeters ;BRAM coppens;  Cato   Dhondt  '
#
# Anke Peeters        AP     12 tekens
# Bram Coppens        BC     12 tekens
# Cato Dhondt         CD     11 tekens
