# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.5 De methodes die je constant gebruikt — Vervangen en splitsen

zin = "appel,peer,kers"

print(zin.replace(",", " en "))     # appel en peer en kers
print(zin.split(","))               # ['appel', 'peer', 'kers']
print("een twee drie".split())      # ['een', 'twee', 'drie']  — splitst op spaties
print("-".join(["a", "b", "c"]))    # a-b-c


# Verwachte uitvoer:
# appel en peer en kers
# ['appel', 'peer', 'kers']
# ['een', 'twee', 'drie']
# a-b-c
