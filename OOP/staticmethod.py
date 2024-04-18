class Math:
  @classmethod
  def add(cls, x, y):
    return x + y
  
class Utility:
  @staticmethod
  def greet(name):
    return f"Hello, {name}"

sum_result = Math.add(3, 5)
greet = Utility.greet("Virat")

print(sum_result)
print(greet)