# Red-Black Tree (insertion-only) — demonstration/teaching version
# - Minimal: insert(key), inorder(), and a simple print_tree() for structure
# - Uses a single shared NIL sentinel node
# - Colors: 'R' = red, 'B' = black

class RBNode:
    __slots__ = ("key", "color", "left", "right", "parent")

    def __init__(self, key=None, color='B', left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RBTree:
    def __init__(self):
        # Single NIL sentinel (black)
        self.NIL = RBNode(key=None, color='B')
        self.root = self.NIL

    # ---------- Utility rotations ----------
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.NIL:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    # ---------- Insertion ----------
    def insert(self, key):
        # Standard BST insert (node starts red)
        z = RBNode(key=key, color='R', left=self.NIL, right=self.NIL, parent=None)
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y is self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self._insert_fixup(z)

    # ---------- Restore RB properties after insert ----------
    def _insert_fixup(self, z):
        while z.parent.color == 'R':  # parent is red → violation
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right  # uncle
                # Case 1: Uncle is red → recolor and move up the tree
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    # Case 2/3: Uncle is black → rotations + recolor
                    if z is z.parent.right:
                        z = z.parent
                        self.left_rotate(z)  # convert to straight line
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.right_rotate(z.parent.parent)
            else:
                # Mirror of above (parent is right child)
                y = z.parent.parent.left  # uncle
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'B'

    # ---------- Helpers to inspect ----------
    def inorder(self):
        """Return sorted list of keys (BST property check)."""
        out = []
        def _inorder(n):
            if n is self.NIL: return
            _inorder(n.left)
            out.append(n.key)
            _inorder(n.right)
        _inorder(self.root)
        return out

    def print_tree(self):
        """Simple level-by-level print: (key,color) with NIL suppressed."""
        if self.root is self.NIL:
            print("")
            return
        q = [(self.root, 0)]
        level = 0
        line = []
        while q:
            node, lvl = q.pop(0)
            if lvl != level:
                print(" ".join(line))
                line = []
                level = lvl
            if node is self.NIL:
                line.append("NIL")
            else:
                line.append(f"({node.key},{node.color})")
                q.append((node.left, lvl+1))
                q.append((node.right, lvl+1))
        if line:
            print(" ".join(line))


# ---------- Demo ----------
if __name__ == "__main__":
    t = RBTree()
    for k in [10, 20, 30, 15, 25, 5, 7,6]:
        t.insert(k)
        # Uncomment to watch the tree evolve:
        print(f"After inserting {k}:")
        t.print_tree(); print()
    print("Inorder:", t.inorder())
    print("Structure:")
    t.print_tree()
