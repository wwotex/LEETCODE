class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        
        return root