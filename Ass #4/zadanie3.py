# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print("wykonanie foo(" + str(self) + ", " + str(x) + ")")

    @classmethod
    def class_foo(self, x):
        print("class_foo(" + str(self) + ", " + str(x) + ")")

    @staticmethod
    def static_foo(x):
        print("wykonanie static_foo(" + str(x) + ")")

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Samochod(ABC):
    @abstractmethod
    def dzwiek(self):
        pass

class Diesel(Samochod):
    def dzwiek(self):
        print("klekleklekle")

class Benzyna(Samochod):
    def dzwiek(self):
        print("pyrpyrpyrpyr")

d = Diesel()
b = Benzyna()
d.dzwiek()
b.dzwiek()


# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Promien musi byc dodatni.")
        self._radius = value

    def area(self):
        return math.pi * self._radius**2

circle_instance = Circle(radius=5)
print("Promien kola:", circle_instance.radius)
print("Pole powierzchni kola: ",circle_instance.area())
circle_instance.radius = 7
print("Nowy promien kola:", circle_instance.radius)

try:
    circle_instance.radius = -3
except ValueError as e:
    print(e)

