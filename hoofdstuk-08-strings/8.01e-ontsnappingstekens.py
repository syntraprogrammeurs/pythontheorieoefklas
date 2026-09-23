# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.1 Tekst maken — Ontsnappingstekens
#
# Op Windows zit hier een valkuil. Een pad als "C:\nieuw\map" bevat \n en \m, en
# Python leest \n als een nieuwe regel. Zet er een r voor om de backslash letterlijk
# te nemen:

pad = r"C:\nieuw\map"
