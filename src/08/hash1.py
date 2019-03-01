class Index:
    def __init__(self, key, index):
        self.key = key
        self.index = index

class Hash:
    def __init__(self, size=100):
        self.size = size
        self.array = [None for _ in range(self.size)] 
        self.indexes = []

    def __hash(self, key):
        return sum([ord(x) for x in key]) % self.size

    def isFull(self):
        return len(self.indexes) >= self.size

    def __replace(self, key, index, value):
        for item in self.array[index]:
            if item.key == key:
                item.value = value

    def __add(self, key, index, value):
        self.array[index].append(Item(key, value))
        self.keys.append(key)

    def keys(self):
        return [x.key for x in self.indexes]

    def put(self, key, value):
        if key not in self.keys() and self.isFull():
            raise Exception('Hash table full!')

        # cari posisi index
        index = self.__hash(key)
        while self.array[index] is not None:
            index = index + 1
            if index >= self.size:
                index = 0
        self.array[index] = value
        self.indexes.append(Index(key, index))

    def remove(self, key):
        indexes = filter(lambda x: x.key == key, self.indexes)
        if len(indexes) == 0:
            raise Exception('Not found: {}'.format(key))

        self.array[indexes[0].index] = None

    def get(self, key):
        indexes = filter(lambda x: x.key == key, self.indexes)
        if len(indexes) == 0:
            raise Exception('Not found: {}'.format(key))
        return self.array[indexes[0].index]
