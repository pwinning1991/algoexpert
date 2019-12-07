import unittest
import cce

class TestCCE(unittest.TestCase):
    def test1(self):
        self.assertEqual(cce.cce("xyz", 2),"zab")
