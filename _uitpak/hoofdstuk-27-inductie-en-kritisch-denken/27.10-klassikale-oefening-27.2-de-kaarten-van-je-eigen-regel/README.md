<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 27.2 — De kaarten van je eigen regel

Uit *Python basis — theoriebundel*, hoofdstuk 27 (Inductie, Mill's methods en kritisch denken), paragraaf 27.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-3-het-programma.py` | uitwerking |  |

## Opgave

**De situatie.** Je collega beweert: *"Als een lid geschorst is, staat er een
reden in het logboek."*

Je mag vier records controleren om die regel te toetsen. Je krijgt van elk record
één helft te zien.

| Kaart | Wat je ziet |
|---|---|
| A | Lid Bram: **geschorst** (je ziet het logboek nog niet) |
| B | Lid Cato: **niet geschorst** (je ziet het logboek nog niet) |
| C | Logboekregel: **"reden: boete niet betaald"** (je ziet het lid nog niet) |
| D | Logboekregel: **geen enkele regel voor dit lid** (je ziet het lid nog niet) |

**Wat je doet.**

1. Welke kaarten draai je om, en waarom precies die?
2. Welke argumentvorm hoort bij elke kaart?
3. Schrijf een programma dat de vier kaarten nagaat en zegt welke de regel kunnen
   breken.
4. Bedenk waarom je in de praktijk toch geneigd bent de verkeerde te kiezen.

## Uitwerking

**1 en 2. De kaarten.**

| Kaart | Omdraaien? | Wat je zoekt | Argumentvorm |
|---|---|---|---|
| A — geschorst | **Ja** | Geen reden in het logboek: dan is de regel gebroken | Modus ponens |
| B — niet geschorst | Nee | De regel zegt niets over niet-geschorste leden | Ontkennen van het antecedens |
| C — er staat een reden | Nee | Wat er ook achter zit, de regel wordt niet gebroken | Bevestigen van het consequens |
| D — geen enkele regel | **Ja** | Is dit lid geschorst, dan is de regel gebroken | Modus tollens |

Precies dezelfde verdeling als bij de kaarten van Wason in 27.3, met de inhoud
van je eigen werk erin.

**3. Het programma.**

```python
# De vier kaarten van Wason, met de regels van De Leeslamp
# Cursus Python basis, hoofdstuk 27, oefening 2

# De regel: geschorst -> reden in het logboek.
# Per kaart: wat je ziet, en wat er nog verborgen is.
KAARTEN = [
    ("A", "geschorst", "geschorst", None),
    ("B", "niet geschorst", "niet_geschorst", None),
    ("C", "er staat een reden", None, "reden"),
    ("D", "geen enkele regel", None, "geen_reden"),
]


def kan_breken(zichtbaar_lid, zichtbaar_log):
    """Kan deze kaart de regel 'geschorst -> reden' schenden?

    Alleen de combinatie geschorst plus geen reden breekt hem. Een kaart
    moet dus omgedraaid worden als die combinatie nog mogelijk is.
    """
    lid_kan_geschorst_zijn = zichtbaar_lid != "niet_geschorst"
    log_kan_leeg_zijn = zichtbaar_log != "reden"
    return lid_kan_geschorst_zijn and log_kan_leeg_zijn


print("Regel: als een lid geschorst is, staat er een reden in het logboek.")
print()
for naam, omschrijving, lid, log in KAARTEN:
    besluit = "OMDRAAIEN" if kan_breken(lid, log) else "laten liggen"
    print(f"  {naam}  {omschrijving:<20} {besluit}")
```

```text
Regel: als een lid geschorst is, staat er een reden in het logboek.

  A  geschorst            OMDRAAIEN
  B  niet geschorst       laten liggen
  C  er staat een reden   laten liggen
  D  geen enkele regel    OMDRAAIEN
```

De functie bevat de hele redenering in twee regels: een kaart moet omgedraaid
worden zolang de combinatie "geschorst én geen reden" nog mogelijk is.

**4. Waarom je toch de verkeerde kiest.**

| Neiging | Wat erachter zit |
|---|---|
| Kaart C willen omdraaien | Bevestigingsdrang: je zoekt een geval dat de regel bevestigt |
| Kaart D niet willen omdraaien | Een leeg logboek voelt als "er is niets", niet als "hier kan de fout zitten" |
| Kaart B willen omdraaien | Volledigheidsdrang: alles nakijken voelt zorgvuldig |

De derde is interessant. Alles nakijken is niet fout, het is verspilling. In deze
oefening kost het weinig; bij een tabel met tien miljoen rijen kost het uren.

Kritisch denken is niet: alles controleren. Het is: weten welke controle iets kan
uitsluiten.

> **Waarom**
>
> Er is een goed gedocumenteerd vervolg op deze proef. Precies dezelfde opgave,
> maar met een sociale regel in plaats van letters en cijfers — "als iemand alcohol
> drinkt, is hij ouder dan achttien" — wordt door de meeste mensen wél juist
> opgelost.
>
> De logica is identiek. Wat verschilt, is dat mensen bij een sociale regel vanzelf
> naar overtreders zoeken, en bij een abstracte regel naar bevestigingen.
>
> De praktische les: **maak je regel concreet vóór je hem toetst**. "Als de invoer
> ongeldig is, komt er een foutmelding" toets je beter door te vragen "wie is er
> langs de controle geglipt" dan door te vragen "werkt de controle".
