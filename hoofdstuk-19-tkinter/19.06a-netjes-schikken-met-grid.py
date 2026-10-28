# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.6 Netjes schikken met grid
#
# pack() zet widgets onder of naast elkaar. Voor een formulier met labels en
# invoervelden is dat onhandig: je wilt de velden mooi onder elkaar uitgelijnd.
# Daarvoor bestaat grid(). Het werkt als een tabel met rijen en kolommen, en je
# telt vanaf nul, zoals bij een lijst.
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

import tkinter as tk

venster = tk.Tk()
venster.title("Nieuw lid")

# grid() zet een widget in een cel van een onzichtbare tabel:
#
#              kolom 0       kolom 1
#   rij 0      Naam:         [............]
#   rij 1      Leeftijd:     [............]
#   rij 2                    [ ] Student
#   rij 3          [ Bewaar ]   (over beide kolommen)
#
# sticky="w" -> de widget kleeft aan de westkant (links) van zijn cel.
# Zonder sticky staat hij in het midden van de cel.
tk.Label(venster, text="Naam:").grid(row=0, column=0, sticky="w",
                                     padx=10, pady=5)

# Het invoerveld maak je EERST en plaats je DAARNA op een aparte regel.
# Waarom? grid() geeft None terug. Schrijf je alles op één regel,
#     naam_veld = tk.Entry(venster).grid(...)
# dan zit er None in naam_veld, en faalt naam_veld.get() later.
naam_veld = tk.Entry(venster, width=25)
naam_veld.grid(row=0, column=1, padx=10, pady=5)

tk.Label(venster, text="Leeftijd:").grid(row=1, column=0, sticky="w",
                                         padx=10, pady=5)
leeftijd_veld = tk.Entry(venster, width=25)
leeftijd_veld.grid(row=1, column=1, padx=10, pady=5)

# Een Checkbutton (aanvinkvakje) heeft GEEN get(). Zijn toestand zit in een
# aparte tkinter-variabele: een object van de klasse tk.BooleanVar.
# Het vakje en je programma delen die ene variabele:
#   student.get()      -> True als het vakje aangevinkt is, anders False
#   student.set(True)  -> vinkt het vakje aan vanuit je code
# (Er bestaan ook tk.StringVar voor tekst en tk.IntVar voor gehele getallen.)
student = tk.BooleanVar()

# variable=student koppelt het vakje aan die BooleanVar.
# Het vakje staat in kolom 1, onder de invoervelden.
tk.Checkbutton(venster, text="Student", variable=student).grid(
    row=2, column=1, sticky="w", padx=5)

# columnspan=2 -> de knop strekt zich uit over 2 kolommen, en staat daardoor
# mooi in het midden onder het formulier.
# (Deze knop heeft nog geen command: hij doet nog niets. Dat volgt in 19.9.)
tk.Button(venster, text="Bewaar").grid(row=3, column=0, columnspan=2,
                                       pady=10)

# LET OP: gebruik nooit pack() en grid() door elkaar in hetzelfde venster.
# Dan krijg je een TclError. Wil je toch beide, groepeer dan met een tk.Frame
# (zie oefening 19.2).

venster.mainloop()


# Wat je ziet: zie 19.06a-netjes-schikken-met-grid.png
