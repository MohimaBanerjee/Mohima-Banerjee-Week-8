from collections import deque

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

def height(root):
    """
    Returns the height of the binary tree.
    Height is number of edges on longest path from root to leaf.
    """
    if root is None:
        return -1  # no edges in empty tree
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    return 1 + max(left_height, right_height)

# Example usage:

# Example 1
nodes1 = ['12', '8', '18', '5', '11']
root1 = buildTree(nodes1)
print(height(root1))  # Output: 2

# Example 2
nodes2 = ['1', '2', '3', '4', 'N', 'N', '5', 'N', 'N', '6', '7']
root2 = buildTree(nodes2)
print(height(root2))  # Output: 3