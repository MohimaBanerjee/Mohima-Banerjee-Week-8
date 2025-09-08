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

def diameter(root):
    """
    Returns the diameter (number of edges on longest path between two leaves) of the binary tree.
    """
    max_diameter = [0]  # Use list to hold max diameter as nonlocal variable
    
    def height(node):
        if node is None:
            return -1  # height in edges, so empty node has height -1
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Diameter at this node is left_height + right_height + 2 edges
        current_diameter = left_height + right_height + 2
        max_diameter[0] = max(max_diameter[0], current_diameter)
        
        # Height of node is max height of subtrees + 1 edge
        return 1 + max(left_height, right_height)
    
    height(root)
    return max_diameter[0]

# Example usage:

# Example 1
nodes1 = ['1', '2', '3']
root1 = buildTree(nodes1)
print(diameter(root1))  # Output: 2

# Example 2
nodes2 = ['5', '8', '6', '3', '7', '9']
root2 = buildTree(nodes2)
print(diameter(root2))  # Output: