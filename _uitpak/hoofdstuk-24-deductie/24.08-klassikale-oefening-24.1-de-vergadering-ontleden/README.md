<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 24.1 — De vergadering ontleden

Uit *Python basis — theoriebundel*, hoofdstuk 24 (Deductie: syllogismen, geldigheid en argumentvormen), paragraaf 24.8.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** Zes uitspraken uit een echte foutbespreking. Ze klinken alle
zes redelijk.

| Nr. | Uitspraak |
|---|---|
| 1 | "Als de cache aanstond, was het snel. Het is snel. Dus de cache staat aan." |
| 2 | "Als de invoer leeg is, crasht het. Het crasht niet. Dus de invoer is niet leeg." |
| 3 | "Het ligt aan de code of aan de gegevens. Aan de code ligt het niet. Dus aan de gegevens." |
| 4 | "Als we de index toevoegen, wordt de zoekopdracht sneller. We voegen de index toe. Dus wordt het sneller." |
| 5 | "Als iemand niet ingelogd is, ziet hij de knop niet. Anke is ingelogd. Dus Anke ziet de knop." |
| 6 | "Als de build faalt, is er een compilerfout. Als er een compilerfout is, staat die in het logboek. Dus als de build faalt, staat er iets in het logboek." |

**Wat je doet.** Benoem per uitspraak de argumentvorm en zeg of ze geldig is.
Geef bij elke ongeldige een concreet tegenvoorbeeld. Zeg bij elke geldige welke
premisse je zou nakijken vóór je erop vertrouwt.

## Uitwerking

| Nr. | Vorm | Geldig? |
|---|---|---|
| 1 | Bevestigen van het consequens | **Nee** |
| 2 | Modus tollens | Ja |
| 3 | Disjunctief syllogisme | Ja |
| 4 | Modus ponens | Ja |
| 5 | Ontkennen van het antecedens | **Nee** |
| 6 | Hypothetisch syllogisme | Ja |

**De tegenvoorbeelden bij de twee ongeldige.**

*Nummer 1.* Het is snel omdat er vanochtend maar drie gebruikers zijn, en de
cache staat uit. Premissen waar, conclusie onwaar. Snelheid heeft meer oorzaken
dan de cache, en dat is precies wat de regel niet uitsluit.

*Nummer 5.* Anke is ingelogd, maar ze heeft geen beheerdersrechten, en de knop
is alleen voor beheerders. De regel zegt wat er gebeurt bij níet ingelogd zijn.
Over ingelogde gebruikers zegt hij niets.

**Wat je bij de vier geldige nakijkt.** Geldig betekent niet deugdelijk. Elke
geldige vorm hangt aan zijn premissen, en dit is waar ze breken.

| Nr. | De premisse die je nakijkt | Waarom juist die |
|---|---|---|
| 2 | "Als de invoer leeg is, crasht het" | Crasht het **altijd**? Eén geval waarin het overleeft en de conclusie valt weg |
| 3 | "Het ligt aan de code of aan de gegevens" | Vals dilemma. Netwerk, configuratie, rechten, tijdzone: de lijst is zelden volledig |
| 4 | "Als we de index toevoegen, wordt het sneller" | Een index versnelt lezen en vertraagt schrijven. Sneller waarin? |
| 6 | Beide implicaties | Kan de build ook falen zonder compilerfout? Ja: een test, een netwerk, een schijf die vol is |

**Wat deze oefening je leert.** De twee ongeldige uitspraken zijn niet dommer
geformuleerd dan de vier geldige. Ze zijn even vloeiend en even overtuigend.
Het onderscheid zit alleen in de vorm, en dat is de reden waarom je die vormen
uit je hoofd wilt kennen.

**En het echte werk zit erna.** Nummer 3 is geldig én bijna altijd het slechtste
argument van de zes, want die lijst van twee oorzaken is meestal verzonnen.
Geldigheid is de laagste lat, niet de hoogste.
