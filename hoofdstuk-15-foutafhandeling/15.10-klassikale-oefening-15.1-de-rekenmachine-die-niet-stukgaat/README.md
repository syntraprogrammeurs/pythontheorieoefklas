<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 15.1 — De rekenmachine die niet stukgaat

Uit *Python basis — theoriebundel*, hoofdstuk 15 (Foutafhandeling met `try` en `except`), paragraaf 15.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** Je maakt een kleine rekenmachine voor de penningmeester van de
club. Ze moet elke denkbare invoer overleven.

**Wat je maakt.** Een functie `reken(links, teken, rechts)` waarbij alle drie de
argumenten **tekst** zijn, zoals ze van de gebruiker komen. De functie geeft het
resultaat terug, of een duidelijke boodschap.

Ze moet correct omgaan met:

1. Gewone berekeningen met `+`, `-`, `*`, `/`.
2. Getallen met een komma in plaats van een punt.
3. Spaties rond de invoer.
4. Iets dat geen getal is.
5. Delen door nul.
6. Een teken dat niet bestaat.
7. Een lege invoer.

Test met minstens tien gevallen in een tabel.

## Uitwerking

```python
# De Leeslamp — een rekenmachine die niet stukgaat
# Cursus Python basis, hoofdstuk 15, oefening 1

TEKENS = ("+", "-", "*", "/")


def naar_getal(tekst: str) -> float:
    """Zet tekst om naar een kommagetal. Werpt een ValueError met uitleg."""
    schoon = tekst.strip().replace(",", ".")
    if not schoon:
        raise ValueError("er is niets ingevuld")
    try:
        return float(schoon)
    except ValueError:
        raise ValueError(f"{tekst.strip()!r} is geen getal") from None


def reken(links: str, teken: str, rechts: str):
    """Rekent twee ingetypte getallen uit. Geeft een getal of een boodschap."""
    try:
        a = naar_getal(links)
        b = naar_getal(rechts)
    except ValueError as fout:
        return f"fout: {fout}"

    teken = teken.strip()
    if teken not in TEKENS:
        return f"fout: {teken!r} is geen bewerking, kies uit {' '.join(TEKENS)}"

    try:
        if teken == "+":
            return a + b
        if teken == "-":
            return a - b
        if teken == "*":
            return a * b
        return a / b
    except ZeroDivisionError:
        return "fout: je kunt niet door nul delen"


gevallen = [
    ("12", "+", "8"),
    ("12", "-", "8"),
    (" 12 ", "*", " 8 "),
    ("12", "/", "8"),
    ("2,5", "*", "4"),
    ("12", "/", "0"),
    ("abc", "+", "3"),
    ("12", "^", "3"),
    ("", "+", "3"),
    ("12", "+", "   "),
    ("-3", "*", "-4"),
]

for links, teken, rechts in gevallen:
    uitkomst = reken(links, teken, rechts)
    print(f"{links!r:>8} {teken!r:^5} {rechts!r:<8} -> {uitkomst}")
```

```text
    '12'  '+'  '8'      -> 20.0
    '12'  '-'  '8'      -> 4.0
  ' 12 '  '*'  ' 8 '    -> 96.0
    '12'  '/'  '8'      -> 1.5
   '2,5'  '*'  '4'      -> 10.0
    '12'  '/'  '0'      -> fout: je kunt niet door nul delen
   'abc'  '+'  '3'      -> fout: 'abc' is geen getal
    '12'  '^'  '3'      -> fout: '^' is geen bewerking, kies uit + - * /
      ''  '+'  '3'      -> fout: er is niets ingevuld
    '12'  '+'  '   '    -> fout: er is niets ingevuld
    '-3'  '*'  '-4'     -> 12.0
```

**De zes ontwerpkeuzes.**

**Twee lagen.** `naar_getal` doet één ding: tekst omzetten of een duidelijke
fout werpen. `reken` vangt die fout op en beslist wat de gebruiker te zien
krijgt. Zo staat de omzetting op één plaats en kun je haar apart testen.

**`raise ... from None`.** Zonder die toevoeging toont Python bij een fout twee
tracebacks onder elkaar: de oorspronkelijke van `float()` en de jouwe. Met
`from None` houd je alleen jouw duidelijke melding over.

**Het teken controleren vóór de berekening.** Zou je het pas in de `if`-ketting
opvangen, dan viel `^` stilzwijgend in de `else` en kreeg je een deling. Dat is
de vergeten `else` uit hoofdstuk 9, en hier vangt de controle vooraan hem op.

**Een lege invoer apart.** `float("")` geeft een `ValueError`, dus technisch was
één `except` genoeg geweest. Maar de melding "'' is geen getal" is minder
behulpzaam dan "er is niets ingevuld". Een goede foutmelding kost één regel
extra.

**`teken.strip()`** vóór de vergelijking. Anders werkt `" + "` niet, terwijl de
gebruiker gewoon een spatie typte.

**Alles teruggeven, niets afdrukken.** De functie geeft een getal óf een tekst
terug. Het hoofdprogramma toont. Daardoor kun je de tabel hierboven schrijven,
en daardoor kun je in hoofdstuk 29 elke rij als test gebruiken.

**Wat er nog aan schort.** De functie geeft soms een getal en soms een tekst
terug. Dat is niet netjes: de aanroeper moet nu het type controleren. Twee
betere vormen bestaan: een tuple `(gelukt, waarde)` teruggeven, of de fout laten
opborrelen en de aanroeper laten opvangen. Voor een basisoefening is dit
aanvaardbaar, maar weet dat het een compromis is.
