class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# ---------- BST Operations ----------

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def min_value_node(root):
    current = root
    while current.left:
        current = current.left
    return current

def max_value_node(root):
    current = root
    while current.right:
        current = current.right
    return current

def delete(root, key):
    if not root:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node with one child or no child
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        # Node with two children
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Successor (next higher value)
def successor(root, key):
    succ = None
    current = root
    while current:
        if key < current.key:
            succ = current
            current = current.left
        else:
            current = current.right
    return succ

# Predecessor (next lower value)
def predecessor(root, key):
    pred = None
    current = root
    while current:
        if key > current.key:
            pred = current
            current = current.right
        else:
            current = current.left
    return pred

# ---------- Test ----------
root = None
for k in [20, 10, 30, 5, 15, 25, 35]:
    root = insert(root, k)

print("Inorder traversal:")
inorder(root)
print()

print("Minimum:", min_value_node(root).key)
print("Maximum:", max_value_node(root).key)

key = 15
succ = successor(root, key)
pred = predecessor(root, key)
print(f"Successor of {key}:", succ.key if succ else None)
print(f"Predecessor of {key}:", pred.key if pred else None)

root = delete(root, 10)
print("Inorder after deleting 10:")
inorder(root)