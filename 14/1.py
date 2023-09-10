#Do klasy Square dodaj zmienną klasową o nazwie square_list, w której będą zapisywane wszystkie tworzone obiekty klasy Square

class Square:
    square_list = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.square_list.append((self.width,
                                self.len))

    def print_size(self):
        print("""{} na {}
              """.format(self.width, self.len))
        

sq = Square(10,10)
sq.print_size
sq1 = Square(20,20)
sq2 = Square(100,100)
print(sq.square_list)