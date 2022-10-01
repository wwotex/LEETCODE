from collections import defaultdict
from distutils.log import debug


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# nice way of being very clean -> instead of checking which level it is you just use a dummy at the end of levels
# to keep just making new left-most nodes NEXTs of the dummy 
# you do level order traversal without a QUEUE because you create the path for yourself with the line curr = curr.next
# the inner while loop is for traversing one level and it starts with dummy.next because we always put the kid on the dummy
# at the end of each level

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = kid = Node(0)
        curr = root
        while curr:
            while curr:
                kid.next = curr.left
                kid = kid.next or kid
                kid.next = curr.right
                kid = kid.next or kid
                curr = curr.next
            curr, kid = dummy.next, dummy
        return root

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None: return None
#         S = [(root, 0)]
#         levels = defaultdict(list)
#         debug_levels = defaultdict(list)
#         debug_nodes = []
#         while S:
#             (curr, lev) = S.pop()
#             curr.next = levels[lev][-1] if levels[lev] else None
#             debug_nodes.append(curr)

#             levels[lev].append(curr) 
#             debug_levels[lev].append(curr.val)

#             if curr.left: S.append((curr.left, lev+1))
#             if curr.right: S.append((curr.right, lev+1))
           
#         return root

sol = Solution()
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(7)
new = sol.connect(root)