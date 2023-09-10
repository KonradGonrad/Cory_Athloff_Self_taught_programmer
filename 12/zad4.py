# Zdefiniuj klasę Hexagon dysponującą metodą o nazwie calculate_perimeter, która oblicza i zwraca obwód sześciokąta. Następnie utwórz obiekt tej klasy, wywołaj jego metodę calculate_perimeter
# i wyświetl zwrócony wynik

class Hexagon:
    def __init__(self, a):
        self.a_length = a
        

    def calculate_perimeter(self):
        perimeter = self.a_length * 6
        return perimeter
    
hexagon = Hexagon(10)
print(hexagon.calculate_perimeter())