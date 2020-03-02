def my_func(a :int, b :int) -> int:
  print(a)
  return a + b 

c = my_func("asdas","asdas")
print(c)

def myUtf(a = 1 ,b = 1):
  print("Default value func",a,b)

myUtf()
myUtf(10,20)
myUtf(b = 10)


