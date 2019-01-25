import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_empty(self):
        a = LinkedList()
        self.assertEqual(a.head, None)
        self.assertEqual(a.tail, None)

    def test_add(self):
        a = LinkedList()
        a.add(5)
        a.add(6)
        a.add(7)
        self.assertEqual(a.head.value, 5)
        self.assertEqual(a.head.next.value, 6)
        self.assertEqual(a.head.next.next.value, 7)
        self.assertEqual(a.tail.value, 7)
        self.assertEqual(a.tail.next, None)
