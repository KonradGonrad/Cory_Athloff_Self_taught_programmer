import re

line = "Piękny jest lepszy niż brzydki."

matches1 = re.findall("Piękny", line)

print(matches1)

line = "Piękny jest lepszy niż brzydki. Za to Brzydki może też być Piękny"

matches2 = re.findall("piękny", line, re.IGNORECASE)

print(matches2)
