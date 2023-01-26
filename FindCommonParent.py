from TreeNode import TreeNode
from BinaryTree import BinaryTree

def find_common_parent(root, i1, i2):
    parents = {}

    def dfs(node, arr):
        # Bass case
        if node is None:
            return

        if node.val == i1:
            parents[i1] = arr.copy()

        if node.val == i2:
            parents[i2] = arr.copy()

        arr.append(node)
        dfs(node.left, arr.copy())
        dfs(node.right, arr.copy())

        return 

    # Populate parents dictionary with ancestor nodes
    dfs(root, [])

    # i1 or i2 not in tree
    if i1 not in parents or i2 not in parents:
        return None
    
    # Find most recent  common parent
    for i in range(len(parents[i1]) -1, -1, -1):
        if parents[i1][i] in parents[i2]:
            return parents[i1][i].val
            
    # Nodes include root node
    return None
