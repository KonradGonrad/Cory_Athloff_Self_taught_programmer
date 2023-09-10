# Napisz program zawierający pętlę nieskończoną ( z opcją naciśnięcia klawisza q w celu jej przerwania) oraz listę liczb. Podczas każdej iteracji tej pętli proś użytkownika o odgadnięcie
# liczby z listy, a następnie wyświetlaj informację, czy udało mu się poprawnie trafić, czy nie

import random

liczby = [5, 10, 13, 50, 34, 75]
liczba = random.choice(liczby)

while True:
    choose = input("Podaj liczbę większą dodatnią naturalną, lub \"q\", aby przerwać program: ")
    if choose == "q":
        print("Kończenie programu")
        break
    if int(choose) == liczba:
        print("Brawo, zgadłeś!")
        break
    elif int(choose) <= liczba:
        print("Nie zgadłeś. Za mało")
    elif int(choose) >= liczba:
        print("Nie zgadłeś. Za dużo")