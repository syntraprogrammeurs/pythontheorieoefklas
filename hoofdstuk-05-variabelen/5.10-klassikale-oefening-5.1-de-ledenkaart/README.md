# Klassikale oefening 5.1 — De ledenkaart

Uit *Python basis — theoriebundel*, hoofdstuk 5 (Variabelen, "constanten" en datatypes), paragraaf 5.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-waarom-bool-en-niet-tekst.py` | uitwerking |  |

## Opgave

**De situatie.** De club wil de gegevens van een lid netjes op één plaats
bijhouden. Jij zet de variabelen op.

**Wat je doet.** Schrijf een programma met:

1. Vier constanten: het lidgeld voor volwassenen (30), voor studenten (15), de
   leeftijdsgrens voor gratis lidmaatschap (12), en het aantal jaren dat je lid
   moet zijn voor korting (3).
2. Zes variabelen voor één lid: naam, leeftijd, of het lid student is, het
   aantal jaren lidmaatschap, het aantal geleende boeken, en het boek dat het
   lid nu leest. Dat laatste is nog niet ingevuld.
3. Een regel die van elk van die zes het type toont.
4. Een lijstje met per variabele: welk type je koos en waarom je dat type koos
   en geen ander.

> **Controle**
>
> Test jezelf voor je verder leest: welk type kies je voor "aantal geleende
> boeken", en waarom is `float` daar fout?

## Uitwerking

```python
# De Leeslamp — de ledenkaart
# Cursus Python basis, hoofdstuk 5, oefening 1

# --- constanten: de afspraken van de club --------------------------------
LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3

# --- de gegevens van dit lid ---------------------------------------------
naam = "Anke Peeters"
leeftijd = 34
is_student = False
jaren_lid = 3
aantal_geleend = 7
huidig_boek = None

print("Naam:", naam, type(naam))
print("Leeftijd:", leeftijd, type(leeftijd))
print("Student:", is_student, type(is_student))
print("Jaren lid:", jaren_lid, type(jaren_lid))
print("Geleend:", aantal_geleend, type(aantal_geleend))
print("Huidig boek:", huidig_boek, type(huidig_boek))
```

```text
Naam: Anke Peeters <class 'str'>
Leeftijd: 34 <class 'int'>
Student: False <class 'bool'>
Jaren lid: 3 <class 'int'>
Geleend: 7 <class 'int'>
Huidig boek: None <class 'NoneType'>
```

**De verantwoording van de types:**

| Variabele | Type | Waarom, en waarom niet anders |
|---|---|---|
| `naam` | `str` | Tekst. Ook een naam die uit cijfers zou bestaan, blijft tekst: je rekent er niet mee |
| `leeftijd` | `int` | Je telt in hele jaren. `float` zou 34,5 jaar toelaten, en dat gebruikt de club niet |
| `is_student` | `bool` | Er zijn precies twee mogelijkheden. Met `"ja"` en `"nee"` als tekst zou je moeten opletten voor `"Ja"`, `"JA"` en `"j"` |
| `jaren_lid` | `int` | Hele jaren, net als de leeftijd |
| `aantal_geleend` | `int` | Je kunt geen half boek lenen. `float` is hier niet fout maar onzinnig, en zou `3.5 boeken` mogelijk maken |
| `huidig_boek` | `NoneType`, later `str` | Er is nu geen boek. `""` zou betekenen "een boek zonder titel", en `0` slaat nergens op |

**Waarom `float` voor het aantal boeken fout is.** Niet omdat Python het weigert
— dat doet het niet. Wel omdat je type een **belofte** is over wat er kan
gebeuren. `float` belooft: hier kan een half boek in. Dat kan niet, dus die
belofte is fout, en een latere lezer moet zich afvragen waarom jij dacht van
wel. Kies het type dat de werkelijkheid beschrijft.

**Waarom `bool` en niet tekst.** Vergelijk:

```python
is_student = False                  # één van twee mogelijkheden
is_student = "nee"                  # één van oneindig veel mogelijkheden
```

Met tekst moet je later `if is_student == "nee"` schrijven, en dan werkt het
niet bij `"Nee"`, `"NEE"`, `"neen"` of `"n"`. Met een `bool` schrijf je gewoon
`if is_student:` en er bestaat geen derde geval.

**Constanten of niet?** `LIDGELD_VOLWASSENE` is een constante: dat is een
afspraak van de club, geldig voor iedereen. `leeftijd` is een variabele: die
verschilt per lid en verandert elk jaar. De vraag die je jezelf stelt: hoort
deze waarde bij het **programma** of bij dit **geval**?
