import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def test_empty(self):
        doc = Tree()
        self.assertEqual(None, doc.root)
        self.assertEqual(0, doc.length())

    def test_1_level(self):
        doc = Tree()
        doc.add('html')
        self.assertEqual('html', doc.root.value)
        self.assertEqual(1, doc.length())

    def test_2_level(self):
        doc = Tree()
        doc.add('html')
        doc.add('head')
        doc.add('body')
        self.assertEqual('html', doc.root.value)
        self.assertEqual(2, len(doc.root.children))
        self.assertEqual('head', doc.root.children[0].value)
        self.assertEqual('body', doc.root.children[1].value)
        self.assertEqual(2, doc.length())

    def test_3_level(self):
        doc = Tree()
        doc.add('html')
        doc.add('head')
        doc.add('body')
        head = doc.root.children[0]
        head.add('title')
        self.assertEqual('html', doc.root.value)
        self.assertEqual(2, len(doc.root.children))
        self.assertEqual('head', doc.root.children[0].value)
        self.assertEqual('body', doc.root.children[1].value)
        self.assertEqual('title', head.children[0].value)
        self.assertEqual(1, len(head.children))
        self.assertEqual(2, head.length())

    def test_count(self):
        doc = Tree()
        self.assertEqual(0, doc.count())

        doc = Tree()
        doc.add('html')
        self.assertEqual(1, doc.count())

        doc = Tree()
        doc.add('html')
        doc.add('head')
        doc.add('body')
        self.assertEqual(3, doc.count())

        doc = Tree()
        doc.add('html')
        doc.add('head')
        doc.add('body')
        head = doc.root.children[0]
        head.add('title')
        self.assertEqual(4, doc.count())
