# Binary Search Tree
# binary tree dimana node tree tersusun dalam keadaan terurut
# don't allow duplicate value
class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value == self.value:
            return
        if value <= self.value:
            if self.left is None:
                self.left = Node(value, self)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = Node(value, self)
            else:
                self.right.add(value)

    def ascending(self):
        left = []
        if self.left is not None:
            left.extend([x for x in self.left.ascending()])
        right = []
        if self.right is not None:
            right.extend([x for x in self.right.ascending()])
        l = []
        l.extend(left)
        l.append(self.value)
        l.extend(right)
        return l

    def descending(self):
        left = []
        if self.left is not None:
            left.extend([x for x in self.left.descending()])
        right = []
        if self.right is not None:
            right.extend([x for x in self.right.descending()])
        l = []
        l.extend(right)
        l.append(self.value)
        l.extend(left)
        return l

    def inorder(self):
        left = []
        if self.left is not None:
            left = [x for x in self.left.inorder()]
        right = []
        if self.right is not None:
            right = [x for x in self.right.inorder()]
        l = []
        l.extend(left)
        l.append(self.value)
        l.extend(right)
        return l

    def preorder(self):
        left = []
        if self.left is not None:
            left = [x for x in self.left.preorder()]
        right = []
        if self.right is not None:
            right = [x for x in self.right.preorder()]
        l = [self.value]
        l.extend(left)
        l.extend(right)
        return l

    def postorder(self):
        left = []
        if self.left is not None:
            left = [x for x in self.left.postorder()]
        right = []
        if self.right is not None:
            right = [x for x in self.right.postorder()]
        l = []
        l.extend(left)
        l.extend(right)
        l.append(self.value)
        return l

    def find(self, value):
        pass

    def height(self):
        return 1 + max([
            self.left.height() if self.left is not None else 0,
            self.right.height() if self.right is not None else 0
            ])

    def depth(self):
        pass

    def ancestors(self):
        pass

    def descendants(self):
        pass

    def common_ancestor(self, n1, n2):
        pass

    def count(self):
        pass

    def __repr__(self):
        return '<Node: {}>'.format(self.value)

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def find(self, value):
        pass

    def depth(self, value):
        pass

    def ancestors(self, value):
        pass

    def descendants(self, value):
        pass

    def height(self):
        if self.root is None:
            return 0
        return self.root.height() - 1

    def common_ancestor(self, v1, v2):
        pass

    def count(self):
        pass

    def ascending(self):
        return self.root.ascending() if self.root is not None else []

    def descending(self):
        return self.root.descending() if self.root is not None else []

    def inorder(self):
        return self.root.inorder() if self.root is not None else []

    def preorder(self):
        return self.root.preorder() if self.root is not None else []

    def postorder(self):
        return self.root.postorder() if self.root is not None else []
