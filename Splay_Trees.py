class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self, trace=False):
        self.root = None
        self.trace = trace  # print each splay step when True

    # ---------- rotations ----------

    def _rotate_left(self, x):
        """x's right child y moves up; x becomes y's left child."""
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        """x's left child y moves up; x becomes y's right child."""
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # ---------- splay ----------

    def _splay(self, x):
        while x.parent is not None:
            p = x.parent
            g = p.parent

            if g is None:
                # ZIG: parent is the root -> single rotation
                self._log(f"zig at {x.key}")
                if x is p.left:
                    self._rotate_right(p)
                else:
                    self._rotate_left(p)

            elif x is p.left and p is g.left:
                # ZIG-ZIG (left-left): rotate grandparent first, then parent
                self._log(f"zig-zig (left-left) at {x.key}")
                self._rotate_right(g)
                self._rotate_right(p)

            elif x is p.right and p is g.right:
                # ZIG-ZIG (right-right)
                self._log(f"zig-zig (right-right) at {x.key}")
                self._rotate_left(g)
                self._rotate_left(p)

            elif x is p.right and p is g.left:
                # ZIG-ZAG (left-right): rotate parent, then grandparent
                self._log(f"zig-zag (left-right) at {x.key}")
                self._rotate_left(p)
                self._rotate_right(g)

            else:
                # ZIG-ZAG (right-left)
                self._log(f"zig-zag (right-left) at {x.key}")
                self._rotate_right(p)
                self._rotate_left(g)

    # ---------- insertion ----------

    def insert(self, key):
        # Phase 1: standard BST insert
        parent = None
        cur = self.root
        while cur is not None:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                # Duplicate: splay the existing node and stop
                self._log(f"{key} already present; splaying it")
                self._splay(cur)
                return

        node = Node(key)
        node.parent = parent
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node

        # Phase 2: splay the new node to the root
        self._splay(node)

    # ---------- helpers for display ----------

    def _log(self, msg):
        if self.trace:
            print("   ", msg)

    def inorder(self):
        out = []

        def walk(n):
            if n:
                walk(n.left)
                out.append(n.key)
                walk(n.right)

        walk(self.root)
        return out

    def show(self):
        """Print the tree sideways: root on the left, right subtree on top."""
        def walk(n, prefix, is_right):
            if n is None:
                return
            walk(n.right, prefix + ("    " if is_right else "│   "), True)
            print(prefix + ("┌── " if is_right else "└── ") + str(n.key))
            walk(n.left, prefix + ("│   " if is_right else "    "), False)

        if self.root is None:
            print("(empty)")
            return
        walk(self.root.right, "", True)
        print(str(self.root.key))
        walk(self.root.left, "", False)


if __name__ == "__main__":
    tree = SplayTree(trace=True)
    for k in [50, 30, 70, 20, 40, 60, 80, 35]:
        print(f"\nInsert {k}:")
        tree.insert(k)
        tree.show()
        assert tree.root.key == k, "inserted key must end up at the root"

    print("\nIn-order:", tree.inorder())