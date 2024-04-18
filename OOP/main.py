# Class:
class MyClass:
  pass


# Object Creation:
obj1 = MyClass()
obj2 = MyClass()

# Instance Variables and Initialization
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Accessing Instance Variables
person1 = Person("Kosin", 30)
person2 = Person("Kwan", 6)
print(person1.name)
print(person2.age)

# Methods:
class Dog:
  def bark(self):
    print("Woof!")

dog = Dog()
dog.bark()
