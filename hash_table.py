class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(f"({current.key}: {current.value})")
            current = current.next
        return " -> ".join(result) if result else "Empty"

class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)

    def search(self, key):
        index = self._hash(key)
        return self.table[index].search(key)

    def remove(self, key):
        index = self._hash(key)
        return self.table[index].remove(key)

    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.table):
            result += f"Bucket {i}: {bucket}\n"
        return result