class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __add_empty(self, node):
        self.head = node
        self.tail = node

    def __add_not_empty(self, node):
        self.tail.next = node
        self.tail = node

    def add(self, value):
        # bentuk node baru
        newNode = Node(value)
        addf = self.__add_not_empty
        if self.tail is None:
            addf = self.__add_empty
        addf(newNode)

    def get(self, index):
        c = -1 
        current = self.head
        while current is not None:
            c = c + 1
            if c == index:
                return current.value
            current = current.next
        return None

    def traverse(self):
        current = self.head
        while current is not None:
            v = current.value
            current = current.next
            yield v

    def __repr__(self):
        values = [x for x in self.traverse()]
        return '<LinkedList: {}>'.format(values)
