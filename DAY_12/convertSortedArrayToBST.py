from TreeManager import BST, TreeNode


class Solution:
    def sortedArrayToBST(self, nums):
        
        def makeTree(left, right):
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            if left != mid: node.left = makeTree(left, mid - 1)
            if right != mid: node.right = makeTree(mid + 1, right)
            return node

        return makeTree(0, len(nums)-1)
        
        