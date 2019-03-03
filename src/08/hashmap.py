class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.keys = [None for _ in range(self.size)]
        self.bucket = [None for _ in range(self.size)]

    def __hash(self, key):
        index = sum([ord(x) for x in key]) % self.size
        while self.keys[index] is not None:
            if self.keys[index] == key: break
            index = index + 1
            if index >= self.size:
                index = 0
        return index

    def isFull(self):
        return len([x for x in self.keys if x is not None]) >= self.size

    def put(self, key, value):
        if self.isFull():
            raise Exception('HashMap full!')

        index = self.__hash(key)
        self.keys[index] = key
        self.bucket[index] = value

    def get(self, key):
        index = self.__hash(key)
        if self.keys[index] == key:
            return self.bucket[index]

        raise Exception('Not found: {}'.format(key))

    def remove(self, key):
        index = self.__hash(key)
        if self.keys[index] == key:
            self.bucket[index] = None
            self.keys[index] = None
        else:
            raise Exception('Not found: {}'.format(key))
