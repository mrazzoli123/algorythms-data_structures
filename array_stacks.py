class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def __str__(self):
        return str([self.stack[i] for i in range(self.top + 1)])

if __name__ == "__main__":
    stack = ArrayStack(5)

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:", stack)

    print("Peek:", stack.peek())

    print("Popped:", stack.pop())

    print("Stack after pop:", stack)
