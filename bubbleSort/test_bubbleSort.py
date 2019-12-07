import unittest
import bubbleSort

class TestbubbleSort(unittest.TestCase):
    def test1(self):
        self.assertEqual(bubbleSort.bubbleSort([8,5,2,9,5,6,3]), [2,3,5,5,6,8,9])


    def test2(self):
        self.assertEqual(bubbleSort.bubbleSort([0]), [0])

    def test3(self):
        self.assertEqual(bubbleSort.bubbleSort([5,3,0,11]), [0,3,5,11])

    def test3(self):
        self.assertEqual(bubbleSort.bubbleSort([10,3,-6,-2]), [-6,-2,3,10])
