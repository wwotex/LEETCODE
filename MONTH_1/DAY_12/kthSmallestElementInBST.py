
from TreeManager import BST, TreeNode


class Solution:
    def kthSmallest(self, root, k):
        ls = []
        def enterNode(node):
            if node is None or len(ls) == k:
                return
            
            enterNode(node.left)
            ls.append(node.val)
            enterNode(node.right)
        
        enterNode(root)
        return ls[k-1]


null = None
ls_tree = [3,1,4,null,2]
k = 1
bst = BST(ls_tree)
sol = Solution()

print(sol.kthSmallest(bst.tree, k))
