import unittest
import find as f

class TestThreeLarge(unittest.TestCase):
    def test_1(self):
        test = f.findThreeLargestNumbers([4,3,1])
        self.assertEqual(test, [1,3,4])

    def test_2(self):
        test = f.findThreeLargestNumbers([141,1,17,-7,-17,-27,18,541,8,7,7])
        self.assertEqual(test, [18,141,541])

    def test_3(self):
        test = f.findThreeLargestNumbers([0,0,0])
        self.assertEqual(test, [0,0,0])
