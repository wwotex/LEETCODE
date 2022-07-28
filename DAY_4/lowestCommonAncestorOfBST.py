from TreeManager import BST, TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass


sol = Solution()
# BST testing module
null = None
ls_tree = [6,2,8,0,4,7,9,null,null,3,5,null,null,null,20]
# ls_tree = list(range(20))
bst = BST(ls_tree)
bst.print()