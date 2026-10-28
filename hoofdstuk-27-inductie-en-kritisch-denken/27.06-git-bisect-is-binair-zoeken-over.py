# Python basis — theoriebundel
# Hoofdstuk 27 — Inductie, Mill's methods en kritisch denken
# 27.6 Foutzoeken als inductief onderzoek — git bisect is binair zoeken over je
# geschiedenis
#
# Lineair zoeken kost zestig keer uitproberen. Binair zoeken, uit hoofdstuk 25, kost
# er zes.

# Binair zoeken naar de eerste stukke commit
#
# De situatie: twee weken geleden werkte je programma, vandaag is het stuk. Daartussen
# zitten zestig COMMITS (de bewaarde versies uit hoofdstuk 2). Eén ervan heeft de fout
# binnengebracht, en alle commits daarna zijn dus ook stuk.
# Dit programma doet na wat het Git-commando GIT BISECT doet: telkens de middelste
# versie testen, en zo de helft van de verdachten in één keer wegstrepen.

# De zestig commits krijgen de namen c01 tot en met c60.
# range(1, 61) geeft 1, 2, ..., 60 (de 61 zelf niet, hoofdstuk 10).
# {n:02d} in de f-string (hoofdstuk 6) schrijft n als geheel getal van minstens twee
# cijfers, aangevuld met een 0 vooraan: 1 -> "01", 43 -> "43".
# LET OP: de lijst begint bij index 0. COMMITS[0] is "c01", COMMITS[42] is "c43".
COMMITS = [f"c{n:02d}" for n in range(1, 61)]
# Het nummer van de commit die de fout binnenbracht. Een "constante" in HOOFDLETTERS
# (hoofdstuk 5). In het echt ken je dit getal niet: je wilt het juist vinden. Het
# staat hier alleen zodat werkt() kan doen alsof hij een echte test uitvoert.
EERSTE_STUKKE = 43          # in het echt weet je dit niet


# werkt() speelt de rol van "die versie uitchecken en je tests draaien".
#   index -> de plaats in COMMITS (0 tot en met 59)
#   geeft True terug als die versie nog werkt, False als ze stuk is
# Waarom "EERSTE_STUKKE - 1"? Commit c43 staat op index 42. Alles vóór index 42
# (dus c01 tot c42) werkt nog; vanaf index 42 is alles stuk.
def werkt(index):
    """Doet alsof we die versie uitchecken en testen."""
    return index < EERSTE_STUKKE - 1


# BINAIR ZOEKEN (hoofdstuk 25): je houdt een zoekgebied bij tussen links en rechts,
# en halveert dat gebied bij elke poging.
#
# De LUSINVARIANT (25.4) staat in de docstring: alles links van 'links' werkt nog,
# en 'rechts' wijst naar een versie die al stuk is (of naar de laatste kandidaat).
# Daardoor ligt de eerste stukke commit altijd ergens tussen links en rechts.
#
# Verschil met binair_zoek uit hoofdstuk 25: daar zocht je één precieze waarde en
# stopte je zodra je ze vond. Hier zoek je een GRENS: de eerste plek waar "werkt"
# van True naar False springt. Daarom staat er "rechts = midden" (midden kan zelf
# de eerste stukke zijn) en niet "rechts = midden - 1".
def zoek_eerste_stukke(commits):
    """De invariant: links werkt nog, rechts is al stuk."""
    # Twee variabelen tegelijk toekennen: links wordt 0, rechts wordt 59.
    links, rechts = 0, len(commits) - 1
    # Hoeveel keer je een versie hebt moeten testen.
    pogingen = 0
    # Zolang er meer dan één kandidaat over is, blijf je halveren.
    while links < rechts:
        # // is de gehele deling (hoofdstuk 6): (0 + 59) // 2 is 29, niet 29.5.
        midden = (links + rechts) // 2
        pogingen += 1
        if werkt(midden):
            # Deze versie werkt: de fout zit er NOG NIET in. Elke versie tot en met
            # midden valt dus af als verdachte. Dat is een MODUS TOLLENS (h. 24):
            # "als de fout er al in zat, zou deze versie falen; ze faalt niet; dus
            # de fout zat er nog niet in."
            links = midden + 1
        else:
            # Deze versie is stuk: de eerste stukke is deze, of een eerdere.
            # Alles na midden valt af.
            rechts = midden
    # Nu is links == rechts: er blijft precies één commit over.
    # return met twee waarden (hoofdstuk 11) geeft een TUPLE terug (hoofdstuk 13).
    return commits[links], pogingen


# De tuple uit de functie meteen uitpakken in twee variabelen.
commit, pogingen = zoek_eerste_stukke(COMMITS)
print(f"Eerste stukke commit : {commit}")
print(f"Aantal pogingen      : {pogingen}")
# LINEAIR zoeken: c01, c02, c03, ... testen tot je de eerste stukke tegenkomt. Om
# c43 te vinden, test je dus 43 versies. Lag de fout in c60, dan waren het er 60.
# Binair zoeken heeft er bij zestig commits nooit meer dan zes nodig, want 2 tot de
# zesde is 64: zes keer halveren brengt 60 kandidaten terug tot één.
print(f"Lineair zou kosten   : {EERSTE_STUKKE}")


# Verwachte uitvoer:
# Eerste stukke commit : c43
# Aantal pogingen      : 6
# Lineair zou kosten   : 43
