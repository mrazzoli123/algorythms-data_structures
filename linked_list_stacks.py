class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0
    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def size(self):
        return self._size

    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return str(result)

if __name__ == "__main__":
    stack = LinkedListStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:", stack)

    print("Peek:", stack.peek())

    print("Popped:", stack.pop())

    print("Stack after pop:", stack)
