# Zmień klasę Square w taki sposób, by podczas wyświetlania obiektu Square był prezentowan komunikat o długości wszystkich boków danego kwadratu. Przykładowo w razie utworzenia obiektu Square(29)
# Python powinien wyświetlić komunikat 29 na 29 na 29 na 29

class Square:
    square_list = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.square_list.append((self.width,
                                self.len))

    def print_size(self):
        print("""{} na {} na {} na {}
              """.format(self.width, self.len, self.width, self.len))
        
sq1 = Square(10, 10)
sq1.print_size()