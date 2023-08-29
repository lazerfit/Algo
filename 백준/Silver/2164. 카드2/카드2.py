N = int(input())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        else:
            current_node = self.tail
            self.tail = new_node
            current_node.next = new_node
            self.length += 1

    def shift(self):
        if self.head is None:
            return
        current = self.head
        self.head = current.next
        current.next = None
        self.length -= 1

    def moveToTheEnd(self):
        current_head = self.head
        current_tail = self.tail
        self.head = self.head.next
        current_head.next = None
        self.tail = current_head
        current_tail.next = current_head


list = LinkedList()
for i in range(1, N + 1):
    list.insertAtEnd(i)

while list.length > 1:
    list.shift()
    list.moveToTheEnd()

print(list.tail.data)