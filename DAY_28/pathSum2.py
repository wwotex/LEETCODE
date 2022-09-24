from collections import deque
from typing import List, Optional
from TreeManager import TreeNode, BST

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: return []
        sum, result, path, S = 0, [], [], [(root, False)]

        while S:
            (curr, visited) = S[-1]
            
            if visited:
                S.pop()
                path.pop()
                sum -= curr.val
                continue
            
            S[-1] = (curr, True)
            path.append(curr.val)
            sum += curr.val

            if not curr.left and not curr.right and sum == targetSum:
                result.append(path.copy())
            
            if curr.left: S.append((curr.left, False))
            if curr.right: S.append((curr.right, False))
            pass

        return result
            
            

sol = Solution()
null = None
ls_tree = [5,4,8,11,null,13,4,7,2,null,null,5,1]
gen = BST(ls_tree)
target = 22
gen.print()
print(sol.pathSum(gen.tree, target))


# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         if root is None: return []
#         visited, sum, result, path, S = set(), 0, [], [], [root]

#         while S:
#             curr = S[-1]
#             visited.add(curr)
            
#             if not curr.left and not curr.right: # leaf
#                 S.pop()
#                 if sum + curr.val == targetSum:
#                     result.append(path + [curr.val])
#                 continue
            
#             if (curr.left in visited or not curr.left) and (curr.right in visited or not curr.right): # no children left to visit
#                 S.pop()
#                 path.pop()
#                 sum -= curr.val
#                 continue

#             path.append(curr.val)
#             sum += curr.val
            
#             if curr.left: S.append(curr.left)
#             if curr.right: S.append(curr.right)
#         return result