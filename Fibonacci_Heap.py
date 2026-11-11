class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None      # pointer to ANY one child; children form a circular list
        self.left = self       # siblings: circular, doubly-linked
        self.right = self
        self.degree = 0        # number of children
        self.mark = False      # has this node lost a child since it became a child?

    def __repr__(self):
        return f"Node({self.key})"


# ---------- circular doubly-linked list helpers (all O(1)) ----------

def _insert_right(a, b):
    """Put the single node b immediately to the right of a."""
    b.left = a
    b.right = a.right
    a.right.left = b
    a.right = b


def _unlink(x):
    """Take x out of whatever circular list it is in."""
    x.left.right = x.right
    x.right.left = x.left
    x.left = x.right = x


def _join(a, b):
    """Concatenate the circular list containing a with the one containing b."""
    a_right, b_left = a.right, b.left
    a.right, b.left = b, a
    b_left.right, a_right.left = a_right, b_left


def _nodes(start):
    """Return the nodes of a circular list as a Python list (a snapshot)."""
    if start is None:
        return []
    result, x = [start], start.right
    while x is not start:
        result.append(x)
        x = x.right
    return result


# ---------------------------- the heap ----------------------------

class FibonacciHeap:
    def __init__(self):
        self.min = None   # min root; also our entry point into the root list
        self.n = 0

    # ----- O(1) operations -----

    def insert(self, key):
        """Make a one-node tree and drop it into the root list. No cleanup."""
        x = Node(key)
        if self.min is None:
            self.min = x
        else:
            _insert_right(self.min, x)
            if x.key < self.min.key:
                self.min = x
        self.n += 1
        return x          # the caller keeps this handle for decrease_key / delete

    def find_min(self):
        return None if self.min is None else self.min.key

    def merge(self, other):
        """Splice the other heap's root list into ours. `other` is emptied."""
        if other.min is None:
            return
        if self.min is None:
            self.min = other.min
        else:
            _join(self.min, other.min)
            if other.min.key < self.min.key:
                self.min = other.min
        self.n += other.n
        other.min, other.n = None, 0

    # ----- extract-min: the only place we tidy up -----

    def extract_min(self):
        z = self.min
        if z is None:
            return None

        # 1. Promote z's children to the root list.
        if z.child is not None:
            for c in _nodes(z.child):
                c.parent = None
                c.mark = False         # roots are never marked
            _join(z, z.child)

        # 2. Remove z itself.
        if z.right is z:               # z was the only node
            self.min = None
        else:
            self.min = z.right         # temporary; consolidate fixes it
            _unlink(z)
            self._consolidate()

        self.n -= 1
        return z.key

    def _consolidate(self):
        """Link roots of equal degree until every root degree is distinct."""
        by_degree = {}                 # degree -> the root of that degree we have seen
        for x in _nodes(self.min):     # snapshot, because linking edits the list
            d = x.degree
            while d in by_degree:
                y = by_degree.pop(d)
                if y.key < x.key:      # smaller key stays on top
                    x, y = y, x
                self._link(y, x)       # y becomes a child of x
                d += 1
            by_degree[d] = x

        # 3. The survivors are the new root list; find the new min.
        self.min = None
        for x in by_degree.values():
            if self.min is None or x.key < self.min.key:
                self.min = x

    def _link(self, y, x):
        """Remove root y from the root list and make it a child of root x."""
        _unlink(y)
        y.parent = x
        if x.child is None:
            x.child = y
        else:
            _insert_right(x.child, y)
        x.degree += 1
        y.mark = False

    # ----- decrease-key, with cuts and cascading cuts -----

    def decrease_key(self, x, new_key):
        if new_key > x.key:
            raise ValueError("new key is larger than current key")
        x.key = new_key
        y = x.parent
        if y is not None and x.key < y.key:   # heap order broken
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x, y):
        """Move x (with its whole subtree) from y's child list to the root list."""
        if x.right is x:
            y.child = None
        elif y.child is x:
            y.child = x.right
        _unlink(x)
        y.degree -= 1
        _insert_right(self.min, x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        """A node may lose one child (gets marked); losing a second one cuts it too."""
        z = y.parent
        while z is not None:           # stop when we reach a root
            if not y.mark:
                y.mark = True          # first lost child: just mark it
                return
            self._cut(y, z)            # second lost child: cut it, keep going up
            y, z = z, z.parent

    # ----- delete = decrease-key to -infinity, then extract-min -----

    def delete(self, x):
        self.decrease_key(x, float("-inf"))
        self.extract_min()

    # ----- printing, for the classroom -----

    def show(self, title=""):
        if title:
            print(f"--- {title} ---")
        if self.min is None:
            print("(empty)\n")
            return
        for root in _nodes(self.min):
            self._show(root, "", True, is_root=True)
        print()

    def _show(self, x, prefix, last, is_root=False):
        label = str(x.key)
        if x is self.min:
            label += "  <- min"
        if x.mark:
            label += "  (marked)"
        if is_root:
            print(label)
            child_prefix = ""
        else:
            print(prefix + ("└── " if last else "├── ") + label)
            child_prefix = prefix + ("    " if last else "│   ")
        kids = _nodes(x.child)
        for i, c in enumerate(kids):
            self._show(c, child_prefix, i == len(kids) - 1)


# ------------------------------ demo ------------------------------

if __name__ == "__main__":
    # Same example as the slides.
    h = FibonacciHeap()
    handle = {}
    for k in [7, 3, 18, 52, 38, 39, 41, 17, 23, 30]:
        handle[k] = h.insert(k)
    h.show("After 10 inserts: just a flat root list")

    print("extract_min ->", h.extract_min())
    h.show("After extract-min: consolidated into a 7 and a degree-3 tree at 17")

    h.decrease_key(handle[52], 2)
    h.show("decrease_key 52 -> 2: cut 2, mark its parent 18")

    h.decrease_key(handle[38], 1)
    h.show("decrease_key 38 -> 1: cut 1; 18 was marked, so cut 18 too")

    h.delete(handle[23])
    h.show("delete 23 (decrease to -inf, then extract-min)")

    print("Draining the heap:", [h.extract_min() for _ in range(h.n)])