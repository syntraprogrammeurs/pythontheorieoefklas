# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# Klassikale oefening 6.2 — De kassabon van de boekenverkoop, uitwerking
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# De Leeslamp — kassabon van de boekenverkoop
# Cursus Python basis, hoofdstuk 6, oefening 2

KORTINGSPERCENTAGE = 0.10
BILJET = 50
BREEDTE = 32

koper = input("Naam van de koper: ")
aantal = int(input("Aantal boeken: "))
prijs_per_stuk = float(input("Prijs per boek in euro: "))

subtotaal = aantal * prijs_per_stuk
korting = subtotaal * KORTINGSPERCENTAGE
te_betalen = subtotaal - korting
wisselgeld = BILJET - te_betalen

print()
print("=" * BREEDTE)
print(f"{'BOEKENCLUB DE LEESLAMP':^{BREEDTE}}")
print(f"{'rommelmarkt':^{BREEDTE}}")
print("=" * BREEDTE)
print(f"Koper: {koper}")
print("-" * BREEDTE)
print(f"{'Boeken':<16}{aantal:>4} x{prijs_per_stuk:>10.2f}")
print(f"{'Subtotaal':<22}{subtotaal:>10.2f}")
print(f"{'Ledenkorting':<12}{KORTINGSPERCENTAGE:>9.0%}{-korting:>11.2f}")
print("-" * BREEDTE)
print(f"{'TE BETALEN':<22}{te_betalen:>10.2f}")
print(f"{'Gegeven':<22}{BILJET:>10.2f}")
print(f"{'Wisselgeld':<22}{wisselgeld:>10.2f}")
print("=" * BREEDTE)


# Voorbeeld van een uitvoering, met de invoer erbij:
# Naam van de koper: Bram Coppens
# Aantal boeken: 4
# Prijs per boek in euro: 6.50
#
# ================================
#      BOEKENCLUB DE LEESLAMP
#           rommelmarkt
# ================================
# Koper: Bram Coppens
# --------------------------------
# Boeken             4 x      6.50
# Subtotaal                  26.00
# Ledenkorting      10%      -2.60
# --------------------------------
# TE BETALEN                 23.40
# Gegeven                    50.00
# Wisselgeld                 26.60
# ================================
