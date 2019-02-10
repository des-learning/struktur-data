import unittest
from doublylinkedlist import DoublyLinkedList

def reduce(function, iterable, start):
    result = start
    for i in iterable:
        result = function(result, i)
    return result

def equalList(list1, list2):
    pairs = zip(list1, list2)
    sameItem = lambda x, y: x and (y[0] == y[1])
    return (len(list1) == len(list2) and 
            reduce(sameItem, pairs, True))

def setupList():
    l = DoublyLinkedList()
    data = [0, 7, 5, 3, 8, 2, 9, 1, 9, 4]
    for i in data:
        l.add(i)
    return l, data

class TestSlice(unittest.TestCase):
    def test_slice(self):
        l, data = setupList()

        self.assertTrue(equalList(l.asList(), data))
        self.assertTrue(equalList(l.slice(0, len(l)).asList(), data))
        self.assertTrue(equalList(l.slice(0, 1).asList(), data[0:1]))
        self.assertTrue(equalList(l.slice(0, 5).asList(), data[0:5]))
        self.assertTrue(equalList(l.slice(5, len(l)).asList(), data[5:]))

    def test_slice_negative(self):
        l, data = setupList()

        self.assertTrue(equalList(l.slice(0, -1).asList(), data[0:-1]))
        self.assertTrue(equalList(l.slice(5, -3).asList(), data[5:-3]))
        self.assertTrue(equalList(l.slice(-3, -1).asList(), data[-3:-1]))
        self.assertTrue(equalList(l.slice(0, -5).asList(), data[0:-5]))

    def test_invalid_slice(self):
        l, data = setupList()

        self.assertTrue(equalList(l.slice(100, 200).asList(), []))
        self.assertTrue(equalList(l.slice(-1, -3).asList(), []))
        self.assertTrue(equalList(l.slice(0, len(l)+1).asList(), []))
