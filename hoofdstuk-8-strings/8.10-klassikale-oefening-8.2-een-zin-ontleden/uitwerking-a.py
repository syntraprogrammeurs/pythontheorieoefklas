# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# Klassikale oefening 8.2 — Een zin ontleden, uitwerking

# De Leeslamp — een leesverslag ontleden
# Cursus Python basis, hoofdstuk 8, oefening 2

tekst = ("Het boek gaat over twee families. Het verhaal speelt zich af in "
         "Nederland. De schrijfstijl is vlot maar het einde stelt teleur.")

woorden = tekst.split()
zonder_spaties = tekst.replace(" ", "")
aantal_zinnen = tekst.count(".")

totale_lengte = 0
langste = ""
aantal_het = 0

for woord in woorden:
    kaal = woord.strip(".,;:!?")
    totale_lengte += len(kaal)
    if len(kaal) > len(langste):
        langste = kaal
    if kaal.lower() == "het":
        aantal_het += 1

gemiddelde = totale_lengte / len(woorden)

print(f"Tekens met spaties    : {len(tekst)}")
print(f"Tekens zonder spaties : {len(zonder_spaties)}")
print(f"Woorden               : {len(woorden)}")
print(f"Zinnen                : {aantal_zinnen}")
print(f"Gemiddelde woordlengte: {gemiddelde:.1f}")
print(f"Langste woord         : {langste}")
print(f"Het woord 'het'       : {aantal_het} keer")
print(f"Achterstevoren        : {tekst[::-1][:40]}")


# Verwachte uitvoer:
# Tekens met spaties    : 127
# Tekens zonder spaties : 106
# Woorden               : 22
# Zinnen                : 3
# Gemiddelde woordlengte: 4.7
# Langste woord         : schrijfstijl
# Het woord 'het'       : 3 keer
# Achterstevoren        : .ruelet tlets ednie teh raam tolv si lji
