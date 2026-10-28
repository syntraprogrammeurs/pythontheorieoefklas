<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 22.2 — Waar, geldig of deugdelijk

Uit *Python basis — theoriebundel*, hoofdstuk 22 (Logica en kritisch denken: de basisbegrippen), paragraaf 22.11.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** Zes redeneringen. Voor elke: is ze geldig, en is ze deugdelijk?
Let op: die twee vragen beantwoord je apart, en in die volgorde.

| Nr. | Redenering |
|---|---|
| 1 | Alle leden krijgen een lidkaart. Bram heeft een lidkaart. Dus Bram is lid |
| 2 | Als de test slaagt, is de code juist. De test slaagt. Dus de code is juist |
| 3 | Alle boeken in de kast zijn Nederlandstalig. Dit boek staat in de kast. Dus dit boek is Nederlandstalig |
| 4 | Als het programma crasht, staat er iets in het logboek. Er staat niets in het logboek. Dus het programma is niet gecrasht |
| 5 | Python is een programmeertaal. Een programmeertaal heeft een compiler. Dus Python heeft een compiler |
| 6 | Elke functie in dit bestand heeft een test. Deze functie heeft geen test. Dus deze functie staat niet in dit bestand |

**Wat je doet.** Beoordeel per redenering de vorm en daarna de inhoud. Zeg bij
elke ongeldige redenering waarom, en geef een tegenvoorbeeld: een situatie waarin
de premissen waar zijn en de conclusie toch onwaar.

## Uitwerking

| Nr. | Geldig? | Deugdelijk? | Waarom |
|---|---|---|---|
| 1 | **Nee** | Nee | Uit "alle leden hebben een kaart" volgt niet dat alleen leden er een hebben |
| 2 | **Nee** | Nee | De premisse "als de test slaagt, is de code juist" is bovendien onwaar |
| 3 | **Ja** | Hangt ervan af | De vorm is onberispelijk. Deugdelijk zodra beide premissen kloppen |
| 4 | **Ja** | Hangt ervan af | Geldige vorm. Deugdelijk als een crash inderdaad altijd gelogd wordt |
| 5 | **Ja** | **Nee** | De vorm klopt; de tweede premisse is onwaar |
| 6 | **Ja** | Hangt ervan af | Geldige vorm, dezelfde als nummer 4 |

**De tegenvoorbeelden bij de ongeldige.**

*Nummer 1.* Bram is oud-lid en heeft zijn kaart nooit ingeleverd. Alle leden
hebben een kaart, Bram heeft een kaart, en Bram is geen lid. Alle premissen waar,
conclusie onwaar; dus ongeldig.

*Nummer 2.* De test controleert `prijs(2) == 4` en de functie geeft altijd 4
terug, ongeacht de invoer. De test slaagt, de code is fout.

**Waarom 4 en 6 dezelfde vorm hebben.** Beide zijn *modus tollens*: als A dan B;
niet B; dus niet A. Dat is een van de geldige vormen uit hoofdstuk 24.

Nummer 1 en 2 zijn de spiegelfout ervan: als A dan B; B; dus A. Dat heet het
**bevestigen van het consequens**, en het is ongeldig. Het is de veelgemaakte
fout die hoofdstuk 24 en 25 uitwerken, en de reden waarom een geslaagde test niet
bewijst dat je code klopt.

**Waarom nummer 5 zo leerzaam is.** Iedereen ziet meteen dat de conclusie fout
is, en de neiging is te zeggen "dus de redenering deugt niet". Maar de redenering
is geldig: als élke programmeertaal een compiler had, dan had Python er een. De
fout zit in de premisse, niet in de vorm.

Dat onderscheid is precies het onderscheid dat je bij het foutzoeken nodig hebt:
klopt mijn logica niet, of klopt mijn aanname niet? Het zijn twee verschillende
soorten werk.
