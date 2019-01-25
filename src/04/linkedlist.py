class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __add_empty(self, node):
        self.head = node
        self.tail = node

    def __add_not_empty(self, node):
        self.tail.next = node
        self.tail = node

    def __index_valid(self, index):
        return 0 <= index < self.length # index >= 0 and index < self.length

    def __goto_index(self, index):
        if not self.__index_valid(index):
            return None
        
        c = -1
        current = self.head
        while current is not None:
            c = c + 1
            if c == index:
                return current
            current = current.next
        return None

    def add(self, value):
        # bentuk node baru
        newNode = Node(value)
        addf = self.__add_not_empty
        if self.tail is None:
            addf = self.__add_empty
        addf(newNode)
        self.length = self.length + 1

    def get(self, index):
        node = self.__goto_index(index)
        if node is not None:
            return node.value
        return None

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
