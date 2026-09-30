# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Klassikale oefening 12.2 — Wat verandert er, en wat niet?, uitwerking
#
# Het antwoord lijkt te kloppen, en dat is precies het gevaar. Kijk wat er gebeurt bij
# een lijst met twee opeenvolgende doelwitten:

lijst = ["a", "b", "b", "c"]
for x in lijst:
    if x == "b":
        lijst.remove(x)
print(lijst)


# Verwachte uitvoer:
# ['a', 'b', 'c']
