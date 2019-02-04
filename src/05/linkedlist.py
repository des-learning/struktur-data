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
        '''add new node to empty linked list'''
        self.head = node
        self.tail = node

    def __add_not_empty(self, node):
        '''add new node to non empty linked list'''
        self.tail.next = node
        self.tail = node

    def __index_valid(self, index):
        '''check where supplied index is valid (0 <= index < length)'''
        return 0 <= index < self.length # index >= 0 and index < self.length

    def __goto_index(self, index):
        '''return cursor to index position within linked list'''
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
        '''add new item into list'''
        # bentuk node baru
        newNode = Node(value)
        addf = self.__add_not_empty
        if self.tail is None:
            addf = self.__add_empty
        addf(newNode)
        self.length = self.length + 1

    def get(self, index):
        '''get item in index position in list'''
        node = self.__goto_index(index)
        if node is not None:
            return node.value
        return None

    def __insert_before_head(self, value):
        '''insert new item before head, not to be called from outside'''
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length = self.length + 1

    def __insert_middle(self, index, value):
        '''insert new item in the middle of the list'''
        newNode = Node(value)
        current = self.__goto_index(index-1)
        newNode.next = current.next
        current.next = newNode
        self.length = self.length + 1

    def insert(self, index, value):
        '''insert new item into list before index position'''
        if not self.__index_valid(index):
            return
        if index == 0:
            self.__insert_before_head(value)
        else:
            self.__insert_middle(index, value)

    def __remove_head(self):
        '''remove list head'''
        self.head = self.head.next
        self.length = self.length - 1

    def __remove_tail(self):
        '''remove list tail'''
        # current needs to be before tail
        current = self.__goto_index(self.length-2)
        self.tail = current
        self.tail.next = None
        self.length = self.length - 1

    def __remove_middle(self, index):
        '''remove node from the middle of the list'''
        current = self.__goto_index(index-1)
        current.next = current.next.next
        self.length = self.length - 1

    def remove(self, index):
        '''remove node from list'''
        if not self.__index_valid(index):
            return
        # hapus head
        if index == 0:
            self.__remove_head()
        # hapus tail
        elif index == self.length - 1:
            self.__remove_tail()
        # hapus middle
        else:
            self.__remove_middle(index)

    def __len__(self):
        return self.length

    def isEmpty(self):
        return len(self) == 0

    def traverse(self):
        '''generator, visiting each node of list from head to tail'''
        current = self.head
        while current is not None:
            v = current.value
            current = current.next
            yield v

    def asList(self):
        '''return linkedlist as python list'''
        return [x for x in self.traverse()]

    def __repr__(self):
        '''linkedlist string representation'''
        return '<LinkedList: {}>'.format(self.asList())
