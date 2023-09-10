import re

text = "Dwa drwa a czar trwaa"

m = re.findall("rwa*", text, re.IGNORECASE)
print(m)

text2 = "__Siemka__stary"

m = re.findall("__.*__", text2, re.IGNORECASE)
print(m)

text3 = "_Hej_jak_się_masz_?"

m = re.findall("_.*_", text3, re.IGNORECASE)
n = re.findall("_.*?_", text3, re.IGNORECASE)

print(m)
print(n)

t = "_jeden__dwa__trzy_"
results = re.findall("_.*?_", t)

for match in results:
    print(match)