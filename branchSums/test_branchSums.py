import unittest
from branchSums import branchSums, BinaryTree

class TestBranchSums(unittest.TestCase):
    def test1(self):
        tree = BinaryTree(1)
        self.assertEqual(branchSums(tree), [1])

    def test2(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(1)
        tree.left.left = BinaryTree(10)
        tree.left.left.left = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

