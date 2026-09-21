# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.6 Uitlijnen en opvullen

print("Boek".ljust(20, ".") + "24.95")
print("Totaal".rjust(20) + " 24.95")
print("De Leeslamp".center(30, "-"))
print("7".zfill(3))


# Verwachte uitvoer:
# Boek................24.95
#               Totaal 24.95
# ---------De Leeslamp----------
# 007
