# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.4 Een knop die iets doet
#
# Een knop krijgt een functie mee met de optie command. Klikt de gebruiker, dan
# roept tkinter die functie op.
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

import tkinter as tk


# Deze functie is een CALLBACK: jij schrijft ze, maar je roept ze nergens zelf
# op. tkinter doet dat, telkens als iemand op de knop klikt.
def begroet():
    # config() is een methode van elke widget: ze verandert een optie achteraf.
    # Hier krijgt het label een nieuwe tekst.
    # groet is een variabele van BUITEN de functie. Dat werkt, omdat de functie
    # pas loopt bij een klik, en dan bestaat groet al. Mooi is het niet:
    # in 19.7 los je dat op met een klasse.
    groet.config(text="Welkom, lezer!")


venster = tk.Tk()
venster.title("Groeten")

# Het label dat straks van tekst verandert.
groet = tk.Label(venster, text="Klik op de knop.")
groet.pack(padx=40, pady=10)

# tk.Button is de klasse voor een knop.
#   text=    -> wat er op de knop staat
#   command= -> de functie die tkinter oproept bij een klik
# LET OP: command=begroet, ZONDER haakjes. Je geeft de functie zelf door.
# Met haakjes, command=begroet(), zou Python de functie nu meteen uitvoeren,
# en zou de knop de terugkeerwaarde (None) krijgen: klikken doet dan niets.
knop = tk.Button(venster, text="Zeg hallo", command=begroet)
knop.pack(pady=(0, 20))

# Vanaf hier wacht het programma. Elke klik op de knop roept begroet() op.
venster.mainloop()


# Wat je ziet: zie 19.04a-een-knop-die-iets-doet-voor.png (bij het starten)
# en 19.04a-een-knop-die-iets-doet-na.png (na een klik op Zeg hallo).
