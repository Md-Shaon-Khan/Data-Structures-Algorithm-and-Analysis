class Node:
    def __init__(self, key): # Node class with height attribute for AVL tree
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(n): # height of a node, if node is None then height is 0
    if not n:
        return 0
    return n.height

def balance(n): # balance factor = height of left subtree - height of right subtree, if node is None then balance is 0 
    if not n:
        return 0
    return height(n.left) - height(n.right)

def right_rotate(y):                                                # right rotation around node y
    x = y.left                                                      # x is left child of y
    T2 = x.right                                                    # T2 is right child of x
    x.right = y                                                     # y becomes right child of x
    y.left = T2                                                     # T2 becomes left child of y
    y.height = 1 + max(height(y.left), height(y.right))             # update height of y
    x.height = 1 + max(height(x.left), height(x.right))             # update height of x
    return x                                                        # x becomes new root after rotation

def left_rotate(x):                                         # left rotation around node x
    y = x.right                                             # y is right child of x
    T2 = y.left                                             # T2 is left child of y
    y.left = x                                              # x becomes left child of y
    x.right = T2                                            # T2 becomes right child of x
    x.height = 1 + max(height(x.left), height(x.right))     # update height of x
    y.height = 1 + max(height(y.left), height(y.right))     # update height of y
    return y                                                # y becomes new root after rotation

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and key < root.left.key:
        return right_rotate(root)
    
    if b < -1 and key > root.right.key:
        return left_rotate(root)
    
    if b > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    if b < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def min_value_node(n):
    current = n
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    if not root:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and balance(root.left) >= 0:
        return right_rotate(root)
    
    if b < -1 and balance(root.right) <= 0:
        return left_rotate(root)
    
    if b > 1 and balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    if b < -1 and balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# ---------------- Test ----------------
root = None
for k in [10, 20, 30, 40, 50, 25]:
    root = insert(root, k)

print("Inorder after insertion:")
inorder(root)

root = delete(root, 40)
root = delete(root, 30)
print("\nInorder after deletion:")
inorder(root)