class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, idx, data):
        new_node = Node(data)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < idx - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def remove(self, idx):
        if not self.head:
            return -1
        if idx == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < idx - 1:
            current = current.next
            count += 1
        if current.next is None:
            return
        current.next = current.next.next

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_all(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_all()

ll.insert(1, 15)
ll.print_all()

ll.remove(2)
ll.print_all()

print("length of the Linked List: ", ll.length())
