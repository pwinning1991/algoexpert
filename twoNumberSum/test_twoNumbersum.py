import unittest
from twoNumberSum import twoNumbersSum

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = sorted(twoNumbersSum([4,6], 10))
        self.assertEqual(output, [4,6])
    def test_case_2(self):
        output = sorted(twoNumbersSum([4,6], 5))
        self.assertEqual(output, [])
    def test_case_3(self):
        output = sorted(twoNumbersSum([4,6,5,-3,-5,33,103,1], 5))
        self.assertEqual(output, [1,4])

if __name__ == '__main__':
    unittest.main()
