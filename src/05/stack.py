from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()


    # add di item pertama
    #def push(self, value):
    #    if len(self.stack) == 0:
    #        self.stack.add(value)
    #    else:
    #        self.stack.insert(0, value)

    # remove di item pertama
    #def pop(self):
    #    if len(self.stack) == 0: return None
    #    value = self.stack.get(0)
    #    self.stack.remove(0)
    #    return value

    # add ke akhir
    def push(self, value):
        self.stack.add(value)

    # remove dari akhir
    def pop(self):
        if len(self.stack) == 0: return None
        last = self.stack.length-1
        value = self.stack.get(last)
        self.stack.remove(last)
        return value

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack.isEmpty()
