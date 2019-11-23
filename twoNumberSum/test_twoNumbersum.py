import unittest
from twoNumberSum import twoNumbersSum

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = sorted(twoNumbersSum([4,6], 10))
        self.assertEqual(output, [4,6])


if __name__ == '__main__':
    unittest.main()
