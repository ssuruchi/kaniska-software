# Create class, object, instance attributes for any entity (vehicle, player, 
# animals, etc). Use the concepts of Inheritance, Polymorphism, 
# Encapsulation, and Abstraction with respect to the class created

from abc import ABC

# Created Class
# Abstract Base Class for Abstraction.
class Animal(ABC):
    def __init__(self, name, age): 
        # Encapsulation
        # Protected Instance Attribute -> self._name
        # instance attributes of entity -> self.age, self.species
        self._name = name
        self.age = age
        self.species = None
    def getSpecies(self):
        # getter method
        return self.species
    def setSpecies(self, species):
        # setter method
        self.species = species
    def makeSound(self):
        # Abstraction
        pass
    def display(self):
        print(self._name)

# Inherited Animal class
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.setSpecies("Dog")
    def makeSound(self, sound = "Woof"):
        # Polymorphism
        return sound
    
# Inherited Animal class
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.setSpecies("Cat")
    def makeSound(self):
        return "Meow!"

# Instance of Dog Class
obj1 = Dog("Bruno", 2)
print(obj1._name, obj1.age, obj1.getSpecies(), obj1.makeSound("Bark!"))

# Instance of Cat Class
obj2 = Cat("Kitty", 3)
print(obj2._name, obj2.age, obj2.getSpecies(), obj2.makeSound())
