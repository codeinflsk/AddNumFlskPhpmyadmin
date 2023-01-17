import unittest

def addTwoNumbers(a,b):
    return a+b


class AddTest(unittest.TestCase):
   def test1(self):
       c = addTwoNumbers(4,5) #9
       self.assertEqual(c,9)

   def test2(self):
       c = addTwoNumbers(4,5)
       self.assertNotEqual(c,5)

