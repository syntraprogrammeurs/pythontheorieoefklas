<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 5.2 — Wat gebeurt hier?

Uit *Python basis — theoriebundel*, hoofdstuk 5 (Variabelen, "constanten" en datatypes), paragraaf 5.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |

## Opgave

**De situatie.** Je gaat aan de hand van kleine stukjes code voorspellen wat er
gebeurt. Eerst voorspellen, dan uitvoeren, dan verklaren. Die volgorde is de
oefening.

**Wat je doet.** Voorspel voor elk stukje wat de uitvoer is. Schrijf je
voorspelling op vóór je uitvoert.

```python
# A
a = 5
b = a
a = 10
print(a, b)

# B
print(7 / 2)
print(type(7 / 2))

# C
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)

# D
naam = "Anke"
Naam = "Bram"
print(naam, Naam)

# E
x = None
print(x == None)
print(x is None)
print(x == 0)

# F
aantal = "24"
print(aantal + aantal)
```

## Uitwerking

**A.**

```text
10 5
```

`b = a` kopieert de **waarde** 5, niet de verwijzing naar `a`. Daarna verwijst
`a` naar 10 en `b` nog altijd naar 5. Bij getallen werkt dat zoals je verwacht.

> Onthoud dit antwoord. In hoofdstuk 14 doe je precies hetzelfde met een lijst,
> en dan komt er iets anders uit. Dat is geen inconsequentie van Python, maar
> het verschil tussen veranderlijke en onveranderlijke waarden.

**B.**

```text
3.5
<class 'float'>
```

De gewone deling geeft altijd een `float`, ook bij `10 / 2`, dat `5.0` geeft.
Wie een geheel getal wil, gebruikt `//`.

**C.**

```text
False
True
```

De eerste regel is de valkuil uit 5.7. De tweede werkt omdat `round()` het
resultaat op twee cijfers afrondt, en dan is het precies 0.3.

Toch is dat geen goede oplossing voor het algemene geval. `round()` gebruiken om
te kunnen vergelijken werkt hier toevallig; bij andere getallen gaat het weer
mis. De betrouwbare manier blijft: kijken of het verschil klein genoeg is.

**D.**

```text
Anke Bram
```

Hoofdletters tellen mee. `naam` en `Naam` zijn twee verschillende variabelen.
Dat is technisch correct maar didactisch een ramp: doe dit nooit. Wie dit in
echte code doet, veroorzaakt fouten die niemand ziet.

**E.**

```text
True
True
False
```

De eerste twee geven allebei `True`, en toch schrijf je altijd de tweede.

`==` vraagt: hebben deze twee dezelfde **waarde**? `is` vraagt: zijn dit
**hetzelfde ding** in het geheugen? Van `None` bestaat er in heel Python maar
één exemplaar, dus `is None` is de exacte vraag die je bedoelt. Bovendien kan
`==` door zelfgeschreven types worden overschreven, en `is` niet.

De derde regel is het belangrijkst: `None == 0` is `False`. Geen waarde hebben
is iets anders dan de waarde nul hebben.

**F.**

```text
2424
```

`"24"` is tekst, geen getal. De `+` plakt tekst aan elkaar. Wilde je 48, dan
moet je eerst omzetten: `int(aantal) + int(aantal)`. Dat is hoofdstuk 6.

Dit is meteen de meest voorkomende fout met invoer: alles wat de gebruiker
intypt, komt binnen als tekst. Wie dat vergeet, telt "24" en "18" op tot "2418".

**Wat deze oefening je leert.** Zes keer voorspelde je iets, en minstens één keer
zat je ernaast. Dat is de bedoeling. Een fout voorspelling is waardevoller dan
een juiste: ze wijst precies aan waar je model van de taal niet klopt.
