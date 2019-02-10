from linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.q = LinkedList()
    
    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, value):
        self.q.add(value)

    def dequeue(self):
        if self.isEmpty(): return None
        value = self.q.get(0)
        self.q.remove(0)
        return value

    def __len__(self):
        return len(self.q)
