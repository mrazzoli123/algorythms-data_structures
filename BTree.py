class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t              # Minimum degree (defines range for keys)
        self.keys = []          # List of keys
        self.children = []      # List of child pointers
        self.leaf = leaf        # True if leaf node

# B-Tree
class BTree:
    def __init__(self, t):
        if t < 2:
            raise ValueError("B-Tree minimum degree t must be >= 2.")
        self.t = t              # Minimum degree
        self.root = BTreeNode(t, True)

    # Utility function to insert a key
    def insert(self, key):
        root = self.root

        # If root is full, need to split
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.insert(0, root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
            self.root = new_root
        else:
            self.insert_non_full(root, key)

    # Insert a key into a node that is not full
    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            # Insert key in sorted order
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # Move to the correct child
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Split child if full
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                # keep routing consistent with the search rule ("equals go right")
                if key >= node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    # Split the child of a node
    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)

        # Save the middle key before modifying y.keys
        middle = y.keys[t-1]

        # Right node gets keys after the middle
        z.keys = y.keys[t:]
        # Left node keeps keys before the middle
        y.keys = y.keys[:t - 1]

        # Move children if not leaf
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        # Insert new child and the middle key into parent
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, middle)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        print(" " * (level * 4) + prefix + str(node.keys))

        if not node.leaf:
            for i, child in enumerate(node.children):
                child_prefix = f"Child {i}: "
                self.print_tree(child, level + 1, child_prefix)

    def inorder(self):
        """Return all keys in the B-Tree in sorted (in-order) order."""
        result = []
        self._inorder_node(self.root, result)
        return result

    def _inorder_node(self, node, result):
        if node.leaf:
            result.extend(node.keys)
        else:
            n = len(node.keys)
            i = 0
            while i < n:
                # traverse the i-th child
                result.append(node.keys[i])

                self._inorder_node(node.children[i], result)
                # then visit the i-th key
                i += 1
            # finally, traverse the last child
            self._inorder_node(node.children[i], result)

    def postorder(self):
        """Return all keys in post-order traversal."""
        result = []
        self._postorder_node(self.root, result)
        return result

    def _postorder_node(self, node, result):
        if node.leaf:
            # Leaf node: just append its keys (after visiting no children)
            result.extend(node.keys)
        else:
            # Visit all children first
            for child in node.children:
                self._postorder_node(child, result)
            # Then visit this node’s own keys
            result.extend(node.keys)


# Example
if __name__ == "__main__":
    bt = BTree(t=2)
    for k in [10, 20, 5, 6, 12, 30, 7, 17, 1, 13, 11]:
        bt.insert(k)
        bt.print_tree()

    bt.print_tree()
    print(bt.inorder())