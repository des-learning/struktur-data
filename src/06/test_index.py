import unittest
from doublylinkedlist import DoublyLinkedList

def setupList():
    l = DoublyLinkedList()
    for i in [0, 7, 6, 7, 7, 8, 7]:
        l.add(i)
    return l

class TestIndexOf(unittest.TestCase):
    def test_index(self):
        l = setupList()
        self.assertEqual(l.indexOf(7), 1)
        self.assertEqual(l.indexOf(5), None)
        self.assertEqual(l.indexOf(6), 2)

    def test_last_index(self):
        l = setupList()
        self.assertEqual(l.lastIndexOf(7), 6)
        self.assertEqual(l.lastIndexOf(5), None)
        self.assertEqual(l.lastIndexOf(6), 2)

    def test_one_item(self):
        l = DoublyLinkedList()
        l.add(7)
        self.assertEqual(l.indexOf(7), 0)
        self.assertEqual(l.lastIndexOf(7), 0)
        self.assertEqual(l.indexOf(8), None)
        self.assertEqual(l.lastIndexOf(8), None)
