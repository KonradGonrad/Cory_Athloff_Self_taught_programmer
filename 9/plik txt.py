import os

os.path.join("Users",
             "konra",
             "Desktop",
             "Python",
             "Programista samouk",
             "9 - Pliki",
             "st.txt")

st = open("Programista samouk\9 - Pliki\st.txt", "w")
st.write("Cześć... zapisano z Pythona!")
st.close()


with open("Programista samouk\9 - Pliki\pt.txt", "w") as f:
    f.write("Hej!")

with open("Programista samouk\9 - Pliki\pt.txt", "r") as f:
    print(f.read())

my_list = list()

with open("Programista samouk\9 - Pliki\pt.txt", "r") as f:
    my_list.append(f.read())

print(my_list)