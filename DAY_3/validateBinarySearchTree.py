import sys
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.visitNode(root, -sys.maxsize, sys.maxsize)

    def visitNode(self, node, min, max):
        if node.val > max or node.val < min:
            return False    
        
        a, b = True, True
        if node.left: 
            a = self.visitNode(node.left, min, node.val-1)
        if node.right:
            b = self.visitNode(node.right, node.val+1, max)
        
        return a and b

