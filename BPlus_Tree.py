# B+ Tree Node
class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.keys = []          # List of keys
        self.children = []      # List of child pointers (internal nodes only)
        self.leaf = leaf        # True if leaf node
        self.next = None        # Link to the next leaf (leaves only)

# B+ Tree
class BPlusTree:
    def __init__(self, t):
        if t < 2:
            raise ValueError("B+ Tree minimum degree t must be >= 2.")
        self.t = t              # Minimum degree: a node holds at most 2t - 1 keys
        self.root = BPlusTreeNode(True)

    # Insert a key (proactive splitting: split full nodes on the way down)
    def insert(self, key):
        root = self.root

        # If root is full, need to split
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BPlusTreeNode(False)
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
            # Move to the correct child ("equals go right")
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Split child if full
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key >= node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    # Split the full child of a node (the child has 2t - 1 keys)
    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BPlusTreeNode(y.leaf)

        # Save the middle key before modifying y.keys
        middle = y.keys[t - 1]

        if y.leaf:
            # Leaf split: COPY up. The middle key stays in the right leaf (it is data).
            z.keys = y.keys[t - 1:]
            y.keys = y.keys[:t - 1]

            # Re-link the leaf chain: y -> z -> old y.next
            z.next = y.next
            y.next = z
        else:
            # Internal split: MOVE up. The middle key leaves this level.
            z.keys = y.keys[t:]
            y.keys = y.keys[:t - 1]
            z.children = y.children[t:]
            y.children = y.children[:t]

        # Insert new child and the middle key into parent
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, middle)

    # Search always goes down to a leaf
    def search(self, key):
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return key in node.keys

    # Range query: find the first leaf, then walk the leaf links
    def range_search(self, lo, hi):
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and lo >= node.keys[i]:
                i += 1
            node = node.children[i]

        result = []
        while node is not None:
            for k in node.keys:
                if k > hi:
                    return result
                if k >= lo:
                    result.append(k)
            node = node.next
        return result

    # All keys in sorted order, read along the leaf links
    def leaves(self):
        node = self.root
        while not node.leaf:
            node = node.children[0]
        result = []
        while node is not None:
            result.extend(node.keys)
            node = node.next
        return result

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        print(" " * (level * 4) + prefix + str(node.keys))

        if not node.leaf:
            for i, child in enumerate(node.children):
                child_prefix = f"Child {i}: "
                self.print_tree(child, level + 1, child_prefix)


# Example (the worked example from the slides: t = 2, so at most 3 keys per node)
if __name__ == "__main__":
    bpt = BPlusTree(t=2)
    for k in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        bpt.insert(k)
        print(f"--- after inserting {k} ---")
        bpt.print_tree()

    print(bpt.leaves())
    print(bpt.range_search(4, 8))
    print(bpt.search(9))