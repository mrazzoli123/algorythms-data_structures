class ArrayBinaryTree:
    def __init__(self, capacity):
        self.tree = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def insert(self, key):
        if self.size < self.capacity:
            self.tree[self.size] = key
            self.size += 1
        else:
            raise Exception("Tree capacity exceeded")

    def left_child_index(self, i):
        left = 2 * i + 1
        if left >= self.size:
            return None
        return left

    def right_child_index(self, i):
        right = 2 * i + 2
        if right >= self.size:
            return None
        return right

    def parent_index(self, i):
        if i == 0:
            return None
        return (i - 1) // 2

    def inorder(self, i=0, result=None):
        if result is None:
            result = []
        if i >= self.size or self.tree[i] is None:
            return
        left = self.left_child_index(i)
        if left is not None:
            self.inorder(left, result)
        result.append(self.tree[i])
        right = self.right_child_index(i)
        if right is not None:
            self.inorder(right, result)
        return result

    def preorder(self, i=0, result=None):
        if result is None:
            result = []
        if i >= self.size or self.tree[i] is None:
            return
        result.append(self.tree[i])
        left = self.left_child_index(i)
        if left is not None:
            self.preorder(left, result)
        right = self.right_child_index(i)
        if right is not None:
            self.preorder(right, result)
        return result

    def postorder(self, i=0, result=None):
        if result is None:
            result = []
        if i >= self.size or self.tree[i] is None:
            return
        left = self.left_child_index(i)
        if left is not None:
            self.postorder(left, result)
        right = self.right_child_index(i)
        if right is not None:
            self.postorder(right, result)
        result.append(self.tree[i])
        return result

    def search(self, key):
        for i in range(self.size):
            if self.tree[i] == key:
                return True
        return False