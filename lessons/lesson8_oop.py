# Classes and Objects
from typing import override


print("--- Object-Oriented Programming ---")

class Dog:
    """A simple class to represent a dog"""

    def __init__(self, name, age, breed):
        """Constructor method - called when creating"""
        self.name = name 
        self.age = age
        self.breed = breed
    
    def bark(self):
        """Method to make the dog bark"""
        return f"{self.name} says: Woof!"

    def get_info(self):
        """Method to get dog information"""
        return f"{self.name} is a {self.age}-year-old {self.breed}"

    def have_birthday(self):
        """Method to increment age"""
        self.age += 1
        return f"{self.name} is now {self.age} years old!"
    
    #Creating objects
my_dog = Dog("Buddy", 3, "Golden Reiever")
print(my_dog.get_info())
print(my_dog.bark())
print(my_dog.have_birthday())

# Inheritance
class Puppy(Dog):
    """A class that inherits from Dog"""

    def __init__(self, name, breed):
        super().__init__(name, 0, breed)

    def bark(self):
        return f"{self.name} says: Yip yip!"

    def play(self):
        return f"{self.name} is playing with a ball!"

# Creating a puppy object
my_puppy = Puppy("Max", "Labridor")
print(my_puppy.get_info())
print(my_puppy.bark())
print(my_puppy.play())