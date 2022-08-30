from TreeManager import BST, TreeNode


class Solution:

    def pathSum(self, root, targetSum):
        self.T = targetSum
        self.result = 0

        self.returnSumsDownwards(root)
        return self.result

    def returnSumsDownwards(self, node):
        if node is None:
            return []
        
        sums = [x + node.val for x in (self.returnSumsDownwards(node.left) + self.returnSumsDownwards(node.right))]
        sums += [node.val]
        
        for el in sums:
            if el == self.T:
                self.result += 1
        
        return sums


sol = Solution()

null = None
ls_tree = [5,4,8,11,null,13,4,7,2,null,null,5,1]
bst = BST(ls_tree)
bst.print()

targetSum = 22
print(sol.pathSum(bst.tree, targetSum))