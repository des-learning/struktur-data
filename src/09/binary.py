class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def addLeft(self, value):
        if self.left is None:
            node = Node(value, self)
            self.left = node
        else:
            self.left.addLeft(value)

    def addRight(self, value):
        if self.right is None:
            node = Node(value, self)
            self.right = node
        else:
            self.right.addRight(value)

    def inorder(self):
        left = []
        if self.left is not None:
            left.extend([x for x in self.left.inorder()])
        right = []
        if self.right is not None:
            right.extend([x for x in self.right.inorder()])
        l = []
        l.extend(left)
        l.append(self.value)
        l.extend(right)
        return l

    def preorder(self):
        left = []
        if self.left is not None:
            left.extend([x for x in self.left.preorder()])
        right = []
        if self.right is not None:
            right.extend([x for x in self.right.preorder()])
        l = []
        l.append(self.value)
        l.extend(left)
        l.extend(right)
        return l

    def postorder(self):
        left = []
        if self.left is not None:
            left.extend([x for x in self.left.postorder()])
        right = []
        if self.right is not None:
            right.extend([x for x in self.right.postorder()])
        l = []
        l.extend(left)
        l.extend(right)
        l.append(self.value)
        return l


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)

    def inorder(self):
        return self.root.inorder() if self.root is not None else []

    def preorder(self):
        return self.root.preorder() if self.root is not None else []

    def postorder(self):
        return self.root.postorder() if self.root is not None else []
