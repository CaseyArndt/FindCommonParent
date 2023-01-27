import unittest
from BinaryTree import BinaryTree
from FindCommonParent import find_common_parent

class FCPTestCase(unittest.TestCase):
    tree_list = [10, 5, 12, 8, 9, 20, 4]
    tree = BinaryTree(tree_list)

    def test1(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 10, 4)), 
            expected)

    def test2(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 1, 4)), 
            expected)

    def test3(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 4, 1)), 
            expected)

    def test4(self):
        expected = 10
        self.assertEqual((find_common_parent(self.tree.root, 5, 12)), 
            expected)

    def test5(self):
        expected = 10
        self.assertEqual((find_common_parent(self.tree.root, 12, 5)), 
            expected)

    def test6(self):
        expected = 10
        self.assertEqual((find_common_parent(self.tree.root, 5, 4)), 
            expected)

    def test7(self):
        expected = 10
        self.assertEqual((find_common_parent(self.tree.root, 4, 5)), 
            expected)

    def test8(self):
        expected = 12
        self.assertEqual((find_common_parent(self.tree.root, 20, 4)), 
            expected)

    def test9(self):
        expected = 12
        self.assertEqual((find_common_parent(self.tree.root, 4, 20)), 
            expected)

    def test10(self):
        expected = 5
        self.assertEqual((find_common_parent(self.tree.root, 8, 9)), 
            expected)

    def test11(self):
        expected = 10
        self.assertEqual((find_common_parent(self.tree.root, 9, 20)), 
            expected)


class FCPTestCase2(unittest.TestCase):
    tree_list = [10]
    tree = BinaryTree(tree_list)

    def test1(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 10, 4)), 
            expected)

    def test2(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 15, 20)), 
            expected)


class FCPTestCase3(unittest.TestCase):
    tree_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    tree = BinaryTree(tree_list)
    """
                 1
          2              3
       4     5        6      7
      8 9  10 11    12 13  14 15
    16
    """

    def test1(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 1, 16)), 
            expected)

    def test2(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 16, 1)), 
            expected)

    def test3(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 1, 16)), 
            expected)

    def test4(self):
        expected = 4
        self.assertEqual((find_common_parent(self.tree.root, 8, 16)), 
            expected)

    def test5(self):
        expected = 4
        self.assertEqual((find_common_parent(self.tree.root, 8, 9)), 
            expected)

    def test6(self):
        expected = 5
        self.assertEqual((find_common_parent(self.tree.root, 10, 11)), 
            expected)

    def test7(self):
        expected = 6
        self.assertEqual((find_common_parent(self.tree.root, 12, 13)), 
            expected)

    def test8(self):
        expected = 7
        self.assertEqual((find_common_parent(self.tree.root, 14, 15)), 
            expected)

    def test9(self):
        expected = 7
        self.assertEqual((find_common_parent(self.tree.root, 15, 14)), 
            expected)

    def test10(self):
        expected = 1
        self.assertEqual((find_common_parent(self.tree.root, 15, 16)), 
            expected)

    def test11(self):
        expected = None
        self.assertEqual((find_common_parent(self.tree.root, 15, 17)), 
            expected)


if __name__ == "__main__":
    unittest.main()