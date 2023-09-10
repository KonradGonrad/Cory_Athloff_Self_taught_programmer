import re

text = "Kocham $pieniądze$"

m = re.findall("\\$",
               text,
               re.IGNORECASE)

print(m)