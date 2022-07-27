
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ls = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.visitNode(root, 0)
        return self.ls
        
    def visitNode(self, node, h):
        if len(self.ls) > h:
            self.ls[h].append(node.val)
        else:
            self.ls.append([node.val])
        
        if node.left: self.visitNode(node.left, h+1)
        if node.right: self.visitNode(node.right, h+1)



