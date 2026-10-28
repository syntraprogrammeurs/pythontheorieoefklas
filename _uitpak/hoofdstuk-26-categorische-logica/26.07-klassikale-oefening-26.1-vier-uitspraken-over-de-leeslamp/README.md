<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 26.1 — Vier uitspraken over De Leeslamp

Uit *Python basis — theoriebundel*, hoofdstuk 26 (Categorische logica en venndiagrammen), paragraaf 26.7.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** Het bestuur doet vier uitspraken.

| Nr. | Uitspraak |
|---|---|
| 1 | Alle leden die geschorst zijn, mogen niet lenen |
| 2 | Geen enkel erelid betaalt lidgeld |
| 3 | Sommige leden zijn student |
| 4 | Sommige leden hebben geen e-mailadres |

**Wat je doet.**

1. Zet elke uitspraak om in een van de vier vormen, en benoem S en P.
2. Teken van elke uitspraak het diagram met drie gebieden.
3. Schrijf van elke uitspraak de ontkenning op, in een van de vier vormen.
4. Zeg per uitspraak of ze omgekeerd mag worden, en wat er dan staat.
5. Bepaal wat er volgt uit uitspraak 3 en 4 samen.

## Uitwerking

**1 en 2. De vormen en de diagrammen.**

**Uitspraak 1** is een A-vorm. S = geschorste leden, P = leden die niet mogen
lenen.

```text
   +-------------+-------------+-------------+
   |    LEEG     |             |             |
   |  geschorst, |  geschorst  |  mag niet   |
   |  mag wel    |  mag niet   |  lenen,     |
   |  lenen      |  lenen      |  niet gesch.|
   +-------------+-------------+-------------+
```

**Uitspraak 2** is een E-vorm. S = ereleden, P = betalers.

```text
   +-------------+-------------+-------------+
   |             |    LEEG     |             |
   |  erelid,    |  erelid en  |  betaalt,   |
   |  betaalt    |  betaalt    |  geen       |
   |  niet       |             |  erelid     |
   +-------------+-------------+-------------+
```

**Uitspraak 3** is een I-vorm. S = leden, P = studenten.

```text
   +-------------+-------------+-------------+
   |             |      X      |             |
   |  lid, geen  |  lid én     |  student,   |
   |  student    |  student    |  geen lid   |
   +-------------+-------------+-------------+
```

**Uitspraak 4** is een O-vorm. S = leden, P = mensen met een e-mailadres.

```text
   +-------------+-------------+-------------+
   |      X      |             |             |
   |  lid, geen  |  lid mét    |  e-mail,    |
   |  e-mail     |  e-mail     |  geen lid   |
   +-------------+-------------+-------------+
```

**3. De ontkenningen.**

| Nr. | Uitspraak | Ontkenning | Vorm |
|---|---|---|---|
| 1 | Alle geschorste leden mogen niet lenen | Sommige geschorste leden mogen wél lenen | A wordt O |
| 2 | Geen enkel erelid betaalt | Sommige ereleden betalen | E wordt I |
| 3 | Sommige leden zijn student | Geen enkel lid is student | I wordt E |
| 4 | Sommige leden hebben geen e-mail | Alle leden hebben e-mail | O wordt A |

Let op wat er **niet** staat. De ontkenning van uitspraak 1 is niet "geen enkel
geschorst lid mag niet lenen". Dat is een veel sterkere bewering, en om uitspraak
1 onderuit te halen heb je maar één geschorst lid nodig dat toch mocht lenen.

> **Waarom dit rechtstreeks je werk raakt**
>
> Dit is de vorm waarin je een bug meldt.
>
> De ontwikkelaar beweert `A`: "alle ongeldige invoer wordt geweigerd." Jij hoeft
> niet `E` te bewijzen: je hoeft niet aan te tonen dat er niets geweigerd wordt.
> Je hoeft `O` te tonen: één stuk ongeldige invoer dat er wél doorkwam.
>
> Wie dat weet, schrijft kortere bugmeldingen en voert kortere discussies. Eén
> tegenvoorbeeld is het volledige bewijs.

**4. Omkeren.**

| Nr. | Vorm | Mag omkeren? | Wat er dan staat |
|---|---|---|---|
| 1 | A | Nee | "Iedereen die niet mag lenen, is geschorst" — onwaar, want onbetaald lidgeld bestaat ook |
| 2 | E | Ja | "Geen enkele betaler is erelid" — even waar |
| 3 | I | Ja | "Sommige studenten zijn lid" — even waar |
| 4 | O | Nee | "Sommige mensen zonder e-mail zijn geen lid" — daar zegt uitspraak 4 niets over |

**5. Wat volgt uit 3 en 4 samen?**

Niets. Twee particuliere premissen leveren geen conclusie op, en dat is regel 5
uit 26.5. Er is bovendien geen middenterm die ze verbindt: uitspraak 3 gaat over
studenten, uitspraak 4 over e-mailadressen.

De verleiding is te denken: er zijn dus studenten zonder e-mailadres. Dat kan
waar zijn, en het volgt niet. De studenten uit 3 en de leden zonder e-mail uit 4
kunnen twee volstrekt verschillende mensen zijn.

**Wat deze oefening je leert.** Vier korte zinnen uit een echte bestuursnota
leveren vier verschillende logische vormen op, met vier verschillende
ontkenningen en twee die je niet mag omkeren. Wie dat op het gehoor doet, heeft
de helft van de tijd gelijk.
