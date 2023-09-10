# W klasie Square zdefiniuj metodę change_size, która pozwoli zwiększać lub zmniejszać ( w razie przekazania wartości ujemnej ) długości krawędzi kwadratu o podaną wartość

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
    
    def change_size(self, x):
        self.width = self.width + x


kwadrat = Square(10, 2)
print(kwadrat.calculate_perimeter())
prostokąt = Rectangle(15, 5)
print(prostokąt.calculate_perimeter())
kwadrat.change_size(-1)
print(kwadrat.calculate_perimeter())