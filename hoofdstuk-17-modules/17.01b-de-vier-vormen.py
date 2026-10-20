# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.1 Importeren — De vier vormen

import math
from math import sqrt, pi
from math import sqrt as wortel
import math as m

print(math.sqrt(16), sqrt(16), wortel(16), m.sqrt(16))


# Verwachte uitvoer:
# 4.0 4.0 4.0 4.0
