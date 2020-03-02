import calculus as c 
import unittest

class CalculusTest(unittest.TestCase):
  def test_add(self):
    self.assertEqual(c.add(1,3), 4) 
    self.assertEqual(c.add(2,3), 5) 
    self.assertEqual(c.add(-3,3), 0) 

  def test_sub(self):
    self.assertEqual(c.sub(1,3), -2)  

  def test_mult(self):
    self.assertEqual(c.mult(1,3), 3) 

  def test_div(self):
    self.assertEqual(c.div(1,1), float(1)) 

if __name__ == '__main__':
  unittest.main()