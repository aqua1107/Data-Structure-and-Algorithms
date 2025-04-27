class Array:

    def __init__(self):
        self.storage = []

    def is_empty(self):
        return len(self.storage) == 0

    def insert(self, idx, data):
        if idx < 0 or idx > len(self.storage):
            raise IndexError("Index out of bounds!")
        self.storage.insert(idx, data)

    def remove(self, idx)
        if self.is_empty():
            raise ValueError("Array is Empty!")
        if idx < 0 or idx >= len(self.storage):
            raise IndexError("Index out of bounds!")
        return self.storage.pop(idx)

    def length(self):
        return len(self.storage)

    def get(self, idx):
        if idx < 0 or idx >= len(self.storage):
            raise IndexError("Index out of bounds!")
        return self.storage[idx]

    def set(self, idx, data):
        if idx < 0 or idx >= len(self.storage):
            raise IndexError("Index out of bounds!")
        self.storage[idx] = data
