

from typing import Optional
from TreeManager import BST, TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:    
        def merkle(node):
            return f'^{node.val}.{merkle(node.left)} {merkle(node.right)}' if node else '#'
        return merkle(subRoot) in merkle(root)

sol = Solution()
null = None
root = [3,4,5,1,2,null,null,null,null,0]
subRoot = [4,1,2]
gen1 = BST(root)
gen2 = BST(subRoot)
gen1.print()
gen2.print()
print(sol.isSubtree(gen1.tree, gen2.tree))
