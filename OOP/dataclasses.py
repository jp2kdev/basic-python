from dataclasses import dataclass

@dataclass
class Point:
  x: int
  y: int

p = Point(3, 4)
print(p)