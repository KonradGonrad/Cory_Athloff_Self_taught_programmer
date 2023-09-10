import re

zen = """Lepiej teraz niż nigdy.
Choć zazwyczaj
nigdy
jest lepsze od *już* teraz.
Jeśli trudno ci wyjaśnić implementację,
to jej użycie będzie złym pomysłem.
Jeśli jednak łatwo ci wyjaśnić,
to może jest warta zachodu?
"""

m = re.findall("^Jeśli", zen, re.MULTILINE)
n = re.findall("nigdy.$", zen, re.MULTILINE)
print(m)
print(n)