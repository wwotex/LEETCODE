

class Solution:
    def findTarget(self, root, k: int) -> bool:
        if not root.left and not root.right:
            return False
        H = set()
        Q = []
        Q.append(root)
        while Q:
            curr = Q.pop()
            if curr.left: Q.append(curr.left)
            if curr.right: Q.append(curr.right)
            if (k - curr.val) in H:
                return True
            H.add(curr.val)
        return False
