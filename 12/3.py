class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("utworzono")

orl = Orange(120, "pomaranczowy")
print(orl.weight)
print(orl.color)
orl.weight = 390
orl.color = "ciemnopomarańczowy"
print(orl.weight)
print(orl.color)