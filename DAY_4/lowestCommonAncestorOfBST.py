from TreeManager import BST, TreeNode

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.p_path = []
        self.q_path = []
        self.searchTree(root, [])
        last_common = None
        shorter = min(len(self.p_path), len(self.q_path))
        for i in range(shorter):
            if self.p_path[i] == self.q_path[i]:
                last_common = self.p_path[i]
            else:
                break
        return last_common

    def searchTree(self, node, path):
        new_path = path + [node]

        if node == self.p:
            self.p_path = new_path
        
        if node == self.q:
            self.q_path = new_path

        if node.left: self.searchTree(node.left, new_path)
        if node.right: self.searchTree(node.right, new_path)




sol = Solution()
# BST testing module
null = None
ls_tree = [6,2,8,0,4,7,9,null,null,3,5,null,null,null,20]
# ls_tree = list(range(20))
bst = BST(ls_tree)
bst.print()
print(sol.lowestCommonAncestor(bst.tree, bst.tree.left, bst.tree.left.right).val)
