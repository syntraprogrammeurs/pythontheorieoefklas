# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.7 Tekst herhalen en samenvoegen
#
# Voeg nooit tekst samen in een lus met +:

regel = ""
for woord in ["een", "twee", "drie"]:
    regel = regel + woord + " "
