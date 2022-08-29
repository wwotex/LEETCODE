from TreeManager import BST, TreeNode


class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        return max(self.height(root.left) + self.height(root.right),
                    self.diameterOfBinaryTree(root.left), 
                    self.diameterOfBinaryTree(root.right))

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left) + 1, self.height(root.right) + 1)

        
null = None
ls_tree = [1,2,2,null,null,3,3,4,null,null,4,5,null,null,5]
bst = BST(ls_tree)
bst.print()

sol = Solution()
print(sol.diameterOfBinaryTree(bst.tree))