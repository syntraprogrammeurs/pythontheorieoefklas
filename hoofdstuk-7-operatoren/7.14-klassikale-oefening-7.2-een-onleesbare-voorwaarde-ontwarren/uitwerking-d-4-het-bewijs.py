# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.2 — Een onleesbare voorwaarde ontwarren, uitwerking
#
# Er zijn vijf ingangen, dus tweeëndertig gevallen. Die loop je niet met de hand af;
# dat laat je de computer doen.

def oud(is_lid, leeftijd, begeleid, aantal, heeft_boete):
    return (not (not is_lid or (leeftijd < 12 and not begeleid) or aantal >= 5)
            and not heeft_boete)


def nieuw(is_lid, leeftijd, begeleid, aantal, heeft_boete):
    oud_genoeg = leeftijd >= 12 or begeleid
    onder_de_limiet = aantal < 5
    in_orde = not heeft_boete
    return is_lid and oud_genoeg and onder_de_limiet and in_orde


verschillen = 0
gevallen = 0
for is_lid in (False, True):
    for leeftijd in (8, 12, 40):
        for begeleid in (False, True):
            for aantal in (0, 4, 5, 9):
                for heeft_boete in (False, True):
                    gevallen += 1
                    a = oud(is_lid, leeftijd, begeleid, aantal, heeft_boete)
                    b = nieuw(is_lid, leeftijd, begeleid, aantal, heeft_boete)
                    if a != b:
                        verschillen += 1
                        print("VERSCHIL:", is_lid, leeftijd, begeleid, aantal, heeft_boete)

print(f"{gevallen} gevallen getest, {verschillen} verschillen")


# Verwachte uitvoer:
# 96 gevallen getest, 0 verschillen
