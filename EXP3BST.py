class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Build tree from preorder list (-1 represents NULL)
def insert_node(values):
    if not values:
        return None

    data = values.pop(0)

    if data == -1:
        return None

    node = Node(data)
    node.left = insert_node(values)
    node.right = insert_node(values)

    return node


# Preorder Traversal
def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


# Inorder Traversal
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


# Postorder Traversal
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


# Main Program
n = int(input("Enter the number of elements: "))

print("Enter the preorder elements (-1 for NULL):")
values = list(map(int, input().split()))

if len(values) != n:
    print("Error: Number of elements does not match.")
else:
    root = insert_node(values)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nInorder Traversal:")
    inorder(root)

    print("\nPostorder Traversal:")
    postorder(root)