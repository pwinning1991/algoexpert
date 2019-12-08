import unittest
import threeNumberSum


class TestThreeNumberSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(threeNumberSum.threeNumberSum([12,3,1,2,-6,5,-8,6], 0), [[-8,2,6],[-8,3,5],[-6,1,5]] )

    def test2(self):
        self.assertEqual(threeNumberSum.threeNumberSum([1,2,3], 6), [[1,2,3]] )

    def test3(self):
        self.assertEqual(threeNumberSum.threeNumberSum([1,2,3], 7), [] )
