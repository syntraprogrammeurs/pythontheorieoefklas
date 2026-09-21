<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 8.2 — Een zin ontleden

Uit *Python basis — theoriebundel*, hoofdstuk 8 (Strings), paragraaf 8.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-de-tekst-over-twee-regels.py` | uitwerking |  |

## Opgave

**De situatie.** De club wil van elk leesverslag een paar kengetallen. Je
schrijft de analyse voor één alinea.

**Wat je doet.** Neem deze tekst:

```text
Het boek gaat over twee families. Het verhaal speelt zich af in Nederland.
De schrijfstijl is vlot maar het einde stelt teleur.
```

Toon:

1. Het aantal tekens, met en zonder spaties.
2. Het aantal woorden.
3. Het aantal zinnen.
4. De gemiddelde woordlengte, op één cijfer.
5. Het langste woord.
6. Hoe vaak het woord `het` voorkomt, ongeacht hoofdletters.
7. De tekst achterstevoren, alleen de eerste veertig tekens.

## Uitwerking

```python
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
```

```text
Tekens met spaties    : 127
Tekens zonder spaties : 106
Woorden               : 22
Zinnen                : 3
Gemiddelde woordlengte: 4.7
Langste woord         : schrijfstijl
Het woord 'het'       : 3 keer
Achterstevoren        : .ruelet tlets ednie teh raam tolv si lji
```

**De vier valkuilen, en hoe je ze omzeilt.**

**Leestekens plakken aan woorden.** `tekst.split()` geeft `families.` mét punt.
Dat vervalst je woordlengte en je telling. `woord.strip(".,;:!?")` haalt alle
genoemde tekens links en rechts weg. Merk op dat `.strip()` met een argument
niet die hele reeks zoekt, maar **elk teken uit die reeks** afknabbelt tot er
iets anders staat.

**Hoofdletters bij het tellen.** Er staan twee keer `Het` met een hoofdletter en
één keer `het` zonder. Zonder `.lower()` tel je er één in plaats van drie.

**Zinnen tellen met punten.** `tekst.count(".")` werkt hier, maar het is een
benadering. Bij `dhr. Mulisch` of `1992.` telt hij te veel, en bij een zin die
eindigt op een vraagteken telt hij te weinig. Voor echte tekstanalyse gebruik je
een taalbibliotheek. Weet dat je hier een aanname doet, en schrijf dat erbij.

**Twee snijbewerkingen na elkaar.** `tekst[::-1][:40]` draait eerst om en neemt
dan de eerste veertig van het omgekeerde. Dat is iets anders dan
`tekst[:40][::-1]`, wat de laatste veertig van het begin omgekeerd geeft. Lees
zulke ketens altijd van links naar rechts.

**De tekst over twee regels.** In de code staat de tekst als twee stukken tussen
haakjes, zonder `+`:

```python
tekst = ("eerste stuk "
         "tweede stuk")
```

Python plakt twee strings die naast elkaar staan vanzelf aan elkaar. Dat is de
nette manier om een lange tekst binnen je regellengte te houden. Let op de
spatie op het einde van het eerste stuk: die vergeten is de meest gemaakte fout
bij deze schrijfwijze.
