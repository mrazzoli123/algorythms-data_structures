class Node:
    __slots__ = ("key", "left", "right", "height")
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # leaf

def height(n):
    return n.height if n else 0

def balance_factor(n):
    return height(n.left) - height(n.right) if n else 0

def update_height(n):
    n.height = 1 + max(height(n.left), height(n.right))

# --- Rotations ---
def right_rotate(y):
    r"""
    Rotate right around y:
           y                x
          / \              / \
         x   T3   ->      T1  y
        / \                  / \
       T1 T2                T2 T3
    """
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    update_height(y)
    update_height(x)
    return x  # new root

def left_rotate(x):
    r"""
    Rotate left around x:
        x                    y
       / \                  / \
      T1  y      ->        x  T3
         / \              / \
        T2 T3            T1 T2
    """
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    update_height(x)
    update_height(y)
    return y  # new root

# --- Insertion (with rebalancing) ---
def insert(root, key):
    # 1) Normal BST insert
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # ignore duplicates (no-op)

    # 2) Update height
    update_height(root)

    # 3) Get balance and rotate if needed
    bf = balance_factor(root)

    # Case LL
    if bf > 1 and key < root.left.key:
        return right_rotate(root)

    # Case RR
    if bf < -1 and key > root.right.key:
        return left_rotate(root)

    # Case LR
    if bf > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case RL
    if bf < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# --- Helpers for quick testing ---
def inorder(n):
    return inorder(n.left) + [n.key] + inorder(n.right) if n else []

def preorder(n):
    return [n.key] + preorder(n.left) + preorder(n.right) if n else []


# --- Deletion (with rebalancing) ---
def min_value_node(n):
    # Inorder successor lives at the leftmost node of a subtree
    current = n
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    # 1) Normal BST delete  (three removal cases)
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Found the node to remove
        if root.left is None:          # leaf  OR  only a right child
            return root.right
        if root.right is None:         # only a left child
            return root.left
        # Two children: copy inorder successor up, then delete it
        succ = min_value_node(root.right)
        root.key = succ.key
        root.right = delete(root.right, succ.key)

    # 2) Update height
    update_height(root)

    # 3) Get balance and rotate if needed
    #    Unlike insert, there is no inserted key to compare against,
    #    so the case is decided by the HEAVY CHILD's balance factor.
    bf = balance_factor(root)

    # Case LL
    if bf > 1 and balance_factor(root.left) >= 0:
        return right_rotate(root)

    # Case LR
    if bf > 1 and balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case RR
    if bf < -1 and balance_factor(root.right) <= 0:
        return left_rotate(root)

    # Case RL
    if bf < -1 and balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root  # no rotation needed at this node

# Example:
if __name__ == "__main__":
    root = None
    for k in [10, 20, 30, 40, 50, 25]:
        root = insert(root, k)
    print("inorder:", inorder(root))
    print("preorder:", preorder(root))
