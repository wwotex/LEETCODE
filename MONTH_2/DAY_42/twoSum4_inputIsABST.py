from typing import Optional
from TreeManager import TreeNode, BST

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        H = set()
        S = [root]
        while S:
            curr = S.pop()
            if curr.left: S.append(curr.left)
            if curr.right: S.append(curr.right)
            if k - curr.val in H:
                return True
            H.add(curr.val)
        return False

# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         S = []
#         ls_tree = []
#         curr = root
#         while True:
#             if curr is not None:
#                 S.append(curr)
#                 curr = curr.left
#             elif S:
#                 curr = S.pop()
#                 ls_tree.append(curr.val)
#                 curr = curr.right
#             else:
#                 break
        
#         left, right = 0, len(ls_tree)-1
#         while left < right:
#             sum = ls_tree[left] + ls_tree[right]
#             if sum == k:
#                 return True
#             elif sum < k:
#                 left += 1
#             else:
#                 right -= 1
#         return False

sol = Solution()
null = None
ls_1 = [5,3,6,2,4,null,7]
k = 9
gen = BST(ls_1)

print(sol.findTarget(gen.tree, k))