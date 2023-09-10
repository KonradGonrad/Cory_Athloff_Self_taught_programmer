# Zdefiniuj klasy Rectangle i Square metodą calculate_perimeter obliczającą obwod danej figury. Utwórz obiekty Rectangle i Square, a następnie wywołaj ich metodę calculate_perimeter

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
        
    def calculate_perimeter(self):
        perimeter = self.width * self.len
        return perimeter



class Square:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def calculate_perimeter(self):
        perimeter = self.width * self.len
        return perimeter


kwadrat = Square(10, 2)
print(kwadrat.calculate_perimeter())
prostokąt = Rectangle(15, 5)
print(prostokąt.calculate_perimeter())