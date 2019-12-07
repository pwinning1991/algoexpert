import unittest
import selectSort

class TestSelectSort(unittest.TestCase):
    def test1(self):
        self.assertEqual(selectSort.selectionSort([8,5,2,9,5,6,3]),[2,3,5,5,6,8,9])

    def test2(self):
        self.assertEqual(selectSort.selectionSort([0]),[0])

    def test3(self):
        self.assertEqual(selectSort.selectionSort([3, -5, 7, 11]),[-5,3,7,11])
