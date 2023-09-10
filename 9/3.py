# Napisz program który zapisze w pliku CSV zawartość następującej listy list:
# [["Top gun", "Ocean's Eleven", "Raport mniejszości"], ["Titanic", "Ostatni Jedi", "Incepcja"], ["Pulp fiction", "Człowiek w ogniu", "Seksmisja"]] 
# Dane z każdej z list powinny zostać zapisane w osobnych wierszach i rozdzielone przecinkami
import csv

lista = [["Top gun", "Ocean's Eleven", "Raport mniejszości"], ["Titanic", "Ostatni Jedi", "Incepcja"], ["Pulp fiction", "Człowiek w ogniu", "Seksmisja"]] 

with open(r"C:\Users\konra\Desktop\Python\Programista samouk\9 - Pliki\lista.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    for each in lista:
        write.writerow(each)
        