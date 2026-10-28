<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 29.1 — De eisen ontleden

Uit *Python basis — theoriebundel*, hoofdstuk 29 (Eindopdracht: alles samen), paragraaf 29.8.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** Dit is de brief die "de klant" stuurt. Hij is met opzet
geschreven zoals klanten schrijven: onvolledig, tegenstrijdig en met aannames
erin.

> Beste,
>
> Wij zijn turnclub De Sprong. We hebben ongeveer tachtig leden, verdeeld over
> zes lesgroepen. Ik wil graag kunnen zien wie er in welke groep zit en wie zijn
> lidgeld betaald heeft. Het lidgeld is 120 euro per jaar, maar jongeren betalen
> minder, en wie twee kinderen inschrijft krijgt korting. Als iemand drie keer
> niet komt opdagen, moet hij uit de groep. Verder wil ik een lijst kunnen
> afdrukken van wie er nog moet betalen.
>
> Het moet eenvoudig zijn, want ik ben niet zo technisch.

**Wat je doet.**

1. Haal de functionele eisen eruit, en zet ze in een tabel.
2. Leg het gegevensmodel vast: welke dingen, welke velden, welk type.
3. Wijs de plaatsen aan waar de brief onvolledig of tegenstrijdig is.
4. Formuleer de vragen die je aan de klant stelt vóór je begint.
5. Schrijf de belangrijkste rekenregel als contract.

## Uitwerking

**1. De functionele eisen.**

| Nr. | Eis | Uit welke zin |
|---|---|---|
| 1 | Leden bewaren, met hun gegevens | "tachtig leden" |
| 2 | Lesgroepen bewaren en leden eraan koppelen | "zes lesgroepen" |
| 3 | Tonen wie in welke groep zit | "wie er in welke groep zit" |
| 4 | Betaalstatus per lid bijhouden | "wie zijn lidgeld betaald heeft" |
| 5 | Lidgeld berekenen, met leeftijdstarief en gezinskorting | "jongeren betalen minder", "korting" |
| 6 | Aanwezigheden bijhouden per les | "drie keer niet komt opdagen" |
| 7 | Een lid uit een groep zetten na drie afwezigheden | Dezelfde zin |
| 8 | Een lijst van wanbetalers tonen of exporteren | "wie er nog moet betalen" |

**2. Het gegevensmodel.**

| Ding | Veld | Type | Opmerking |
|---|---|---|---|
| **Lid** | `nummer` | `int` | Uniek; de klant noemt het niet, jij hebt het nodig |
| | `naam` | `str` | Niet leeg |
| | `geboortejaar` | `int` | Beter dan leeftijd: leeftijd verandert |
| | `groep_id` | `int` | Verwijst naar een groep |
| | `gezin_id` | `int` of `None` | Voor de gezinskorting |
| | `betaald_centen` | `int` | In centen, niet in euro's |
| **Groep** | `id` | `int` | |
| | `naam` | `str` | "Kleuters", "Recreanten" |
| | `dag` en `uur` | `str` | |
| **Aanwezigheid** | `lid_nummer` | `int` | |
| | `datum` | `str` | ISO-vorm: `2026-09-10` |
| | `aanwezig` | `bool` | |

> **Waarom**
>
> Twee keuzes in die tabel verdienen uitleg, en beide komen uit eerdere
> hoofdstukken.
>
> **Geboortejaar in plaats van leeftijd.** Leeftijd is afgeleide informatie die
> elk jaar verandert. Wat je opslaat, is wat vaststaat; wat je berekent, bereken je
> wanneer je het nodig hebt.
>
> **Bedragen in centen als `int`.** Dat is de valkuil uit hoofdstuk 6:
> `0.1 + 0.2 == 0.3` is onwaar. Reken in hele centen en deel pas door honderd bij
> het tonen, dan klopt elke optelling.

**3. Waar de brief onvolledig is.**

| Nr. | Wat er ontbreekt of botst |
|---|---|
| 1 | "Jongeren betalen minder": hoeveel minder, en tot welke leeftijd? |
| 2 | "Wie twee kinderen inschrijft": hoeveel korting, en op welk kind? |
| 3 | Gelden beide kortingen samen, en in welke volgorde worden ze toegepast? |
| 4 | "Drie keer niet komt opdagen": drie keer na elkaar, of drie keer in totaal? |
| 5 | "Moet hij uit de groep": automatisch, of met een bevestiging door de trainer? |
| 6 | Wat gebeurt er met een lid dat halverwege het jaar instapt? |
| 7 | Kan een lid in meer dan één groep zitten? |
| 8 | "Nog moet betalen": vanaf welke datum is iemand te laat? |
| 9 | Wat betekent "eenvoudig"? Dat is geen eis maar een wens |

**4. De vragen aan de klant.**

De kunst is er niet twintig te stellen maar de vijf te kiezen die je werk het
meest veranderen.

| Vraag | Waarom deze |
|---|---|
| Wat is het jeugdtarief, en tot welke leeftijd geldt het? | Zonder dit kun je eis 5 niet bouwen |
| Hoeveel is de gezinskorting, en op welk lid wordt ze toegepast? | Idem, en het bepaalt je gegevensmodel |
| Drie keer afwezig in totaal, of drie keer na elkaar? | Twee volstrekt verschillende programma's |
| Gaat iemand er automatisch uit, of stelt het programma het alleen voor? | Automatisch verwijderen is onomkeerbaar; dat wil je zelden |
| Vanaf welke datum heet iemand een wanbetaler? | Anders is de lijst uit eis 8 niet te maken |

> **Wat je hier eigenlijk doet**
>
> Dit is hoofdstuk 22 in de praktijk. Elke ontbrekende regel die je zelf invult, is
> een **verzwegen premisse** die in werkende code terechtkomt.
>
> De klant merkt hem pas wanneer het programma iets doet wat hij niet verwachtte,
> en dan heet het een bug terwijl het een aanname was.
>
> Eén vraag stellen kost vijf minuten. Eén verkeerde aanname kost een halve dag
> herbouwen, plus het vertrouwen.

**5. De rekenregel als contract.**

Stel dat de klant antwoordt: jeugdtarief 90 euro tot en met 17 jaar, gezinskorting
15 euro per lid vanaf het tweede lid van hetzelfde gezin, en de kortingen
stapelen.

| Deel | Bewering |
|---|---|
| Preconditie | `geboortejaar` ligt tussen 1900 en het huidige jaar; `rang_in_gezin` is 1 of meer |
| Postconditie | Het resultaat is een geheel aantal centen, tussen 0 en 12000 |
| Regel | Basis 12000 centen, of 9000 bij een leeftijd tot en met 17; daarna 1500 centen korting vanaf het tweede gezinslid; nooit onder nul |
