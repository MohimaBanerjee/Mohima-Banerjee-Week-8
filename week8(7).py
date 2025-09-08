from collections import deque
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(nodes):
    """
    Build a binary tree from a list of values (where 'N' represents None).
    Returns the root of the binary tree.
    """
    if not nodes or nodes[0] == 'N':
        return None
    
    root = Node(int(nodes[0]))
    queue = deque([root])
    i = 1
    n = len(nodes)
    
    while queue and i < n:
        current = queue.popleft()
        
        # Left child
        if i < n and nodes[i] != 'N':
            current.left = Node(int(nodes[i]))
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < n and nodes[i] != 'N':
            current.right = Node(int(nodes[i]))
            queue.append(current.right)
        i += 1
    
    return root

def isBST(root):
    """
    Check if the binary tree is a valid BST (no duplicates).
    """
    def helper(node, min_val, max_val):
        if node is None:
            return True
        
        if not (min_val < node.data < max_val):
            return False
        
        return (helper(node.left, min_val, node.data) and
                helper(node.right, node.data, max_val))
    
    return helper(root, -sys.maxsize - 1, sys.maxsize)

# Example usage:

# Example 1
nodes1 = ['2', '1', '3', 'N', 'N', 'N', '5']
root1 = buildTree(nodes1)
print(isBST(root1))  # Output: True

# Example 2
nodes2 = ['2', 'N', '7', 'N', '6', 'N', '9']
root2 = buildTree(nodes2)
print(isBST(root2))  # Output: False

# Example 3
nodes3 = ['10', '5', '20', 'N', 'N', '9', '25']
root3 = buildTree(nodes3)
print(isBST(root3))  # Output: False