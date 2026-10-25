class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a value according to BST rules
def insert_bst(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert_bst(root.left, data)
    elif data > root.data:
        root.right = insert_bst(root.right, data)

    return root


# Search for a key in the BST: O(h) time complexity
def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Preorder Traversal (Root -> Left -> Right)
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Inorder Traversal (Left -> Root -> Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Postorder Traversal (Left -> Right -> Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Main Program
n = int(input("Enter the number of elements: "))

print(f"Enter {n} numbers separated by spaces:")
values = list(map(int, input().split()))

if len(values) != n:
    print(f"Error: Expected {n} elements, but got {len(values)}.")
else:
    root = None
    for val in values:
        root = insert_bst(root, val)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nInorder Traversal (Sorted):")
    inorder(root)

    print("\nPostorder Traversal:")
    postorder(root)

    key = int(input("\n\nEnter the value to search: "))

    if search(root, key):
        print(f"{key} found in the tree.")
    else:
        print(f"{key} not found in the tree.")
