class Stack:

    def __init__(self):
        self.storage = []

    def insert(self, data):
        self.storage.append(data)

    def remove(self):
        if len(self.storage) == 0:
            raise ValueError("Stack is empty!")
        else:
            return self.storage.pop()

    def peek(self):
        if len(self.storage) == 0:
            raise ValueError("Stack is empty!")
        else:
            return self.storage[-1]

    def length(self):
        return len(self.storage)

    def is_empty(self):
        return len(self.storage) == 0
