import unittest

def dividetwonumbers(a,b):
    return a/b


class DevideTest(unittest.TestCase):
   def test1(self):
       c = dividetwonumbers(5,5) #1
       self.assertEqual(c,1)

   def test2(self):
       c = dividetwonumbers(5,5)
       self.assertNotEqual(c,5)


