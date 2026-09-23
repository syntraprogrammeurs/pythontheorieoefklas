<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 7.1 — De waarheidstabel van de club

Uit *Python basis — theoriebundel*, hoofdstuk 7 (Operatoren, waarheidstabellen en booleaanse logica), paragraaf 7.13.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a-3-en-4-het-programma.py` | uitwerking |  |
| `uitwerking-b-5-de-gewijzigde-regel.py` | uitwerking |  |

## Opgave

**De situatie.** De club heeft een regel voor de gratis extra uitlening: een lid
krijgt er één als het **ofwel** al drie jaar lid is, **ofwel** in het voorbije
jaar meer dan tien boeken las, maar **niet** als allebei waar zijn. Wie aan
beide voldoet, krijgt namelijk al de jaarkorting.

**Wat je doet.**

1. Herken welke logische poort deze regel is.
2. Schrijf de waarheidstabel met de hand, vóór je code schrijft.
3. Schrijf een programma dat de tabel afdrukt voor alle vier de gevallen.
4. Schrijf de regel op drie manieren: met `!=`, met de letterlijke definitie uit
   `and`, `or` en `not`, en met `^`. Toon dat de drie hetzelfde geven.
5. De club verandert de regel: "een extra uitlening krijg je alleen als je
   **noch** drie jaar lid bent **noch** meer dan tien boeken las". Welke poort
   is dat, en hoe schrijf je ze?

## Uitwerking

**1 — De poort.**

"Ofwel het een, ofwel het ander, maar niet allebei" is **XOR**, de exclusieve
of. De aanwijzing zit in het woordje "niet als allebei": dat is precies wat XOR
onderscheidt van een gewone OR.

**2 — De waarheidstabel.**

| Drie jaar lid | Meer dan tien boeken | Extra uitlening |
|---|---|---|
| nee | nee | nee |
| nee | ja | **ja** |
| ja | nee | **ja** |
| ja | ja | nee |

**3 en 4 — Het programma.**

```python
# De Leeslamp — wie krijgt een gratis extra uitlening?
# Cursus Python basis, hoofdstuk 7, oefening 1

print(f"{'3 jaar':<8}{'>10 boeken':<12}{'!=':<7}{'and/or/not':<12}{'^':<7}")
print("-" * 46)

for drie_jaar in (False, True):
    for veel_gelezen in (False, True):
        met_ongelijk = drie_jaar != veel_gelezen
        met_woorden = (drie_jaar or veel_gelezen) and not (drie_jaar and veel_gelezen)
        met_dakje = bool(drie_jaar ^ veel_gelezen)

        print(f"{drie_jaar!s:<8}{veel_gelezen!s:<12}"
              f"{met_ongelijk!s:<7}{met_woorden!s:<12}{met_dakje!s:<7}")
```

```text
3 jaar  >10 boeken  !=     and/or/not  ^      
----------------------------------------------
False   False       False  False       False  
False   True        True   True        True   
True    False       True   True        True   
True    True        False  False       False  
```

De drie kolommen zijn identiek. De drie schrijfwijzen zijn dus gelijkwaardig.

**Welke gebruik je?** `!=`. Ze is de kortste, ze werkt zonder omzetting, en elke
Python-programmeur leest ze meteen. De middelste is nuttig om te **begrijpen**
wat XOR is; de laatste is bedoeld voor bits en werkt hier alleen omdat booleans
in Python getallen zijn.

**5 — De gewijzigde regel.**

"Noch het een, noch het ander" is **NOR**: waar alleen wanneer beide onwaar zijn.

```python
for drie_jaar in (False, True):
    for veel_gelezen in (False, True):
        nor_1 = not (drie_jaar or veel_gelezen)
        nor_2 = (not drie_jaar) and (not veel_gelezen)
        print(f"{drie_jaar!s:<8}{veel_gelezen!s:<8}{nor_1!s:<8}{nor_2!s:<8}")
```

```text
False   False   True    True    
False   True    False   False   
True    False   False   False   
True    True    False   False   
```

De twee kolommen zijn gelijk, en dat is De Morgan uit 7.6: de ontkenning van een
`or` wordt een `and` van ontkenningen.

**Welke van de twee schrijf je?** `not (a or b)`. Die leest als de zin uit het
reglement: "niet het een of het ander". De vorm met twee ontkenningen is
technisch identiek maar vraagt meer denkwerk van de lezer.

**Een opmerking bij de regel zelf.** Deze nieuwe regel is didactisch een mooi
NOR-voorbeeld, maar hij is inhoudelijk vreemd: hij beloont juist de leden die
niets deden. Wanneer je in de praktijk een regel uitschrijft en de logica klopt
maar het resultaat is onzinnig, ligt de fout meestal niet in je code maar in de
opdracht. Zeg dat dan.
