# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.3 Widgets: de bouwstenen van een venster
#
# Elke widget heeft opties die je meegeeft als benoemde argumenten:
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

import tkinter as tk

# Het hoofdvenster: één object van de klasse tk.Tk.
venster = tk.Tk()
venster.title("De Leeslamp")
venster.geometry("800x600")
# Een Label met extra opties:
#   font  -> een tuple: (lettertype, grootte, stijl). Stijl is "bold" of "italic".
#   fg    -> "foreground": de tekstkleur. Een naam ("gray") of een kleurcode
#            ("#15324a", rood-groen-blauw in hexadecimaal).
titel = tk.Label(venster, text="De Leeslamp",
                 font=("Segoe UI", 18, "bold"), fg="#15324a")

# pady=(20, 0) is een tuple: 20 pixels boven, 0 pixels onder.
# Zo plakt de ondertitel straks netjes onder de titel.
titel.pack(padx=30, pady=(150, 0))

# Een tweede Label-object. titel en ondertitel zijn twee OBJECTEN van dezelfde
# KLASSE tk.Label, elk met hun eigen tekst en kleur (zoals twee Boek-objecten
# in hoofdstuk 18 elk hun eigen titel hebben).
ondertitel = tk.Label(venster, text="Boekenclub voor wie graag leest",
                      fg="gray")

# Omgekeerd: 0 pixels boven, 20 pixels onder.
ondertitel.pack(padx=30, pady=(0, 20))

# Wil je een optie later nog veranderen, dan gebruik je de methode config():
#     titel.config(text="Gesloten")

# Start de gebeurtenislus: wacht tot de gebruiker het venster sluit.
venster.mainloop()


# Wat je ziet: zie 19.03-widgets-de-bouwstenen-van-een-venster.png
