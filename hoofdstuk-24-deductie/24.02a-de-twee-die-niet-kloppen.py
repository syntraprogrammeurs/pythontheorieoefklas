# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.2 De vier vormen met "als … dan" — De twee die niet kloppen
#
# Vertaald naar code is dit de else-tak die te veel aanneemt.
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

# LET OP: dit is een FRAGMENT. De namen geschorst, weiger en leen_uit bestaan in dit
# bestand niet. Start je het toch, dan stopt Python meteen op de eerste regel met
# NameError: name 'geschorst' is not defined. Lees het als een stukje code dat je
# ergens in een groter programma zou tegenkomen.
#
# Wat het fragment toont: de drogreden ONTKENNEN VAN HET ANTECEDENS uit 24.2.
# De regel van de bibliotheek is een IMPLICATIE (hoofdstuk 23):
#     p -> q      "als een lid geschorst is (p), dan mag het niet lenen (q)"
# p heet het ANTECEDENS (wat voorafgaat), q het CONSEQUENS (wat volgt).
#
# De if-tak hieronder is in orde: dat is MODUS PONENS. p is waar, dus doe je q.
# De else-tak is het probleem. Die redeneert zo:
#     als geschorst, dan weigeren. Niet geschorst. Dus NIET weigeren.
# Dat is p -> q, niet p, dus niet q: ongeldig. De regel zegt alleen wat er gebeurt
# bij schorsing. Over alle andere gevallen (lidgeld niet betaald, te veel boeken
# thuis, een boek te laat) zegt hij niets. De else doet alsof schorsing de ENIGE
# reden is om te weigeren.

# Is het lid geschorst? Dan weigeren: dit deel klopt (modus ponens).
if geschorst:
    weiger()
# else betekent "in alle andere gevallen". Hier zit de fout: niet geschorst wil nog
# niet zeggen dat alles in orde is. Een lid dat zijn lidgeld niet betaalde, komt
# hier ook terecht en krijgt toch een boek mee.
else:
    leen_uit()          # ontkennen van het antecedens, in Python

# Hoe het wel moet, zie je in hoofdstuk 25: in 25.6 (fout 1, de else die te veel
# aanneemt) en in 25.7 (bewaakclausules: elke reden om te weigeren apart).
