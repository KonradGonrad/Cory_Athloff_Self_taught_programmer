# Zdefiniuj klasę Circle dysponującą metodą area, która oblicza i zwraca pole koła. Następnie utwórz obiekt Circle, wywołaj jego metodę area i wyświetl wynik. Skorzystaj przy tym z funkcji
# pi dostępnej we wbudowanym module math
import math

class Circle_1:
    def __init__(self, r):
        self.radius = r
        

    def area(self):
        pi = float(3.14159)
        area_circle = pi * (self.radius)**2
        return area_circle

circle_1 = Circle_1(12)
print(circle_1.area())

class Circle_2:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        area = math.pi * math.pow(self.radius, 2)
        return area
    
circle_2 = Circle_2(12)
print(circle_2.area())