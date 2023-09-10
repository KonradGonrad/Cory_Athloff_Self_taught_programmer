# Napisz wyrażenie regularne, które będzie odnajdywać słowa zaczynające się od dowolnej litery, po której będą umieszczone dwie litery o. Następnie użyj modułu re Pythona, by odszukać takie słowa
# w łańcuchu "Bieg na orientację dookoła miejskiego zoo."

import re

text = "Bieg na orientację dookoła miejskiego zoo."

m = re.findall(".oo.*?", text, re.IGNORECASE)

print(m)