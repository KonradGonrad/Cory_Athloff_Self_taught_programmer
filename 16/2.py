# Napisz wyrażenie regularne, które zwróci wszystkie cyfry z łańcucha znaków Arizona 479, 501, 870. California 209, 213, 650.

import re

text = "Arizona 479, 501, 870. California 209, 213, 650."

trzy_cyfrowe = re.findall("\\d\d\d", text)
pojedyncze = re.findall("\\d", text)
print("Wszystkie liczby trzycyfrowe: ",trzy_cyfrowe)
print("Wszystkie liczby pojedyńcze: ", pojedyncze)