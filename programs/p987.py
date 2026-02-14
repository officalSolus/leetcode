class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = []
        
        def dfs(node, col, row):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)
        
        dfs(root, 0, 0)
        nodes.sort(key=lambda x: (x[0], x[1], x[2]))
        
        result = []
        prev_col = nodes[0][0]
        current_group = []
        
        for col, row, val in nodes:
            if col != prev_col:
                result.append(current_group)
                current_group = []
                prev_col = col
            current_group.append(val)
        if current_group:
            result.append(current_group)
            
        return result