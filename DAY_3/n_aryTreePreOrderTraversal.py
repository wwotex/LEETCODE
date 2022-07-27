from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        traversal_ls = []
        queue = []
        queue.append(root)
        while queue:
            curr = queue.pop()
            traversal_ls.append(curr.val)
            for el in reversed(curr.children):
                queue.append(el)
        return traversal_ls
            
            

sol = Solution()

