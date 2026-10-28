# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.7 Je venster als klasse
#
# Stel dat het venster moet tellen hoe vaak er geklikt is. Met een gewone functie
# heb je dan een variabele nodig die tussen twee klikken blijft bestaan:
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

# Een teller die moet blijven bestaan tussen twee klikken. Een lokale variabele
# in klik() zou bij elke klik opnieuw op 0 beginnen, dus staat hij buiten de
# functie, als globale variabele.
klikken = 0


def klik():
    # Zonder "global" denkt Python dat klikken een NIEUWE lokale variabele is,
    # en geeft klikken += 1 een UnboundLocalError.
    # Dit werkt, maar het is precies wat hoofdstuk 11 je afleerde: met tien
    # velden heb je tien globals. De betere oplossing: een klasse (zie 19.07b).
    global klikken
    klikken += 1
    melding.config(text=f"{klikken} keer geklikt.")
