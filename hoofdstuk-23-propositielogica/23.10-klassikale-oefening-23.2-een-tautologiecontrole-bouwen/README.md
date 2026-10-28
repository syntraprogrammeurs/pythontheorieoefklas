<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 23.2 — Een tautologiecontrole bouwen

Uit *Python basis — theoriebundel*, hoofdstuk 23 (Propositielogica en waarheidstabellen), paragraaf 23.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-de-dode-taktest.py` | uitwerking |  |

## Opgave

**De situatie.** Je hebt in 23.7 een tabel laten afdrukken. Nu maak je er
gereedschap van dat een oordeel geeft in plaats van een tabel.

**Wat je doet.** Schrijf een functie `beoordeel(aantal, formule)` die zegt of een
formule een tautologie, een contradictie of een contingentie is. Test ze op vijf
formules, waaronder deze twee, waarvan je op voorhand zegt wat je verwacht:

- `(p → q) ∨ (q → p)`
- `(p ∧ q) → (p ∨ q)`

Voeg daarna een controle toe die een `if`-voorwaarde uit echte code onderzoekt
op dode takken.

## Uitwerking

```python
# Tautologie, contradictie of contingentie
from itertools import product


def beoordeel(aantal, formule):
    """Zegt wat de laatste kolom van de waarheidstabel doet."""
    uitkomsten = [formule(*w)
                  for w in product([True, False], repeat=aantal)]
    if all(uitkomsten):
        return "tautologie"
    if not any(uitkomsten):
        return "contradictie"
    return "contingentie"


formules = [
    ("p OF NIET p", 1, lambda p: p or not p),
    ("p EN NIET p", 1, lambda p: p and not p),
    ("p -> q", 2, lambda p, q: (not p) or q),
    ("(p -> q) OF (q -> p)", 2,
     lambda p, q: ((not p) or q) or ((not q) or p)),
    ("(p EN q) -> (p OF q)", 2,
     lambda p, q: (not (p and q)) or (p or q)),
]

for naam, aantal, formule in formules:
    print(f"{naam:<24}{beoordeel(aantal, formule)}")
```

```text
p OF NIET p             tautologie
p EN NIET p             contradictie
p -> q                  contingentie
(p -> q) OF (q -> p)    tautologie
(p EN q) -> (p OF q)    tautologie
```

**Waarom die vierde een tautologie is, en waarom dat vervelend is.**
`(p → q) ∨ (q → p)` is altijd waar. Van twee willekeurige beweringen volgt er
altijd minstens één uit de andere, hoe onzinnig het verband ook is.

Neem `p` = "het regent" en `q` = "2 + 2 = 4". Dan is `p → q` waar, want `q` is
altijd waar. En daarmee is de hele formule waar, zonder dat regen ook maar iets
met rekenen te maken heeft.

Dat is de bekendste beperking van de propositielogica: ze kijkt alleen naar
waarheidswaarden, niet naar betekenis of oorzaak. Ze bewijst dus nooit dat er
een verband ís, alleen dat de vorm klopt.

**De dode-taktest.**

```python
# Een voorwaarde uit echte code op dode takken onderzoeken
from itertools import product


def onbereikbaar(namen, formule):
    """De combinaties waarvoor deze voorwaarde nooit waar wordt."""
    return [dict(zip(namen, w))
            for w in product([True, False], repeat=len(namen))
            if not formule(*w)]


NAMEN = ["betaald", "geschorst", "te_veel"]


def voorwaarde(betaald, geschorst, te_veel):
    """De uitleenregel uit oefening 23.1."""
    return betaald and not (geschorst or te_veel)


gevallen = onbereikbaar(NAMEN, voorwaarde)
print(f"{len(gevallen)} van de 8 combinaties geven geen toestemming.")
print()


def altijd_waar(betaald, geschorst, te_veel):
    """Een voorwaarde met een fout: hij kan niet onwaar worden."""
    return betaald or not betaald


print("Dode tak in 'altijd_waar':",
      len(onbereikbaar(NAMEN, altijd_waar)) == 0)


def nooit_waar(betaald, geschorst, te_veel):
    """En een voorwaarde die nooit uitvoert."""
    return geschorst and not geschorst


print("Dode tak in 'nooit_waar': ",
      len(onbereikbaar(NAMEN, nooit_waar)) == 8)
```

```text
7 van de 8 combinaties geven geen toestemming.

Dode tak in 'altijd_waar': True
Dode tak in 'nooit_waar':  True
```

**Wat dit gereedschap je in de praktijk oplevert.**

| Uitkomst | Wat het betekent | Wat je doet |
|---|---|---|
| Nul combinaties onwaar | Tautologie: de `if` voert altijd uit | De `if` weghalen, of de voorwaarde herschrijven |
| Alle combinaties onwaar | Contradictie: de tak is dood | De tak weghalen, of de fout erin zoeken |
| Iets ertussenin | Normale voorwaarde | Nakijken of de verdeling klopt met wat je bedoelde |

**De grens van deze aanpak.** Ze werkt alleen voor booleans. Zodra je voorwaarde
over getallen gaat, zoals `leeftijd < 12`, zijn er geen twee mogelijkheden meer
maar oneindig veel. Dan gebruik je equivalentieklassen en grenswaarden, en dat is
hoofdstuk 28.
