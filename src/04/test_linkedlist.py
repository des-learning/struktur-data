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

    def test_get(self):
        a = LinkedList()
        a.add(5)
        a.add(6)
        a.add(7)
        self.assertEqual(a.get(0), 5)
        self.assertEqual(a.get(1), 6)
        self.assertEqual(a.get(2), 7)
        self.assertEqual(a.get(3), None)
        self.assertEqual(a.get(10), None)
        self.assertEqual(a.get(-1), None)

    def test_remove(self):
        a = LinkedList()
        a.add(5)
        a.add(6)
        a.add(7)
        a.remove(1)
        self.assertEqual(a.asList(), [5, 7])
        a.remove(1)
        self.assertEqual(a.asList(), [5])
        a.remove(0)
        self.assertEqual(a.asList(), [])

    def test_insert(self):
        a = LinkedList()
        a.add(5)
        a.add(6)
        a.add(7)
        a.insert(1, 8)
        self.assertEqual(a.asList(), [5, 8, 6, 7])
        a.insert(3, 9)
        self.assertEqual(a.asList(), [5, 8, 6, 9, 7])
        a.insert(0, 10)
        self.assertEqual(a.asList(), [10, 5, 8, 6, 9, 7])
