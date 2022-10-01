from typing import Optional
from TreeManager import TreeNode, BST


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        S = []
        S.append(p)
        S.append(q)
        while S:
            n1 = S.pop()
            n2 = S.pop()
            
            if not n1 and not n2:
                continue

            if type(n1) != type(n2) or n1.val != n2.val:
                return False
            
            S.append(n1.left)
            S.append(n2.left)
            S.append(n1.right)
            S.append(n2.right)
        
        return True