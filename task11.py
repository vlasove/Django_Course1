def myVariadic(*args):
  print(type(args))
  print(args)

def myKWVariadic(*args, **kwargs):
  print(type(kwargs))
  print(kwargs)

myKWVariadic(name= "Bob", lastname = "Jack")

def ComboFunc(a,b, d, c = 20):
  return a + b + c + d

ComboFunc(1,2,3)

func_list = [ComboFunc, myKWVariadic, myVariadic]
a = ComboFunc
def ULTRAFUNC():
  return ComboFunc


print((lambda x, y: x + y)(1,2))

a = [10,20,-30,40,-1,2]
a.sort(key= lambda y: abs(y))
print(a)

def Add(x):
  def SubAdd(y):
    def SubSubAdd(z):
      return x + y + z 
    return SubSubAdd
  return SubAdd


print(Add(5)(3)(2))

