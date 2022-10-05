from collections import deque
from typing import Optional
from TreeManager import BST, TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        Q = deque([(root, 1)])
        while Q:
            (node, d) = Q.popleft()
            if d == depth-1:
                temp_left = TreeNode(val)
                temp_left.left = node.left
                temp_right = TreeNode(val)
                temp_right.right = node.right
                node.left = temp_left
                node.right = temp_right
                continue
            if node.left: Q.append((node.left, d+1))
            if node.right: Q.append((node.right, d+1))
        return root