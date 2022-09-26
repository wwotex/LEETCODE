

from typing import Optional
from TreeManager import BST, TreeNode

# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:    
#         def isSameOrContains(node, comp):
#             print(f'\n\nrec: {node.val if node else None}, {comp.val if comp else None}')
#             if not node and not comp: 
#                 print('True, False')
#                 return True, False
#             if not comp:
#                 print('no comp->keep going')
#                 return isSameOrContains(node, subRoot)
#             if not node:
#                 print('False, False')
#                 return False, False
            
#             if node.val != comp.val:
#                 print('wrong val')
#                 isLeftSame, leftContains = isSameOrContains(node.left, subRoot)
#                 isRightSame, rightContains = isSameOrContains(node.right, subRoot)
#                 print(f'False, {(leftContains or rightContains)} for -> {node.val if node else None}, {comp.val if comp else None}')
#                 return False, (leftContains or rightContains)
#             else:
#                 print('good val')
#                 isLeftSame, leftContains = isSameOrContains(node.left, comp.left)
#                 isRightSame, rightContains = isSameOrContains(node.right, comp.right)
#                 print(f'{(isLeftSame and isRightSame)}, {(leftContains or rightContains)} for -> {node.val if node else None}, {comp.val if comp else None}')
#                 return (isLeftSame and isRightSame), (leftContains or rightContains or isLeftSame or isRightSame)
#         isSame, contains = isSameOrContains(root, subRoot)
#         return contains


# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:    
#         def merkle(node):
#             return f'^{node.val}.{merkle(node.left)} {merkle(node.right)}' if node else '#'
#         return merkle(subRoot) in merkle(root)

sol = Solution()
null = None
root = [3,4,5,1,2,null,null,null,null,0]
subRoot = [4,1,2]
gen1 = BST(root)
gen2 = BST(subRoot)
gen1.print()
gen2.print()
print(sol.isSubtree(gen1.tree, gen2.tree))
