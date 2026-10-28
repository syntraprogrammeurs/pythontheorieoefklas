<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 25.2 — De invariant die een fout blootlegt

Uit *Python basis — theoriebundel*, hoofdstuk 25 (Deductief redeneren en je code), paragraaf 25.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-a-2-waar-de-invariant-breekt.py` | uitwerking |  |
| `uitwerking-b-3-de-herstelde-functie.py` | uitwerking |  |

## Opgave

**De situatie.** Deze functie moet het hoogste aantal bladzijden vinden. Ze werkt
op de voorbeelden waarop ze getest is.

```python
def hoogste(getallen):
    """Het grootste getal uit de reeks. Bevat een fout."""
    grootste = 0
    for getal in getallen:
        if getal > grootste:
            grootste = getal
    return grootste
```

**Wat je doet.**

1. Schrijf de preconditie, de postconditie en de invariant op.
2. Zoek met de invariant de invoer waarvoor de functie fout is.
3. Herstel de functie, en toon met een `assert` in de lus dat de invariant nu
   staat.
4. Zeg wat er met het lege geval moet gebeuren, en waarom dat een beslissing is
   en geen technische vraag.

## Uitwerking

**1. De drie beweringen.**

| Deel | Bewering |
|---|---|
| Preconditie | `getallen` bevat minstens één getal |
| Invariant | Na `i` ronden is `grootste` het grootste van de eerste `i` getallen |
| Postconditie | Het resultaat komt in `getallen` voor, en niets in `getallen` is groter |

**2. Waar de invariant breekt.** Vóór de eerste ronde is `grootste` nul, en nul
is niet "het grootste van de eerste nul getallen". Er ís geen grootste van nul
getallen. De beginwaarde deugt dus niet, en dat is geen detail: ze verzint een
element dat er niet is.

Concreet gaat het mis zodra alle getallen negatief zijn.

```python
def hoogste_fout(getallen):
    """De versie met de foute beginwaarde."""
    grootste = 0
    for getal in getallen:
        if getal > grootste:
            grootste = getal
    return grootste


print("gewone lijst  :", hoogste_fout([320, 180, 250]))
print("negatieve lijst:", hoogste_fout([-5, -12, -3]))
print("lege lijst    :", hoogste_fout([]))
```

```text
gewone lijst  : 320
negatieve lijst: 0
lege lijst    : 0
```

Bij de negatieve lijst geeft de functie 0 terug, en 0 staat niet in de lijst. De
postconditie "het resultaat komt in de reeks voor" is geschonden. Bij de lege
lijst geeft ze eveneens 0, en dat is een antwoord op een vraag die geen antwoord
heeft.

> **Waarom**
>
> Dit is waarom die postconditie zo geformuleerd is. "Het resultaat is het
> grootste" klinkt volledig en is het niet: 0 is groter dan alles in
> `[-5, -12, -3]`, dus ook die versie van de postconditie zou standhouden.
>
> Pas met "het resultaat **komt in de reeks voor**" erbij vang je de fout. Een goede
> postconditie zegt niet alleen hoe groot iets is, maar ook waar het vandaan komt.

**3. De herstelde functie.**

```python
def hoogste(getallen):
    """Het grootste getal uit de reeks.

    Preconditie : getallen bevat minstens één getal.
    Invariant   : `grootste` is het grootste van de reeds bekeken getallen.
    Postconditie: het resultaat zit in getallen, en niets erin is groter.
    """
    assert len(getallen) > 0, "hoogste() verwacht minstens één getal"

    grootste = getallen[0]                 # beginwaarde uit de reeks zelf
    for i, getal in enumerate(getallen[1:], start=2):
        if getal > grootste:
            grootste = getal
        assert grootste == max(getallen[:i]), "invariant geschonden"

    assert grootste in getallen
    assert all(getal <= grootste for getal in getallen)
    return grootste


print("gewone lijst   :", hoogste([320, 180, 250]))
print("negatieve lijst:", hoogste([-5, -12, -3]))
print("één element    :", hoogste([7]))
```

```text
gewone lijst   : 320
negatieve lijst: -3
één element    : 7
```

De enige echte wijziging is de beginwaarde: `getallen[0]` in plaats van `0`. De
invariant wees precies naar die regel.

> **Wat hier gebeurde**
>
> De fout zat niet in de lus en niet in de vergelijking. Ze zat in de **aanname
> vóór de lus**: dat nul een geldig startpunt is.
>
> Zo'n aanname vind je niet door de code te lezen, want er staat niets fout. Je
> vindt hem door de invariant op te schrijven en te vragen: is die waar vóór de
> eerste ronde? Dat is de stap "beginwaarde" uit 25.4, en het is de stap die het
> vaakst wordt overgeslagen.

**4. Het lege geval.** Er zijn drie verdedigbare antwoorden, en de keuze is niet
technisch.

| Keuze | Wanneer je die neemt |
|---|---|
| Een fout opgooien met `raise ValueError` | Een lege lijst wijst op een fout eerder in het programma |
| `None` teruggeven | De aanroeper hoort met "er is er geen" om te kunnen gaan |
| Een standaardwaarde meegeven, zoals `max(reeks, default=0)` | De aanroeper weet welke waarde in zijn geval zinvol is |

Python zelf kiest de eerste voor `max()` en biedt de derde aan als optie. Dat is
geen toeval: stilzwijgend iets verzinnen is de enige keuze die je nooit wilt.

En dat is de kern. "Wat moet er gebeuren bij een lege lijst" is een vraag aan de
opdrachtgever, niet aan de programmeur. Wie hem zelf beantwoordt zonder het te
zeggen, heeft precies de fout gemaakt uit de tabel van 22.7: een onuitgesproken
premisse in werkende code.
