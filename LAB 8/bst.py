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
        
# Construct the binary tree
root = construct_binary_tree()


print("Pre-order Traversal:")
preorder_traversal(root)