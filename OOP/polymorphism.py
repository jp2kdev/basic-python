# Polymorphism:
class Computer:
  def cal(self):
    pass

class Labtop(Computer):
  def cal(self):
    print("Calculator")

class PC(Computer):
  def cal(self):
    print("Personal Computer")

computers = [Labtop(), PC()]
for computer in computers:
  computer.cal()