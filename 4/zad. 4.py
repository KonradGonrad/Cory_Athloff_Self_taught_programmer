#Napisz program definiujący dwie funkcje. Pierwsza z nich powinna pobierać parametr będący liczbą całkowitą i zwracać tę liczbę podzieloną przez 2. 
#Druga funkcja także ma pobierać parametr typu int, lecz zwracać wartość tego parametru pomnożoną razy 4.
#Główna część programu ma wywoływać pierwszą funkcję, zapisywać zwrócony przez nią wynik w zmiennej, a następnie przekazywać go w wywołaniu drugiej funkcji

def przez_dwa(x):
    """
    print out parameter divided by 2.
    :param x: int.
    """
    wynik = int(x / 2)
    print(wynik)

def razy_cztery(x):
    """
    print out parameter multiplied by 4.
    :param x: int.
    """
    wynik = int(x * 4)
    print(wynik)

print("Witaj użytkowniku!")
x = int(input("Proszę podać parametr w postaci liczby całkowitej: "))
przez_dwa(x)
razy_cztery(x)
