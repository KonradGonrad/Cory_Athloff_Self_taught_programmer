#Znajdź na swoim komputerze jakiś plik i wyświetl jego zawartość


with open(r"C:\Users\konra\Documents\xxxx.txt", "r") as f:
    print(f.read())