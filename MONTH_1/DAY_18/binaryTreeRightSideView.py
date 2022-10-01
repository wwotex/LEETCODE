from collections import deque
from typing import List, Optional
from TreeManager import TreeNode, BST

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result = []
        Q = deque()
        Q.append((root, 0))
        while Q:
            (node, level) = Q.popleft()
            if len(result) <= level:
                result.append(node.val)
            else:
                result[level] = node.val

            if node.left: 
                Q.append((node.left, level+1))
            if node.right:
                Q.append((node.right, level+1))

        return result

null = None
ls_tree = [1,2,3,null,5,null,4]
bst = BST(ls_tree)
sol = Solution()
print(sol.rightSideView(bst.tree))
