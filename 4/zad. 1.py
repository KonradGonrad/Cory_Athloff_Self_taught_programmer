# Napisz funkcję, która pobiera liczbę i zwraca tę liczbę podniesioną do kwadratu

def do_kwadratu():
    """
    return/print out: x**2.
    :input x: str.
    :convert str(x): into int(x).
    :print out: x**2.
    """
    x = input("Podaj liczbę, którą chcesz podnieść do kwadratu: ")
    x = int(x)
    print(x**2)

do_kwadratu()