# Encapsulation:
class Car:
  def __init__(self):
    self.__max_speed = 200
  def drive(self):
    print(f"Driving at max speed : {self.__max_speed}")

car = Car()
car.drive()