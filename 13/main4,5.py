class Person():
    def __init__(self, name):
        self.name = name

class Dog(Person):
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner

mick = Person("Mick Jagger")
stan = Dog("Stanley",
           "Bulldog",
           mick)

print(stan.owner.name)
