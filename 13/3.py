# Utwórz klasę Square. Zdefiniuj w niej metodę what_am_i, która będzie wyświetlać łańcuch znaków "Jesteś figurą". Zmodyfikuj klasy Square i Rectangle z poprzednich zadań, tak dziedziczyły po 
# klasie Shape. Utwórz obiekty Square i Rectangle, a następnie wywołaj ich metodę what_am_i

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} na {}""".format(self.width, self.len))

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
        
    def calculate_perimeter(self):
        perimeter = self.width * self.len
        return perimeter



class Square(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def calculate_perimeter(self):
        perimeter = self.width * self.len
        return perimeter
    
    def change_size(self, x):
        self.width = self.width + x

    def what_am_i(self):
        text = "Jestes figura"
        print(text)
        
    def what_am_i_2(self):
        text = "Jestes figura"
        return text

rectangle = Rectangle(10, 4)
rectangle.print_size()
square = Square(10,10)
square.print_size()
square.what_am_i()
print(square.what_am_i_2())
