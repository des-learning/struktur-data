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
        if value == self.value:
            return self
        if value < self.value and self.left is not None:
            return self.left.find(value)
        if value > self.value and self.right is not None:
            return self.right.find(value)
        return None

    def height(self):
        return 1 + max([
            self.left.height() if self.left is not None else 0,
            self.right.height() if self.right is not None else 0
            ])

    def depth(self):
        return ((1 if self.parent is not None else 0) +
                self.parent.depth() if self.parent is not None else 0)

    def ancestors(self):
        l = [self.parent] if self.parent is not None else []
        if self.parent is not None:
            l.extend(self.parent.ancestors())
        return l

    def descendants(self):
        l = []
        if self.left is not None:
            l.append(self.left)
        if self.right is not None:
            l.append(self.right)
        if self.left is not None:
            l.extend(self.left.descendants())
        if self.right is not None:
            l.extend(self.right.descendants())
        return l

    def common_ancestor(self, n1, n2):
        if self is None:
            return None

        if self.value > n1.value and self.value > n2.value:
            return self.left.common_ancestor(n1, n2)
        if self.value < n1.value and self.value < n2.value:
            return self.right.common_ancestor(n1, n2)

        return self

    def count(self):
        return (1 +
                (self.left.count() if self.left is not None else 0) +
                (self.right.count() if self.right is not None else 0)
               )

    def findMinNode(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def findMaxNode(self):
        current = self
        while current.right is not None:
            current = current.right
        return current


    def remove(self, value):
        # jika value lebih kecil cari dan hapus node disebelah kiri
        if self.left is not None and value < self.value:
            self.left.remove(value)
        # jika value lebih besar cari dan hapus node disebelah kanan
        elif self.right is not None and value > self.value:
            self.right.remove(value)
        # jika tidak berarti node ini yang akan dihapus
        else:
            if self.left is None and self.right is None:
                if self.parent.left == self:
                    self.parent.left = None
                elif self.parent.right == self:
                    self.parent.right = None
            # jika ada dua anak
            # cari node paling kecil (temp) dari anak kanan, pindahkan ke self
            else:
                if self.right is not None:
                    minimum = self.right.findMinNode()
                    minvalue  = minimum.value
                    self.value = minimum.value
                # hapus node temp
                    self.right.remove(minvalue)
                elif self.left is not None:
                    maximum = self.left.findMaxNode()
                    maxvalue = maximum.value
                    self.value = maximum.value
                    self.left.remove(maxvalue)
        
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
        if self.root is None:
            return None
        return self.root.find(value)

    def depth(self, value):
        if self.root is None:
            return -1
        node = self.root.find(value)
        return node.depth() if node is not None else -1

    def ancestors(self, value):
        if self.root is None:
            return []
        node = self.root.find(value)
        return node.ancestors() if node is not None else []

    def descendants(self, value):
        if self.root is None:
            return []
        node = self.root.find(value)
        return node.descendants() if node is not None else []

    def height(self):
        if self.root is None:
            return 0
        return self.root.height() - 1

    def common_ancestor(self, v1, v2):
        if self.root is None:
            return None
        n1, n2 = self.root.find(v1), self.root.find(v2)
        if n1 is None or n2 is None:
            return None
        return self.root.common_ancestor(n1, n2)

    def count(self):
        if self.root is None:
            return 0
        return self.root.count()

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

    def addList(self, l):
        for i in l:
            self.add(i)

    def remove(self, value):
        if self.root is None:
            return
        self.root.remove(value)
