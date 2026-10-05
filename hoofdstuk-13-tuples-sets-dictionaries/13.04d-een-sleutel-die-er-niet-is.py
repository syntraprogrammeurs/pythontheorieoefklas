# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.4 Dictionaries — Een sleutel die er niet is
#
# Er zijn drie manieren om dat te vermijden:

lid = {"naam": "Anke"}

print("telefoon" in lid)
print(lid.get("telefoon"))
print(lid.get("telefoon", "onbekend"))


# Verwachte uitvoer:
# False
# None
# onbekend
