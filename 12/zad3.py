# Zdefiniuj klasę Triangle dysponującą metodą area, która oblicza i zwraca pole trójkąta. Następnie utwórz obiekt Triangle, wywołaj jego metodę area i wyświetl uzyskany wynik

def pole_trojkata():
    print("Kalkulator pola trójkąta \n")
    a = int(input("Podaj długość podstawy trójkąta: "))
    h = int(input("Podaj wysokość trójkąta: "))
    triangle = Triangle(a, h)
    print("Pole trójkąta wynosi: ",triangle.area())



class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.height = h
    
    def area(self):
        wynik = 0.5 * (self.a * self.height)
        return wynik
    
pole_trojkata()