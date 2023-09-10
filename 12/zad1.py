#  Zdefinuij klasę Apple, dysponującą czterema zmiennymi instancyjnymi reprezentującymi cztery różne cechy jabłek

class Apple:
    def __init__(self, w, c, t):
        self.weight = w
        self.color = c
        self.type = t
        print("utworzono")
    
    def rot(self, days, temperature):
        self.mold = days * temperature

    def change_values(self, w, c, t):
        self.weight = w
        self.color = c
        self.type = t

apple1 = Apple(210, "zielony", "papierówka") 
print("Jabłko waży", apple1.weight, " Jest koloru", apple1.color, "oraz jego gatunek to", apple1.type)
apple1.rot(2, 29)
apple1.change_values(310, "czerwony", "papierówka")
print("Jabłko waży", apple1.weight, " Jest koloru", apple1.color, "oraz jego gatunek to", apple1.type)