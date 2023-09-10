# Napisz program zawierający pętlę nieskończoną ( z opcją naciśnięcia klawisza q w celu jej przerwania) oraz listę liczb. Podczas każdej iteracji tej pętli proś użytkownika o odgadnięcie
# liczby z listy, a następnie wyświetlaj informację, czy udało mu się poprawnie trafić, czy nie
import random

liczby = ["5", "10", "43", "35", "51", "73"]
liczba = random.choice(liczby)
print(liczba)
while True:
    print("Witaj w grze w \"Zgadnij liczbę\"")
    choose = input("Twoim zadaniem jest, aby odgadnąć liczbę, podając ją niżej. Jeżeli chcesz przerwać, zamiast liczby wpisz \"q\" \nPodaj liczbę: ")
    if choose > liczba:
        print("Za dużo. Nie trafiłeś")
    elif choose < liczba:
        print("Za mało. Nie Trafiłeś")
    elif choose == liczba:
        print("Brawo. Trafiłeś!")
        break
    elif choose == "q":
        break
    