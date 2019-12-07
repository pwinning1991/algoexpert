import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
    def test1(self):
        self.assertEqual(palindrome.isPalindrome('abc'), False)

    def test2(self):
        self.assertEqual(palindrome.isPalindrome('abcdcba'),True)

    def test3(self):
        self.assertEqual(palindrome.isPalindrome1('abc'), False)

    def test4(self):
        self.assertEqual(palindrome.isPalindrome1('abcdcba'),True)
