# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Klassikale oefening 10.1 — De leesstatistiek van het jaar, uitwerking

# De Leeslamp — leesstatistiek van het jaar
# Cursus Python basis, hoofdstuk 10, oefening 1

BLADZIJDEN_PER_STER = 50

bladzijden = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]

# 1 — de lijst
print("Boek   Bladzijden")
print("-" * 20)
for nummer, aantal in enumerate(bladzijden, start=1):
    print(f"{nummer:>4}   {aantal:>6}")

# 2 — het totaal
totaal = 0
for aantal in bladzijden:
    totaal += aantal

# 3 — het gemiddelde
gemiddelde = totaal / len(bladzijden)

# 4 — het dikste en het dunste
dikste = bladzijden[0]
dikste_nr = 1
dunste = bladzijden[0]
dunste_nr = 1

for nummer, aantal in enumerate(bladzijden, start=1):
    if aantal > dikste:
        dikste = aantal
        dikste_nr = nummer
    if aantal < dunste:
        dunste = aantal
        dunste_nr = nummer

# 5 — boven het gemiddelde
boven = 0
for aantal in bladzijden:
    if aantal > gemiddelde:
        boven += 1

print()
print(f"Totaal            : {totaal}")
print(f"Gemiddelde        : {gemiddelde:.1f}")
print(f"Dikste            : boek {dikste_nr}, {dikste} bladzijden")
print(f"Dunste            : boek {dunste_nr}, {dunste} bladzijden")
print(f"Boven gemiddelde  : {boven} van de {len(bladzijden)}")

# 6 — het staafdiagram
print()
print("Staafdiagram, één ster per 50 bladzijden")
for nummer, aantal in enumerate(bladzijden, start=1):
    sterren = "*" * (aantal // BLADZIJDEN_PER_STER)
    print(f"{nummer:>3} {sterren:<14}{aantal:>4}")


# Verwachte uitvoer:
# Boek   Bladzijden
# --------------------
#    1      320
#    2      180
#    3      250
#    4      410
#    5       96
#    6      512
#    7      288
#    8      175
#    9      640
#   10      205
#   11      330
#   12      148
#
# Totaal            : 3554
# Gemiddelde        : 296.2
# Dikste            : boek 9, 640 bladzijden
# Dunste            : boek 5, 96 bladzijden
# Boven gemiddelde  : 5 van de 12
#
# Staafdiagram, één ster per 50 bladzijden
#   1 ******         320
#   2 ***            180
#   3 *****          250
#   4 ********       410
#   5 *               96
#   6 **********     512
#   7 *****          288
#   8 ***            175
#   9 ************   640
#  10 ****           205
#  11 ******         330
#  12 **             148
