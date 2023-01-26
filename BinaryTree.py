from TreeNode import TreeNode

class BinaryTree:
    def __init__(self, items: list):
        self.root = self.to_binary_tree(items)


    def to_binary_tree(self, items: list) -> TreeNode:
        if len(items) == 0:
            return None

        elif len(items) == 1:
            return TreeNode(items[0])

        # Replace elements in list with TreeNodes in place, O(n) item complexity
        for i, n in enumerate(items):
            items[i] = TreeNode(n)
    
        # Construct tree in place, O(n) time complexity
        l, r = 0, 1
        while r < len(items):
            if items[l].left is None:
                items[l].left = items[r]
            elif items[l].right is None:
                items[l].right = items[r]
            else:
                l += 1
                continue

            r += 1

        return items[0]

    def dfs(self, root: TreeNode, val) -> TreeNode:
        if root is None:
            return None
        
        if root.val == val:
            return root

        return self.dfs(root.left, val) or self.dfs(root.right, val)
