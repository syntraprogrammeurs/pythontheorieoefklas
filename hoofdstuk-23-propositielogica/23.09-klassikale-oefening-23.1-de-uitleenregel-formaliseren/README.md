<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 23.1 — De uitleenregel formaliseren

Uit *Python basis — theoriebundel*, hoofdstuk 23 (Propositielogica en waarheidstabellen), paragraaf 23.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-5-in-python-met-het-bewijs.py` | uitwerking |  |

## Opgave

**De situatie.** Het bestuur van De Leeslamp beschrijft de uitleenregel zo:

> Een lid mag een boek lenen als het lidgeld betaald is en het lid niet
> geschorst is. Wie meer dan drie boeken thuis heeft, mag niets meer lenen,
> ook al is alles betaald.

**Wat je doet.**

1. Kies letters voor de atomaire beweringen en schrijf op wat ze betekenen.
2. Schrijf de regel in symbolen.
3. Maak de volledige waarheidstabel.
4. Vereenvoudig de voorwaarde met de wetten uit 23.6.
5. Schrijf de `if` in Python, en toon dat je vereenvoudiging gelijkwaardig is.

## Uitwerking

**1. De letters.**

| Letter | Betekenis |
|---|---|
| `b` | het lidgeld is betaald |
| `s` | het lid is geschorst |
| `v` | het lid heeft meer dan drie boeken thuis |
| `l` | het lid mag lenen |

**2. In symbolen.** De regel geeft de voorwaarde om te mogen lenen:

`l ≡ b ∧ ¬s ∧ ¬v`

**3. De waarheidstabel.**

| b | s | v | ¬s | ¬v | b ∧ ¬s ∧ ¬v |
|---|---|---|---|---|---|
| W | W | W | O | O | O |
| W | W | O | O | W | O |
| W | O | W | W | O | O |
| W | O | O | W | W | **W** |
| O | W | W | O | O | O |
| O | W | O | O | W | O |
| O | O | W | W | O | O |
| O | O | O | W | W | O |

Eén rij van de acht geeft toestemming. Dat is te verwachten: drie voorwaarden
die alle drie moeten kloppen.

**4. Vereenvoudigen.** Met De Morgan kun je de twee negaties samennemen:

`b ∧ ¬s ∧ ¬v ≡ b ∧ ¬(s ∨ v)`

In woorden: betaald, en geen van beide bezwaren. Dat is één ontkenning in plaats
van twee, en het leest beter.

**5. In Python, met het bewijs erbij.**

```python
# De Leeslamp — de uitleenregel, twee schrijfwijzen
from itertools import product


def mag_lenen_lang(betaald, geschorst, te_veel):
    """De regel zoals het bestuur hem uitsprak."""
    return betaald and not geschorst and not te_veel


def mag_lenen_kort(betaald, geschorst, te_veel):
    """Dezelfde regel, met De Morgan samengenomen."""
    return betaald and not (geschorst or te_veel)


rijen = list(product([True, False], repeat=3))
print("b       s       v       lang    kort")
print("-" * 40)
for b, s, v in rijen:
    lang = mag_lenen_lang(b, s, v)
    kort = mag_lenen_kort(b, s, v)
    print(f"{b!s:<8}{s!s:<8}{v!s:<8}{lang!s:<8}{kort}")

print()
print("Gelijkwaardig:",
      all(mag_lenen_lang(*r) == mag_lenen_kort(*r) for r in rijen))
```

```text
b       s       v       lang    kort
----------------------------------------
True    True    True    False   False
True    True    False   False   False
True    False   True    False   False
True    False   False   True    True
False   True    True    False   False
False   True    False   False   False
False   False   True    False   False
False   False   False   False   False

Gelijkwaardig: True
```

**Waarom je dit doet en niet gewoon "het werkt".** De laatste regel is een
bewijs voor álle acht de gevallen, niet voor het geval dat je toevallig
uitprobeerde. Dat is het verschil tussen deductie en inductie uit hoofdstuk 22,
en hier zie je wat het waard is: bij drie booleans is volledig bewijs gratis.

**De vraag die de groep hier stelt.** "Mag ik `l ≡ …` ook als implicatie
schrijven?" Nee, en dat is een goede vraag. `b ∧ ¬s ∧ ¬v → l` zegt alleen: wie
aan alles voldoet, mag lenen. Het verbiedt niet dat iemand anders óók mag lenen.
De biconditionele `≡` zegt "precies dan", en dat is wat het bestuur bedoelt.

Vertaald naar code: een implicatie is een `if` zonder `else`. Een biconditionele
is een `if`-`else` waarin de `else` weigert.
