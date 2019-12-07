import unittest
import insertSort

class TestInsertSort(unittest.TestCase):
    def test1(self):
       self.assertEqual(insertSort.insertionSort([]), [])
    def test2(self):
       self.assertEqual(insertSort.insertionSort([8,5,2,9,5,6,3]), [2,3,5,5,6,8,9])


