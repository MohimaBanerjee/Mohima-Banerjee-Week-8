# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: TreeNode, key: int) -> TreeNode:
    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insertIntoBST(root.left, key)
    elif key > root.val:
        root.right = insertIntoBST(root.right, key)
    # If key == root.val, do nothing (no insertion)
    
    return root

def inorderTraversal(root: TreeNode) -> list:
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []

# Helper function to build a tree from list (level order) with 'N' as None
from collections import deque
def buildTree(nodes):
    if not nodes or nodes[0] == 'N':
        return None
    
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        curr = queue.popleft()
        
        if i < len(nodes) and nodes[i] != 'N':
            curr.left = TreeNode(int(nodes[i]))
            queue.append(curr.left)
        i += 1
        
        if i < len(nodes) and nodes[i] != 'N':
            curr.right = TreeNode(int(nodes[i]))
            queue.append(curr.right)
        i += 1
    
    return root

# Example usage:

# Input 1
root_list = ["2", "1", "3"]
key = 4
root = buildTree(root_list)
root = insertIntoBST(root, key)
print(inorderTraversal(root))  # Output: [1, 2, 3, 4]

# Input 2
root_list = ["2", "1", "3", "N", "N", "N", "6"]
key = 4
root = buildTree(root_list)
root = insertIntoBST(root, key)
print(inorderTraversal(root))  # Output: [1, 2, 3, 4, 6]

# Input 3
root_list = ["2", "1", "3"]
key = 2
root = buildTree(root_list)
root = insertIntoBST(root, key)
print(inorderTraversal(root))  # Output: [1, 2, 3]
