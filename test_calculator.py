import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 5), 7)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        self.assertEqual(self.calc.multiply(8, 5), 40)
        self.assertEqual(self.calc.multiply(20, 10), 200)
        self.assertEqual(self.calc.divide(8, 4), 2)  
        self.assertEqual(self.calc.divide(60, 3), 20) 
        self.assertEqual(self.calc.modulo(10, 3), 1) 
        self.assertEqual(self.calc.modulo(50, 6), 2) 

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()