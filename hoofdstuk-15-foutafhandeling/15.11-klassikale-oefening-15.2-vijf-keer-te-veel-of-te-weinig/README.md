<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen

Uit *Python basis — theoriebundel*, hoofdstuk 15 (Foutafhandeling met `try` en `except`), paragraaf 15.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave | draait met opzet niet |
| `uitwerking-a-deel-a-een-kale-except.py` | uitwerking |  |
| `uitwerking-b-deel-a-een-kale-except.py` | uitwerking |  |
| `uitwerking-c-deel-b-een-fout-wegmoffelen.py` | uitwerking |  |
| `uitwerking-d-deel-b-een-fout-wegmoffelen.py` | uitwerking |  |
| `uitwerking-e-deel-c-de-verkeerde-foutsoort.py` | uitwerking | loopt met opzet vast |
| `uitwerking-f-deel-c-de-verkeerde-foutsoort.py` | uitwerking |  |
| `uitwerking-g-deel-d-pass-maakt-de-fout.py` | uitwerking |  |
| `uitwerking-h-deel-d-pass-maakt-de-fout.py` | uitwerking |  |
| `uitwerking-i-deel-e-een-try-blok.py` | uitwerking |  |
| `uitwerking-j-deel-e-een-try-blok.py` | uitwerking |  |

## Opgave

**De situatie.** Je krijgt vijf stukjes code. Elk vangt fouten op, en elk doet
dat verkeerd. Zeg wat er fout is en herstel het.

```python
# A
try:
    getal = int("abc")
    resultaat = 100 / getal
    print(resultaat)
except:
    print("er ging iets mis")

# B
def lees_leeftijd(tekst):
    try:
        return int(tekst)
    except ValueError:
        return 0

# C
leden = ["Anke", "Bram"]
try:
    print(leden[5])
except ValueError:
    print("die staat er niet in")

# D
def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass

# E
lid = {"naam": "Anke"}
try:
    naam = lid["naam"]
    leeftijd = lid["leeftijd"]
    print(f"{naam} is {leeftijd}")
except KeyError:
    print("gegevens onvolledig")
```

## Uitwerking

**A — een kale `except` verbergt alles.**

```python
try:
    getal = int("abc")
    resultaat = 100 / getal
    print(resultaat)
except:
    print("er ging iets mis")
```

```text
er ging iets mis
```

Twee problemen. De kale `except` vangt ook fouten op die je niet verwachtte, en
de boodschap vertelt niets. Bovendien kunnen er hier **twee** verschillende
dingen misgaan, en je weet niet welk.

```python
try:
    getal = int("abc")
except ValueError:
    print("dat is geen geldig getal")
else:
    try:
        print(100 / getal)
    except ZeroDivisionError:
        print("het getal was nul, delen kan niet")
```

```text
dat is geen geldig getal
```

**B — een fout wegmoffelen als geldige waarde.**

```python
def lees_leeftijd(tekst):
    try:
        return int(tekst)
    except ValueError:
        return 0


print(lees_leeftijd("abc"))
print(lees_leeftijd("0"))
```

```text
0
0
```

Dit is de gevaarlijkste van de vijf. `"abc"` en `"0"` geven allebei nul, en de
aanroeper kan de twee niet uit elkaar houden. Een niet-ingevulde leeftijd wordt
zo stilletjes nul jaar, en dat lid krijgt gratis lidmaatschap.

Twee juiste vormen:

```python
def lees_leeftijd(tekst: str) -> int | None:
    """Het getal, of None wanneer de tekst geen getal is."""
    try:
        return int(tekst)
    except ValueError:
        return None


print(lees_leeftijd("abc"))
print(lees_leeftijd("0"))
```

```text
None
0
```

Of, wanneer de aanroeper moet beslissen: vang niets op en laat de `ValueError`
door. Beide zijn goed. Nul teruggeven is dat niet.

**C — de verkeerde foutsoort.**

```python
leden = ["Anke", "Bram"]
try:
    print(leden[5])
except ValueError:
    print("die staat er niet in")
```

```text
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    print(leden[5])
          ~~~~~^^^
IndexError: list index out of range
```

Het programma crasht alsnog: een positie buiten de lijst geeft een `IndexError`,
geen `ValueError`. De `except` staat er voor niets.

```python
leden = ["Anke", "Bram"]
try:
    print(leden[5])
except IndexError:
    print("die staat er niet in")
```

```text
die staat er niet in
```

> De les: schrijf nooit een `except` op goed geluk. Veroorzaak de fout één keer
> bewust, lees de laatste regel van de traceback, en gebruik precies die naam.

**D — `pass` maakt de fout onzichtbaar.**

```python
def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass


print(deel(10, 2))
print(deel(10, 0))
```

```text
5.0
None
```

De tweede aanroep geeft `None`, zonder dat iemand het weet. Reken je daarmee
verder, dan krijg je een `TypeError` ergens anders in je programma, en zoek je
de fout op de verkeerde plaats.

`pass` in een `except` is bijna altijd fout. Kies er één van:

```python
def deel(a: float, b: float) -> float | None:
    """Deelt a door b. Geeft None wanneer b nul is."""
    if b == 0:
        return None
    return a / b


print(deel(10, 0))
```

```text
None
```

Of laat de fout gewoon door en documenteer dat in je docstring. Wat je niet
doet, is hem opvangen en negeren.

**E — een `try`-blok dat te veel omvat.**

```python
lid = {"naam": "Anke"}
try:
    naam = lid["naam"]
    leeftijd = lid["leeftijd"]
    print(f"{naam} is {leeftijd}")
except KeyError:
    print("gegevens onvolledig")
```

```text
gegevens onvolledig
```

Het antwoord klopt toevallig, maar het `try`-blok vangt twee opzoekingen én de
`print` op. Ontbreekt straks de naam in plaats van de leeftijd, dan krijg je
dezelfde boodschap en weet je niet welk veld ontbrak.

```python
lid = {"naam": "Anke"}

naam = lid.get("naam", "onbekend")
leeftijd = lid.get("leeftijd")

if leeftijd is None:
    print(f"{naam}: leeftijd niet ingevuld")
else:
    print(f"{naam} is {leeftijd}")
```

```text
Anke: leeftijd niet ingevuld
```

Hier is helemaal geen `try` nodig. Dat is de eerste vraag die je jezelf stelt:
**kan ik dit voorkomen in plaats van opvangen?** Bij een dictionary is het
antwoord meestal ja, met `.get()`.

**De vijf lessen samen.**

| Fout | Regel |
|---|---|
| A | Vang de soorten op die je verwacht, nooit alles |
| B | Geef geen geldig ogende waarde terug voor een fout |
| C | Gebruik de foutsoort die echt optreedt |
| D | `pass` in een `except` verbergt het probleem |
| E | Houd het `try`-blok bij de regel die kan mislukken |
