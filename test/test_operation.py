
import unittest
from src.math_operation import add, sub

class TestMathOperation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(2, 2), 0)
        self.assertEqual(sub(-1, 1), -2)

if __name__ == '__main__':
    unittest.main()
  
