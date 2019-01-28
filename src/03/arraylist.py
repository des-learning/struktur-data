CHUNK = 10

class ArrayList:
    def __init__(self):
        self.items = []
        self.capacity = CHUNK

    def length(self):
        return len(self.items)

    def indexValid(self, index):
        return 0 <= index < self.length()
        
    def add(self, value):
        if self.lenght >= self.capacity:
            self.capacity = self.capacity + CHUNK
        self.items.append(value)

    def get(self, index):
        if self.indexValid(index):
            return self.items[index]
        return None

    def set(self, index, value):
        if self.indexValid(index):
            self.items[index] = value

    def remove(self, index):
        if self.indexValid(index):
            del self.items[index]

    def insert(self, index, value):
        if self.indexValid(index):
            self.items.insert(index, value)
