class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_binary_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root

# Pre-order traversal function
def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# In-order traversal function
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Post-order traversal function
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

# Construct the binary tree
root = construct_binary_tree()


print("Pre-order Traversal:")
preorder_traversal(root)
print("\nIn-order Traversal:")
inorder_traversal(root)
print("\nPost-order Traversal:")
postorder_traversal(root)
