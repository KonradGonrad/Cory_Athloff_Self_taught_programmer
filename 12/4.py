class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("utworzono")
    
    def rot(self, days, temp):
        self.mold = days * temp

orl = Orange(120, "pomaranczowy")
print(orl.mold)
orl.rot(10, 29)
print(orl.mold)