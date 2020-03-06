def BAD():
  #print(1/0)
  [1,2][3]
try:
  BAD()
except ZeroDivisionError as zerr:
  print("SOMETHING WRONG:", zerr)
except IndexError as ierr:
  print(ierr)
except:
  pass 
finally:
  print("IMMORTAL RUN!")



def f(**kwargs):
  print(kwargs) 

f()

