<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 12.2 — Wat verandert er, en wat niet?

Uit *Python basis — theoriebundel*, hoofdstuk 12 (Lijsten — en waarom Python geen arrays heeft), paragraaf 12.12.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-a-deel-a.py` | uitwerking |  |
| `uitwerking-b-deel-b.py` | uitwerking |  |
| `uitwerking-c-deel-c.py` | uitwerking |  |
| `uitwerking-d-deel-d.py` | uitwerking |  |
| `uitwerking-e-deel-e.py` | uitwerking |  |
| `uitwerking-f-deel-f.py` | uitwerking |  |
| `uitwerking-g-deel-f.py` | uitwerking |  |
| `uitwerking-h-pas-nooit-een-lijst.py` | uitwerking |  |

## Opgave

**De situatie.** Deze oefening bestaat volledig uit voorspellen. Ze bereidt
hoofdstuk 14 voor, waar je de verklaring krijgt.

**Wat je doet.** Voorspel voor elk stukje de uitvoer, schrijf je voorspelling
op, en voer dan pas uit.

```python
# A
lijst = [1, 2, 3]
kopie = lijst
kopie.append(4)
print(lijst)

# B
getal = 5
ander = getal
ander += 1
print(getal)

# C
lijst = [1, 2, 3]
resultaat = lijst.append(4)
print(resultaat)

# D
lijst = [3, 1, 2]
nieuw = sorted(lijst)
lijst.sort()
print(nieuw == lijst)

# E
a = [1, 2]
b = [1, 2]
print(a == b, a is b)

# F
lijst = ["a", "b", "c"]
for x in lijst:
    if x == "b":
        lijst.remove(x)
print(lijst)
```

## Uitwerking

**A.**

```python
lijst = [1, 2, 3]
kopie = lijst
kopie.append(4)
print(lijst)
```

```text
[1, 2, 3, 4]
```

`kopie = lijst` maakt **geen kopie**. Het geeft dezelfde lijst een tweede naam.
Wat je via de ene naam verandert, zie je via de andere. Dit is de belangrijkste
regel van dit hoofdstuk en hoofdstuk 14 legt uit waarom.

**B.**

```python
getal = 5
ander = getal
ander += 1
print(getal)
```

```text
5
```

Bij een getal gebeurt precies wat je verwacht. Waarom het verschil met A? Omdat
een getal **onveranderlijk** is: `ander += 1` maakt een nieuw getal en laat
`ander` daarnaar wijzen. Een lijst is veranderlijk: `append` past het bestaande
object aan.

> De vuistregel: bij `int`, `float`, `str`, `bool` en `tuple` gedraagt een
> tweede naam zich als een kopie. Bij `list`, `dict` en `set` niet.

**C.**

```python
lijst = [1, 2, 3]
resultaat = lijst.append(4)
print(resultaat)
```

```text
None
```

`.append()` past de lijst aan en geeft niets terug. Wie het resultaat toewijst,
is zijn lijst kwijt.

**D.**

```python
lijst = [3, 1, 2]
nieuw = sorted(lijst)
lijst.sort()
print(nieuw == lijst)
```

```text
True
```

`sorted()` maakte een nieuwe gesorteerde lijst; `.sort()` sorteerde het origineel.
Nu bevatten ze allebei `[1, 2, 3]`, dus zijn ze gelijk in **waarde**. Ze zijn
niet hetzelfde object; `nieuw is lijst` zou `False` geven.

**E.**

```python
a = [1, 2]
b = [1, 2]
print(a == b, a is b)
```

```text
True False
```

Dezelfde inhoud, twee verschillende objecten. Dit is het verschil tussen `==` en
`is` uit hoofdstuk 7, nu op lijsten.

**F.**

```python
lijst = ["a", "b", "c"]
for x in lijst:
    if x == "b":
        lijst.remove(x)
print(lijst)
```

```text
['a', 'c']
```

Het antwoord lijkt te kloppen, en dat is precies het gevaar. Kijk wat er
gebeurt bij een lijst met twee opeenvolgende doelwitten:

```python
lijst = ["a", "b", "b", "c"]
for x in lijst:
    if x == "b":
        lijst.remove(x)
print(lijst)
```

```text
['a', 'b', 'c']
```

Er blijft een `b` staan. De lus houdt intern een positie bij. Verwijder je het
element op positie 1, dan schuift alles op, en de lus gaat verder op positie 2.
Het tweede element `b` is dan al voorbijgeschoven.

> **Let op**
>
> **Pas nooit een lijst aan waarover je aan het lopen bent.** Werk in de plaats
> daarvan op een kopie, of bouw een nieuwe lijst:
>
> ```python
> lijst = ["a", "b", "b", "c"]
> lijst = [x for x in lijst if x != "b"]
> print(lijst)
> ```
>
> ```text
> ['a', 'c']
> ```
>
> Die schrijfwijze met de vierkante haken heet een comprehension, en die leer je
> in hoofdstuk 14.

**Wat deze zes voorspellingen je leerden.** Drie ervan gedragen zich anders dan
je op het eerste gezicht zou denken, en alle drie hebben dezelfde oorzaak: een
lijst is één object dat meerdere namen kan hebben, en dat je kunt aanpassen. Dat
is de kern van hoofdstuk 14.
