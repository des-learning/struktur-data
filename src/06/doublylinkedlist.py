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
        # jika item tinggal 1
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # head
            if index == 0:
                nextNode = self.head.next
                nextNode.prev = None
                self.head.next = None
                self.head = nextNode
            # tail
            elif index == self.length-1:
                prevNode = self.tail.prev
                prevNode.next = None
                self.tail.prev = None
                self.tail = prevNode
            # middle
            else:
                current = self.__goto_index(index-1)
                nextNode = current.next
                afterNextNode = nextNode.next
                nextNode.prev = None
                nextNode.next = None
                current.next = afterNextNode
                afterNextNode.prev = current
        self.length = self.length - 1

    def normalize_index(self, index):
        if 0 <= index <= self.length:
            return index
        if index < 0 and self.length + index >= 0:
            return self.length + index
        return None

    def slice(self, start=None, end=None):
        nStart = self.normalize_index(start) if start is not None else 0
        nEnd = self.normalize_index(end) if end is not None else self.length-1

        l = DoublyLinkedList()
        if nStart is None or nEnd is None or nStart > nEnd:
            return l

        head = self.__goto_index(nStart)
        tail = self.__goto_index(nEnd)
        cur = head
        while cur is not None and cur != tail:
            l.add(cur.value)
            cur = cur.next
        return l

    # function overloading/overriding, __len__ if magic function
    # of python that returns length of an object
    def __len__(self):
        return self.length

    def indexOf(self, value):
        # see http://book.pythontips.com/en/latest/enumerate.html
        for i in enumerate(self.traverse()):
            if i[1] == value:
                return i[0]
        return None


    def lastIndexOf(self, value):
        for i in enumerate(self.traverseReverse()):
            if i[1] == value:
                return len(self)-1-i[0]
        return None

    # traverse linked list from tail to head, yield node value every
    # iteration
    def traverseReverse(self):
        current = self.tail
        while current is not None:
            v = current.value
            current = current.prev
            yield v

    # traverse linked list from head to tail, yield node valu every
    # iteration
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
