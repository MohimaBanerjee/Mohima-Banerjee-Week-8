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

def mirrorTree(root):
    """
    Convert the binary tree to its mirror.
    """
    if root is None:
        return None
    
    # Swap left and right children recursively
    root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
    return root

def levelOrderTraversal(root):
    """
    Return the level order traversal of the tree as a list.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('N')
    
    # Remove trailing 'N's which represent null nodes beyond the last leaf
    while result and result[-1] == 'N':
        result.pop()
    
    return result

# Example usage:

# Example 1
nodes1 = ['1', '2', '3', 'N', 'N', '4']
root1 = buildTree(nodes1)
mirrorTree(root1)
print(levelOrderTraversal(root1))  # Output: [1, 3, 2, 'N', 4]

# Example 2
nodes2 = ['1', '2', '3', '4', '5']
root2 = buildTree(nodes2)
mirrorTree(root2)
print(levelOrderTraversal(root2))  # Output: [1, 3, 2, 'N', 'N', 5, 4]