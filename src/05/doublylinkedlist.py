class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.length = self.length + 1

    def __index_valid(self, index):
        if self.length == 0:
            return False
        return 0 <= index < self.length or -1 >= index >= -self.length

    def __goto_index(self, index):
        if not self.__index_valid(index): return None
        current = self.head if index >= 0 else self.tail
        nextNode = lambda x: x.next if index >= 0 else x.prev
        nIndex = abs(index) - (0 if index >= 0 else 1)
        for i in range(0, nIndex):
            current = nextNode(current)
        return current

    def get(self, index):
        current = self.__goto_index(index)
        return current.value if current is not None else None

    def set(self, index, value):
        current = self.__goto_index(index)
        if current is not None:
            current.value = value

    def insert(self, index, value):
        if not self.__index_valid(index):
            return
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            current = self.__goto_index(index-1)
            newNode.next = current.next
            newNode.prev = current
            current.next.prev = newNode
            current.next = newNode
        self.length = self.length + 1


    def remove(self, index):
        if not self.__index_valid(index):
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if index == 0:
                nextNode = self.head.next
                nextNode.next.prev = None
                self.head.next = None
                self.head = nextNode
            elif index == self.length-1:
                prevNode = self.tail.prev
                prevNode.next = None
                self.tail.prev = None
                self.tail = prevNode
            else:
                current = self.__goto_index(index-1)
                nextNode = current.next
                afterNextNode = nextNode.next
                nextNode.prev = None
                nextNode.next = None
                current.next = afterNextNode
                afterNextNode.prev = current
        self.length = self.length - 1

    def traverse(self):
        current = self.head
        while current is not None:
            v = current.value
            current = current.next
            yield v

    def asList(self):
        return [x for x in self.traverse()]

    def __repr__(self):
        return '<LinkedList: {}>'.format(self.asList())
