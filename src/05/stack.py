from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        if len(self.stack) == 0:
            self.stack.add(value)
        else:
            self.stack.insert(0, value)

    def pop(self):
        if len(self.stack) == 0: return None
        value = self.stack.get(0)
        self.stack.remove(0)
        return value

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack.isEmpty()
