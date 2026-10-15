# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.2 try en except
#
# Zodra er in het try-blok iets misgaat, springt Python onmiddellijk naar except. De
# rest van het try-blok wordt overgeslagen:

try:
    print("een")
    getal = int("abc")
    print("twee")
except ValueError:
    print("fout")


# Verwachte uitvoer:
# een
# fout
