class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node_data, data):
        current_node = self.head
        while current_node and current_node.data != prev_node_data:
            current_node = current_node.next
        if not current_node:
            print("The mentioned node is not found.")
            return
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("The node with data", key, "is not found.")
            return

        prev_node.next = current_node.next
        current_node = None

    def search(self, key):
            current_node = self.head
            while current_node and current_node.data != key:
                current_node = current_node.next
            if current_node:
                return True
            return False

    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("The linked list is empty.")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_beginning(0)

    print("Linked list after insertion:")
    linked_list.print_list()

    linked_list.delete_node(2)
    print("Linked list after deleting node with data 2:")
    linked_list.print_list()

    found = linked_list.search(3)
    print("Node with data 3 found:", found)
    
    print("Length of the linked list:", linked_list.length())