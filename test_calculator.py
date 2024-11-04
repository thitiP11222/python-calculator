import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # give parameter and expect output

    # Add the following test methods to the TestCalculator class:
    # test_add
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-2, -2), -4)
    def test_add_zero(self):
        self.assertEqual(self.calc.add(4, 0), 4)

    #test_substract
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(1, 3), 2)
        
    def test_subtract_negetive(self):
        self.assertEqual(self.calc.subtract(1, -1), -2)
        
    #test_multiply
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(2, 10), 20)
        
    def test_multiply_negetive(self):
        self.assertEqual(self.calc.multiply(-1, 2), -2)
        
    #test-divide
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(13, 2), 6)
    def test_divide_negetive(self):
        self.assertEqual(self.calc.divide(12, -2), -6)  

    #test_modulo
    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
    def test_modulo_negetive(self):
        self.assertEqual(self.calc.modulo(-10, -9), -1)  
        
if __name__ == '__main__':
    unittest.main()