<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 6.1 — De leestijd omrekenen

Uit *Python basis — theoriebundel*, hoofdstuk 6 (Getallen, casting, invoer en uitvoer), paragraaf 6.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking | vraagt invoer |
| `uitwerking-b-naar-boven-afronden.py` | uitwerking | bouwt verder op `uitwerking-a.py`, vraagt invoer |
| `uitwerking-c-naar-boven-afronden.py` | uitwerking | bouwt verder op `uitwerking-a.py`, vraagt invoer |

## Opgave

**De situatie.** De club wil weten hoe lang een boek ongeveer duurt om te lezen.
Gemiddeld leest een lid 250 woorden per minuut, en een gemiddelde bladzijde
telt 300 woorden.

**Wat je maakt.** Een programma dat vraagt hoeveel bladzijden een boek telt, en
dan toont:

1. Het totale aantal woorden.
2. De leestijd in minuten, afgerond op één cijfer.
3. Diezelfde leestijd in uren en minuten, netjes gescheiden.
4. Hoeveel dagen dat is als het lid 20 minuten per dag leest, naar boven
   afgerond op een heel aantal dagen.

Gebruik constanten voor de drie gemiddelden. Gebruik f-strings met opmaak.

> **Controle**
>
> Voor 400 bladzijden moet er 8 uur en 0 minuten uitkomen, en 24 dagen.

## Uitwerking

```python
# De Leeslamp — de leestijd van een boek schatten
# Cursus Python basis, hoofdstuk 6, oefening 1

WOORDEN_PER_BLADZIJDE = 300
WOORDEN_PER_MINUUT = 250
MINUTEN_PER_DAG = 20

bladzijden = int(input("Hoeveel bladzijden telt het boek? "))

woorden = bladzijden * WOORDEN_PER_BLADZIJDE
minuten = woorden / WOORDEN_PER_MINUUT

uren = int(minuten) // 60
rest_minuten = int(minuten) % 60

dagen = minuten / MINUTEN_PER_DAG
hele_dagen = int(dagen)
if dagen > hele_dagen:
    hele_dagen = hele_dagen + 1

print()
print(f"Bladzijden : {bladzijden}")
print(f"Woorden    : {woorden:,}")
print(f"Leestijd   : {minuten:.1f} minuten")
print(f"Dat is     : {uren} uur en {rest_minuten} minuten")
print(f"Bij {MINUTEN_PER_DAG} min/dag: {hele_dagen} dagen")
```

```text
Hoeveel bladzijden telt het boek? 400

Bladzijden : 400
Woorden    : 120,000
Leestijd   : 480.0 minuten
Dat is     : 8 uur en 0 minuten
Bij 20 min/dag: 24 dagen
```

**Waar het om draaide.**

**Het paar `//` en `%`.** 480 minuten omzetten naar uren en minuten is precies
het patroon uit 6.1: `480 // 60` geeft 8 uur, `480 % 60` geeft 0 minuten. Dit
patroon gebruik je de rest van je loopbaan, voor tijd, geld en afmetingen.

**Naar boven afronden.** `round()` rondt naar het dichtstbijzijnde getal, en dat
is hier fout: 23,4 dagen betekent dat je op dag 24 nog leest, dus 24 dagen. De
truc hierboven werkt, maar het kan korter:

```python
import math
hele_dagen = math.ceil(dagen)
```

Of, zonder import, met een bekende rekenkundige truc:

```python
hele_dagen = -(-int(minuten) // MINUTEN_PER_DAG)
```

Die laatste ziet er raar uit en is precies daarom geen goede code: hij werkt,
maar niemand leest hem. Gebruik `math.ceil()`. Je leert `import` in
hoofdstuk 17.

**Waarom `int(minuten)` vóór `//`?** Omdat `minuten` een `float` is en `//` op
een `float` ook een `float` teruggeeft: `480.0 // 60` geeft `8.0`, en dan toont
je programma "8.0 uur en 0.0 minuten". Door eerst naar `int` om te zetten, houd
je gehele getallen. Dat is een keuze die je bewust maakt, niet iets dat vanzelf
goed gaat.

**Waarom de constanten bovenaan?** Verandert de leessnelheid, dan pas je één
regel aan. Bovendien legt `WOORDEN_PER_MINUUT` uit wat 250 betekent; het losse
getal 250 halverwege een berekening zou dat niet doen.
