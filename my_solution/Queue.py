from collections import deque

class Queue:

    def __init__(self):
        self.storage = deque()

    def insert(self, data):
        self.storage.append(data)

    def remove(self):
        if not self.storage:
            raise ValueError("Queue is empty!")
        else:
            return self.storage.popleft()

    def length(self):
        return len(self.storage)

    def peek(self):
        if not self.storage:
            raise ValueError("Queue is empty!")
        else:
            return self.storage[0]

    def is_empty(self):
        return len(self.storage) == 0

