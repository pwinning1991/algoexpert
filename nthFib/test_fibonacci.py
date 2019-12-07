import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fibonacci.getNthFib(4), 2)

    def test_2(self):
        self.assertEqual(fibonacci.getNthFib(1), 0)

    def test_3(self):
        self.assertEqual(fibonacci.getNthFib(2), 1)

    def test_4(self):
        self.assertEqual(fibonacci.getNthFib(6), 5)

    def test_5(self):
        self.assertEqual(fibonacci.getNthFib(7), 8)

    def test_5(self):
        self.assertEqual(fibonacci.getNthFib(8), 13)
