# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.7 Netjes tonen: de f-string — Opmaak binnen een f-string
#
# Dit is waar f-strings echt sterk worden.

bedrag = 1234.5678

print(f"{bedrag:.2f}")        # 1234.57      twee cijfers na de komma
print(f"{bedrag:10.2f}")      #    1234.57   rechts uitgelijnd in 10 tekens
print(f"{bedrag:<10.2f}")     # 1234.57      links uitgelijnd
print(f"{bedrag:,.2f}")       # 1,234.57     met duizendtalscheiding
print(f"{0.215:.1%}")         # 21.5%        als percentage
print(f"{42:05d}")            # 00042        opgevuld met nullen
