from typing import Optional
from TreeManager import BST, TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def DFS(node, sum):
            if not node: return False
            sum += node.val
            if not node.left and not node.right: return targetSum == sum
            
            return DFS(node.left, sum) or DFS(node.right, sum)
        
        return DFS(root, 0)