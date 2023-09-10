# Napisz funkcję, która pobiera dwa obiekty jako parametry i zwraca True, jeśli okaże się że są to te same obiekty, oraz wartość False w przeciwnym przypadku

class Person():

    def __init__(self, name, truename, age, eye_color, hair_color):
        self.name = name
        self.truename = truename
        self.age = age 
        self.eye_color = eye_color
        self.hair_color = hair_color


class Sprawdzenie():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sprawdzenie(self):
        if self.x is self.y:
            return True
        else:
            return False

person1 = Person("Konrad", "Kargul", "18", "green", "brown")
person2 = Person("Bogdan", "Cichy", "61", "brown", "brown")
person3 = person1
person4 = person1.name

sprawdzenie1 = Sprawdzenie(person1, person2)
print(sprawdzenie1.sprawdzenie())
sprawdzenie2 = Sprawdzenie(person3, person1)
print(sprawdzenie2.sprawdzenie())
sprawdzenie3 = Sprawdzenie(person4, person1)
print(sprawdzenie3.sprawdzenie())
