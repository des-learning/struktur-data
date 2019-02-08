import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
    def test_empty(self):
        q = Queue()
        self.assertEqual(len(q), 0)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.isEmpty(), True)

    def test_queue(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(1)
        self.assertEqual(len(q), 5)
        self.assertEqual(q.isEmpty(), False)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 7)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.isEmpty(), True)
        self.assertEqual(len(q), 0)
