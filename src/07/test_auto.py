import unittest
from linkedlist import LinkedList

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
    l = LinkedList(ascending)
    data = [0, 7, 5, 3, 8, 2, 9, 1, 9, 4]
    for i in data:
        l.add(i)
    return l, data

class TestAuto(unittest.TestCase):
    def test_auto_ascending(self):
        l, data = setupList()

        self.assertEqual(len(l), len(data))
        self.assertEqual(l.get(0), 0)
        self.assertEqual(l.get(len(l)-1), 9)
        self.assertTrue(equalList(l.asList(), sorted(data)))

    #def test_auto_descending(self):
    #    l, data = setupList(ascending=False)
#
#        self.assertEqual(len(l), len(data))
#        self.assertEqual(l.get(0), 9)
#        self.assertEqual(l.get(len(l)-1), 0)
#        self.assertTrue(equalList(l.asList(), sorted(data, reverse=True)))
