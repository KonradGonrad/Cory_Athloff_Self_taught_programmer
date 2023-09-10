class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} na {}""".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len
    
    def print_size(self):
        print("""Moje wymiary to: {} na {}. A moje pole wynosi: {}
              """.format(self.width, self.len, Square.area(self)))
        
a_square = Square(20, 20)
a_square.print_size()