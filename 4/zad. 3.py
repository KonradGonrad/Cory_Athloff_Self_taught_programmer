# Napisz funkcję, która ma trzy wymagane parametry i dwa parametry opcjonalne
def rarara(choose, y, z, c = 2, v = 3):
    """
    calculator, returns what user choose.
    :param choose: int.
    :param y: int.
    :param z: int.
    :param c: int.
    :param v: int.
    """
    if choose == 1:
        wynik = y + z
    elif choose == 2:
        wynik = y - z
    elif choose == 3:
        wynik = y * z
    elif choose == 4:
        wynik = y / z
    elif choose == 5:
        wynik = (y + z) ** c
    elif choose == 6:
        wynik = (y + z) ** v
    return wynik

choose = int(input("Witaj w prostym kalkulatorze \nWybierz jakie działanie chcesz wykonać: \n1.Dodawanie \n2.Odejmowanie \n3.Mnożenie \n4.Dzielenie \n5.Kwadrat sumy liczb \n6.szescian sumy liczb \nWybor: "))
y = int(input("Podaj pierwszą liczbę: "))
z = int(input("Podaj drugą liczbę: "))

print(rarara(choose, y, z))



