class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self, key):
        if self.root==None:
            self.root=Node(key)
        else:
            self._insert(self.root,key)
            
    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
                
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.value:
            return True
        elif key < current_node.value:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)
        
    def inorder(self):
        elements = []
        self._inorder(self.root, elements)
        return elements

    def _inorder(self, current_node, elements):
        if current_node:
            self._inorder(current_node.left, elements)
            elements.append(current_node.value)
            self._inorder(current_node.right, elements)
            
    def preorder(self):
        elements = []
        self._preorder(self.root, elements)
        return elements
    
    def _preorder(self, current_node, elements):
        if current_node:
            elements.append(current_node.value)
            self._preorder(current_node.left, elements)
            self._preorder(current_node.right, elements)
            
    def postorder(self):
        elements = []
        self._postorder(self.root, elements)
        return elements
    
    def _postorder(self, current_node, elements):
        if current_node:
            self._postorder(current_node.left, elements)
            self._postorder(current_node.right, elements)
            elements.append(current_node.value)
            
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value
    
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current