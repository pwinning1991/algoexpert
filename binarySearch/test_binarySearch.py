import unittest
from binarySearch import binarySearch

class TestBinarySearch(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([1,5,23,111], 111),3)
    def test_case_2(self):
        self.assertEqual(binarySearch([1,5,23,111], 101),-1)
    def test_case_3(self):
        self.assertEqual(binarySearch([-5,-1,11,23,111], 11),2)
    def test_case_4(self):
        self.assertEqual(binarySearch([-5,-1,11,23,33,56,112], 112),6)



if __name__ == '__main__':
    unittest.main()
