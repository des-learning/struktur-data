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

def setupList(ascending=True):
    l = DoublyLinkedList(ascending)
    data = [0, 7, 5, 3, 8, 2, 9, 1, 9, 4]
    for i in data:
        l.add(i)
    return l, data

class TestFilter(unittest.TestCase):
    def test_filter(self):
        l, data = setupList()

        lebihbesar5 = lambda x: x > 5
        filteredlist = l.filter(lebihbesar5)
        filtereddata = filter(lebihbesar5, data)
        self.assertEqual(len(filteredlist), len(filtereddata))
        self.assertTrue(equalList(filteredlist.asList(), filtereddata))

        negatif = lambda x: x < 0
        filteredlist = l.filter(negatif)
        filtereddata = filter(negatif, data)
        self.assertEqual(len(filteredlist), len(filtereddata))
        self.assertTrue(equalList(filteredlist, filtereddata))
