from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def sound(self):
        print("Dog eats")

d1 = Dog()
d1.sound()
d1.eat()