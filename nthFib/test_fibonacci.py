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

    def test_6(self):
        self.assertEqual(fibonacci.getNthFib1(8), 13)

    def test_7(self):
        self.assertEqual(fibonacci.getNthFib1(4), 2)

    def test_8(self):
        self.assertEqual(fibonacci.getNthFib1(1), 0)

    def test_9(self):
        self.assertEqual(fibonacci.getNthFib1(2), 1)

    def test_10(self):
        self.assertEqual(fibonacci.getNthFib1(6), 5)

    def test_11(self):
        self.assertEqual(fibonacci.getNthFib1(7), 8)

    def test_12(self):
        self.assertEqual(fibonacci.getNthFib2(7), 8)

    def test_12(self):
        self.assertEqual(fibonacci.getNthFib2(6), 5)


