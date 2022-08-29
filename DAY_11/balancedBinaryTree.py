from TreeManager import BST, TreeNode

# cleaner solution
class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1
    
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left) + 1, self.height(root.right) + 1)

# class Solution:
#     def isBalanced(self, root):
#         if root is None:
#             return True
        
#         def height(root):
#             if root is None:
#                 return 0
#             if not root.left and not root.right:
#                 return 1
#             hl, hr = height(root.left), height(root.right)
#             if hl == -1 or hr == -1 or abs(hl - hr) > 1:
#                 return -1
#             else:
#                 return max(height(root.left) + 1, height(root.right) + 1)
    
#         return False if height(root) == -1 else True

null = None
ls_tree = [1,2,2,3,3,null,null,4,4]
bst = BST(ls_tree)
bst.print()

sol = Solution()
print(sol.isBalanced(bst.tree))