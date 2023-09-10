# Zdefiniuj klasę Horse oraz Rider. Używając kompozycji, zamodeluj fakt, że koń może mieć jeźdźca

class Rider:
    def __init__(self, n, t, a, g):
        self.name = n
        self.truename = t
        self.age = a
        self.gender = g
        self.fullname = self.name + " " + self.truename

class Horse(Rider):
    def __init__(self, h, c, a, r, u):
        self.height = h
        self.color = c
        self.age = a
        self.race = r
        self.user = u

rider1 = Rider("Marcin",
               "Krasucki",
               "26",
               "M")

horse1 = Horse("183",
               "brown",
               "5",
               "andalusian",
               rider1)

print(horse1.user.name + " " + horse1.user.truename)
