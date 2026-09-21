<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 7.2 — Een onleesbare voorwaarde ontwarren

Uit *Python basis — theoriebundel*, hoofdstuk 7 (Operatoren, waarheidstabellen en booleaanse logica), paragraaf 7.14.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave | fragment, draait niet los |
| `uitwerking-a-2-de-morgan-toepassen.py` | uitwerking | fragment, draait niet los |
| `uitwerking-b-2-de-morgan-toepassen.py` | uitwerking | fragment, draait niet los |
| `uitwerking-c-3-met-namen.py` | uitwerking |  |
| `uitwerking-d-4-het-bewijs.py` | uitwerking |  |

## Opgave

**De situatie.** Je vindt deze regel in de code van de club. Niemand durft hem
nog aan te raken.

```python
if not (not is_lid or (leeftijd < 12 and not begeleid) or aantal >= 5) and not heeft_boete:
    print("Mag lenen")
```

**Wat je doet.**

1. Zeg in gewone taal wat deze voorwaarde betekent.
2. Pas De Morgan toe om de buitenste ontkenning weg te werken.
3. Herschrijf hem met tussenvariabelen die een naam hebben.
4. Bewijs dat je herschrijving hetzelfde doet, door alle gevallen af te lopen.
5. Zeg welke van de drie versies je in het project zou zetten, en waarom.

## Uitwerking

**1 — In gewone taal.**

Lees van binnen naar buiten. De haakjes bevatten drie redenen om **niet** te
mogen lenen: geen lid zijn, jonger dan twaalf zonder begeleiding, of al vijf
boeken uit hebben. Daar staat `not` voor, dus: geen enkele van die drie redenen
geldt. En daarbovenop mag er geen boete openstaan.

Kortom: **je mag lenen als je lid bent, als je oud genoeg bent of begeleid
wordt, als je er nog geen vijf uit hebt, en als je geen boete hebt.**

**2 — De Morgan toepassen.**

De buitenste vorm is `not (X or Y or Z)`. Volgens De Morgan wordt dat
`not X and not Y and not Z`:

```python
if is_lid and not (leeftijd < 12 and not begeleid) and aantal < 5 and not heeft_boete:
    print("Mag lenen")
```

Er staat nog één ontkenning. Pas De Morgan opnieuw toe op
`not (leeftijd < 12 and not begeleid)`, wat `leeftijd >= 12 or begeleid` wordt:

```python
if is_lid and (leeftijd >= 12 or begeleid) and aantal < 5 and not heeft_boete:
    print("Mag lenen")
```

Nu staan er alleen nog positieve voorwaarden, op één na. Dat leest al veel
beter: elke term is een reden waarom je wél mag.

**3 — Met namen.**

```python
is_lid = True
leeftijd = 34
begeleid = False
aantal = 3
heeft_boete = False

oud_genoeg = leeftijd >= 12 or begeleid
onder_de_limiet = aantal < 5
in_orde = not heeft_boete

mag_lenen = is_lid and oud_genoeg and onder_de_limiet and in_orde

if mag_lenen:
    print("Mag lenen")
```

```text
Mag lenen
```

**4 — Het bewijs.**

Er zijn vijf ingangen, dus tweeëndertig gevallen. Die loop je niet met de hand
af; dat laat je de computer doen.

```python
def oud(is_lid, leeftijd, begeleid, aantal, heeft_boete):
    return (not (not is_lid or (leeftijd < 12 and not begeleid) or aantal >= 5)
            and not heeft_boete)


def nieuw(is_lid, leeftijd, begeleid, aantal, heeft_boete):
    oud_genoeg = leeftijd >= 12 or begeleid
    onder_de_limiet = aantal < 5
    in_orde = not heeft_boete
    return is_lid and oud_genoeg and onder_de_limiet and in_orde


verschillen = 0
gevallen = 0
for is_lid in (False, True):
    for leeftijd in (8, 12, 40):
        for begeleid in (False, True):
            for aantal in (0, 4, 5, 9):
                for heeft_boete in (False, True):
                    gevallen += 1
                    a = oud(is_lid, leeftijd, begeleid, aantal, heeft_boete)
                    b = nieuw(is_lid, leeftijd, begeleid, aantal, heeft_boete)
                    if a != b:
                        verschillen += 1
                        print("VERSCHIL:", is_lid, leeftijd, begeleid, aantal, heeft_boete)

print(f"{gevallen} gevallen getest, {verschillen} verschillen")
```

```text
96 gevallen getest, 0 verschillen
```

Let op de gekozen waarden voor `leeftijd` en `aantal`: 8, 12 en 40 zijn
respectievelijk onder de grens, precies op de grens en erboven. Voor `aantal`
idem: 0, 4, 5 en 9. Dat zijn de grenswaarden uit hoofdstuk 3. Zou je alleen 8 en
40 testen, dan mis je precies de fout waar `<` en `<=` verwisseld zijn.

**5 — Welke versie in het project?**

De derde, met de namen. Redenen, in volgorde van gewicht:

| Reden | Toelichting |
|---|---|
| Leesbaar | Een collega begrijpt hem in vijf seconden in plaats van in vijf minuten |
| Te debuggen | In de debugger zie je `oud_genoeg` staan, en dus meteen welk deel fout is |
| Te testen | Je kunt elk deel apart controleren |
| Uitbreidbaar | Komt er een voorwaarde bij, dan voeg je één regel toe |

De tweede versie is een goede tussenstap, maar `leeftijd >= 12 or begeleid`
staat er nog zonder uitleg. Een lezer moet dan zelf bedenken waarom die twee bij
elkaar staan. De naam `oud_genoeg` vertelt dat.

**Wat je hieruit meeneemt.** Onleesbare voorwaarden zijn geen kwestie van
slimheid maar van gewoonte. Je maakt ze leesbaar met twee handelingen: De Morgan
toepassen tot de ontkenningen weg zijn, en elk deel een naam geven.
