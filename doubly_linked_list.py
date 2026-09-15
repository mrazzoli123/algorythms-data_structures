class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            print("List is empty, nothing to delete.")
            return

        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        print(f"Node with data {data} not found.")

    def display(self):
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    def reverse_display(self):
        if self.is_empty():
            print("List is empty.")
            return

        current = self.tail
        while current:
            print(current.data, end=" <-> " if current.prev else "\n")
            current = current.prev

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()

dll.delete(20)
dll.display()

dll.reverse_display()
