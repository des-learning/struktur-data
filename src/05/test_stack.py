import unittest
from stack import Stack

class StackTest(unittest.TestCase):
    def test_empty(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertEqual(s.pop(), None)

    def test_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
