# Python basis — theoriebundel
# Hoofdstuk 5 — Variabelen, "constanten" en datatypes
# 5.7 De valkuil van kommagetallen
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

# fout
if totaal == 0.3:
    ...

# goed
if abs(totaal - 0.3) < 0.000001:
    ...

# beter, voor geld: reken in centen
prijs_in_cent = 3050          # 30,50 euro
