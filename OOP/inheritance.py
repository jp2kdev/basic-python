# Inheritance:
class Animal:
  def speak(self):
    pass

class Cat(Animal):
  def speak(self):
    print('Woof!')

cat = Cat()
cat.speak()