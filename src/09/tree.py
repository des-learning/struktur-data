class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.children = []

    def add(self, value):
        node = Node(value, self)
        self.children.append(node)

    def sibling(self):
        siblings = []
        if self.parent is not None:
            siblings = [child for child in self.parent.children if child is not self]
        return siblings

    def render(self, space=0):
        s = '{}{}\n'.format('-'*space, self.value)
        for child in self.children:
            s = s + child.render(space+4)
        return s
        #return '{}{}\n{}'.format(' '*space, self.value,
        #        ''.join([x.render(space+1) for x in self.children]))

    def length(self):
        children_length = [child.length() for child in self.children]
        children_length.append(0)
        return 1 + max(children_length)

    def __repr__(self):
        return '<Node: {}>'.format(self.value)

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            node = Node(value)
            self.root = node
        else:
            self.root.add(value)

    def length(self):
        return self.root.length() if self.root is not None else 0

    def __repr__(self):
        return self.root.render() if self.root is not None else '<Empty Tree>'
