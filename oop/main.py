class Figure:
  def __init__(self, a=1, b=1):
    self.a = a
    self.b = b 
    self.c = "10000"

  @classmethod
  def perimeter(cls):
    return cls(2,3)

  @staticmethod
  def speed():
    pass

  def __str__(self):
    return "%s and %s and %s"%(self.a, self.b, self.c)

  def __repr__(self):
    return ""


class Triangle(Figure):
  pass 


t1 = Triangle(1,2)
f = Figure(2,3)

print(t1)
print(type(t1))
print(type(t1.perimeter()))
print(type(f.perimeter()))

