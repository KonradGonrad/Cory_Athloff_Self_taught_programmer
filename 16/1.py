# Napisz wyrażenie regularne, które zostanie dopasowane do słowa Holendrem, z tekstu w pliku zen.txt

import re

zen ="""Piękne jest lepsze niż brzydkie.
Wyraźne jest lepsze niż ukryte.
Proste jest lepsze niż złożone.
Złożone jest lepsze niż skomplikowane.
Mieszkanie jest lepsze niż zagnieżdżone.
Rzadkie jest lepsze niż gęste.
Liczy się czytelność.
Specjalne przypadki nie są na tyle wyjątkowe, aby łamać zasady.
Choć praktyczność przewyższa czystość.
Błędy nigdy nie powinny przechodzić cicho.
Chyba, że zostanie wyraźnie uciszony.
W obliczu niejasności odrzuć pokusę zgadywania.
Powinien istnieć jeden - a najlepiej tylko jeden - oczywisty sposób, aby to zrobić.
Chociaż na początku może to nie być oczywiste, chyba że jesteś Holendrem.
Teraz jest lepiej niż nigdy.
Chociaż nigdy nie jest często lepsze niż *w tej chwili*.
Jeśli wdrożenie jest trudne do wyjaśnienia, jest to zły pomysł.
Jeśli wdrożenie jest łatwe do wyjaśnienia, może to być dobry pomysł.
Przestrzenie nazw to naprawdę świetny pomysł — róbmy ich więcej!
"""

m = re.findall("Holendrem", zen, re.IGNORECASE)

print(m)
for guess in m:
    print(zen.index(guess))