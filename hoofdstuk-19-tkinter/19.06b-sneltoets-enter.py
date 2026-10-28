# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.6 Netjes schikken met grid — Sneltoets
#
# Laat Enter hetzelfde doen als klikken op de knop:
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf. Zet de regel vóór venster.mainloop() in
# 19.05-invoer-lezen-en-meldingen-tonen.py, dan werkt Enter daar als de knop.

# bind() is een methode van elke widget (ook van het venster). Ze koppelt een
# GEBEURTENIS aan een functie:
#   "<Return>"  -> de gebeurtenis: de gebruiker drukt op Enter
#   de lambda   -> wat er dan moet gebeuren
#
# Verschil met command van een knop: bind geeft ALTIJD één argument mee, een
# "event"-object met informatie over de gebeurtenis (welke toets, waar, ...).
# Daarom heeft de lambda een parameter event, ook al gebruik je hem niet.
# Met "lambda: controleer()" krijg je bij Enter:
#   TypeError: <lambda>() takes 0 positional arguments but 1 was given
import tkinter as tk

venster = tk.Tk()
venster.bind("<Return>", lambda event: controleer())
