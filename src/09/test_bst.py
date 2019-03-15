import unittest
from bst import Tree

def listEqual(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def setup_tree():
    values = [10, 7, 6, 3, 4, 3, 2, 1, 5]
    tree = Tree()
    for v in values:
        tree.add(v)
    return values, tree

def extract_values(nodes):
    l = []
    for node in nodes:
        l.append(node.value)
    return l

class TestTree(unittest.TestCase):
    def test_empty(self):
        tree = Tree()
        self.assertEqual(tree.root, None)
        self.assertTrue(listEqual([], tree.inorder()))
        self.assertTrue(listEqual([], tree.postorder()))
        self.assertTrue(listEqual([], tree.preorder()))

    def test_add(self):
        values, tree = setup_tree()
        sorted_values = list(sorted(set(values)))
        self.assertEqual(tree.root.value, 10)
        self.assertTrue(listEqual(sorted_values, tree.inorder()))

        preorder_values = [10, 7, 6, 3, 2, 1, 4, 5]
        self.assertTrue(listEqual(preorder_values, tree.preorder()))

        postorder_values = [1, 2, 5, 4, 3, 6, 7, 10]
        self.assertTrue(listEqual(postorder_values, tree.postorder()))

    def test_find(self):
        values, tree = setup_tree()
        node = tree.find(100)
        self.assertEqual(None, node)

        node = tree.find(10)
        self.assertEqual(node.value, 10)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.left.value, 7)
        self.assertEqual(node.right, None)

        node = tree.find(3)
        self.assertEqual(node.value, 3)
        self.assertEqual(node.parent.value, 6)
        self.assertEqual(node.left.value, 2)
        self.assertEqual(node.right.value, 4)

    def test_height(self):
        values, tree = setup_tree()
        self.assertEqual(tree.height(), 5)

    def test_depth(self):
        values, tree = setup_tree()

        depth = tree.depth(3)
        self.assertEqual(depth, 3)

    def test_ancestors(self):
        values, tree = setup_tree()

        ancestors = tree.ancestors(3)
        self.assertTrue(listEqual([6, 7, 10], extract_values(ancestors)))

        ancestors = tree.ancestors(10)
        self.assertTrue(listEqual([], extract_values(ancestors)))

        ancestors = tree.ancestors(5)
        self.assertTrue(listEqual([4, 3, 6, 7, 10], extract_values(ancestors)))

    def test_descendants(self):
        values, tree = setup_tree()

        descendants = tree.descendants(10)
        self.assertTrue(listEqual([7, 6, 3, 2, 4, 1, 5], extract_values(descendants)))

        descendants = tree.descendants(3)
        self.assertTrue(listEqual([2, 4, 1, 5], extract_values(descendants)))

        descendants = tree.descendants(4)
        self.assertTrue(listEqual([5], extract_values(descendants)))

        descendants = tree.descendants(5)
        self.assertTrue(listEqual([], extract_values(descendants)))

    def test_common_ancestor(self):
        values, tree = setup_tree()

        common_ancestor = tree.common_ancestor(1, 5)
        self.assertNotEqual(common_ancestor, None)
        self.assertEqual(common_ancestor.value, 3)

    def test_count(self):
        values, tree = setup_tree()

        self.assertEqual(tree.count(), len(set(values)))
