class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<Item: {}>'.format(self.key)

class Hash:
    def __init__(self, size=100):
        self.size = size
        self.array = [[] for _ in range(self.size)] 
        self.keys = []

    def __hash(self, key):
        return sum([ord(x) for x in key]) % self.size

    def isFull(self):
        return len([x for x in self.array if len(x) > 0]) >= self.size

    def __replace(self, key, index, value):
        for item in self.array[index]:
            if item.key == key:
                item.value = value

    def __add(self, key, index, value):
        self.array[index].append(Item(key, value))
        self.keys.append(key)

    def put(self, key, value):
        if key not in self.keys and self.isFull():
            raise Exception('Hash table full!')

        # cari posisi index
        index = self.__hash(key)
        putfn = self.__replace if key in self.keys else self.__add
        putfn(key, index, value)


    def remove(self, key):
        index = self.__hash(key)
        delItem = None
        for item in self.array[index]:
            if item.key == key:
                delItem = item
                break

        if delItem is not None:
            self.array[index].remove(delItem)
        else:
            raise Exception('Not found: {}'.format(key))

    def get(self, key):
        index = self.__hash(key)
        for item in self.array[index]:
            if item.key == key:
                return item.value
        raise Exception('Not found: {}'.format(key))
