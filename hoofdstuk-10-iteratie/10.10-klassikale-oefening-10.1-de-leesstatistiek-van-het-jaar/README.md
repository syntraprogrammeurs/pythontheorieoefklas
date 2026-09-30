<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 10.1 — De leesstatistiek van het jaar

Uit *Python basis — theoriebundel*, hoofdstuk 10 (Iteratie: `while`, `for`, `range`, `break` en `continue`), paragraaf 10.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-wat-je-in-de-praktijk-zou.py` | uitwerking |  |

## Opgave

**De situatie.** De club heeft de bladzijden van de twaalf boeken van het
voorbije jaar. Je maakt er een overzicht van.

```python
bladzijden = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]
```

**Wat je maakt.** Een programma dat toont:

1. Elk boek genummerd, met het aantal bladzijden.
2. Het totaal.
3. Het gemiddelde, op één cijfer.
4. Het dikste en het dunste boek, met hun nummer.
5. Hoeveel boeken boven het gemiddelde zitten.
6. Een staafdiagram met sterretjes, één sterretje per vijftig bladzijden.

Schrijf punt 2 tot en met 5 met lussen, niet met `sum()`, `max()` en `min()`.
Die bestaan wel, maar je oefent het patroon.

## Uitwerking

```python
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
```

```text
Boek   Bladzijden
--------------------
   1      320
   2      180
   3      250
   4      410
   5       96
   6      512
   7      288
   8      175
   9      640
  10      205
  11      330
  12      148

Totaal            : 3554
Gemiddelde        : 296.2
Dikste            : boek 9, 640 bladzijden
Dunste            : boek 5, 96 bladzijden
Boven gemiddelde  : 5 van de 12

Staafdiagram, één ster per 50 bladzijden
  1 ******         320
  2 ***            180
  3 *****          250
  4 ********       410
  5 *               96
  6 **********     512
  7 *****          288
  8 ***            175
  9 ************   640
 10 ****           205
 11 ******         330
 12 **             148
```

**De vier dingen waar het om ging.**

**De beginwaarde van het maximum.** `dikste = bladzijden[0]` en niet `dikste = 0`.
Met nul beginnen werkt hier, want alle boeken hebben meer dan nul bladzijden.
Maar het is een aanname die je nergens opschreef, en die bij het eerstvolgende
programma met negatieve getallen stilletjes fout gaat.

**Het nummer meenemen.** Het maximum vinden is eenvoudig; weten *welk* boek het
is, vraagt dat je bij elke vervanging ook het nummer bijhoudt. Vergeet je die
regel, dan krijg je het juiste aantal met het verkeerde nummer, en dat merk je
niet.

**Het gemiddelde vóór de telling.** Je kunt pas tellen hoeveel boeken boven het
gemiddelde zitten nadat je het gemiddelde kent. Dat betekent **twee** lussen
over dezelfde lijst. Dat is geen verspilling: het is de enige manier. Wie het in
één lus probeert, vergelijkt met een gemiddelde dat nog niet af is.

**De gehele deling voor het staafdiagram.** `aantal // 50` geeft het aantal
volledige sterretjes. Met `/` zou je `6.4` sterretjes krijgen, en `"*" * 6.4`
geeft een `TypeError`. Dit is een van de weinige plaatsen waar `//` echt
onmisbaar is.

**Wat je in de praktijk zou schrijven.** De ingebouwde functies:

```python
bladzijden = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]

totaal = sum(bladzijden)
gemiddelde = totaal / len(bladzijden)
dikste = max(bladzijden)
dunste = min(bladzijden)
dikste_nr = bladzijden.index(dikste) + 1

print(totaal, f"{gemiddelde:.1f}", dikste, dunste, dikste_nr)
```

```text
3554 296.2 640 96 9
```

Vijf regels in plaats van vijfentwintig. Schrijf dit in een echt project. Het
patroon met de lus moet je kennen omdat je het nodig hebt zodra de berekening
niet in een ingebouwde functie past.
