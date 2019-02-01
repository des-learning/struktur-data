class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        pass

    def get(self, index):
        pass

    def set(self, index, value):
        pass

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass

    def __repr__(self):
        pass

    def traverse(self):
        current = self.head
        while current is not None:
            v = current.value
            current = current.next
            yield v

    def asList(self):
        return [x for x in self.traverse()]

    def __repr__(self):
        return '<LinkedList: {}>'.format(self.aslist())
