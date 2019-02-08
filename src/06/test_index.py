import unittest
from doublylinkedlist import DoublyLinkedList

def test_indexOf(unittest.TestCase):
    def test_index(self):
        l = DoublyLinkedList()
        for i in [0, 7, 6, 7, 7, 8, 7]:
            l.add(i)
        self.assertEqual(l.indexOf(7), 1)
        self.assertEqual(l.indexOf(5), None)
        self.assertEqual(l.indexOf(6), 2)
        self.assertEqual(l.lastIndexOf(7), 6)
        self.assertEqual(l.lastIndexOf(5), None)
        self.assertEqual(l.lastIndexOf(6), 2)
