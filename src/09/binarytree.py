class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.value:
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

    def ascending(self):
        return self.root.ascending() if self.root is not None else []
