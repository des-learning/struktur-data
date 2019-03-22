# Binary Search Tree
# binary tree dimana node tree tersusun dalam keadaan terurut
# don't allow duplicate value
class Node:
    def __init__(self, key, value, parent=None):
        self.parent = parent
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def add(self, key, value):
        if key == self.key:
            return
        if key <= self.key:
            if self.left is None:
                self.left = Node(key, value, self)
            else:
                self.left.add(key, value)
        else:
            if self.right is None:
                self.right = Node(key, value, self)
            else:
                self.right.add(key, value)

    def find(self, key):
        if key == self.key:
            return self
        if key < self.key and self.left is not None:
            return self.left.find(key)
        if key > self.key and self.right is not None:
            return self.right.find(key)
        return None

    def __repr__(self):
        return '<Node: {} - {}>'.format(self.key, self.value)

class Tree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root.add(key, value)

    def find(self, key):
        if self.root is None:
            return None
        return self.root.find(key)

    def addList(self, l):
        for i in l:
            self.add(i[0], i[1])
