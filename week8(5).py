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

def leftView(root):
    """
    Return the left view of the binary tree as a list.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # The first node in this level is part of the left view
            if i == 0:
                result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example usage:

# Example 1
nodes1 = ['1', '2', '3', '4', '5', 'N', 'N']
root1 = buildTree(nodes1)
print(leftView(root1))  # Output: [1, 2, 4]

# Example 2
nodes2 = ['1', '2', '3', 'N', 'N', '4', 'N', 'N', '5', 'N', 'N']
root2 = buildTree(nodes2)
print(leftView(root2))  # Output: [1, 2, 4, 5]